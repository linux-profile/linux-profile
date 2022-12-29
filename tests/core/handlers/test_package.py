from linux_profile.handlers.package import HandlerPackage


item_install = {
    "debug": True,
    "sudo": "of",
    "command": "install", 
    "name": "konsole"
}

item_uninstall = {
    "debug": True,
    "sudo": "of",
    "command": "uninstall", 
    "name": "konsole"
}


def test_handlers_package_install_sudo_on():
    item_install["sudo"] = 'on'
    output = HandlerPackage(type="apt", **item_install)
    assert output.debug_command == "sudo apt install konsole -y"


def test_handlers_package_install_sudo_of():
    item_install["sudo"] = 'of'
    output = HandlerPackage(type="apt", **item_install)
    assert output.debug_command == "apt install konsole -y"


def test_handlers_package_install_apt_get():
    output = HandlerPackage(type="apt-get", **item_install)
    assert output.debug_command == "apt-get install konsole -y"


def test_handlers_package_install_apt():
    output = HandlerPackage(type="apt", **item_install)
    assert output.debug_command == "apt install konsole -y"


def test_handlers_package_install_snap():
    output = HandlerPackage(type="snap", **item_install)
    assert output.debug_command == "snap install konsole"


def test_handlers_package_install_yum():
    output = HandlerPackage(type="yum", **item_install)
    assert output.debug_command == "yum install konsole"


def test_handlers_package_install_dnf():
    output = HandlerPackage(type="dnf", **item_install)
    assert output.debug_command == "dnf install konsole"


def test_handlers_package_install_pacman():
    output = HandlerPackage(type="pacman", **item_install)
    assert output.debug_command == "pacman -S konsole"


def test_handlers_package_install_zypper():
    output = HandlerPackage(type="zypper", **item_install)
    assert output.debug_command == "zypper install konsole"


def test_handlers_package_install_spack():
    output = HandlerPackage(type="spack", **item_install)
    assert output.debug_command == "spack install konsole"


def test_handlers_package_install_brew():
    output = HandlerPackage(type="brew", **item_install)
    assert output.debug_command == "brew install konsole"


def test_handlers_package_install_pip():
    output = HandlerPackage(type="pip", **item_install)
    assert output.debug_command == "pip install konsole"


def test_handlers_package_uninstall_apt_get():
    output = HandlerPackage(type="apt-get", **item_uninstall)
    assert output.debug_command == "apt-get remove konsole -y"


def test_handlers_package_uninstall_apt():
    output = HandlerPackage(type="apt", **item_uninstall)
    assert output.debug_command == "apt remove konsole -y"


def test_handlers_package_uninstall_snap():
    output = HandlerPackage(type="snap", **item_uninstall)
    assert output.debug_command == "snap remove konsole"


def test_handlers_package_uninstall_yum():
    output = HandlerPackage(type="yum", **item_uninstall)
    assert output.debug_command == "yum remove konsole"


def test_handlers_package_uninstall_dnf():
    output = HandlerPackage(type="dnf", **item_uninstall)
    assert output.debug_command == "dnf remove konsole"


def test_handlers_package_uninstall_pacman():
    output = HandlerPackage(type="pacman", **item_uninstall)
    assert output.debug_command == "pacman -R konsole"


def test_handlers_package_uninstall_zypper():
    output = HandlerPackage(type="zypper", **item_uninstall)
    assert output.debug_command == "zypper rm konsole"


def test_handlers_package_uninstall_spack():
    output = HandlerPackage(type="spack", **item_uninstall)
    assert output.debug_command == "spack uninstall konsole"


def test_handlers_package_uninstall_brew():
    output = HandlerPackage(type="brew", **item_uninstall)
    assert output.debug_command == "brew remove konsole"


def test_handlers_package_uninstall_pip():
    output = HandlerPackage(type="pip", **item_uninstall)
    assert output.debug_command == "pip uninstall konsole -y"
