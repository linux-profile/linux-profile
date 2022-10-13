#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from linux_profile import __version__
from setuptools import setup
from setuptools.command.install import install


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


class CustomInstallCommand(install):
    def run(self):
        install.run(self)


setup(
    name="linuxp",
    version=__version__,
    author="Fernando Celmer",
    author_email="email@fernandocelmer.com",
    description="Linux profile management tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MyLinuxProfile/linux-profile",
    cmdclass={
        'install': CustomInstallCommand,
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    include_package_data=True,
    python_requires=">=3.6",
    zip_safe=True,
    fullname='linuxp',
    entry_points={
        'console_scripts': ['linuxp=linux_profile.main:main'],
    },
)
