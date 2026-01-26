import logging
import sys

class ColoredFormatter(logging.Formatter):
    """
    A custom logging formatter that adds colors to log levels.
    """
    grey = "\x1b[38;20m"
    blue = "\x1b[34;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    # Matching the format in main_orchestrator.py and base_agent.py
    format_str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format_str + reset,
        logging.INFO: blue + format_str + reset,
        logging.WARNING: yellow + format_str + reset,
        logging.ERROR: red + format_str + reset,
        logging.CRITICAL: bold_red + format_str + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

def configure_colored_logging(logger_name=None, level=logging.INFO):
    """
    Configures a logger with ColoredFormatter if stdout is a TTY.
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # Avoid adding multiple handlers if already configured
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        if sys.stdout.isatty():
             handler.setFormatter(ColoredFormatter())
        else:
             handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        logger.addHandler(handler)

    return logger
