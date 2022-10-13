from os import system

from linux_profile.base.system import System
from linux_profile.utils.file import write_file


class HandlerScript(System):

    def setup_system(self, shebang: str):
        path_file = f"{self.temp}/{self.name}"
        for index, line in enumerate(self.body):
            if index == 0:
                system(f"echo '{shebang}' > {path_file}")

            write_file(
                content=line + '\n',
                path_file=path_file,
                mode='a'
            )
        system(f"sudo chmod +x {path_file}")
        system(path_file)

    def setup_shell(self):
        shebang = self.shebang if self.shebang else '#!/bin/bash'
        self.setup_system(shebang=shebang)

    def setup_python(self):
        shebang = self.shebang if self.shebang else '#!/usr/bin/env python'
        self.setup_system(shebang=shebang)

    def setup_python3(self):
        shebang = self.shebang if self.shebang else '#!/usr/bin/env python3'
        self.setup_system(shebang=shebang)

    def setup_ruby(self):
        shebang = self.shebang if self.shebang else '#!/usr/bin/env ruby'
        self.setup_system(shebang=shebang)
