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
    FORMATS = {
        logging.DEBUG: Colors.BLUE + "%(asctime)s - %(levelname)s - %(message)s" + Colors.ENDC,
        logging.INFO: Colors.GREEN + "ℹ️ %(asctime)s - %(levelname)s - %(message)s" + Colors.ENDC,
        logging.WARNING: Colors.WARNING + "⚠️ %(asctime)s - %(levelname)s - %(message)s" + Colors.ENDC,
        logging.ERROR: Colors.FAIL + "❌ %(asctime)s - %(levelname)s - %(message)s" + Colors.ENDC,
        logging.CRITICAL: Colors.FAIL + Colors.BOLD + "🚨 %(asctime)s - %(levelname)s - %(message)s" + Colors.ENDC
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt='%H:%M:%S')
        return formatter.format(record)
