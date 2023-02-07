from linux_profile.utils.text import option
from linux_profile.validators import InputAccount
from linux_profile.base.settings import Settings


class Account(Settings):

    def setup(self):
        """Defines the functions that are executed each
        time the class is instantiated.
        """
        self.fields = InputAccount(**{
            "email": option(text="Email: ", required=True),
            "password": option(text="Password: ", required=True, password=True)}
        )

        if self.signup:
            self.setup_signup()

        if self.login:
            self.setup_login()

    def setup_signup(self):
        pass

    def setup_login(self):
        pass
