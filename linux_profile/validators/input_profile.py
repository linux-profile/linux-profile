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
    error_path_traversal = "File name must not contain path separators or '..'."

    def _check_path_traversal(self, value: str, argument: str) -> None:
        """Reject path traversal attempts in profile filenames."""
        if '..' in value or '/' in value or '\\' in value:
            raise ErrorArgumentIsInvalid(
                argument=argument,
                error=self.error_path_traversal)

    def validator_url(self, value=None):
        if value:
            if urlsplit(value).scheme not in ["http", "https"]:
                raise ErrorArgumentIsInvalid(
                    argument='--url',
                    error="The URL must have http or https.")
        return value

    def validator_switch(self, value=None):
        if value:
            self._check_path_traversal(value, '--switch')

            if not Settings.Base.path_profile.joinpath(value).exists():
                raise ErrorArgumentIsInvalid(
                    argument='--switch',
                    error=self.error_file_not_exist)
        return value

    def validator_output(self, value=None):
        file_profile = value if value else Settings.Variable.file_profile

        # Security: reject path traversal
        self._check_path_traversal(file_profile, '--output')

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
            # Security: reject path traversal FIRST, before other checks
            self._check_path_traversal(value, '--new')

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
            # Security: reject path traversal FIRST
            self._check_path_traversal(value, '--delete')

            if not Settings.Base.path_profile.joinpath(value).exists():
                raise ErrorArgumentIsInvalid(
                    argument='--delete',
                    error=self.error_file_not_exist)

            return Path(Settings.Base.path_profile.joinpath(value))
        return value

    def validator_list(self, value=False):
        return value
