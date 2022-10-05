import json
import uuid
from os.path import exists


class BaseFile():

    def write(self, content: str, path_file: str, mode: str ='w') -> None:
        with open(path_file, mode, encoding='utf8') as outfile:
            outfile.write(content)

    def read(self, path_file: str, mode: str ='r') -> str:
        with open(path_file, mode, encoding='utf8') as content:
            content = content.read()
        return content

    def touch(self, path: str):
        data = json.dumps(dict(), indent=4)
        self.write(data, path)


class HandlerModule(BaseFile):

    def __init__(self, module: str, tag: str, json: dict,) -> None:
        self.model_id = uuid.uuid4().hex.upper()
        self.module = module
        self.tag = tag
        self.json = json

        if not self.json.get(module):
            self.json[module] = dict()

        if not self.json[self.module].get(self.tag):
            self.json[self.module][self.tag] = list()

    def _insert(self, content: dict):
        if not content.get('id'):
            content['id'] = self.model_id
        self.json[self.module][self.tag].append(content)

        return self.json

    def _update(self, content: dict, model_id: str):
        position = self._search(key='id', value=model_id)

        if position >= 0:
            content["id"] = model_id
            self.json[self.module][self.tag][position] = content

        return self.json

    def _search(self, key: str, value: str, position: bool = True):
        for x, item in enumerate(self.json[self.module][self.tag]):
            if item.get(key) == value:
                if position:
                    return x
                else:
                    return item

    def _search_tag(self, tag: str):
        return self.json[self.module].get(tag)

class Storage(BaseFile):

    def __init__(self, database: str) -> None:
        self.database = database

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

    def insert(self, content: dict, check_key = None):
        item = self.handler._search(key=check_key, value=content.get(check_key), position=False)
        if item:
            response = self.handler._update(content=content, model_id=item.get("id"))
        else:
            response = self.handler._insert(content)

        self.write(
            path_file=self.database,
            content=json.dumps(response, indent=4)
        )

    def update(self, content: dict, model_id: str):
        response = self.handler._update(content=content, model_id=model_id)
        self.write(
            path_file=self.database,
            content=json.dumps(response, indent=4)
        )

    def search(self, key: str, value: str):
        return self.handler._search(key=key, value=value, position=False)

    def search_tag(self, tag: str):
        return self.handler._search_tag(tag=tag)
