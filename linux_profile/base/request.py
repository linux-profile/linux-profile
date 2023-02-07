from json import dumps
from urllib import parse
from http.client import HTTPSConnection


class Request:

    def __init__(self, url: str = '127.0.0.1') -> None:
        self.url = url
        self.local = None
        self.path = None
        self.params = {}
        self.headers = {}
        self.setup()

    def setup(self) -> None:
        self.init_local()
        self.init_path()
        self.init_headers()
        self.connection = HTTPSConnection(self.local)

    def init_local(self) -> None:
        self.local = parse.urlsplit(self.url).netloc

    def init_path(self) -> None:
        self.path = parse.urlsplit(self.url).path

    def init_headers(self) -> None:
        self.headers = {'Content-Type': 'application/json'}

    def request(
            self,
            method: str,
            body: dict = {},
            params: dict = {},
            headers: dict = {}):
        """Base Request
        """
        try:
            self.connection.request(
                method=method,
                body=dumps(body),
                url=self.path + parse.urlencode(params),
                headers=headers if headers else self.headers,
            )
            with self.connection.getresponse() as response:
                return response.read()

        except Exception:
            raise ValueError("Failed to make the request")
