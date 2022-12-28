from json import dumps
from linux_profile.base.error import ErrorFile


class BaseFile:

    def write(
            self,
            content: str,
            path_file: str,
            mode: str = 'w',
            encoding: str = 'utf8') -> None:
        try:
            with open(file=path_file, mode=mode, encoding=encoding) as outfile:
                outfile.write(content)
        except Exception:
            raise ErrorFile

    def read(
            self,
            path_file: str,
            mode: str = 'r',
            encoding: str = 'utf8') -> str:
        try:
            with open(file=path_file, mode=mode, encoding=encoding) as content:
                return content.read()
        except Exception:
            raise ErrorFile

    def write_lines(
            self,
            content: list,
            path_file: str,
            mode: str = 'w',
            encoding: str = 'utf8') -> None:
        try:
            with open(file=path_file, mode=mode, encoding=encoding) as outfile:
                outfile.writelines(content)
        except Exception:
            raise ErrorFile

    def read_lines(
            self,
            path_file: str,
            mode: str = 'r',
            encoding: str = 'utf8') -> list:
        try:
            with open(file=path_file, mode=mode, encoding=encoding) as content:
                return content.readlines()
        except Exception:
            raise ErrorFile

    def touch(self, path: str):
        try:
            self.write(dumps(dict(), indent=4), path)
        except Exception:
            raise ErrorFile
