from databricks.fileManagement.types.DatabricksJobManagerTypes import (
    DatabricksCreateJobRequestType,
    DatabricksCreateJobResponseType,
    DatabricksListJobsResponseType
)
from databricks.databricks import Databricks
import requests


class JobManager:
    _databricks: Databricks

    def __init__(
        self,
        databricks: Databricks
    ) -> None:
        self._databricks = databricks

    @property
    def databricks(self) -> Databricks:
        return self._databricks

    def __assert(self) -> None:
        assert self._databricks.token, "Invalid Databricks Token"
        assert self._databricks.url, "Invalid Databricks Url"

    def createNewJob(
        self,
        options: DatabricksCreateJobRequestType
    ) -> DatabricksCreateJobResponseType:
        self.__assert()
        req = requests.post(
            f'{self._databricks.url}/api/2.1/jobs/create',
            headers={
                'Authorization': f'Bearer {self._databricks.token}',
                'Content-Type': 'application/json'
            },
            json={options}
        )
        if req.status_code != 200:
            req.raise_for_status()
        data: DatabricksCreateJobResponseType = req.json()
        return data

    def listJobs(
        self,
        limit: int=20,
        page_token: str='',
        name: str='',
        expand_tasks: bool=False
    ) -> DatabricksListJobsResponseType:
        self.__assert()
        req = requests.get(
            f'{self._databricks.url}/api/2.1/jobs/list?limit={limit}&page_token={page_token}&name={name}&expand_tasks={expand_tasks}',
            headers={
                'Authorization': f'Bearer {self._databricks.token}',
                'Content-Type': 'application/json'
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data: DatabricksListJobsResponseType = req.json()
        return data
