#!/usr/bin/env python3

from core.base.config import BaseConfig
from core.base.setup import SetupPackage, SetupAlias


class Install(BaseConfig):

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.add_config()
        self.load_config()
        self.load_profile()

        func = f"{self.__class__.__name__}_{self.module}".lower()
        call_add = getattr(self, func)
        call_add()

    def install_package(self):
        if self.category:
            for item in self.profile[self.module][self.category]:
                SetupPackage(**item)
        else:
            for category in self.profile[self.module]:
                for item in self.profile[self.module][category]:
                    SetupPackage(**item)


    def install_alias(self):
        if self.category:
            for item in self.profile[self.module][self.category]:
                SetupAlias(**item)
        else:
            for category in self.profile[self.module]:
                for item in self.profile[self.module][category]:
                    SetupAlias(**item)
