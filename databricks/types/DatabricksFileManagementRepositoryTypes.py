from typing import (
    List,
    TypedDict
)

class DatabricksRepositoryPropertiesType(TypedDict):
    path: str
    is_dir: bool
    file_size: int
    modification_time: int

class DatabricksFileGetContentResponseType(TypedDict):
    bytes_read: int
    data: str

class DatabricksListDirResponseType(TypedDict):
    files: List[DatabricksRepositoryPropertiesType]