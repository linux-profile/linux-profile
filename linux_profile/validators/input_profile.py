from urllib.parse import urlsplit
from pathlib import Path

from linux_profile.base.settings import Settings
from linux_profile.base.validator import Validator
from linux_profile.base.error import ErrorArgumentIsInvalid


class InputProfile(Validator):

    error_json_extension = "File name is invalid. It is necessary to put the .json extension."
    error_json_characters = "File name is invalid. Must be more than five (5) characters."
    error_file_not_exist = "Profile file does not exist."
    error_file_already_exist = "Profile file already exists."

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
                    error=self.error_file_not_exist)
        return value

    def validator_output(self, value=None):
        file_profile = value if value else Settings.Variable.file_profile

        if not file_profile[len(file_profile) - 5:] == ".json":
            raise ErrorArgumentIsInvalid(
                argument='--output',
                error=self.error_json_extension)

        if not len(file_profile) > 5:
            raise ErrorArgumentIsInvalid(
                argument='--output',
                error=self.error_json_characters)

        return str(Settings.Base.path_profile.joinpath(file_profile))

    def validator_new(self, value=None):
        if value:
            if not value[len(value) - 5:] == ".json":
                raise ErrorArgumentIsInvalid(
                    argument='--new',
                    error=self.error_json_extension)

            if not len(value) > 5:
                raise ErrorArgumentIsInvalid(
                    argument='--new',
                    error=self.error_json_characters)

            if Settings.Base.path_profile.joinpath(value).exists():
                raise ErrorArgumentIsInvalid(
                    argument='--new',
                    error=self.error_file_already_exist)

            return Path(Settings.Base.path_profile.joinpath(value))
        return value

    def validator_delete(self, value=False):
        if value:
            if not Settings.Base.path_profile.joinpath(value).exists():
                raise ErrorArgumentIsInvalid(
                    argument='--delete',
                    error=self.error_file_not_exist)

            return Path(Settings.Base.path_profile.joinpath(value))
        return value

    def validator_list(self, value=False):
        return value
