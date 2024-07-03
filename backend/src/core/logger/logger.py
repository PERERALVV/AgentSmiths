import logging
from logging.handlers import RotatingFileHandler
import os
import json

try:
    from colorlog import ColoredFormatter
    COLORLOG_AVAILABLE = True
except ImportError:
    COLORLOG_AVAILABLE = False

class Logger:
    def __init__(self, name=__name__, log_file='/code/backend/logs/agent.log', level=logging.INFO, max_size=5*1024*1024, backups=3):
        """
        Initializes a logger with both console and file handlers.
        
        :param name: Name of the logger.
        :param log_file: Path to the log file.
        :param level: Logging level, e.g., logging.INFO.
        :param max_size: Maximum size of the log file in bytes before it is rotated.
        :param backups: Number of backup log files to keep.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        self.formatter = logging.Formatter('%(asctime)s - %(pathname)s:%(lineno)d - %(name)s - %(levelname)s -\n%(message)s')

       
        file_handler = RotatingFileHandler(log_file, maxBytes=max_size, backupCount=backups)
        file_handler.setFormatter(self.formatter)
        self.logger.addHandler(file_handler)

        endmarker='-'*100
        if COLORLOG_AVAILABLE:
            console_formatter = ColoredFormatter(f'%(log_color)s%(asctime)s - %(purple)s%(pathname)s:%(lineno)d - %(log_color)s%(name)s - %(levelname)-8s%(reset)s -\n%(white)s%(message)s \n%(log_color)s{endmarker}%(reset)s',
                                                 datefmt=None,
                                                 reset=True,
                                                 log_colors={
                                                     'DEBUG': 'cyan',
                                                     'INFO': 'green',
                                                     'WARNING': 'yellow',
                                                     'ERROR': 'red',
                                                     'CRITICAL': 'red,bg_white',
                                                 },
                                                 secondary_log_colors={},
                                                 style='%')
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(console_formatter)
            self.logger.addHandler(console_handler)
        else:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            self.logger.addHandler(console_handler)

    def log_json(self, message, level=logging.INFO):
        """
        Logs a message that is a JSON object with proper indentation.
        
        :param message: The message to log. Should be a dict or list.
        :param level: Logging level, e.g., logging.INFO.
        """
        if isinstance(message, (dict, list)):
            message = json.dumps(message, indent=4)
        if level == logging.DEBUG:
            self.logger.debug(message)
        elif level == logging.WARNING:
            self.logger.warning(message)
        elif level == logging.ERROR:
            self.logger.error(message)
        elif level == logging.CRITICAL:
            self.logger.critical(message)
        else:
            self.logger.info(message)

    def get_logger(self):
        """
        Returns the configured logger.
        """
        return self.logger