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


class Handler():

    def __init__(self, module: str, tag: str, json: dict) -> None:
        self.module = module
        self.tag = tag
        self.json = json

        if not self.json.get(module):
            self.json[module] = dict()

        if not self.json[self.module].get(self.tag):
            self.json[self.module][self.tag] = list()

    def _insert(self, content: dict) -> dict:
        self.json[self.module][self.tag].append(content)
        return self.json

    def _search_field(self, key: str, value: str, position: bool = False, ipop=False):
        for tag in self.json[self.module]:
            for index, item in enumerate(self.json[self.module][tag]):
                fields = lambda: [field for field in item.keys()]

                if key in fields() and item.get(key) == value:
                    if ipop:
                        return self.json[self.module][tag].pop(index)
                    return index if position == True else item

    def _search_tag(self, tag: str):
        return self.json[self.module].get(tag)


class Storage(BaseFile):
    
    def __init__(self, database: str) -> None:
        self.database = database

        if not exists(self.database):
            self.touch(path=self.database)

    def load(self):
        output = self.read(path_file=self.database)
        return json.loads(output)

    def begin(self, module: str, tag: str):
        self.handler = Handler(module=module, tag=tag, json=self.load())

    def run(self, content: dict, key: str = None):
        item = self.handler._search_field(key=key, value=content.get(key), ipop=True)

        if not item:
            content["id"] = uuid.uuid4().hex.upper()
        else:
            content["id"] = item["id"]

        data = self.handler._insert(content=content)
        self.write(
            path_file=self.database,
            content=json.dumps(data, indent=4)
        )

    def search(self, key: str, value: str):
        return self.handler._search_field(key=key, value=value, position=False)

    def search_tag(self, tag: str):
        return self.handler._search_tag(tag=tag)
