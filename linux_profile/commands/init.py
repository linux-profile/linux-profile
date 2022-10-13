import urllib.request

from linux_profile.base.log import run_profile
from linux_profile.base.config import BaseConfig
from linux_profile.base.validator import InputInitConfig


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
        fields_config = InputInitConfig(**{
                "file_url_get": input("Profile file URL (GET): "),
                "file_url_post": input("Profile file URL (POST): ")
            }
        )

        if fields_config.file_url_get:
            urllib.request.urlretrieve(
                fields_config.file_url_get, self.file.get("profile")
            )
            self.log.info("Profile import executed successfully.")
