from core.base.system import System
from core.base.error import print_not_implemented


class SystemInstallPackage(System):

    def __init__(self, command = 'install', **kwargs):
        super().__init__(command=command, **kwargs)

    def setup_apt_get(self):
        self.setup_system(b_arg=["-f"], l_arg=["-y", "-q"])

    def setup_apt(self):
        self.setup_system(b_arg=["-f"], l_arg=["-y", "-q"])

    def setup_pacman(self):
        self.setup_system(b_arg=["-S"])

    def setup_snap(self):
        self.setup_system()

    def setup_dnf(self):
        self.setup_system()

    def setup_zypper(self):
        self.setup_system()

    def setup_spack(self):
        self.setup_system()

    def setup_brew(self):
        self.setup_system()

    def setup_pip(self):
        self.setup_basic(sudo=False)

    def setup_deb(self):
        print_not_implemented(f"ID: {self.id}")

    def setup_sh(self):
        print_not_implemented(f"ID: {self.id}")

    def setup_py(self):
        print_not_implemented(f"ID: {self.id}")
