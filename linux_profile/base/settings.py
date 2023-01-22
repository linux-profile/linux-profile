"""
Module Settings
"""

from json import loads
from os import makedirs
from pathlib import Path

from linux_profile.base.file import File


def path(value: str) -> str:
    return Path.home().joinpath(value)


class Settings:

    attr_base = []
    attr_variable = []

    class Base:
        path_install = path("/opt/linuxp")
        path_temp = path("/tmp/linuxp")
        path_config = path(".config/linuxp")
        path_profile = path(".config/linuxp/profile")
        file_aliases = path(".bash_aliases")
        file_bashrc = path(".bashrc")
        file_config = "linux_config.json"

    class Variable:
        file_profile = "linux_profile.json"

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
        for attribute in ['Base', 'Variable']:
            for attr_name, attr_content in getattr(self, attribute).__dict__.items():
                if not (attr_name.startswith('_') or attr_name.endswith('_')):
                    setattr(self, attr_name, attr_content)
                    getattr(self, f"attr_{attribute.lower()}").append(attr_name)

    def _load_structure(self) -> None:
        for attribute in self.attr_base + self.attr_variable:
            try:
                if attribute.find("path") == 0:
                    makedirs(str(getattr(self, attribute)))
            except Exception:
                pass

    def _load_config(self):
        path_config = str(self.path_config.joinpath(self.file_config))
        try:
            self.config = loads(File.read(path_file=path_config))
            for attr in self.attr_variable:
                value = self.config.get(attr)
                if not value:
                    value = getattr(self, attr)
                    self.config.update({attr: value})
                    File.write(content=self.config, path_file=path_config)
                setattr(self, attr, value)

        except Exception:
            data_config = {}
            for attr in self.attr_variable:
                data_config.update({attr: getattr(self, attr)})
            File.write(path_file=path_config, content=data_config)
            self._load_config()

    def _load_profile(self):
        path_profile = str(self.path_profile.joinpath(self.file_profile))
        try:
            self.profile = loads(File.read(path_file=path_profile))
        except Exception:
            File.write(path_file=path_profile, content={})
            self._load_profile()

    @classmethod
    def join(cls, value: list, separator: str = "/") -> str:
        return separator.join(value)
