from core.utils.text import color
from core.base.log import run_app

LOG_APP = run_app(name_log='app')


class ErrorLoadSettings(Exception):

    def __init__(self):
        message = "It is not possible to load the basic settings."
        LOG_APP.error(message)
        super(ErrorLoadSettings, self).__init__(message)


class ErrorParameterIsMissing(Exception):

    def __init__(self, parameter):
        message = f"Parameter --{parameter} is missing"
        LOG_APP.error(message)
        super(ErrorParameterIsMissing, self).__init__(message)


class ErrorInvalidValue(Exception):

    def __init__(self, parameter):
        message = f"Parameter --{parameter} invalid value"
        LOG_APP.error(message)
        super(ErrorInvalidValue, self).__init__(message)


def print_error_settings(error):
    message = "It is not possible to load the basic settings."
    LOG_APP.error(f"{message} [{str(error)}]")
    print(
        color(
            text="ERROR: " + message,
            types=['bold', 'red']
        )
    )


def print_error_estrange(error):
    message = "Some weird error happened, but that's ok."
    LOG_APP.error(f"{message} [{str(error)}]")

    print(
        color(
            text="ERROR: " + message,
            types=['bold', 'yellow']
        )
    )


def print_parameter_is_missing(parameter):
    message = f"Parameter --{parameter} is missing"
    LOG_APP.warning(message)

    print(
        color(
            text=message.format("WARNING: "+parameter),
            types=['bold', 'yellow']
        )
    )


def print_option_is_missing(parameter):
    message = f"Option [{parameter}] is missing"
    LOG_APP.warning(message)

    print(
        color(
            text=message.format("WARNING: "+parameter),
            types=['bold', 'yellow']
        )
    )


def print_option_invalid_value(parameter):
    message = f"Option [{parameter}] invalid value"
    LOG_APP.warning(message)

    print(
        color(
            text=message.format("WARNING: "+parameter),
            types=['bold', 'yellow']
        )
    )


def print_error_invalid_value(parameter):
    message = f"Parameter --{parameter} invalid value"
    LOG_APP.warning(message)

    print(
        color(
            text=message.format("WARNING: "+parameter),
            types=['bold', 'yellow']
        )
    )


def print_error(parameter):
    message = f"[{parameter}]"
    LOG_APP.warning(message)

    print(
        color(
            text=message.format("ERROR: "+ parameter),
            types=['bold', 'red']
        )
    )
