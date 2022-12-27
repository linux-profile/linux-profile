from os import system
from linux_profile.base.system import System


class HandlerPackage(System):

    def setup_system(
            self,
            sudo: bool = 'on',
            parameter: list = []):
        sudo = "sudo" if self.sudo == 'on' else ""
        parameter = " ".join(parameter)

        command = []
        commands = [sudo, self.type, self.command, self.name, parameter]
        for item in commands:
            if item:
                command.append(item)
        system(" ".join(command).replace("  ", " "))

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

    def setup_deb(self):
        path_file = f"{self.temp}/{self.file}"

        system(f"curl {self.url} --output {path_file}")
        system(f"sudo dpkg -i {path_file}")
        system("sudo apt install -f")

        # Removing the temporary installation file
        system(f"sudo rm -r {path_file}")

    def setup_shell(self):
        path_file = f"{self.temp}/{self.name}"

        system(f"curl {self.url} --output {path_file}")
        system(f"chmod +x {path_file}")
        system(path_file)

        # Removing the temporary installation file
        system(f"sudo rm -r {path_file}")
