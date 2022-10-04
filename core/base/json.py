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
        data = json.dumps(dict(module=dict(default=[])), indent=4)
        self.write(data, path)


class HandlerJsonModule(BaseFile):

    DEFAULT = dict(default=list())

    def __init__(self, module: str, tag: str, json: dict,) -> None:
        self.model_id = uuid.uuid4().hex.upper()
        self.module = module
        self.tag = tag
        self.json = json

        if not self.json.get(module):
            self.json[module] = dict(tag=list())

    def insert(self, content: dict):
        content['id'] = self.model_id
        self.json[self.module][self.tag].append(content)

        return self.json

    def update(self, content: dict, model_id: str):
        position = self.search(key='id', value=model_id)
        if position:
            content["id"] = model_id
            self.json[self.module][self.tag][position[0]] = content

        return self.json

    def search(self, key: str, value: str):
        for x, item in enumerate(self.json[self.module][self.tag]):
            if item.get(key) == value:
                return x, item


class JsonData(BaseFile):

    def __init__(self, database: str) -> None:
        self.database = database
        if not exists(self.database):
            self.touch(path=self.database)

        self.json = self.load_data()

    def load_module(self, module: str = 'default', tag: str = 'tag'):
        self.handler = HandlerJsonModule(module=module, tag=tag, json=self.json)

    def load_data(self):
        output = self.read(path_file=self.database)
        return json.loads(output)

    def insert_item_module(self, content: dict):
        response = self.handler.insert(content)
        self.write(
            path_file=self.database,
            content=json.dumps(response, indent=4)
        )
        return self.load_data()

    def update_item_module(self, content: dict, model_id: str):
        response = self.handler.update(content=content, model_id=model_id)
        self.write(
            path_file=self.database,
            content=json.dumps(response, indent=4)
        )
        return self.load_data()
