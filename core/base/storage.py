import json
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


class HandlerStorage():

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

    def _search_field(
            self,
            key: str,
            value: str,
            position: bool = False,
            ipop=False):
        for tag in self.json[self.module]:
            for index, item in enumerate(self.json[self.module][tag]):
                fields = lambda: [field for field in item.keys()]

                if key in fields() and item.get(key) == value:
                    if ipop:
                        return self.json[self.module][tag].pop(index)
                    return index if position else item

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
        self.handler = HandlerStorage(module=module, tag=tag, json=self.load())

    def run(self, content: dict, key: str = None):
        item = self.handler._search_field(
            key=key,
            value=content.get(key),
            ipop=True
        )

        if item:
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


class StorageQuery(BaseFile):

    def __init__(self, database: str) -> None:
        self.database = database

        if not exists(self.database):
            self.touch(path=self.database)

        self.json = self.load()

    def load(self):
        output = self.read(path_file=self.database)
        return json.loads(output)

    def module(self, module: str):
        return self.json.get(module)

    def module_list(self, module: str, tag: str = None):
        module_list = lambda: [item for item in self.json[module]]
        if tag in module_list():
            return [tag]
        else:
            return module_list()

    def tag(self, tag: str, module: str = None):
        try:
            return self.json.get(module).get(tag)
        except AttributeError:
            pass

        for _module in self.json:
            for _tag in self.json.get(_module):
                if tag == _tag:
                    return self.json[_module][_tag]

    def key(
            self,
            key: str,
            value: str = None,
            tag: str = None,
            module: str = None):
        try:
            _tag = self.json.get(module).get(tag)
            for item in _tag:
                if item.get(key) == value:
                    return item
        except AttributeError:
            pass

        for _module in self.json:
            for _tag in self.json[_module]:
                for item in self.json[_module][_tag]:
                    if item.get(key) == value:
                        return item

    def deep_search(
            self,
            module: str,
            tag: str = None,
            key: str = None,
            value: str = None,
            output: list = list(),
            lvl: int = 0):

        if module is not None:
            lvl = 3
        if module and tag is not None:
            lvl = 2
        if module and tag and key and value is not None:
            lvl = 1

        # Search by parameter of [module], [tag], [key] and [value].
        if lvl == 1:
            try:
                _tag = self.json[module][tag]
                for item in _tag:
                    if item.get(key) == value:
                        return [item]
            except:
                pass

        # Search by parameter of [module] and [tag].
        if lvl == 2:
            try:
                return self.json[module][tag]
            except:
                pass

        # Search by parameter of [module].
        if lvl == 3:
            try:
                for _tag in self.json[module]:
                    for item in self.json[module][_tag]:
                        output.append(item)
            except:
                pass

        return output
