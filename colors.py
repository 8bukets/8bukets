import logging

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
    def format(self, record):
        if record.levelno == logging.INFO:
            record.levelname = f"{Colors.GREEN}{record.levelname}{Colors.ENDC}"
            record.msg = f"{Colors.GREEN}{record.msg}{Colors.ENDC}"
        elif record.levelno == logging.WARNING:
            record.levelname = f"{Colors.WARNING}{record.levelname}{Colors.ENDC}"
            record.msg = f"{Colors.WARNING}{record.msg}{Colors.ENDC}"
        elif record.levelno >= logging.ERROR:
            record.levelname = f"{Colors.FAIL}{record.levelname}{Colors.ENDC}"
            record.msg = f"{Colors.FAIL}{record.msg}{Colors.ENDC}"

        return super().format(record)
