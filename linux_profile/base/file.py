from os import system
from pathlib import Path
from os.path import exists
from json import dumps, loads

from linux_profile.base.error import ErrorFile


class BaseFile:

    @classmethod
    def write(
            cls,
            content: str,
            path_file: str,
            mode: str = 'w',
            encoding: str = 'utf8') -> None:
        try:
            with open(file=path_file, mode=mode, encoding=encoding) as outfile:
                if type(content) == dict:
                    content = dumps(content, indent=4)
                outfile.write(content)
        except Exception:
            raise ErrorFile

    @classmethod
    def read(
            cls,
            path_file: str,
            mode: str = 'r',
            encoding: str = 'utf8') -> str:
        try:
            with open(file=path_file, mode=mode, encoding=encoding) as content:
                return content.read()
        except Exception:
            raise ErrorFile

    @classmethod
    def write_lines(
            cls,
            content: list,
            path_file: str,
            mode: str = 'w',
            encoding: str = 'utf8') -> None:
        try:
            with open(file=path_file, mode=mode, encoding=encoding) as outfile:
                outfile.writelines(content)
        except Exception:
            raise ErrorFile

    @classmethod
    def read_lines(
            cls,
            path_file: str,
            mode: str = 'r',
            encoding: str = 'utf8') -> list:
        try:
            with open(file=path_file, mode=mode, encoding=encoding) as content:
                return content.readlines()
        except Exception:
            raise ErrorFile

    @classmethod
    def touch(cls, path: str):
        try:
            cls.write(dumps(dict(), indent=4), path)
        except Exception:
            raise ErrorFile


class BaseStorage:

    backup = str(Path.home())

    def __init__(self, database: str) -> None:
        self.database = database

        if not exists(self.database):
            BaseFile.touch(path=self.database)

        system(f"cp {self.database} ~/.linux_profile_backup.json")
        self.json = loads(BaseFile.read(path_file=self.database))


class BaseSearch(BaseStorage):

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


class BaseAction(BaseSearch):

    def _create_item(self, content: dict, module: str, tag: str):
        try:
            self.json[module][tag].append(content)
            BaseFile.write(path_file=self.database, content=self.json)
        except KeyError as error:
            if error.args[0] == module:
                self.json[module] = {}
                self._create_item(content=content, module=module, tag=tag)

            if error.args[0] == tag:
                self.json[module][tag] = []
                self._create_item(content=content, module=module, tag=tag)

        except Exception:
            raise ErrorFile

    def _update_item(self, content: dict, value: str, key: str = 'id'):
        index = self._item(key=key, value=value)
        try:
            if index:
                for field in content:
                    if content.get(field):
                        self.json[index[0]][index[1]][index[2]][field] = content.get(field)
                BaseFile.write(path_file=self.database, content=self.json)
                return True
            return False
        except Exception:
            raise ErrorFile

    def _delete_item(self, value: str, key: str = 'id'):
        index = self._item(key=key, value=value)
        try:
            if index:
                self.json[index[0]][index[1]].pop(index[2])
                BaseFile.write(path_file=self.database, content=self.json)
                return True
            return False
        except Exception:
            raise ErrorFile
