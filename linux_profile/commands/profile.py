import urllib.request

from linux_profile.base.settings import Settings


class Profile(Settings):

    def setup(self):
        """Defines the functions that are executed each
        time the class is instantiated.
        """
        if self.get:
            self.setup_get()

    def setup_get(self):
        urllib.request.urlretrieve(
            self.get, self.join([self.path_config, self.file_profile])
        )
