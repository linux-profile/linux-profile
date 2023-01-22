from urllib.parse import urlsplit

from linux_profile.base.settings import Settings
from linux_profile.base.validator import Validator
from linux_profile.base.error import ErrorArgumentIsInvalid


class InputProfile(Validator):

    def validator_url(self, value=None):
        if value:
            if urlsplit(value).scheme not in ["http", "https"]:
                raise ErrorArgumentIsInvalid(
                    argument='--url',
                    error="The URL must have http or https.")
        return value

    def validator_switch(self, value=None):
        if value:
            if not Settings.Base.path_profile.joinpath(value).exists():
                raise ErrorArgumentIsInvalid(
                    argument='--switch',
                    error="Profile file does not exist.")
        return value

    def validator_output(self, value=None):
        file_profile = value if value else Settings.Variable.file_profile

        if not file_profile[len(file_profile) - 5:] == ".json":
            raise ErrorArgumentIsInvalid(
                argument='--output',
                error="File name is invalid. It is necessary to put the .json extension.")

        if not len(file_profile) > 5:
            raise ErrorArgumentIsInvalid(
                argument='--output',
                error="File name is invalid. Must be more than five (5) characters.")

        return str(Settings.Base.path_profile.joinpath(file_profile))

    def validator_list(self, value=False):
        return value
