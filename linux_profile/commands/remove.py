from linux_profile.base.action import Action
from linux_profile.base.config import Config


class Remove(Config):

    def setup(self):
        """Defines the functions that are executed each
        time the class is instantiated.
        """
        action = Action(
            self.join([self.linuxp_path_config, self.linuxp_file_profile]))
        status = action._delete_item(value=self.id)
        if status:
            print("ID:", self.id)
