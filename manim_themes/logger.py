"""
This module is used to log messages to the console.

It's main purpose is make the logging output more readable by using the rich library.
One might argue, that a library should do any styling to the logging output, which I think is a valid for most cases.

However, Manta is ment to be used with as little configuration as possible for the end user, so I decided to use the
rich library for styling the logging output.
"""

import logging
from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
    handlers=[RichHandler(show_path=False)]
)

# create file handler which logs messages
# fh = logging.FileHandler(PATHS.LOGS_FILE_PATH)
# fh.setLevel(logging.INFO)

log = logging.getLogger("rich")

if __name__ == '__main__':
    log.info("This is an info message")
    log.warning("This is a warning message")
    log.error("This is an error message")
    log.critical("This is a critical message")
