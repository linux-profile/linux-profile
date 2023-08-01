from linux_profile.base.system import System


class HandlerPackage(System):

    def setup_system(self, parameter: list = []):
        if self.args:
            self.args = f"--{self.args}"

        command = [
            self.type,
            self.command,
            self.name,
            " ".join(parameter),
            self.args
        ]
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
        if hasattr(self, 'version'):
            self.name = f"{self.name}=={self.version}"

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

    def setup_poetry(self):
        if self.command == 'install':
            self.command = 'add'

        if self.command == 'uninstall':
            self.command = 'remove'

        self.setup_system()

    def setup_conda(self):
        if self.command == 'uninstall':
            self.command = 'remove'
        self.setup_system()

    def setup_gem(self):
        self.setup_system()

    def setup_npm(self):
        self.setup_system()

    def setup_yarn(self):
        if self.command == 'install':
            self.command = 'add'

        if self.command == 'uninstall':
            self.command = 'remove'

        self.setup_system()

    def setup_port(self):
        self.setup_system()

    def setup_fink(self):
        if self.command == 'uninstall':
            self.command = 'dpkg --remove'
        self.setup_system()
