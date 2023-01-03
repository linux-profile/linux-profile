"""
Module File
"""


from json import dumps
from linux_profile.base.error import ErrorFile


class File:

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
    def touch(cls, path: str, content={}):
        try:
            cls.write(content=content, path_file=path)
        except Exception:
            raise ErrorFile
