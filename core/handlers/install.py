#!/usr/bin/env python3
import os
from pathlib import Path

from core.settings import FILE_INSTALL_LOG
from core.base.log import run_profile
from core.base.config import BaseConfig
from core.utils.file import write_file


class Install(BaseConfig):

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.add_config()
        self.load_profile()
        self.command = "install_"+self.module
        self.log = run_profile(name_log=self.module)

        call_add = getattr(self, self.command)
        call_add()

    def install_package(self):
        if self.category:
            for item in self.profile[self.module][self.category]:
                self.run_package(
                    type_pkg=item["type"],
                    name_pkg=item["name"]
                )

        else:
            for category in self.profile[self.module]:
                for item in self.profile[self.module][category]:
                    self.run_package(
                        type_pkg=item["type"],
                        name_pkg=item["name"]
                    )

    def install_alias(self):
        if self.category:
            for item in self.profile[self.module][self.category]:
                self.run_alias(
                    command=item["command"],
                    content=item["content"]
                )
        else:
            for category in self.profile[self.module]:
                for item in self.profile[self.module][category]:
                    self.run_alias(
                        command=item["command"],
                        content=item["content"]
                    )

    def run_package(self, type_pkg: str, name_pkg: str):
        if type_pkg == 'apt-get':
            os.system(
                "sudo {type} install {name} -y >> {file}".format(
                    type=type_pkg,
                    name=name_pkg,
                    file=FILE_INSTALL_LOG
                )
            )
            self.log.info(f"Command: {self.command} - ID: {name_pkg}")

        if type_pkg == 'snap':
            os.system(
                "sudo {type} install {name} >> {file}".format(
                    type=type_pkg,
                    name=name_pkg,
                    file=FILE_INSTALL_LOG
                )
            )
            self.log.info(f"Command: {self.command} - ID: {name_pkg}")

    def run_alias(self, command: str, content: str):
        write_file(
            content=f'\nalias {command}="{content}"',
            path_file=str(Path.home()) + '/.bash_aliases',
            mode='a'
        )
