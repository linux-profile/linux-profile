#!/usr/bin/env python3

from core.base.storage import Storage
from core.base.config import BaseConfig
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
        self.load_config()
        self.load_profile()

        self.data = Storage(database=self.file_profile)

        func = f"{self.__class__.__name__}_{self.module}".lower()
        call_add = getattr(self, func)
        call_add()

    def add_package(self):
        fields = ValidatorAddPackage(**{
                "category": input("Package Category [default]: "),
                "manager": input("Package Manager: "),
                "name": input("Package Name: "),
                "url": input("Package URL: "),
                "file": input("Package File: ")
            }
        )

        if not fields.is_valid:
            return

        self.data.begin(module=self.module, tag=fields.category)
        self.data.run(
            content=fields.__dict__,
            key='name'
        )

    def add_alias(self):
        fields = ValidatorAddAlias(**{
                "category": input("Alias Category [default]: "),
                "command": input("Alias Command: "),
                "content": input("Alias Content: "),
                "type": "exec"
            }
        )

        if not fields.is_valid:
            return

        self.data.begin(module=self.module, tag=fields.category)
        self.data.run(
            content=fields.__dict__,
            key='command'
        )

    def add_terminal(self):
        fields = ValidatorAddTerminal(**{
                "category": input("Terminal Category [default]: "),
                "name": input("Terminal Name: ")
            }
        )

        if not fields.is_valid:
            return

        self.data.begin(module=self.module, tag=fields.category)
        self.data.run(
            content={
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
            },
            key='name'
        )
