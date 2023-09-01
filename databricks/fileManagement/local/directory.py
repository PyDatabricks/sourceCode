from databricks.fileManagement.local.repository import Repository
from typing import List
from os import (
    listdir,
    makedirs
)

class Directory(Repository):
    def __init__(
        self,
        path: str
    ) -> None:
        super().__init__(path)

    def listDir(self) -> List[str]:
        return listdir(self._path.repositoryPath)

    def create(self) -> bool:
        makedirs(self.path, exist_ok=True)
