from databricks.fileManagement.types.DatabricksTypes import DatabricksListClustersResponseType
import requests

class Databricks:
    _url: str
    _token: str

    def __init__(
        self,
        url: str,
        token: str
    ) -> None:
        self._url = url
        self._token = token

    @property
    def token(self) -> str:
        return self._token

    @property
    def url(self) -> str:
        return self._url

    def listClusters(self) -> DatabricksListClustersResponseType:
        assert self._token, "Invalid Databricks Token"
        assert self._url, "Invalid Databricks Url"
        req = requests.get(
            f'{self._url}/api/2.0/clusters/list',
            headers={
                'Authorization': f'Bearer {self._token}',
                'Content-Type': 'application/json'
            }
        )
        if req.status_code != 200:
            req.raise_for_status()
        data: DatabricksListClustersResponseType = req.json()
        return data

    def getToken(self) -> str:
        return self._token

    def getUrl(self) -> str:
        return self._url

if __name__ == "__main__":
    dt = Databricks(
        "https://adb-6549464872659391.11.azuredatabricks.net",
        "dapi875e195df70eb028bf477acce594ff50"
    )
    print(dt.listClusters())