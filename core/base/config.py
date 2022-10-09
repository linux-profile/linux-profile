#!/usr/bin/env python3

from os import mkdir
from os.path import exists

from core.base.storage import Storage
from core.utils.file import get_system, get_distro
from core.settings import FILE, FOLDER


class BaseConfig():

    def __init__(
            self,
            module: str = None,
            tag: str = None,
            value: str = None,
            option: str = None,
            _file: dict = FILE,
            _folder: dict = FOLDER):
        """
        Structure that defines the main variables.
        """
        self.module = module
        self.tag = tag
        self.value = value
        self.option = option

        self.file = _file
        self.folder = _folder
        self.set_folder()

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
