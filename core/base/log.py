import logging
from core.base.config import BaseConfig
from logging.config import dictConfig
from core.settings import FILE_CONFIG_LOG, FILE_PROFILE_LOG


BaseConfig()


logging_config = dict(
    version = 1,
    formatters = {
        'f': {'format':
              '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
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


def setup_log(name_log: str, file_log: str, level: logging):
    log_handler = logging.FileHandler(file_log)
    log_handler.setFormatter(log_format)

    logger = logging.getLogger(name_log)
    logger.setLevel(level)
    logger.addHandler(log_handler)

    return logger

def run_app(name_log: str):
    return setup_log(
        name_log=name_log,
        file_log=FILE_CONFIG_LOG, 
        level=logging.WARNING
    )

def run_profile(name_log: str):
    return setup_log(
        name_log=name_log,
        file_log=FILE_PROFILE_LOG,
        level=logging.DEBUG
    )
