from linux_profile.base.system import System
from linux_profile.base.file import File


class HandlerScript(System):

    def setup_system(self, shebang: str):
        path_file = f"{self.temp}/{self.name}"

        File.write(content=shebang, path_file=path_file, dump=False)
        File.write_lines(content=self.body, path_file=path_file, mode="a")

        self.system(cmd=["chmod", "+x", path_file])
        self.system(cmd=[path_file])

    def setup_shell(self):
        shebang = self.shebang if hasattr(self, "shebang") else "#!/bin/bash"
        self.setup_system(shebang=shebang)

    def setup_python(self):
        shebang = self.shebang if hasattr(self, "shebang") else "#!/usr/bin/env python"
        self.setup_system(shebang=shebang)

    def setup_python3(self):
        shebang = self.shebang if hasattr(self, "shebang") else "#!/usr/bin/env python3"
        self.setup_system(shebang=shebang)

    def setup_ruby(self):
        shebang = self.shebang if hasattr(self, "shebang") else "#!/usr/bin/env ruby"
        self.setup_system(shebang=shebang)
