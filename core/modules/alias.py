from pathlib import Path

from core.base.system import System
from core.utils.file import write_file


class SystemAlias(System):

    def setup_exec(self):
        write_file(
            content=f'\nalias {self.command}="{self.content}"',
            path_file=str(Path.home()) + '/.bash_aliases',
            mode='a'
        )
