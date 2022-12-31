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
            dump: bool = True,
            jump_line: bool = True,
            encoding: str = 'utf8') -> None:
        try:
            with open(file=path_file, mode=mode, encoding=encoding) as outfile:
                content = dumps(content, indent=4) if dump else content
                content = content = f"{content}\n" if jump_line else content
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
            encoding: str = 'utf8',
            jump_line: bool = True) -> None:
        try:
            if jump_line:
                content = [f"{line}\n" for line in content]

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
            cls.write(content=dict(), path_file=path)
        except Exception:
            raise ErrorFile


class BaseStorage:

    def __init__(self, database: str) -> None:
        self.database = database
        if not exists(self.database):
            BaseFile.touch(path=self.database)

        try:
            self.json = loads(BaseFile.read(path_file=self.database))
        except Exception:
            BaseFile.touch(path=self.database)
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
