from linux_profile.base.config import BaseConfig


class Update(BaseConfig):

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.load_profile()
