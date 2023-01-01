"""
Module Action
"""


from linux_profile.base.file import File
from linux_profile.base.search import Search
from linux_profile.base.error import ErrorFile


class Action(Search):

    def _create_item(self, content: dict, module: str, tag: str):
        try:
            self.json[module][tag].append(content)
            File.write(path_file=self.database, content=self.json)
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
                File.write(path_file=self.database, content=self.json)
                return True
            return False
        except Exception:
            raise ErrorFile

    def _delete_item(self, value: str, key: str = 'id'):
        index = self._item(key=key, value=value)
        try:
            if index:
                self.json[index[0]][index[1]].pop(index[2])
                File.write(path_file=self.database, content=self.json)
                return True
            return False
        except Exception:
            raise ErrorFile
