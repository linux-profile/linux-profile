#!/usr/bin/env python3

from setuptools import Command


class BaseCommand(Command):
    """ Run command.
    """
    description = 'LinuxProfile'
    user_options = [
            ('module=', 'i', 'input module'),
            ('value=', 'i', 'input value')
        ]

    modules = [
        'alias',
        'packages'
    ]

    def initialize_options(self):
        self.module = None
        self.value = None

    def finalize_options(self):
        pass

    def run(self):
        pass
