from linux_profile.base.system import System


class HandlerPackage(System):

    def setup_system(self, parameter: list = []):
        command = [self.type, self.command, self.name, " ".join(parameter)]
        self.system(cmd=command)

    def setup_apt_get(self):
        if self.command == 'install':
            self.setup_system(parameter=["-y"])

        if self.command == 'uninstall':
            self.command = 'remove'
            self.setup_system(parameter=["-y"])

    def setup_apt(self):
        if self.command == 'install':
            self.setup_system(parameter=["-y"])

        if self.command == 'uninstall':
            self.command = 'remove'
            self.setup_system(parameter=["-y"])

    def setup_snap(self):
        if self.command == 'uninstall':
            self.command = 'remove'
        self.setup_system()

    def setup_yum(self):
        if self.command == 'uninstall':
            self.command = 'remove'
        self.setup_system()

    def setup_dnf(self):
        if self.command == 'uninstall':
            self.command = 'remove'
        self.setup_system()

    def setup_pacman(self):
        if self.command == 'install':
            self.command = '-S'
            self.setup_system()

        if self.command == 'uninstall':
            self.command = '-R'
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
            self.setup_system()

        if self.command == 'uninstall':
            self.setup_system(parameter=[" -y"])

    def setup_swupd(self):
        if self.command == 'install':
            self.command = 'bundle-add'

        if self.command == 'uninstall':
            self.command = 'bundle-remove'

        self.setup_system()

    def setup_guix(self):
        if self.command == 'uninstall':
            self.command = 'remove'
        self.setup_system()

    def setup_flatpak(self):
        self.setup_system()
