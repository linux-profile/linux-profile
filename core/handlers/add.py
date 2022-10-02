#!/usr/bin/env python3
import uuid
import json

from core.base.log import run_profile
from core.base.error import print_error_estrange
from core.base.config import BaseConfig
from core.utils.file import write_file
from core.utils.text import color, cleaning_option
from core.base.validator import (
    ValidatorAddPackage,
    ValidatorAddAlias,
    ValidatorAddTerminal
)


class Add(BaseConfig):

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.add_config()
        self.load_profile()
        self.command = "add_"+self.module
        self.log = run_profile(name_log=self.module)

        call_add = getattr(self, self.command)
        call_add()

    def add_package(self):
        old_dict = None
        new_dict = None
        pkg_url = None
        pkg_file = None

        fields = ValidatorAddPackage(**{
                "category": input("Package Category [default]: "),
                "manager": input("Package Manager [apt-get, snap, deb]: "),
                "name": input("Package Name: ")
            }
        )

        if not fields.is_valid:
            return

        if fields.manager == 'deb':
            pkg_url = input("Package URL: ")
            pkg_file = input("Package File: ")

        old_dict = self.dict_search_key(self.module, key='name', value=fields.name)

        new_dict = {
            "id": old_dict["id"] if old_dict else fields.id,
            "type": fields.manager,
            "name": fields.name,
            "url": cleaning_option(pkg_url) if pkg_url else pkg_url,
            "file": cleaning_option(pkg_file) if pkg_file else pkg_file
        }

        self.dict_save(category=fields.category, new_dict=new_dict)

    def add_alias(self):
        old_dict = None
        new_dict = None

        fields = ValidatorAddAlias(**{
                "category": input("Alias Category [default]: "),
                "command": input("Alias Command: "),
                "content": input("Alias Content: ")
            }
        )

        if not fields.is_valid:
            return

        old_dict = self.dict_search_key(self.module, key='command', value=fields.command)

        new_dict = {
            "id": old_dict["id"] if old_dict else fields.id,
            "content": fields.content,
            "command": fields.command,
        }

        self.dict_save(category=fields.category, new_dict=new_dict)

    def add_terminal(self):
        old_dict = None
        new_dict = None

        fields = ValidatorAddTerminal(**{
                "category": input("Terminal Category [default]: "),
                "name": input("Terminal Name: ")
            }
        )

        if not fields.is_valid:
            return

        old_dict = self.dict_search_key(self.module, key='name', value=fields.name)
        category = category.lower() if category else 'default'

        new_dict = {
            "id": old_dict["id"] if old_dict else fields.id,
            "name": fields.name,
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
            path_file=self.file_profile
        )

        _id = new_dict.get("id")
        message = f"Command: {self.command} - ID: {_id}"

        self.log.info(message)

        print(
            color(
                text=message,
                types=['bold', 'green']
            )
        )
