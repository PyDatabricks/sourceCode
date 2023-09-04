from databricks.types import DatabricksClusterInfoType
from databricks.databricks import Databricks
from time import sleep
import requests

class Cluster:
    _databricks: Databricks
    _id: str

    def __init__(
        self,
        databricks: Databricks,
        id: str
    ) -> None:
        self._databricks = databricks
        self._id = id
    
    @property
    def databricks(self) -> Databricks:
        return self._databricks

    @property
    def id(self) -> str:
        return self._id
    
    def __asserts(self) -> None:
        databricks = self._databricks
        assert self._id, "Invalid Cluster Id"
        assert databricks.token, "Invalid Databricks Token"
        assert databricks.url, "Invalid Databricks Url"
    
    def forceStart(self) -> None:
        if self.getInfo().get("state") == "RUNNING":
            return
        while True:
            state = self.getInfo().get("state")
            if state == "RUNNING": return
            if state == "TERMINATED":
                self.start()
            sleep(5)

    def getClusterActivityEvents(self) -> None: pass

    def getPermissions(self) -> None: pass

    def getPermissionLevels(self) -> None: pass

    def getInfo(self) -> DatabricksClusterInfoType:
        self.__asserts()
        req = requests.get(
            f'{self._databricks.url}/api/2.0/clusters/get?cluster_id={self._id}',
            headers={
                'Authorization': f'Bearer {self._databricks.token}',
                'Content-Type': 'application/json'
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data: DatabricksClusterInfoType = req.json()
        return data

    def restart(
        self,
        restart_user: str
    ) -> None:
        self.__asserts()
        req = requests.post(
            f'{self._databricks.url}/api/2.0/clusters/restart',
            headers={
                'Authorization': f'Bearer {self._databricks.token}',
                'Content-Type': 'application/json'
            },
            json={
                'cluster_id': self._id,
                'restart_user': restart_user
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data = req.json()
        return data

    def start(self) -> None:
        self.__asserts()
        req = requests.post(
            f'{self._databricks.url}/api/2.0/clusters/start',
            headers={
                'Authorization': f'Bearer {self._databricks.token}',
                'Content-Type': 'application/json'
            },
            json={
                'cluster_id': self._id
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data = req.json()
        return data

    def terminate(self) -> None:
        self.__asserts()
        req = requests.post(
            f'{self._databricks.url}/api/2.0/clusters/delete',
            headers={
                'Authorization': f'Bearer {self._databricks.token}',
                'Content-Type': 'application/json'
            },
            json={
                'cluster_id': self._id
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data = req.json()
        return data

    def getDatabricks(self) -> Databricks:
        return self._databricks

    def getId(self) -> str:
        return self._id
