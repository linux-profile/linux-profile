import json
import uuid
from os.path import exists


class BaseFile():

    def write(self, content: str, path_file: str, mode: str = 'w') -> None:
        with open(path_file, mode, encoding='utf8') as outfile:
            outfile.write(content)

    def read(self, path_file: str, mode: str = 'r') -> str:
        with open(path_file, mode, encoding='utf8') as content:
            content = content.read()
        return content

    def touch(self, path: str):
        data = json.dumps(dict(), indent=4)
        self.write(data, path)


class HandlerModule(BaseFile):

    def __init__(self, module: str, tag: str, json: dict) -> None:
        self.module = module
        self.tag = tag
        self.json = json

        if not self.json.get(module):
            self.json[module] = dict()

        if not self.json[self.module].get(self.tag):
            self.json[self.module][self.tag] = list()

    def _insert(
            self,
            content: dict,
            index: int = 0) -> dict:
        self.json[self.module][self.tag].insert(index, content)
        return self.json

    def _update(
            self,
            content: dict,
            key: str,
            value: str) -> dict:
        position = self._search_field(key=key, value=value)
        if position >= 0:
            self.json[self.module][self.tag][position] = content

        return self.json

    def _search_field(
            self,
            key: str,
            value: str,
            position: bool = True):
        for index, item in enumerate(self.json[self.module][self.tag]):
            fields = lambda: [field for field in item.keys()]

            if key in fields() and item.get(key) == value:
                return index if position == True else item

    def _search_tag(self, tag: str):
        return self.json[self.module].get(tag)


class Storage(BaseFile):

    def __init__(self, database: str) -> None:
        self.database = database
        self.model_id = uuid.uuid4().hex.upper()

        if not exists(self.database):
            self.touch(path=self.database)

    def load(self, module: str = 'default', tag: str = 'tag'):
        self.handler = HandlerModule(
            module=module,
            tag=tag,
            json=self.load_data()
        )

    def load_data(self):
        output = self.read(path_file=self.database)
        return json.loads(output)

    def insert(self, content: dict, key: str = None, index: int = 0):
        item = self.handler._search_field(
            key=key,
            value=content.get(key),
            position=False
        )
        if item:
            content["id"] = item["id"]
            response = self.handler._update(
                content=content,
                key=key,
                value=content.get(key)
            )
        else:
            if not content.get("id"):
                content["id"] = self.model_id
            response = self.handler._insert(content=content, index=index)

        self.write(
            path_file=self.database,
            content=json.dumps(response, indent=4)
        )

    def update(self, content: dict, key: str = None):
        response = self.handler._update(
            content=content,
            key=key,
            value=content.get(key)
        )
        self.write(
            path_file=self.database,
            content=json.dumps(response, indent=4)
        )

    def search(self, key: str, value: str):
        return self.handler._search_field(key=key, value=value, position=False)

    def search_tag(self, tag: str):
        return self.handler._search_tag(tag=tag)
