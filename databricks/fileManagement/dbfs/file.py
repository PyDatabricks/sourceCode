from databricks.types.DatabricksFileManagementRepositoryTypes import DatabricksFileGetContentResponseType
from databricks.fileManagement.dbfs.repository import Repository
from databricks.fileManagement.local.file import File as LocalFile
from databricks import databricks
from multipledispatch import dispatch
from threading import Thread
from enum import Enum
from typing import (
    List,
    Union
)
import requests
import base64

class FileContent:
    _content: Union[str, bytes]

    def __init__(
        self,
        content: Union[str, bytes]
    ) -> None:
        self._content = content

    @property
    def content(self) -> Union[str, bytes]:
        return self._content

    @content.setter
    def content(
        self,
        content: Union[str, bytes]
    ) -> None:
        self._content = content

    def decode(
        self,
        encoding: str
    ) -> str:
        return base64.b64decode(self._content).decode(encoding)

class FileContentDownloaderState(Enum):
    PENDING="PENDING"
    RUNNING="RUNNING"
    ERROR="ERROR"
    FINISHED="FINISHED"


class FileContentDownloader(Thread):
    _id: int
    _file: 'File'
    _content: Union[DatabricksFileGetContentResponseType, None]= None
    _threadState: FileContentDownloaderState= FileContentDownloaderState.PENDING
    _offset: int

    def __init__(
        self,
        id: int,
        file: 'File',
        offset: int,
    ) -> None:
        Thread.__init__(self)
        self._id = id
        self._file = file
        self._offset = offset
        self._threadState = FileContentDownloaderState.PENDING

    @property
    def id(self) -> int:
        return self._id

    @property
    def content(self) -> Union[DatabricksFileGetContentResponseType, None]:
        return self._content
    
    @property
    def threadState(self) -> FileContentDownloaderState:
        return self._threadState

    def run(self) -> None:
        self._threadState = FileContentDownloaderState.RUNNING

        try:
            content = self._file.getPartialContent(self._offset)
        except:
            self._threadState = FileContentDownloaderState.ERROR
            return

        fileContent = FileContent(content.get('data'))
        content['data'] = fileContent.decode(self._file.encoding)
        self._content = content
        # print(content['data'])
        self._threadState = FileContentDownloaderState.FINISHED


class FileContentDownloaderManager:
    _contentArray: List[str]
    _file: 'File'
    _fileContent: List[str]
    _fileSize: int
    _maxWorkers: int
    _workers: List[FileContentDownloader]

    def __init__(
        self,
        file: 'File',
        maxWorkers: int=10
    ) -> None:
        self._file = file
        self._fileContent = []
        self._maxWorkers = maxWorkers
        self._workers = []
        properties = self._file.getProperties()
        self._fileSize = properties.get('file_size')

    def setMaxWorkers(self) -> None:
        _max = self._fileSize // 1000 + 1
        self._maxWorkers = _max if _max < self._maxWorkers else self._maxWorkers
    
    @dispatch()
    def alocateWorker(self) -> None:
        index = len(self._fileContent)
        self._fileContent.append(f'{index}')
        self.instanceWorker(index)
    
    @dispatch(int)
    def alocateWorker(
        self,
        index: int
    ) -> None:
        self.instanceWorker(index)
    
    def instanceWorker(
        self,
        index: int
    ) -> None:
        worker = FileContentDownloader(
            index,
            self._file,
            1000*index
        )
        worker.start()
        self._workers.append(worker)
        self._fileContent[index] = worker
    
    def normalizeFileContent(self) -> None:
        self._fileContent = [x for x in self._fileContent if type(x) != FileContentDownloader]

    def download(self) -> List[str]:
        bytesDownloaded = 0

        while bytesDownloaded < self._fileSize:
            if len(self._workers) < self._maxWorkers:
                self.alocateWorker()

            for worker in self._workers:
                if worker.threadState == FileContentDownloaderState.FINISHED:
                    bytesDownloaded += worker.content.get('bytes_read')
                    self._fileContent[worker.id] = worker.content.get('data')
                    self._workers.pop(self._workers.index(worker))
                elif worker.threadState == FileContentDownloaderState.ERROR:
                    self.alocateWorker()

        self.normalizeFileContent()
        return self._fileContent

class File(Repository):
    _encoding: str

    def __init__(
        self,
        databricks: databricks,
        path: str,
        encoding: str='utf-8'
    ) -> None:
        super().__init__(databricks, path)
        self._encoding = encoding

    @property
    def encoding(self) -> str:
        return self._encoding

    def __assert(self) -> None:
        assert self.databricks.token, "Invalid Databricks Token"
        assert self.databricks.url, "Invalid Databricks Url"

    def move(
        self,
        destination: str
    ) -> None:
        self.__assert()
        req = requests.post(
            f'{self.databricks.url}/api/2.0/dbfs/move',
            headers={
                'Authorization': f'Bearer {self.databricks.token}',
                'Content-Type': 'application/json'
            },
            json={
                'source_path': self.path,
                'destination_path': destination
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data = req.json()
        return data

    def upload(
        self,
        content: str,
        overwrite: False
    ) -> None:
        self.__assert()
        req = requests.post(
            f'{self.databricks.url}/api/2.0/dbfs/put',
            headers={
                'Authorization': f'Bearer {self.databricks.token}',
                'Content-Type': 'application/json'
            },
            json={
                'path': self.path,
                'contents': content,
                'overwrite': overwrite
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data = req.json()
        return data


    def getPartialContent(
        self,
        offset: int
    ) -> DatabricksFileGetContentResponseType:
        self.__assert()
        req = requests.get(
            f'{self.databricks.url}/api/2.0/dbfs/read?path={self.path}&offset={offset}&length={1000}',
            headers={
                'Authorization': f'Bearer {self.databricks.token}',
                'Content-Type': 'application/json'
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data: DatabricksFileGetContentResponseType = req.json()
        return data
    
    def getContent(
        self,
        workers=5
    ) -> List[str]:
        self.__assert()
        manager = FileContentDownloaderManager(self, workers)
        return manager.download()
    
    def download(
        self,
        to: str,
        workers: int=5
    ) -> None:
        fileContent = self.getContent(workers)
        localFile = LocalFile(to)
        localFile.write("", 'w+', self._encoding)
        localFile.write(fileContent, self._encoding)
