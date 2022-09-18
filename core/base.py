#!/usr/bin/env python3

from os import mkdir
from os.path import exists
from setuptools import Command

from core.settings.config import (
    FILE_CONFIG,
    FOLDER_CONFIG,
    FOLDER_PROFILE
)


class BaseConfig():

    def __init__(
            self,
            file_config: str = FILE_CONFIG,
            folder_config: str = FOLDER_CONFIG,
            folder_profile: str = FOLDER_PROFILE):
        """
        Structure that defines the main variables.
        """
        self.file_config = file_config
        self.folder_config = folder_config
        self.folder_profile = folder_profile

        self.setup()

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.set_folder()

    def set_folder(self) -> None:
        """
        Setup Folder

        Checks and creates the structure of configuration
        folders that are used by the package.
        """
        if not exists(self.folder_config):
            mkdir(self.folder_config)

        if not exists(self.folder_profile):
            mkdir(self.folder_profile)


class BaseCommand(Command):
    """ Run my command.
    """
    description = 'LinuxProfile'

    user_options = [
            ('email=', 'i', 'input email'),
            ('token=', 'i', 'input token')
        ]

    def initialize_options(self):
        self.email = None
        self.token = None

    def finalize_options(self):
        pass

    def run(self):
        pass
