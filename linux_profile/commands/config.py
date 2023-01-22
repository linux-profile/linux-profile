import urllib.request

from linux_profile.validators import InputConfig
from linux_profile.base.settings import Settings


class Config(Settings):

    def setup(self):
        """Defines the functions that are executed each
        time the class is instantiated.
        """
        self.fields = InputConfig(**{
            "url": self.url}
        )

        if self.fields.url:
            self.setup_url()

    def setup_url(self):
        urllib.request.urlretrieve(
            self.url, str(self.path_config.joinpath(self.file_config)))
