"""
Module File
"""


from os import system
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
            jump: bool = True,
            encoding: str = 'utf8') -> None:
        content = dumps(content, indent=4) if dump else content
        content = f"{content}\n" if jump else content
        try:
            with open(file=path_file, mode=mode, encoding=encoding) as outfile:
                outfile.write(content)
        except PermissionError:
            cls.write_system(content=content, path_file=path_file, mode=mode)

        except Exception as error:
            raise ErrorFile(parameter=error)

    @classmethod
    def write_lines(
            cls,
            content: list,
            path_file: str,
            mode: str = 'w',
            jump: bool = True,
            encoding: str = 'utf8') -> None:
        try:
            if jump:
                content = [f"{line}\n" for line in content]
            with open(file=path_file, mode=mode, encoding=encoding) as outfile:
                outfile.writelines(content)
        except PermissionError:
            cls.write_system(content=content, path_file=path_file, mode=mode)

        except Exception as error:
            raise ErrorFile(parameter=error)

    @classmethod
    def write_system(
            cls,
            content: str,
            path_file: str,
            mode: str = ">") -> None:
        mode_write = {"w": ">", "a": ">>"}
        system(f"sudo echo {content} {mode_write.get(mode)} {path_file}")

    @classmethod
    def read(
            cls,
            path_file: str,
            mode: str = 'r',
            encoding: str = 'utf8') -> str:
        try:
            with open(file=path_file, mode=mode, encoding=encoding) as content:
                return content.read()
        except FileNotFoundError:
            cls.touch(path=path_file)
            return cls.read(path_file=path_file, mode=mode, encoding=encoding)

        except Exception as error:
            raise ErrorFile(parameter=error)

    @classmethod
    def read_lines(
            cls,
            path_file: str,
            mode: str = 'r',
            encoding: str = 'utf8') -> list:
        try:
            with open(file=path_file, mode=mode, encoding=encoding) as content:
                return content.readlines()
        except FileNotFoundError:
            cls.touch(path=path_file)
            return cls.read_lines(path_file=path_file, mode=mode, encoding=encoding)

        except Exception as error:
            raise ErrorFile(parameter=error)

    @classmethod
    def touch(cls, path: str):
        try:
            cls.write(path_file=path, content="\n", dump=False, jump=False)
        except Exception as error:
            raise ErrorFile(parameter=error)
