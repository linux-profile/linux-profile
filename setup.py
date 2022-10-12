#!/usr/bin/env python3

from setuptools import setup
from setuptools.command.install import install


class CustomInstallCommand(install):
    def run(self):
        install.run(self)


setup(
    name="linuxp",
    version="1.0.1",
    author="Fernando Celmer",
    author_email="email@fernandocelmer.com",
    cmdclass={
        'install': CustomInstallCommand,
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
        "Programming Language :: Python :: 3.10",
    ],
    include_package_data=True,
    python_requires=">=3.6",
    zip_safe=True,
    fullname='linuxp',
    entry_points={
        'console_scripts': ['linuxp=linuxp.main:main'],
    },
)
