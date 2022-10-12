#!/usr/bin/env python3

from setuptools import setup
from core.base.error import (
    ErrorInvalidValue,
    ErrorParameterIsMissing,
    ErrorLoadSettings,
    ErrorOptionIsMissing,
    ShowHelper,
    print_warning,
    print_error
)
from core.main import (
    CommandInit,
    CommandAdd,
    CommandInstall,
    CommandUninstall,
    CommandList
)

try:
    setup(
        name="linux-profile",
        author="Fernando Celmer",
        author_email="email@fernandocelmer.com",
        cmdclass={
            'init': CommandInit,
            'add': CommandAdd,
            'install': CommandInstall,
            'uninstall': CommandUninstall,
            'list': CommandList
        },
        classifiers=[
            "Operating System :: OS Independent",
            "License :: OSI Approved :: MIT License",
            'Intended Audience :: Developers',
            'Natural Language :: English',
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
        ],
        python_requires=">=3.6"
    )

except ErrorParameterIsMissing as error:
    print_warning(str(error))

except ErrorInvalidValue as error:
    print_warning(str(error))

except ErrorOptionIsMissing as error:
    print_warning(str(error))

except ErrorLoadSettings as error:
    print_error(str(error))

except ShowHelper:
    pass

except Exception as error:
    print_error(str(error))
