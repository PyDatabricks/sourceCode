from databricks.fileManagement.path import RepositoryPath
from os import path, remove
from shutil import rmtree

class Repository:
    _path: RepositoryPath

    def __init__(
        self,
        path: str
    ) -> None:
        self._path = RepositoryPath(path)

    @property
    def path(self) -> str:
        return self._path.toString()

    def delete(self) -> None:
        if self.isDir():
            rmtree(self.path)
            return
        remove(self.path)
            
    def exists(self) -> bool:
        return path.exists(self.path)

    def isDir(self) -> bool:
        return path.isdir(self.path)

    def isFile(self) -> bool:
        return path.isfile(self.path)
