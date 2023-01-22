from linux_profile.base.action import Action
from linux_profile.base.settings import Settings


class Remove(Settings):

    def setup(self):
        """Defines the functions that are executed each
        time the class is instantiated.
        """
        action = Action(
            str(self.path_profile.joinpath(self.file_profile)))

        status = action._delete_item(value=self.id)
        if status:
            print("ID:", self.id)
