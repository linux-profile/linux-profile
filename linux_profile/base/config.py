#!/usr/bin/env python3

from os import system, mkdir
from os.path import exists

from linux_profile.base.file import BaseStorage
from linux_profile.utils.file import get_system, get_distro
from linux_profile.settings import file_location, folder_location


class BaseConfig():

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

        self.set_folder()
        self.set_file()

        self.class_profile = BaseStorage(database=self.file.get('profile'))
        self.class_config = BaseStorage(database=self.file.get('config'))

        self.setup()

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.load_profile()

    def set_folder(self) -> None:
        """
        Setup Folder

        Checks and creates the structure of configuration
        folders that are used by the package.
        """
        for folder in self.folder:
            if not exists(self.folder.get(folder)):
                try:
                    mkdir(self.folder.get(folder))
                except PermissionError:
                    system(f"sudo mkdir {self.folder.get(folder)}")

    def set_file(self) -> None:
        """
        Setup File

        Checks and creates files.
        """
        if not exists(self.file.get('bash_aliases')):
            system(f"touch {self.file.get('bash_aliases')}")


    def load_profile(self) -> None:
        """
        Load Profile

        Load basic information from profiles for use in the
        application and internal operations.
        """
        self.profile = self.class_profile.json
