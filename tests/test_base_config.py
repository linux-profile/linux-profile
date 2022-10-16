from shutil import rmtree
from os import path, remove

from linux_profile.base.config import BaseConfig
from tests.settings import file_location, folder_location


class Config(BaseConfig):

    def __init__(
            self,
            _file: dict = file_location,
            _folder: dict = folder_location,
            **kwargs):
        """
        Structure that defines the main variables.
        """
        self.file = _file
        self.folder = _folder

        if kwargs:
            for arg in kwargs:
                setattr(self, arg, kwargs.get(arg))


def test_set_folder():
    test_config = Config()
    test_config.set_folder()

    assert path.isdir(folder_location.get("config")) == True
    assert path.isdir(folder_location.get("linuxp")) == True
    assert path.isdir(folder_location.get("profile")) == True
    assert path.isdir(folder_location.get("log")) == True
    assert path.isdir(folder_location.get("temp")) == True

    rmtree(folder_location.get("config"))


def test_set_file():
    test_config = Config()
    test_config.set_file()

    assert path.isfile(file_location.get("bash_aliases")) == True
    remove(file_location.get("bash_aliases"))
