#!/usr/bin/env python3

from os.path import exists
from os import mkdir, system

from linux_profile.base.storage import Storage
from linux_profile.utils.file import get_system, get_distro
from linux_profile.settings import FILE, FOLDER


class BaseConfig():

    def __init__(
            self,
            module: str = None,
            tag: str = None,
            item: str = None,
            _file: dict = FILE,
            _folder: dict = FOLDER,
            **kwargs):
        """
        Structure that defines the main variables.
        """
        self.module = module
        self.tag = tag
        self.item = item
        self.file = _file
        self.folder = _folder

        if kwargs:
            for arg in kwargs:
                setattr(self, arg, kwargs.get(arg))

        self.set_folder()
        self.set_file()

        self.class_profile = Storage(database=self.file.get('profile'))
        self.class_config = Storage(database=self.file.get('config'))

        self.setup()

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.add_config()
        self.load_config()
        self.load_profile()

    def set_folder(self) -> None:
        """
        Setup Folder

        Checks and creates the structure of configuration
        folders that are used by the package.
        """
        for folder in self.folder:
            if not exists(self.folder.get(folder)):
                mkdir(self.folder.get(folder))

    def set_file(self) -> None:
        """
        Setup File

        Checks and creates files.
        """
        if not exists(self.file.get('bash_aliases')):
            system(f"touch {self.file.get('bash_aliases')}")

    def add_config(self):
        """
        Configuring system settings

        Function that configures the basic settings of the
        operating system that the LinuxProfle package is running.

        Saved in the linux_config.json configuration file more
        specifically Hardware and Distribution information.
        """
        self.class_config.begin(module='info', tag='distro')
        if not len(self.class_config.search_tag('distro')):
            self.class_config.run(content=get_distro())

        self.class_config.begin(module='info', tag='system')
        if not len(self.class_config.search_tag('system')):
            self.class_config.run(content=get_system())

    def load_config(self) -> None:
        """
        Load Config

        Loads basic configuration information for use
        in the application and internal operations.
        """
        self.config = self.class_config.load()

    def load_profile(self) -> None:
        """
        Load Profile

        Load basic information from profiles for use in the
        application and internal operations.
        """
        self.profile = self.class_profile.load()
