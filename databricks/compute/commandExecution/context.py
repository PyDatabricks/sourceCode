from databricks.types.DatabricksCommandExecution import (
    DatabricksCommandStatusResponseType,
    DatabricksCreateCommandResponseType,
    DatabricksDeleteCommandResponseType,
    Language
)
from databricks.compute.cluster.cluster import Cluster
from databricks.databricks import Databricks
import requests

class Context:
    _cluster: Cluster
    _language: Language
    _id: str

    def __init__(
        self,
        cluster: Cluster,
        language: Language="python"
    ) -> None:
        self._cluster = cluster
        self._language = language
    
    @property
    def cluster(self) -> Cluster:
        return self._cluster
    
    @property
    def databricks(self) -> Databricks:
        return self._cluster.databricks
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def language(self) -> Language:
        return self._language

    def __assert(self) -> None:
        assert self.databricks.token, "Invalid Databricks Token"
        assert self.databricks.url, "Invalid Databricks Url"
        assert self._cluster.id, "Invalid Cluster Id"

    def create(self) -> DatabricksCreateCommandResponseType:
        self.__assert()
        req = requests.post(
            f'{self.databricks.url}/api/1.2/contexts/create',
            headers={
                'Authorization': f'Bearer {self.databricks.token}',
                'Content-Type': 'application/json'
            },
            json={
                'clusterId': self._cluster.id,
                'language': self._language
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data: DatabricksCreateCommandResponseType = req.json()
        self._id = data.get('id')
        return data
    
    def getStatus(self) -> DatabricksCommandStatusResponseType:
        self.__assert()
        assert self._id, f"Invalid context Id. Try to run create() method before."
        req = requests.get(
            f'{self.databricks.url}/api/1.2/contexts/status?clusterId={self._cluster.id}&contextId={self._id}',
            headers={
                'Authorization': f'Bearer {self.databricks.token}',
                'Content-Type': 'application/json'
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data: DatabricksCommandStatusResponseType = req.json()
        return data

    def delete(self) -> DatabricksDeleteCommandResponseType:
        self.__assert()
        assert self._id, f"Invalid context Id. Try to run create() method before."
        req = requests.post(
            f'{self.databricks.url}/api/1.2/contexts/destroy',
            headers={
                'Authorization': f'Bearer {self.databricks.token}',
                'Content-Type': 'application/json'
            },
            json={
                'clusterId': self._cluster.id,
                'contextId': self._id
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data: DatabricksDeleteCommandResponseType = req.json()
        return data
