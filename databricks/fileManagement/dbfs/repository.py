from databricks.types.DatabricksFileManagementRepositoryTypes import DatabricksRepositoryPropertiesType
from databricks.fileManagement.path import RepositoryPath
from databricks.databricks import Databricks
import requests


class Repository:
    _databricks: Databricks
    _path: RepositoryPath

    def __init__(
        self,
        databricks: Databricks,
        path: str
    ) -> None:
        self._databricks = databricks
        self._path = RepositoryPath(path)
    
    @property
    def databricks(self) -> Databricks:
        return self._databricks

    @property
    def path(self) -> str:
        return self._path.toString()
    
    def __assert(self) -> None:
        assert self._databricks.token, "Invalid Databricks Token"
        assert self._databricks.url, "Invalid Databricks Url"

    def delete(
        self,
        recursive: bool=False
    ) -> None:
        self.__assert()
        req = requests.post(
            f'{self._databricks.url}/api/2.0/dbfs/delete',
            headers={
                'Authorization': f'Bearer {self._databricks.token}',
                'Content-Type': 'application/json'
            },
            json={
                'path': self.path,
                'recursive': recursive
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data = req.json()
        return data

    def getProperties(self) -> DatabricksRepositoryPropertiesType:
        self.__assert()
        req = requests.get(
            f'{self._databricks.url}/api/2.0/dbfs/get-status?path={self.path}',
            headers={
                'Authorization': f'Bearer {self._databricks.token}',
                'Content-Type': 'application/json'
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data: DatabricksRepositoryPropertiesType = req.json()
        return data

    def isDir(self) -> bool:
        properties = self.getProperties()
        return properties.get('is_dir')

    def isFile(self) -> bool:
        properties = self.getProperties()
        return not properties.get('is_dir')
