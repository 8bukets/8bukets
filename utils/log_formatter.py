import logging
import sys

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ColoredFormatter(logging.Formatter):
    FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: Colors.BLUE + FORMAT + Colors.ENDC,
        logging.INFO: Colors.GREEN + FORMAT + Colors.ENDC,
        logging.WARNING: Colors.WARNING + FORMAT + Colors.ENDC,
        logging.ERROR: Colors.FAIL + FORMAT + Colors.ENDC,
        logging.CRITICAL: Colors.FAIL + Colors.BOLD + FORMAT + Colors.ENDC
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno, self.FORMAT)
        formatter = logging.Formatter(log_fmt, datefmt='%H:%M:%S')
        return formatter.format(record)

def setup_colored_logging():
    """
    Sets up the root logger to use the ColoredFormatter.
    """
    root_logger = logging.getLogger()

    # Remove all existing handlers to prevent duplicate logs
    if root_logger.handlers:
        for handler in root_logger.handlers:
            root_logger.removeHandler(handler)

    # Create console handler with a higher log level
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)

    # Create formatter and add it to the handlers
    ch.setFormatter(ColoredFormatter())

    # Add the handlers to the logger
    root_logger.addHandler(ch)

    # Set the logging level
    root_logger.setLevel(logging.INFO)
