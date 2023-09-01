from databricks.fileManagement.local.repository import Repository
from databricks.fileManagement.local.directory import Directory
from typing import (
    List,
    Literal,
    Union
)

class File(Repository):
    def __init__(
        self,
        path: str
    ) -> None:
        super().__init__(path)
    
    def __write(
            self,
        content: Union[List[str], str],
        mode: Literal["w", "w+", "wt", "tw", "a", "at", "ta", "x", "xt", "tx"]='w+',
        encoding: str='utf-8'
    ) -> None:
        if type(content) == list:
            for partialContent in content:
                self.__write(partialContent, "a", encoding)
            return
        with open(self.path, mode, encoding=encoding) as file:
            file.write(content)

    def write(
        self,
        content: Union[List[str], str],
        mode: Literal["w", "w+", "wt", "tw", "a", "at", "ta", "x", "xt", "tx"]='w+',
        encoding: str='utf-8'
    ) -> None:
        filePath = Directory(self._path.getPath())
        if not filePath.exists():
            filePath.create()
        self.__write(content, mode, encoding)

    def read(
        self,
        mode: Literal["r", "rt", "tr", "U", "rU", "Ur", "rtU", "rUt", "Urt", "trU", "tUr", "Utr"],
        encoding: str='utf-8'
    ) -> List[str]:
        with open(self.path, mode, encoding=encoding) as file:
            return file.readlines()