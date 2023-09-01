from databricks.fileManagement.types.DatabricksJobRunTypes import DatabricksJobInfoResponseType
from databricks.fileManagement.types.DatabricksJobTypes import (
    DatabricksRunJobRequestType,
    DatabricksRunJobResponseType
)
from databricks.databricks import Databricks
import requests

class Job:
    _databricks: Databricks
    _id: str

    def __init__(
        self,
        id: str,
        databricks: Databricks
    ) -> None:
        self._id = id
        self._databricks = databricks
    
    @property
    def databricks(self) -> Databricks:
        return self._databricks
    
    @property
    def id(self) -> str:
        return self._id

    def __assert(self) -> None:
        assert self._databricks.token, "Invalid Databricks Token"
        assert self._databricks.url, "Invalid Databricks Url"
        assert self._id, "Invalid Job Id"

    def getPermissions(self) -> None: pass

    def setPermissions(self) -> None: pass

    def updatePermissionLevels(self) -> None: pass

    def overwriteAllSettings(self) -> None: pass

    def partialUpdate(self) -> None: pass

    def listJobRuns(self) -> None: pass

    def getInfo(self) -> DatabricksJobInfoResponseType:
        self.__assert()
        req = requests.get(
            f'{self._databricks.url}/api/2.1/jobs/get?job_id={self._id}',
            headers={
                'Authorization': f'Bearer {self._databricks.token}',
                'Content-Type': 'application/json'
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data: DatabricksJobInfoResponseType = req.json()
        return data

    def delete(self) -> None:
        self.__assert()
        req = requests.post(
            f'{self._databricks.url}/api/2.1/jobs/delete',
            headers={
                'Authorization': f'Bearer {self._databricks.token}',
                'Content-Type': 'application/json'
            },
            json={
                'job_id': self._id
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data = req.json()
        return data

    def run(
        self,
        params: DatabricksRunJobRequestType
    ) -> DatabricksRunJobResponseType:
        self.__assert()
        req = requests.post(
            f'{self._databricks.url}/api/2.1/jobs/run-now',
            headers={
                'Authorization': f'Bearer {self._databricks.token}',
                'Content-Type': 'application/json'
            },
            json={
                'job_id': self._id,
                **params
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data: DatabricksRunJobResponseType = req.json()
        return data

    def calcelAllJobRuns(self) -> None:
        self.__assert()
        req = requests.post(
            f'{self._databricks.url}/api/2.1/jobs/runs/cancel-all',
            headers={
                'Authorization': f'Bearer {self._databricks.token}',
                'Content-Type': 'application/json'
            },
            json={
                'job_id': self._id
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data = req.json()
        return data
