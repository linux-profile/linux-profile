from os import system
from pathlib import Path

from linux_profile.base.file import File
from linux_profile.base.system import System
from linux_profile.utils.file import write_file, get_content


class HandlerAlias(System):

    def setup_exec(self):
        path_file = str(Path.home()) + '/.bash_aliases'

        bash_aliases = File.read(path_file=path_file)
        body = get_content(path_file=bash_aliases, separator="=")
        current_alias = f'alias {self.command}="{self.body}"'

        rebase_alias = list()
        for item in body:
            if item[5:len(item)] != self.command:
                new_alias = f'alias {item[5:len(item)]}="{body.get(item)}"'
                rebase_alias.append(new_alias)

        system(f"true > {path_file}")
        for _rebase in rebase_alias:
            if _rebase != '\n':
                system(f"echo '{_rebase}' >> {path_file}")

        write_file(
            content=current_alias,
            path_file=path_file,
            mode='a'
        )
