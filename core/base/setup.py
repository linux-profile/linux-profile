import os
from pathlib import Path

from core.base.error import print_error, print_not_implemented
from core.utils.file import write_file


class Setup():

    def __init__(self, **kwargs):
        for arg in kwargs:
            value = kwargs.get(arg)
            setattr(self, arg, value)

        func = f"setup_{self.type}".replace("-", "_")
        if hasattr(self, func):
            getattr(self, func, None)()


class SetupPackage(Setup):

    def setup_default(
            self,
            b_arg: str = '',
            l_arg: str = '',
            log: str = ''):
        try:
            command = "sudo {type}{b_arg} install {name}{l_arg}{log}".format(
                    type=self.type,
                    name=self.name,
                    b_arg=b_arg,
                    l_arg=l_arg,
                    log=log
                )
            os.system(command)
        except Exception as error:
            print_error(error)

    def setup_apt_get(self):
        self.setup_default(b_arg=" -f", l_arg=" -y -q")

    def setup_apt(self):
        self.setup_default(b_arg=" -f", l_arg=" -y -q")

    def setup_snap(self):
        self.setup_default()

    def setup_deb(self):
        print_not_implemented(f"ID: {self.id}")

    def setup_sh(self):
        print_not_implemented(f"ID: {self.id}")

    def setup_py(self):
        print_not_implemented(f"ID: {self.id}")

    def setup_dnf(self):
        self.setup_default()

    def setup_pacman(self):
        self.setup_default(b_arg=" -S")

    def setup_zypper(self):
        self.setup_default()

    def setup_spack(self):
        self.setup_default()

    def setup_brew(self):
        self.setup_default()


class SetupAlias(Setup):

    def setup_exec(self):
        write_file(
            content=f'\nalias {self.command}="{self.content}"',
            path_file=str(Path.home()) + '/.bash_aliases',
            mode='a'
        )
