"""
Module Command
"""


from linux_profile import (
    __version__,
    __info__
)
from linux_profile.base.error import (
    ErrorInvalidValue,
    ErrorParameterIsMissing,
    ErrorLoadSettings,
    ErrorOptionIsMissing,
    ErrorOptionIsInvalid,
    ErrorArgumentIsInvalid,
    ErrorFile,
    print_warning,
    print_error
)


class Command:

    list_option = ['id', 'module', 'tag', 'item', 'sudo', 'debug', 'group']

    def __init__(self, parser, arguments) -> None:
        self.parser = parser
        self.arguments = arguments

        self.setup_options()
        self.execute()

    def is_bool(self, value: str) -> str:
        bool_list = [
            ("on", True),
            ("true", True),
            ("True", True),
            ("1", True),
            ("yes", True),
            ("ok", True),
            ("y", True),
            ("Y", True),
            ("of", False),
            ("false", False),
            ("False", False),
            ("0", False),
            ("no", False),
            ("not", False),
            ("n", False),
            ("N", False)
        ]
        for item in bool_list:
            if value in item:
                return item[1]

        return value

    def setup_options(self):
        for option in self.list_option:
            if hasattr(self.arguments, option):
                setattr(self, option, self.is_bool(getattr(self.arguments, option)))
            else:
                setattr(self, option, None)


