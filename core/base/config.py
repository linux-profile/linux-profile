#!/usr/bin/env python3

import json

from os import mkdir
from os.path import exists
from core.base.json import JsonData
from core.utils.file import (
    get_system,
    get_distro,
    write_file,
    read_file
)
from core.settings import (
    FILE_CONFIG,
    FILE_PROFILE,
    FOLDER_CONFIG,
    FOLDER_LOG
)


class BaseConfig():

    def __init__(
            self,
            module: str = None,
            category: str = None,
            value: str = None,
            file_config: str = FILE_CONFIG,
            file_profile: str = FILE_PROFILE,
            folder_config: str = FOLDER_CONFIG,
            folder_log: str = FOLDER_LOG):
        """
        Structure that defines the main variables.
        """
        self.module = module
        self.category = category
        self.value = value
        self.file_config = file_config
        self.file_profile = file_profile
        self.folder_config = folder_config
        self.folder_log = folder_log

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
        folders = [
            self.folder_config,
            self.folder_log
        ]
        for folder in folders:
            if not exists(folder):
                mkdir(folder)

    def add_config(self):
        """
        Configuring system settings

        Function that configures the basic settings of the
        operating system that the LinuxProfle package is running.

        Saved in the linux_config.ini configuration file more
        specifically Hardware and Distribution information.
        """
        data = JsonData(database=self.file_config)

        data.load(module='info', tag='distro')
        data.insert(content=get_distro())

        data.load(module='info', tag='system')
        data.insert(content=get_system())

    def load_config(self) -> None:
        """
        Load Config

        Loads basic configuration information for use
        in the application and internal operations.
        """
        data = JsonData(database=self.file_config)

        data.load(module='info', tag='system')
        self.system = data.search_tag(tag='system')

        data.load(module='info', tag='distro')
        self.distro = data.search_tag(tag='distro')

    def add_profile(self) -> None:
        """
        Add Profile

        Save default profile settings in linux_profile.json.
        """

        if not exists(self.file_profile):
            write_file(
                content=json.dumps(dict(), indent=4),
                path_file=self.file_profile
            )

    def load_profile(self) -> None:
        """
        Load Profile

        Load basic information from profiles for use in the
        application and internal operations.
        """

        profile = read_file(
            path_file=self.file_profile
        )
        self.profile = json.loads(profile)
