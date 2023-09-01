from typing import (
    Dict,
    List,
    Literal,
    TypedDict
)

Language = Literal["python", "scala", "sql"]
# class Language(Enum):
#     PYTHON="python"
#     SCALA="scala"
#     SQL="sql"

class DatabricksCreateCommandResponseType(TypedDict):
    id: str

class DatabricksDeleteCommandResponseType(TypedDict):
    clusterId: str
    contextId: str

class DatabricksCommandStatusResponseType(TypedDict):
    id: str
    status: Literal["Running", "Pending", "Error"]

class DatabricksRunCommandResponseType(TypedDict):
    id: str

class DatabricksGetCommandStatusResponseResultsType(TypedDict):
    resultType: Literal["error", "image", "images", "table", "text"]
    summary: str
    cause: str
    fileName: str
    fileNames: str
    data: Dict[str, str]
    schema: List[Dict[str, str]]
    truncated: bool
    isJsonSchema: bool
    pos: int

class DatabricksGetCommandStatusResponseType(TypedDict):
    id: str
    status: Literal["Cancelled", "Cancelling", "Error", "Finished", "Queued", "Running"]
    results: DatabricksGetCommandStatusResponseResultsType