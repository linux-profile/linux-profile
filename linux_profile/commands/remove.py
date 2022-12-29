from linux_profile.base.config import BaseConfig
from linux_profile.base.file import BaseAction


class Remove(BaseConfig):

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.add_config()
        self.load_config()
        self.load_profile()

        action = BaseAction(self.file.get("profile"))
        status = action._delete_item(value=self.id)
        if status:
            print("ID:", self.id)
