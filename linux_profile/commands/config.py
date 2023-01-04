import urllib.request

from linux_profile.base.config import Config as _Config


class Config(_Config):

    def setup(self):
        """Defines the functions that are executed each
        time the class is instantiated.
        """
        if self.get:
            self.setup_get()

    def setup_get(self):
        urllib.request.urlretrieve(
            self.get, self.join([self.linuxp_path_config, self.linuxp_file_profile])
        )
