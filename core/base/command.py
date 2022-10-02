#!/usr/bin/env python3

from setuptools import Command
from core.error import ErrorParameterIsMissing, ErrorInvalidValue


class BaseCommand(Command):
    """ Run command.
    """
    description = 'LinuxProfile'
    user_options = [
            ('module=', 'i', 'input module'),
            ('category=', 'i', 'input category'),
            ('value=', 'i', 'input value')
        ]

    modules = [
        'alias',
        'package',
        'terminal'
    ]

    def initialize_options(self):
        self.module = None
        self.category = None
        self.value = None

    def finalize_options(self):
        if self.module is None:
            raise ErrorParameterIsMissing("module")

        if self.module not in self.modules:
            raise ErrorInvalidValue("module")

    def run(self):
        pass
