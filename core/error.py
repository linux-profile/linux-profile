from core.utils.text import color


class ErrorLoadSettings(Exception):

    def __init__(self,
                 message="It is not possible to load the basic settings."):
        super(ErrorLoadSettings, self).__init__(message)


class ErrorParameterIsMissing(Exception):

    def __init__(self, parameter):
        super(ErrorParameterIsMissing, self).__init__(
            "Parameter --{} is missing".format(parameter))


class ErrorInvalidValue(Exception):

    def __init__(self, parameter):
        super(ErrorInvalidValue, self).__init__(
            "Parameter --{} invalid value".format(parameter))


def print_error_settings():
    print(
        color(
            text="ERROR: It is not possible to load the basic settings.",
            types=['bold', 'red']
        )
    )


def print_parameter_is_missing(parameter):
    print(
        color(
            text="WARNING: Parameter --{} is missing".format(parameter),
            types=['bold', 'yellow']
        )
    )

def print_option_is_missing(parameter):
    print(
        color(
            text="WARNING: Option [{}] is missing".format(parameter),
            types=['bold', 'yellow']
        )
    )

def print_error_invalid_value(parameter):
    print(
        color(
            text="WARNING: Parameter --{} invalid value".format(parameter),
            types=['bold', 'yellow']
        )
    )
