from os import system
from core.base.error import print_not_implemented


class System(object):

    def __init__(self, type: str, command: str, name: str, **kwargs) -> None:
        self.type = type
        self.command = command
        self.name = name

        for arg in kwargs:
            value = kwargs.get(arg)
            setattr(self, arg, value)

        self.func = f"setup_{self.type}".replace("-", "_")
        if hasattr(self, self.func):
            getattr(self, self.func, None)()

    def setup_system(self, sudo: bool = True, b_arg: list = list(), l_arg: list = list()):
        sudo = "sudo" if sudo else ""
        b_arg = " ".join(b_arg)
        l_arg = " ".join(l_arg)
        command = [sudo, self.type, b_arg, self.command, self.name, l_arg]
        system(" ".join(command).replace("  ", " "))

    def setup_apt_get(self):
        if self.command == 'install':
            self.setup_system(b_arg=["-f"], l_arg=["-y", "-q"])

        if self.command == 'uninstall':
            self.command = 'remove'
            self.setup_system(l_arg=[" -y"])
        
    def setup_apt(self):
        if self.command == 'install':
            self.setup_system(b_arg=["-f"], l_arg=["-y", "-q"])

        if self.command == 'uninstall':
            self.command = 'remove'
            self.setup_system(l_arg=[" -y"])

    def setup_pacman(self):
        if self.command == 'uninstall':
            self.setup_system(b_arg=["-S"])

        if self.command == 'uninstall':
            self.command = '-R'
            self.setup_system()

    def setup_snap(self):
        if self.command == 'uninstall':
            self.command = 'remove'
        self.setup_system()

    def setup_dnf(self):
        if self.command == 'uninstall':
            self.command = 'remove'
        self.setup_system()

    def setup_zypper(self):
        if self.command == 'uninstall':
            self.command = 'rm'
        self.setup_system()

    def setup_spack(self):
        self.setup_system()

    def setup_brew(self):
        if self.command == 'uninstall':
            self.command = 'remove'
        self.setup_system()

    def setup_pip(self):
        if self.command == 'install':
            self.setup_system(sudo=False)

        if self.command == 'uninstall':
            self.setup_system(sudo=False, l_arg=[" -y"])

    def setup_deb(self):
        print_not_implemented(f"Type: [deb] - ID: {self.id}")

    def setup_sh(self):
        print_not_implemented(f"Type: [sh] - ID: {self.id}")

    def setup_py(self):
        print_not_implemented(f"Type: [py] - ID: {self.id}")
