"""
Module Settings
"""


from os import makedirs
from json import loads
from pathlib import Path

from linux_profile.base.file import File


def config_path(value: str) -> str:
    home = str(Path.home())
    return "/".join([home, value])


class Settings:

    attributes = []

    class Base:
        path_install = "/opt/linuxp"
        path_temp = "/tmp/linuxp"
        path_config = config_path(".config/linuxp")
        file_aliases = config_path(".bash_aliases")
        file_bashrc = config_path(".bashrc")
        file_profile = "linux_profile.json"
        file_config = "linux_config.json"

    def __init__(self, **kwargs) -> None:
        self.profile = {}
        self.config = {}

        for arg in kwargs:
            setattr(self, arg, kwargs.get(arg))

        self._load_attributes()
        self._load_structure()
        self._load_config()
        self._load_profile()

        self.setup()

    def setup(self) -> str:
        return "Method not Implemented"

    def _load_attributes(self) -> None:
        for attr_name, attr_content in self.Base.__dict__.items():
            if not (attr_name.startswith('_') or attr_name.endswith('_')):
                setattr(self, attr_name, attr_content)
                self.attributes.append(attr_name)

    def _load_structure(self) -> None:
        for item in self.attributes:
            if item.find("path") == 0:
                try:
                    makedirs(getattr(self, item))
                except Exception:
                    pass

    def _load_config(self):
        path_config = self.join(
            [self.path_config, self.file_config])

        try:
            self.config = loads(File.read(path_file=path_config))
            for attr in self.attributes:
                value = self.config.get(attr)
                if not value:
                    value = getattr(self, attr)
                    self.config.update({attr: value})
                    File.write(content=self.config, path_file=path_config)
                setattr(self, attr, value)

        except Exception:
            data_config = {}
            for attr in self.attributes:
                data_config.update({attr: getattr(self, attr)})
            File.write(path_file=path_config, content=data_config)
            self._load_config()

    def _load_profile(self):
        path_profile = self.join(
            [self.path_config, self.file_profile])

        try:
            self.profile = loads(File.read(path_file=path_profile))
        except Exception:
            File.write(path_file=path_profile, content={})
            self._load_profile()

    @classmethod
    def join(cls, value: list, separator: str = "/") -> str:
        return separator.join(value)
