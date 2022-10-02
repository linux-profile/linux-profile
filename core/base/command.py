#!/usr/bin/env python3

from setuptools import Command
from core.base.error import print_parameter_is_missing, print_error_invalid_value


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
            print_parameter_is_missing("module")

        if self.module not in self.modules:
            print_error_invalid_value("module")

    def run(self):
        pass
