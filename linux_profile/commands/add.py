from linux_profile.utils.text import option
from linux_profile.base.storage import Storage
from linux_profile.base.config import BaseConfig
from linux_profile.base.validator import (
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
                "tag": option(text="Package Tag [default]: "),
                "type": option(text="Package Manager: ", required=True),
                "name": option(text="Package Name: ", required=True),
                "url": option(text="Package URL: "),
                "file": option(text="Package File: "),
                "description": option(text="Package Description [limit 85]: ")
            }
        )

        self.data.begin(module=self.module, tag=fields.tag)
        self.data.run(
            content=fields.__dict__,
            key='name'
        )

    def add_alias(self):
        fields = InputAddAlias(**{
                "tag": option(text="Alias Tag [default]: "),
                "name": option(text="Alias Name: ", required=True),
                "command": option(text="Alias Command: ", required=True),
                "body": option(text="Alias Body: ", required=True),
                "description": option(text="Package Description [limit 85]: "),
                "type": "exec"
            }
        )

        self.data.begin(module=self.module, tag=fields.tag)
        self.data.run(
            content=fields.__dict__,
            key='command'
        )

    def add_terminal(self):
        fields = InputAddTerminal(**{
                "tag": option(text="Terminal Tag [default]: "),
                "name": option(text="Terminal Name: ", required=True),
                "description": option(text="Package Description [limit 85]: "),
            }
        )

        self.data.begin(module=self.module, tag=fields.tag)
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
                "tag": option(text="Script Tag [default]: "),
                "type": option(text="Script Type: ", required=True),
                "name": option(text="Script Name: ", required=True),
                "body": option(text="Script Body: ", required=True, body=True),
                "shebang": option(text="Script Shebang: "),
                "description": option(text="Package Description [limit 85]: "),
            }
        )

        self.data.begin(module=self.module, tag=fields.tag)
        self.data.run(
            content=fields.__dict__,
            key='name'
        )
