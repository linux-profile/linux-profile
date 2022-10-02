#!/usr/bin/env python3
import json

from core.base.config import BaseConfig
from core.utils.file import write_file
from core.error import print_option_is_missing


class Add(BaseConfig):

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.add_config()
        self.load_profile()

        call_add = getattr(self, "add_"+self.module)
        call_add()

    def add_package(self):
        category = input("Package Category [default]: ")
        manager = input("Package Manager [apt, snap, dnf, pacman, zypper]: ")
        name = input("Package Name: ")

        category = category if category else 'default'

        if not manager:
            print_option_is_missing(parameter='Package Manager')

        if not name:
            print_option_is_missing(parameter='Package name')

        new_dict = {
            "type": manager,
            "name": name,
            "url": None,
            "file": None
        }

        if self.profile[self.module].get(category):
            self.profile[self.module][category].append(new_dict)

        else:
            self.profile[self.module][category] = [new_dict]

        write_file(
            content=json.dumps(self.profile, indent=4),
            path_file=self.file_profile,
            type_file='.json'
        )

    def add_alias(self):
        pass
