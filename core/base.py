#!/usr/bin/env python3

import json

from os import mkdir
from os.path import exists
from setuptools import Command

from core.utils.file import get_system, get_distro, write_file
from core.settings.config import (
    FILE_CONFIG,
    FOLDER_CONFIG,
    FOLDER_PROFILE,
    FOLDER_MODULE
)


class BaseConfig():

    def __init__(
            self,
            file_config: str = FILE_CONFIG,
            folder_config: str = FOLDER_CONFIG,
            folder_profile: str = FOLDER_PROFILE,
            folder_modele: str = FOLDER_MODULE):
        """
        Structure that defines the main variables.
        """
        self.file_config = file_config
        self.folder_config = folder_config
        self.folder_profile = folder_profile
        self.folder_modele = folder_modele
        self.setup()

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.set_folder()
        self.add_config()

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

        if not exists(self.folder_modele):
            mkdir(self.folder_modele)

    def add_config(self):
        """
        Configuring system settings

        Function that configures the basic settings of the
        operating system that the LinuxProfle package is running.

        Saved in the linux_config.ini configuration file more
        specifically Hardware and Distribution information.
        """

        config = {
            "system": get_system(),
            "distro": get_distro()
        }

        write_file(
            content=json.dumps(config, indent=4),
            path_file=self.file_config,
            type_file='.json'
        )


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