class BaseCommand:

    def __init__(self, parser):
        self.parser = parser
        self.subparsers = self.parser.add_subparsers()

        self.argument_module = {
            "required": True,
            "choices": ['package', 'alias', 'script', 'file']}

        self.argument_option = {
            "default": "of",
            "choices": ['on', 'of']}

        self.parser._positionals.title = 'Commands'
        self.parser._optionals.title = 'Default Options'
        self.parser.add_argument(
            '-v',
            '--version',
            action='version',
            version=f'linuxp=={__version__}',
            help="Show program's version number and exit.")

        self.help = {
            "config": "Settings file management.",
            "profile": "Profile file management.",
            "add": "Parameter used to add a new item to the list in your profile file.",
            "remove": "Removes items from the profile file.",
            "install": "This parameter is used to install the modules, package, alias and script.",
            "uninstall": "Command used to uninstall items. Be very careful when running.",
            "list": "Lists all modules in the terminal and can also apply filters to find items."
        }

        self.setup_config()
        self.setup_profile()
        self.setup_add()
        self.setup_remove()
        self.setup_execute()
        self.setup_install()
        self.setup_uninstall()
        self.setup_list()

    def setup_config(self):
        self.cmd_config = self.subparsers.add_parser(
            'config', help=self.help.get("config"))

        help_url = "URL to download and sync config."

        self.cmd_config = self.cmd_config.add_argument_group(
            'Usage: linuxp config [OPTIONS]')
        self.cmd_config.add_argument('--url', help=help_url)

    def setup_profile(self):
        self.cmd_profile = self.subparsers.add_parser(
            'profile', help=self.help.get("profile"))

        help_url = "URL to download and sync profile."
        help_output = "File name to save."
        help_switch = "File name for profile switching."
        help_new = " Creates a new profile."
        help_delete = "Deletes a profile."
        help_list = "Argument to list existing profiles"

        self.cmd_profile = self.cmd_profile.add_argument_group(
            'Usage: linuxp profile [OPTIONS]')
        self.cmd_profile.add_argument('--url', help=help_url)
        self.cmd_profile.add_argument('--output', help=help_output)
        self.cmd_profile.add_argument('--switch', help=help_switch)
        self.cmd_profile.add_argument('--new', help=help_new)
        self.cmd_profile.add_argument('--delete', help=help_delete)
        self.cmd_profile.add_argument('--list', action='store_true', help=help_list)

    def setup_add(self):
        self.cmd_add = self.subparsers.add_parser(
            'add', help=self.help.get("add"))

        self.cmd_add = self.cmd_add.add_argument_group(
            'Usage: linuxp add [OPTIONS]')
        self.cmd_add.add_argument('-m', '--module', **self.argument_module)

    def setup_remove(self):
        self.cmd_remove = self.subparsers.add_parser(
            'remove', help=self.help.get("remove"))

        help_id = "Reference ID of a storage item."

        self.cmd_remove = self.cmd_remove.add_argument_group(
            'Usage: linuxp remove [OPTIONS]')
        self.cmd_remove.add_argument('--id', required=True, help=help_id)

    def setup_execute(self):
        self.cmd_execute = self.subparsers.add_parser('execute')

        help_id = "Reference ID of a storage item."

        self.cmd_execute = self.cmd_execute.add_argument_group(
            'Usage: linuxp execute [OPTIONS]')
        self.cmd_execute.add_argument('--id', required=True, help=help_id)

    def setup_install(self):
        self.cmd_install = self.subparsers.add_parser(
            'install', help=self.help.get("install"))

        help_sudo = "Run the command with system root permissions."
        help_debug = "Run a command in test mode. It only shows the command."
        help_group = "Group items for executing a command."

        self.cmd_install = self.cmd_install.add_argument_group(
            'Usage: linuxp install [OPTIONS]')
        self.cmd_install.add_argument('-m', '--module', **self.argument_module)
        self.cmd_install.add_argument('-t', '--tag')
        self.cmd_install.add_argument('-i', '--item')
        self.cmd_install.add_argument('--sudo', action='store_true', help=help_sudo)
        self.cmd_install.add_argument('--debug', action='store_true', help=help_debug)
        self.cmd_install.add_argument('--group', action='store_true', help=help_group)

    def setup_uninstall(self):
        self.cmd_uninstall = self.subparsers.add_parser(
            'uninstall', help=self.help.get("uninstall"))

        help_sudo = "Run the command with system root permissions."
        help_debug = "Run a command in test mode. It only shows the command."
        help_group = "Group items for executing a command."

        self.cmd_uninstall = self.cmd_uninstall.add_argument_group(
            'Usage: linuxp uninstall [OPTIONS]')
        self.cmd_uninstall.add_argument('-m', '--module', **self.argument_module)
        self.cmd_uninstall.add_argument('-t', '--tag')
        self.cmd_uninstall.add_argument('-i', '--item')
        self.cmd_uninstall.add_argument('--sudo', action='store_true', help=help_sudo)
        self.cmd_uninstall.add_argument('--debug', action='store_true', help=help_debug)
        self.cmd_uninstall.add_argument('--group', action='store_true', help=help_group)

    def setup_list(self):
        self.cmd_list = self.subparsers.add_parser(
            'list', help=self.help.get("list"))

        self.cmd_list = self.cmd_list.add_argument_group(
            'Usage: linuxp list [OPTIONS]')
        self.cmd_list.add_argument('-m', '--module', **self.argument_module)
        self.cmd_list.add_argument('-t', '--tag')
        self.cmd_list.add_argument('-i', '--item')

    def run(self):
        try:
            arguments = self.parser.parse_args()
            if hasattr(arguments, 'exec'):
                arguments.exec(parser=self.parser, arguments=arguments)
            else:
                try:
                    import urllib.request
                    text_ascii = urllib.request.urlopen(
                        "https://linuxprofile.com/text-ascii").read().decode('utf-8')
                except Exception:
                    text_ascii = f"\nLinuxProfile {__version__}"

                print(text_ascii + __info__)

        except ErrorParameterIsMissing as error:
            print_warning(str(error))

        except ErrorOptionIsMissing as error:
            print_warning(str(error))

        except ErrorOptionIsInvalid as error:
            print_warning(str(error))

        except ErrorInvalidValue as error:
            print_warning(str(error))

        except ErrorArgumentIsInvalid as error:
            print_warning(str(error))

        except ErrorLoadSettings as error:
            print_error(str(error))

        except ErrorFile as error:
            print_error(str(error))

        except Exception as error:
            print_error(str(error))
