from typing import TypedDict

class DatabricksRequestError(TypedDict):
    error_code: str
    message: str