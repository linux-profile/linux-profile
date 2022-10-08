#!/usr/bin/env python3

from setuptools import setup
from core.commands import (
        CommandInit,
        CommandAdd,
        CommandInstall,
        CommandUninstall
)


setup(
        name="linux-profile",
        cmdclass={
                'init': CommandInit,
                'add': CommandAdd,
                'install': CommandInstall,
                'uninstall': CommandUninstall
            }
    )
