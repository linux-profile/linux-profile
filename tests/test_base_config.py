from os import path
from shutil import rmtree

from linux_profile.base.config import BaseConfig
from tests.settings import (
    FILE_CONFIG,
    FILE_PROFILE,
    FOLDER_CONFIG,
    FOLDER_MODULE,
    FOLDER_PROFILE
)


class Config(BaseConfig):

    def __init__(
            self,
            module: str = None,
            file_config: str = FILE_CONFIG,
            file_profile: str = FILE_PROFILE,
            folder_config: str = FOLDER_CONFIG,
            folder_profile: str = FOLDER_PROFILE,
            folder_module: str = FOLDER_MODULE):
        self.module = module
        self.file_config = file_config
        self.file_profile = file_profile
        self.folder_config = folder_config
        self.folder_profile = folder_profile
        self.folder_module = folder_module

def test_set_folder():
    test_config = Config()
    test_config.set_folder()

    assert path.isdir(FOLDER_CONFIG) == True
    assert path.isdir(FOLDER_PROFILE) == True
    assert path.isdir(FOLDER_MODULE) == True

    rmtree(FOLDER_CONFIG)


def test_add_config():
    test_config = Config()
    test_config.set_folder()
    test_config.add_config()

    assert path.isfile("{}.json".format(FILE_CONFIG)) == True

def test_load_config():
    test_config = Config()
    test_config.set_folder()
    test_config.add_config()

    test_config.load_config()

    assert test_config.distro
    assert test_config.system
