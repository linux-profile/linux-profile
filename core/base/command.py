from setuptools import Command
from core.settings import FILE
from core.utils.text import color
from core.base.storage import StorageQuery
from core.base.error import (
    ErrorParameterIsMissing,
    ErrorInvalidValue,
    ShowHelper
)


class BaseCommand(Command):
    """ Run command.
    """
    query = StorageQuery(FILE.get("help"))

    description = 'LinuxProfile'
    user_options = [
            ('module=', 'm', 'input module'),
            ('tag=', 't', 'input tag'),
            ('value=', 'i', 'input value'),
            ('option=', 'o', 'input option'),
            ('help=', 'h', 'input help'),
        ]

    modules = [
        'alias',
        'package',
        'terminal',
        'script'
    ]

    def initialize_options(self):
        self.module = None
        self.tag = None
        self.value = None
        self.option = None
        self.help = None

    def finalize_options(self):
        if self.module is None:
            raise ErrorParameterIsMissing("module")

        if self.tag is None:
            raise ErrorParameterIsMissing("tag")

        if self.value is None:
            raise ErrorParameterIsMissing("value")

        if self.option is None:
            raise ErrorParameterIsMissing("option")

        if self.module not in self.modules:
            raise ErrorInvalidValue("module")

    def run(self):
        try:
            data = self.query.deep_search(
                module='help',
                tag=self.distribution.script_args[0]
            )
            if self.help != 0:
                print("Documented commands (type help <topic>):")
                print(color(text=40*"=", types=['bold']))
                for text in data[0]["text"]:
                    print(text)
                print(color(text=40*"=", types=['bold']))

                raise ShowHelper()
        except:
            raise ShowHelper()
