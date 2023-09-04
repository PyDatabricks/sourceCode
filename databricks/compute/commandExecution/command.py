from databricks.compute.commandExecution.context import Context
from databricks.fileManagement.types.DatabricksCommandExecution import (
    DatabricksRunCommandResponseType,
    DatabricksGetCommandStatusResponseType
)
from databricks.compute.cluster.cluster import Cluster
from databricks.databricks import Databricks
import requests


class Command:
    _command: str
    _context: Context
    _id: str

    def __init__(
        self,
        command: str,
        context: Context
    ) -> None:
        self._command = command
        self._context = context
    
    @property
    def cluster(self) -> Cluster:
        return self._context.cluster

    @property
    def databricks(self) -> Databricks:
        return self._context.databricks
    
    @property
    def context(self) -> Context:
        return self._context

    @property
    def id(self) -> str:
        return self._id

    def __assert(self) -> None:
        assert self._command, "Invalid Command"
        assert self.databricks.token, "Invalid Databricks Token"
        assert self.databricks.url, "Invalid Databricks Url"
        assert self.cluster.id, "Invalid Cluster Id"
        assert self._context.id, "Invalid Context Id"

    def run(self) -> DatabricksRunCommandResponseType:
        self.__assert()
        req = requests.post(
            f'{self.databricks.url}/api/1.2/commands/execute',
            headers={
                'Authorization': f'Bearer {self.databricks.token}',
                'Content-Type': 'application/json'
            },
            json={
                'clusterId': self.cluster.id,
                'contextId': self._context.id,
                'language': self._context.language,
                'command': self._command
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data: DatabricksRunCommandResponseType = req.json()
        self._id = data.get('id')
        return data

    def getStatus(self) -> DatabricksGetCommandStatusResponseType:
        self.__assert()
        assert self._id, "Invalid Command Id. Try to run Command.run() method before."
        req = requests.get(
            f'{self.databricks.url}/api/1.2/commands/status?clusterId={self.cluster.id}&contextId={self._context.id}&commandId={self._id}',
            headers={
                'Authorization': f'Bearer {self.databricks.token}',
                'Content-Type': 'application/json'
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data: DatabricksGetCommandStatusResponseType = req.json()
        return data
    
    def cancel(self) -> None:
        self.__assert()
        assert self._id, "Invalid Command Id. Try to run Command.run() method before."
        req = requests.post(
            f'{self.databricks.url}/api/1.2/commands/cancel',
            headers={
                'Authorization': f'Bearer {self.databricks.token}',
                'Content-Type': 'application/json'
            },
            json={
                'clusterId': self.cluster.id,
                'contextId': self._context.id,
                'commandId': self._id
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data = req.json()
        return data
