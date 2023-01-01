"""
Module Config
"""


from os import getenv, makedirs
from json import loads
from pathlib import Path
from linux_profile.base.file import File


PATH = str(Path.home())


class Config:

    attributes = []

    class Meta:
        linuxp_path = "/opt/linuxp"
        linuxp_path_config = f"{PATH}/.config/linuxp"
        linuxp_path_temp = "/tmp/linuxp"
        linuxp_file_profile = "linux_profile.json"
        linuxp_file_config = "linux_profile.conf"

    def __init__(self, **kwargs) -> None:
        self.profile = None
        self.config = None

        for arg in kwargs:
            setattr(self, arg, kwargs.get(arg))

        self._load_attributes()
        self._load_structure()
        self._load_storage()

        self.setup()

    def setup(self) -> str:
        return "Method not Implemented"

    def _load_attributes(self) -> None:
        for attr_name, attr_content in self.Meta.__dict__.items():
            if not (attr_name.startswith('_') or attr_name.endswith('_')):
                self.attributes.append(attr_name)

                attr = self.local_getattr(key=attr_name)
                if not attr:
                    self.local_setattr(key=attr_name, value=attr_content)
                setattr(self, attr_name, attr_content)

    def _load_structure(self) -> None:
        for item in self.attributes:
            if item.find("path") > 0:
                try:
                    makedirs(getattr(self, item))
                except Exception:
                    pass

    def _load_storage(self) -> None:
        path_profile = self.join(
            [self.linuxp_path_config, self.linuxp_file_profile])
        path_config = self.join(
            [self.linuxp_path_config, self.linuxp_file_config])

        try:
            self.profile = loads(File.read(path_file=path_profile))
        except Exception:
            File.touch(path=path_profile)
            self._load_storage()

        try:
            self.config = loads(File.read(path_file=path_config))
        except Exception:
            File.touch(path=path_config, content="")
            self._load_storage()

    @classmethod
    def join(cls, value: list, separator: str = "/") -> str:
        return separator.join(value)

    @classmethod
    def local_getattr(cls, key: str, path_file: str = None) -> str:
        path_file = path_file if path_file else cls.join([PATH, ".bashrc"])
        key_value = getenv(key.upper())
        if not key_value:
            bashrc = File.read_lines(path_file=path_file)
            for line in bashrc:
                if line.find("export") == 0:
                    text = line.split("=")
                    if key.upper() == text[0][7:]:
                        return loads(text[1])
        return key_value

    @classmethod
    def local_setattr(
            cls,
            key: str,
            value: str,
            path_file: str = None) -> None:
        path_file = path_file if path_file else cls.join([PATH, ".bashrc"])
        File.write(
            content=f'export {key.upper()}="{value}"',
            path_file=path_file,
            mode='a',
            dump=False
        )
