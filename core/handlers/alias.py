from os import system
from pathlib import Path

from core.base.system import System
from core.utils.file import read_file, get_content


class HandlerAlias(System):

    def setup_exec(self):
        path_file = str(Path.home()) + '/.bash_aliases'

        file_system = read_file(path_file=path_file)
        body = get_content(path_file=file_system, separator="=")

        current_alias = f'\nalias {self.command}="{self.body}"'

        rebase_alias = list()
        for item in body:
            if item[5:len(item)] != self.command:
                new_alias = f'\nalias {item[5:len(item)]}="{body.get(item)}"'
                rebase_alias.append(new_alias)
    
        system(f"true > {path_file}")
        for _rebase in rebase_alias:
            if _rebase != '\n':
                system(f"echo '{_rebase}' >> {path_file}")

        system(f"echo '{current_alias}' >> {path_file}")
