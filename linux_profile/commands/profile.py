import urllib.request

from linux_profile.validators import InputProfile
from linux_profile.base.settings import Settings
from linux_profile.base.file import File


class Profile(Settings):

    def setup(self):
        """Defines the functions that are executed each
        time the class is instantiated.
        """
        self.fields = InputProfile(**{
            "url": self.url,
            "switch": self.switch,
            "output": self.output}
        )

        if self.fields.url:
            self.setup_url()

        if self.fields.switch:
            self.setup_switch()

    def setup_url(self):
        urllib.request.urlretrieve(self.url, self.fields.output)

    def setup_switch(self):
        self.config['file_profile'] = self.fields.switch
        File.write(
            content=self.config,
            path_file=self.join(value=[self.path_config, self.file_config]))
