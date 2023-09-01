
from databricks.compute.commandExecution.command import Command
from databricks.compute.commandExecution.context import Context
from databricks.types.DatabricksCommandExecution import (
    DatabricksGetCommandStatusResponseResultsType,
    Language
)
from databricks.compute.cluster.cluster import Cluster
from databricks.databricks import Databricks
from time import sleep

class CommandExecution:
    _command: str
    _cluster: Cluster
    _language: Language
    _cmd: Command
    _ctx: Context

    def __init__(
        self,
        command: str,
        cluster: Cluster,
        language: Language="python"
    ) -> None:
        self._command = command
        self._cluster = cluster
        self._language = language

    @property
    def cluster(self) -> Cluster:
        return self._cluster

    @property
    def databricks(self) -> Databricks:
        return self._cluster.getDatabricks()

    @property
    def language(self) -> Language:
        return self._language

    @property
    def command(self) -> str:
        return self._command


    def __createContext(self) -> Context:
        self._ctx = Context(self._cluster, self._language)
        res = self._ctx.create()
        if not res.get('id'):
            print(res)
        return self._ctx


    def __createCommand(self) -> None:
        assert self._ctx, "Invalid context. You have to use CommandExecution.createContext() before."
        self._cmd = Command(self._command, self._ctx)


    def run(self) -> DatabricksGetCommandStatusResponseResultsType:
        self._cluster.forceStart()
        self.__createContext()
        self.__createCommand()
        self._cmd.run()
        result: DatabricksGetCommandStatusResponseResultsType = {}
        while True:
            status = self._cmd.getStatus()
            if status.get('status') in ["Finished", "Cancelled", "Error"]:
                result = status.get('results')
                break
            sleep(3)
        self._ctx.delete()
        return result


    def cancel(self) -> None:
        assert self._cmd, "Invalid Command Id. Try to run CommandExecution.run() before."
        self._cmd.cancel()
        self._ctx.delete()
