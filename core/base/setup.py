import os
from pathlib import Path

from core.base.error import print_not_implemented
from core.utils.file import write_file


class Setup():

    SUDO = 'sudo'
    INSTALL = 'install'
    UNINSTALL = 'uninstall'
    SEARCH = 'serach'
    DELETE = 'delete'
    REMOVE = 'remove'
    LIST = 'list'
    CONFIG = 'config'
    B_ARG = ''
    L_ARG = ''
    LOG = ''

    def __init__(self, **kwargs):
        for arg in kwargs:
            value = kwargs.get(arg)
            setattr(self, arg, value)

        self.run = getattr(Setup, self.command.upper())
        self.func = f"setup_{self.type}".replace("-", "_")

        if hasattr(self, self.func):
            getattr(self, self.func, None)()

    def setup(
            self,
            sudo: str = SUDO,
            run: str = None,
            b_arg: list = list(),
            l_arg: list = list(),
            log: str = LOG):
        b_arg = " ".join(b_arg)
        l_arg = " ".join(l_arg)
        run = run if run else self.run

        command = [sudo, self.type, b_arg, run, self.name, l_arg, log]
        os.system(" ".join(command).replace("  ", " "))


class SetupPackage(Setup):

    def setup_apt_get(self):
        self.setup(b_arg=["-f"], l_arg=["-y", "-q"])

    def setup_apt(self):
        self.setup(b_arg=["-f"], l_arg=["-y", "-q"])

    def setup_snap(self):
        self.setup()

    def setup_deb(self):
        print_not_implemented(f"ID: {self.id}")

    def setup_sh(self):
        print_not_implemented(f"ID: {self.id}")

    def setup_py(self):
        print_not_implemented(f"ID: {self.id}")

    def setup_dnf(self):
        self.setup()

    def setup_pacman(self):
        self.setup(run=self.run, b_arg=["-S"])

    def setup_zypper(self):
        self.setup()

    def setup_spack(self):
        self.setup()

    def setup_brew(self):
        self.setup()


class SetupAlias(Setup):

    def setup_exec(self):
        write_file(
            content=f'\nalias {self.command}="{self.content}"',
            path_file=str(Path.home()) + '/.bash_aliases',
            mode='a'
        )
