#!/usr/bin/env python3

from setuptools import Command
from core.base.error import (
    ErrorParameterIsMissing,
    ErrorInvalidValue
)


class BaseCommand(Command):
    """ Run command.
    """
    description = 'LinuxProfile'
    user_options = [
            ('module=', 'i', 'input module'),
            ('category=', 'i', 'input category'),
            ('value=', 'i', 'input value'),
            ('option=', 'i', 'input option'),
        ]

    modules = [
        'alias',
        'package',
        'terminal',
        'script'
    ]

    def initialize_options(self):
        self.module = None
        self.category = None
        self.value = None
        self.option = None

    def finalize_options(self):
        if self.module is None:
            raise ErrorParameterIsMissing("module")

        if self.category is None:
            raise ErrorParameterIsMissing("category")

        if self.value is None:
            raise ErrorParameterIsMissing("value")

        if self.option is None:
            raise ErrorParameterIsMissing("option")

        if self.module not in self.modules:
            raise ErrorInvalidValue("module")

    def run(self):
        pass
