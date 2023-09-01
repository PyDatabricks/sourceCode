from databricks.databricks import Databricks

class Workspace:
    _databricks: Databricks
    _path: str

    def __init__(
        self,
        databricks: Databricks,
        path: str
    ) -> None:
        self._databricks = databricks
        self._path = path

    def delete(self) -> None: pass

    def export(self) -> None: pass

    def getStatus(self) -> None: pass

    def importWorkspace(self) -> None: pass

    def listContents(self) -> None: pass

    def createDirectory(self) -> None: pass

    def getDatabricks(self) -> Databricks:
        return self._databricks
