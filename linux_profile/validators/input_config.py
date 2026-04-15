from urllib.parse import urlsplit

from linux_profile.base.validator import Validator
from linux_profile.base.error import ErrorArgumentIsInvalid


# Whitelist of known safe editors and shells
SAFE_EDITORS = {"vim", "vi", "nano", "emacs", "code", "gedit", "nvim", "micro", "subl"}
SAFE_SHELLS = {"bash", "sh", "zsh", "fish", "ksh", "tcsh", "csh"}


class InputConfig(Validator):

    def validator_url(self, value=None):
        if value:
            if urlsplit(value).scheme not in ["http", "https"]:
                raise ErrorArgumentIsInvalid(
                    argument='--url',
                    error="The URL must have http or https.")
        return value

    def validator_editor(self, value=None):
        if value is not None:
            # Security: reject empty strings
            if not value.strip():
                raise ErrorArgumentIsInvalid(
                    argument='--editor',
                    error="Editor name must not be empty.")

            # Security: reject command injection characters
            for char in [';', '&', '|', '`', '$', '(', ')']:
                if char in value:
                    raise ErrorArgumentIsInvalid(
                        argument='--editor',
                        error="Editor name contains invalid characters.")

            # Security: reject absolute/relative paths — only allow bare names
            if '/' in value or '\\' in value or '..' in value:
                raise ErrorArgumentIsInvalid(
                    argument='--editor',
                    error="Editor must be a command name, not a path.")

        return value

    def validator_shell(self, value=None):
        if value is not None:
            # Security: reject command injection characters
            for char in [';', '&', '|', '`', '$', '(', ')']:
                if char in value:
                    raise ErrorArgumentIsInvalid(
                        argument='--shell',
                        error="Shell name contains invalid characters.")

            # Security: reject absolute/relative paths — only allow bare names
            if '/' in value or '\\' in value or '..' in value:
                raise ErrorArgumentIsInvalid(
                    argument='--shell',
                    error="Shell must be a command name, not a path.")

        return value
