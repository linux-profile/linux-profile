from os.path import exists
from urllib.parse import urlsplit

from linux_profile.base.settings import Settings
from linux_profile.base.validator import Validator
from linux_profile.base.error import ErrorArgumentIsInvalid
from linux_profile.utils.text import slugify


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
            if not exists(Settings.join(value=[Settings.Base.path_config, value])):
                raise ErrorArgumentIsInvalid(
                    argument='--switch',
                    error="Profile file does not exist.")
        return value

    def validator_output(self, value=None):
        file_profile = Settings.join(
            value=[slugify(value), "json"],
            separator=".") if value else Settings.Base.file_profile

        value = Settings.join(value=[Settings.Base.path_config, file_profile])
        return value
