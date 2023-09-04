from databricks.types.DatabricksFileManagementRepositoryTypes import DatabricksListDirResponseType
from databricks.fileManagement.dbfs.repository import Repository
from databricks.fileManagement.path import RepositoryPath
from databricks.fileManagement.dbfs.file import File
from databricks.databricks import Databricks
from time import sleep
import requests


class Directory(Repository):
    def __init__(
        self,
        databricks: Databricks,
        path: str
    ) -> None:
        super().__init__(databricks, path)

    def __assert(self) -> None:
        assert self.databricks.token, "Invalid Databricks Token"
        assert self.databricks.url, "Invalid Databricks Url"

    def create(self) -> None:
        self.__assert()
        req = requests.post(
            f'{self.databricks.url}/api/2.0/dbfs/mkdirs',
            headers={
                'Authorization': f'Bearer {self.databricks.token}',
                'Content-Type': 'application/json'
            },
            json={
                'path': self.path
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data = req.json()
        return data

    def listDir(self) -> DatabricksListDirResponseType:
        self.__assert()
        req = requests.get(
            f'{self.databricks.url}/api/2.0/dbfs/list?path={self.path}',
            headers={
                'Authorization': f'Bearer {self.databricks.token}',
                'Content-Type': 'application/json'
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data: DatabricksListDirResponseType = req.json()
        return data
    
    def download(
        self,
        to: str,
        encoding: str='utf-8',
        workers: int=5
    ) -> None:
        for file in self.listDir().get('files'):
            path = RepositoryPath(file.get('path'))
            repo = Repository(self.databricks, f'{self.path}/{path.getRepositoryName()}')
            sleep(2)
            properties = repo.getProperties()

            if properties.get('is_dir'):
                directory = Directory(self.databricks, f'{self.path}/{path.getRepositoryName()}')
                directory.download(f'{to}/{path.getRepositoryName()}', encoding, workers)
                return
            file = File(self.databricks, f'{self.path}/{path.getRepositoryName()}', encoding)
            file.download(f'{to}/{path.getRepositoryName()}', workers)
        