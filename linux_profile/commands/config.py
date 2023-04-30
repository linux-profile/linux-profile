import urllib.request

from linux_profile.validators import InputConfig
from linux_profile.base.settings import Settings
from linux_profile.base.file import File


class Config(Settings):

    def setup(self):
        """Defines the functions that are executed each
        time the class is instantiated.
        """
        self.fields = InputConfig(**{
            "url": self.url,
            "editor": self.editor}
        )

        if self.fields.url:
            self.setup_url()

        if self.fields.editor:
            self.setup_editor()

    def setup_url(self):
        urllib.request.urlretrieve(
            self.url, str(self.path_config.joinpath(self.file_config)))

    def setup_editor(self):
        self.config['text_editor'] = self.fields.editor
        File.write(
            content=self.config,
            path_file=str(self.path_config.joinpath(self.file_config)))
