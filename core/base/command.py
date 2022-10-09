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
            ('module=', 'm', 'input module'),
            ('tag=', 'c', 'input tag'),
            ('value=', 'x', 'input value'),
            ('option=', 'y', 'input option'),
        ]

    modules = [
        'alias',
        'package',
        'terminal',
        'script'
    ]

    def initialize_options(self):
        self.module = None
        self.tag = None
        self.value = None
        self.option = None

    def finalize_options(self):
        if self.module is None:
            raise ErrorParameterIsMissing("module")

        if self.tag is None:
            raise ErrorParameterIsMissing("tag")

        if self.value is None:
            raise ErrorParameterIsMissing("value")

        if self.option is None:
            raise ErrorParameterIsMissing("option")

        if self.module not in self.modules:
            raise ErrorInvalidValue("module")

    def run(self):
        pass
