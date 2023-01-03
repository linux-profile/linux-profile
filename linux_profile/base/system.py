"""
Module System
"""


from os import system as _system


class System:

    def __init__(self, **kwargs) -> None:
        self.sudo = False
        self.debug = False
        self.debug_command = None
        self.command = 'exec'
        self.type = 'default'

        for arg in kwargs:
            value = kwargs.get(arg)
            if value is not None:
                setattr(self, arg, value)

        self.func = f"setup_{self.type}".replace("-", "_")
        if hasattr(self, self.func):
            try:
                getattr(self, self.func, None)()
            finally:
                if not self.debug:
                    if hasattr(self, 'id'):
                        print("ID:", self.id)

    def system(self, cmd: list):
        cmd = " ".join(cmd).replace("  ", " ")
        if cmd[-1] == " ":
            cmd = cmd[0:len(cmd) - 1]

        if self.sudo:
            cmd = f"sudo {cmd}"

        if self.debug:
            self.debug_command = cmd
            print(cmd)
        else:
            _system(cmd)

    def setup_default(self):
        return "Method not Implemented"
