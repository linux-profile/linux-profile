#!/usr/bin/env python

from setuptools import setup
from command import Init, Add, Sync


setup(
        name="linux-profile",
        cmdclass={
                'init': Init,
                'add': Add,
                'sync': Sync
            }
    )
