#!/usr/bin/env python3
import uuid
import json

from core.base.log import Log
from core.error import print_option_is_missing, print_error_estrange
from core.base.config import BaseConfig
from core.utils.file import write_file
from core.utils.text import color, cleaning_option


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
        old_dict = None
        new_dict = None
        pkg_url = None
        pkg_file = None

        category = input("Package Category [default]: ")
        manager = input("Package Manager [apt-get, snap, deb]: ")
        name = input("Package Name: ")

        if manager == 'deb':
            pkg_url = input("Package URL: ")
            pkg_file = input("Package File: ")

        category = category.lower() if category else 'default'

        if not manager:
            print_option_is_missing(parameter='Package Manager')
            return

        if not name:
            print_option_is_missing(parameter='Package name')
            return

        old_dict = self.dict_search_key(self.module, key='name', value=name)

        new_dict = {
            "id": old_dict["id"] if old_dict else uuid.uuid4().hex.upper(),
            "type": cleaning_option(manager).lower(),
            "name": cleaning_option(name),
            "url": cleaning_option(pkg_url) if pkg_url else pkg_url,
            "file": cleaning_option(pkg_file) if pkg_file else pkg_file
        }

        self.dict_save(category=category, new_dict=new_dict)

    def add_alias(self):
        old_dict = None
        new_dict = None

        category = input("Alias Category [default]: ")
        command = input("Alias Command: ")
        content = input("Alias Content: ")

        category = category.lower() if category else 'default'

        if not content:
            print_option_is_missing(parameter='Alias Content')
            return

        if not command:
            print_option_is_missing(parameter='Alias Command')
            return

        old_dict = self.dict_search_key(self.module, key='command', value=command)

        new_dict = {
            "id": old_dict["id"] if old_dict else uuid.uuid4().hex.upper(),
            "content": content,
            "command": cleaning_option(command).lower(),
        }

        self.dict_save(category=category, new_dict=new_dict)

    def add_terminal(self):
        old_dict = None
        new_dict = None

        category = input("Terminal Category [default]: ")
        name = input("Terminal Name: ")

        old_dict = self.dict_search_key(self.module, key='name', value=name)
        category = category.lower() if category else 'default'

        new_dict = {
            "id": old_dict["id"] if old_dict else uuid.uuid4().hex.upper(),
            "name": name,
            "colorscheme": {},
            "profile": {
                "Appearance": {
                    "ColorScheme": None
                },
                "General": {
                    "Name": None,
                    "Parent": None
                }
            }
        }

        self.dict_save(category=category, new_dict=new_dict)

    def dict_search_key(self, module: str, key: str, value: str):
        """
        """
        for item in self.profile[module]:
            for i,x in enumerate(self.profile[module][item]):
                try:
                    if x[key] == value:
                        return self.profile[module][item].pop(i)

                except Exception as error:
                    print_error_estrange(error)

    def dict_save(self, category: str, new_dict: dict):
        """
        """
        if self.profile[self.module].get(category):
            self.profile[self.module][category].append(new_dict)
        else:
            self.profile[self.module][category] = [new_dict]

        write_file(
            content=json.dumps(self.profile, indent=4),
            path_file=self.file_profile,
            type_file='.json'
        )

        message = "New item added - {}".format(new_dict["id"])
        LOG_PROFILE = Log().run_profile()
        LOG_PROFILE.info(f"{message} - {self.module}")

        print(
            color(
                text=f"SUCCESS: {message}",
                types=['bold', 'green']
            )
        )
