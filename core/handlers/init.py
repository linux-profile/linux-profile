#!/usr/bin/env python3
import urllib.request

from core.base.log import run_profile
from core.base.config import BaseConfig
from core.base.validator import ValidatorInit


class Init(BaseConfig):

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.add_config()
        self.load_config()
        self.load_profile()

        self.log = run_profile(name_log=self.__class__.__name__)
        self.init_profile()

    def init_profile(self):
        fields = ValidatorInit(**{
                "file_url": input("Profile file URL: ")
            }
        )
        if fields.file_url:
            urllib.request.urlretrieve(fields.file_url, self.file_profile)
            self.log.info("Profile import executed successfully.")

