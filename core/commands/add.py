from core.utils.text import option
from core.base.storage import Storage
from core.base.config import BaseConfig
from core.base.validator import (
    InputAddPackage,
    InputAddAlias,
    InputAddTerminal,
    InputAddScript
)


class Add(BaseConfig):

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.add_config()
        self.load_config()
        self.load_profile()
        self.command = self.__class__.__name__.lower()
        self.data = Storage(database=self.file.get("profile"))

        func = f"{self.command }_{self.module}"
        call = getattr(self, func, self)
        call()

    def add_package(self):
        fields = InputAddPackage(**{
                "category": option(text="Package Category [default]: "),
                "type": option(text="Package Manager: ", required=True),
                "name": option(text="Package Name: ", required=True),
                "url": option(text="Package URL: "),
                "file": option(text="Package File: ")
            }
        )

        self.data.begin(module=self.module, tag=fields.category)
        self.data.run(
            content=fields.__dict__,
            key='name'
        )

    def add_alias(self):
        fields = InputAddAlias(**{
                "category": option(text="Alias Category [default]: "),
                "command": option(text="Alias Command: ", required=True),
                "body": option(text="Alias Body: ", required=True),
                "type": "exec"
            }
        )

        self.data.begin(module=self.module, tag=fields.category)
        self.data.run(
            content=fields.__dict__,
            key='command'
        )

    def add_terminal(self):
        fields = InputAddTerminal(**{
                "category": option(text="Terminal Category [default]: "),
                "name": option(text="Terminal Name: ", required=True)
            }
        )

        self.data.begin(module=self.module, tag=fields.category)
        self.data.run(
            content={
                "name": fields.name,
                "colorscheme": {},
                "profile": {
                    "Appearance": {
                        "ColorScheme": None
                    },
                    "General": {
                        "Name": None,
                        "Parent": None
                    }
                }
            },
            key='name'
        )

    def add_script(self):
        fields = InputAddScript(**{
                "category": option(text="Script Category [default]: "),
                "type": option(text="Script Type: ", required=True),
                "name": option(text="Script Name: ", required=True),
                "shebang": option(text="Script Shebang: "),
                "body": option(text="Script Body: ", required=True, body=True),
            }
        )

        self.data.begin(module=self.module, tag=fields.category)
        self.data.run(
            content=fields.__dict__,
            key='name'
        )
