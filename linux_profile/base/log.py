import logging
from linux_profile.base.config import BaseConfig
from logging.config import dictConfig
from linux_profile.settings import FILE


logging_config = dict(
    version = 1,
    formatters = {
        'f': {'format':
              '%(asctime)s - %(name)s - %(levelname)s - %(message)s'}
        },
    handlers = {
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.DEBUG}
        },
    root = {
        'handlers': ['h'],
        'level': logging.DEBUG,
        }
)

log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class LogBaseConfig(BaseConfig):

    def setup(self):
        """
        Defines the functions that are executed each
        time the class is instantiated.
        """
        self.set_folder()


def setup_log(name_log: str, file_log: str, level: logging):
    LogBaseConfig()

    # logging.config.dictConfig(logging_config)

    log_handler = logging.FileHandler(file_log)
    log_handler.setFormatter(log_format)

    logger = logging.getLogger(name_log)
    logger.setLevel(level)
    logger.addHandler(log_handler)

    return logger

def run_app(name_log: str):
    return setup_log(
        name_log=name_log,
        file_log=FILE.get("log_config"),
        level=logging.WARNING
    )

def run_profile(name_log: str):
    return setup_log(
        name_log=name_log,
        file_log=FILE.get("log_profile"),
        level=logging.DEBUG
    )
