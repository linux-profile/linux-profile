#!/usr/bin/env python3

from setuptools import setup
from core.base.error import print_error
from core.commands import (
    CommandInit,
    CommandAdd,
    CommandInstall,
    CommandUninstall
)

try:
    setup(
        name="linux-profile",
        cmdclass={
            'init': CommandInit,
            'add': CommandAdd,
            'install': CommandInstall,
            'uninstall': CommandUninstall
        }
    )

except Exception as error:
    print_error(error)
