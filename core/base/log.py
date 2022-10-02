import logging
from core.base.config import BaseConfig
from logging.config import dictConfig
from core.settings import FOLDER_LOG


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


class Log(BaseConfig):
    
    def setup_log(self, name_log, file_log: str, level: logging):
        log_handler = logging.FileHandler(file_log)
        log_handler.setFormatter(log_format)

        logger = logging.getLogger(name_log)
        logger.setLevel(level)
        logger.addHandler(log_handler)

        return logger

    def run_app(self):
        return self.setup_log(
            name_log='app',
            file_log=FOLDER_LOG + '/app.log', 
            level=logging.WARNING
        )

    def run_profile(self):
        return self.setup_log(
            name_log='profile',
            file_log=FOLDER_LOG + '/profile.log',
            level=logging.DEBUG
        )
