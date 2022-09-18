#!/usr/bin/env python

from setuptools import Command


class BaseCommand(Command):
    """ Run my command.
    """
    description = 'LinuxProfile'

    user_options = [
            ('email=', 'i', 'input email'),
            ('token=', 'i', 'input token')
        ]

    def initialize_options(self):
        self.email = None
        self.token = None

    def finalize_options(self):
        pass

    def run(self):
        pass
