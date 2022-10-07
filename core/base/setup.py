import os
from pathlib import Path

from core.base.log import run_profile
from core.utils.file import write_file
from core.settings import FILE_INSTALL_LOG


class Setup():

    def __init__(self, **kwargs):
        for arg in kwargs:
            value = kwargs.get(arg)
            setattr(self, arg, value)

        log = run_profile(name_log=self.__class__.__name__)
        log.info(f"ID: {self.id}")

        if hasattr(self, f"setup_{self.type}"):
            getattr(self, f"setup_{self.type}", None)()


class SetupPackage(Setup):

    def setup_apt_get(self):
        os.system("sudo {type} install {name} -y".format(
                type=self.type,
                name=self.name,
                file=FILE_INSTALL_LOG
            )
        )   

    def setup_apt(self):
        os.system("sudo {type} install {name} -y".format(
                type=self.type,
                name=self.name,
                file=FILE_INSTALL_LOG
            )
        )

    def setup_snap(self):
        os.system("sudo {type} install {name}".format(
                type=self.type,
                name=self.name,
                file=FILE_INSTALL_LOG
            )
        )


class SetupAlias(Setup):

    def setup_exec(self):
        write_file(
            content=f'\nalias {self.command}="{self.content}"',
            path_file=str(Path.home()) + '/.bash_aliases',
            mode='a'
        )
