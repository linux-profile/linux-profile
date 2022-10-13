from linux_profile.base.error import (
    ErrorInvalidValue,
    ErrorParameterIsMissing,
    ErrorLoadSettings,
    ErrorOptionIsMissing,
    print_warning,
    print_error
)


class Command():

    list_option = ['module', 'tag', 'value']

    def __init__(self, parser, arguments) -> None:
        self.parser = parser
        self.arguments = arguments

        self.setup_options()
        self.execute()

    def setup_options(self):
        self.module = None
        self.tag = None
        self.value = None

        for item in self.list_option:
            if hasattr(self.arguments, item):
                setattr(self, item, getattr(self.arguments, item))


class BaseCommand:

    list_module = ['package', 'alias', 'script']

    def __init__(self, parser):
        self.parser = parser
        self.subparsers = self.parser.add_subparsers()

        self.argument_module = {"required": True, "choices":self.list_module}

        self.setup_init()
        self.setup_add()
        self.setup_install()
        self.setup_uninstall()
        self.setup_list()

    def setup_init(self):
        self.cmd_init = self.subparsers.add_parser('init')

    def setup_add(self):
        self.cmd_add = self.subparsers.add_parser('add')
        self.cmd_add.add_argument('--module', '-m', **self.argument_module)

    def setup_install(self):
        self.cmd_install = self.subparsers.add_parser('install')
        self.cmd_install.add_argument('--module', '-m', **self.argument_module)
        self.cmd_install.add_argument('--tag', '-t')
        self.cmd_install.add_argument('--value', '-v')

    def setup_uninstall(self):
        self.cmd_uninstall = self.subparsers.add_parser('uninstall')
        self.cmd_uninstall.add_argument('--module', '-m', **self.argument_module)
        self.cmd_uninstall.add_argument('--tag', '-t')
        self.cmd_uninstall.add_argument('--value', '-v')

    def setup_list(self):
        self.cmd_list = self.subparsers.add_parser('list')
        self.cmd_list.add_argument('--module', '-m', **self.argument_module)
        self.cmd_list.add_argument('--tag', '-t')
        self.cmd_list.add_argument('--value', '-v')

    def run(self):
        try:

            arguments = self.parser.parse_args()
            arguments.exec(parser=self.parser, arguments=arguments)

        except ErrorParameterIsMissing as error:
            print_warning(str(error))

        except ErrorInvalidValue as error:
            print_warning(str(error))

        except ErrorOptionIsMissing as error:
            print_warning(str(error))

        except ErrorLoadSettings as error:
            print_error(str(error))

        except Exception as error:
            print_error(str(error))
