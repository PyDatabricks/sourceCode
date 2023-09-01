from typing import List

class RepositoryPath:
    _repositoryPath: str

    def __init__(
        self,
        repositoryPath: str
    ) -> None:
        self._repositoryPath = repositoryPath

    def __str__(self) -> str:
        return self._repositoryPath

    @property
    def repositoryPath(self) -> str:
        return self._repositoryPath

    def getPathArray(self) -> List[str]:
        arr = self._repositoryPath.split('\\')
        arr = '/'.join(arr)
        return arr.split('/')
    
    def getRepositoryPath(self) -> str:
        return self._repositoryPath
    
    def getPath(self) -> str:
        arr = self.getPathArray()
        if len(arr) == 0:
            return ''
        arr.pop()
        return '/'.join(arr)

    def getRepositoryName(self) -> str:
        arr = self.getPathArray()
        if len(arr) == 0:
            return ''
        return arr[-1]

    def toString(self) -> str:
        return self._repositoryPath