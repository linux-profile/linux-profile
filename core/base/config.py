#!/usr/bin/env python3

import json

from os import mkdir
from os.path import exists

from core.utils.file import get_system, get_distro, write_file, read_file
from core.settings import (
    FILE_CONFIG,
    FILE_PROFILE,
    FOLDER_CONFIG,
    FOLDER_PROFILE,
    FOLDER_MODULE
)


class BaseConfig():

    def __init__(
            self,
            module: str = None,
            file_config: str = FILE_CONFIG,
            file_profile: str = FILE_PROFILE,
            folder_config: str = FOLDER_CONFIG,
            folder_profile: str = FOLDER_PROFILE,
            folder_module: str = FOLDER_MODULE):
        """
        Structure that defines the main variables.
        """
        self.module = module
        self.file_config = file_config
        self.file_profile = file_profile
        self.folder_config = folder_config
        self.folder_profile = folder_profile
        self.folder_module = folder_module

        self.profile = {}
        self.system = {}
        self.distro = {}

        self.setup()

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.set_folder()

        self.add_config()
        self.load_config()

        self.add_profile()
        self.load_profile()

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

        if not exists(self.folder_module):
            mkdir(self.folder_module)

    def add_config(self):
        """
        Configuring system settings

        Function that configures the basic settings of the
        operating system that the LinuxProfle package is running.

        Saved in the linux_config.ini configuration file more
        specifically Hardware and Distribution information.
        """
        if not exists(self.file_config):
            config = {
                "system": get_system(),
                "distro": get_distro()
            }

            write_file(
                content=json.dumps(config, indent=4),
                path_file=self.file_config,
                type_file='.json'
            )

    def load_config(self) -> None:
        """
        Load Config

        Loads basic configuration information for use
        in the application and internal operations.
        """

        config = read_file(
            path_file=self.file_config,
            type_file='.json'
        )
        config = json.loads(config)

        self.system = config["system"]
        self.distro = config["distro"]

    def add_profile(self) -> None:
        """
        Add Profile

        Save default profile settings in linux_profile.json.
        """
        if not exists(self.file_profile):
            profile = {}

            write_file(
                content=json.dumps(profile, indent=4),
                path_file=self.file_profile,
                type_file='.json'
            )

    def load_profile(self) -> None:
        """
        Load Profile

        Load basic information from profiles for use in the
        application and internal operations.
        """

        profile = read_file(
            path_file=self.file_profile,
            type_file='.json'
        )
        self.profile = json.loads(profile)