import urllib.request

from linux_profile.base.config import BaseConfig


class Config(BaseConfig):

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.add_config()
        self.load_config()
        self.load_profile()

        if self.get:
            self.setup_get()

    def setup_get(self):
        urllib.request.urlretrieve(
            self.get, self.file.get("profile")
        )
