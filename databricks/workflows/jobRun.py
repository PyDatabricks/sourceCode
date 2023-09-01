from databricks.types.DatabricksJobRunTypes import (
    DatabricksJobRunRequestType,
    DatabricksJobRunResponseType,
    JobRunOutputResponseType
)
from databricks.databricks import Databricks
import requests


class JobRun:
    _databricks: Databricks
    _id: str

    def __init__(
        self,
        databricks: Databricks,
        id
    ) -> None:
        self._id = id
        self._databricks = databricks

    @property
    def databricks(self) -> Databricks:
        return self._databricks

    @property
    def id(self) -> str:
        return self._id

    def __asserts(self) -> None:
        assert self._id, "Invalid Job Run Id"
        assert self._databricks.token, "Invalid Databricks Token"
        assert self._databricks.url, "Invalid Databricks Url"

    def cancel(self) -> None:
        self.__asserts()
        req = requests.post(
            f'{self._databricks.url}/api/2.1/jobs/runs/cancel',
            headers={
                'Authorization': f'Bearer {self._databricks.token}',
                'Content-Type': 'application/json'
            },
            json={
                'run_id': self._id
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data = req.json()
        return data

    def deleteJobRun(self) -> None:
        self.__asserts()
        req = requests.post(
            f'{self._databricks.url}/api/2.1/jobs/runs/delete',
            headers={
                'Authorization': f'Bearer {self._databricks.token}',
                'Content-Type': 'application/json'
            },
            json={
                'run_id': self._id
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data = req.json()
        return data

    def getOutput(self) -> JobRunOutputResponseType:
        self.__asserts()
        req = requests.get(
            f'{self._databricks.url}/api/2.1/jobs/runs/get-output?run_id={self._id}',
            headers={
                'Authorization': f'Bearer {self._databricks.token}',
                'Content-Type': 'application/json'
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data: JobRunOutputResponseType = req.json()
        return data

    def repair(
        self,
        params: DatabricksJobRunRequestType
    ) -> DatabricksJobRunResponseType:
        self.__asserts()
        req = requests.post(
            f'{self._databricks.url}/api/2.1/jobs/runs/repair',
            headers={
                'Authorization': f'Bearer {self._databricks.token}',
                'Content-Type': 'application/json'
            },
            json={
                'run_id': self._id,
                **params
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data: DatabricksJobRunResponseType = req.json()
        return data
