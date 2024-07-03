from .logger import Logger
# Instantiate the Logger object
# Adjust 'my_app.log', logging level, max_size, and backups as needed
log = Logger(name='AGENTlogger').get_logger()