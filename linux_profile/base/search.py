"""
Module Search
"""


from json import loads
from os.path import exists
from linux_profile.base.file import File


class Search:

    def __init__(self, database: str) -> None:
        self.database = database
        if not exists(self.database):
            File.touch(path=self.database)

        try:
            self.json = loads(File.read(path_file=self.database))
        except Exception:
            File.touch(path=self.database)
            self.json = loads(File.read(path_file=self.database))

    def get(self):
        return self.json

    def _module(self, key: str) -> list:
        response = []
        for module in self.json:
            if key == module:
                response.append(module)
                return response

    def _tag(self, key: str) -> list:
        response = []
        for module in self.json:
            for tag in self.json[module]:
                if key == tag:
                    response.append(module)
                    response.append(tag)
                    return response

    def _item(self, key: str, value: str) -> list:
        response = []
        for module in self.json:
            for tag in self.json[module]:
                for index, item in enumerate(self.json[module][tag]):
                    for search in item:
                        if key == search:
                            if str(item[search]) == str(value):
                                response.append(module)
                                response.append(tag)
                                response.append(index)
                                response.append(key)
                                return response

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
            except Exception:
                pass

        # Search by parameter of [module] and [tag].
        if lvl == 2:
            try:
                return self.json[module][tag]
            except Exception:
                pass

        # Search by parameter of [module].
        if lvl == 3:
            try:
                for _tag in self.json[module]:
                    for item in self.json[module][_tag]:
                        output.append(item)
            except Exception:
                pass

        return output
