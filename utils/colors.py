import logging
import sys

class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

class ColoredFormatter(logging.Formatter):
    LEVEL_COLORS = {
        logging.DEBUG: Colors.CYAN,
        logging.INFO: Colors.GREEN,
        logging.WARNING: Colors.YELLOW,
        logging.ERROR: Colors.RED,
        logging.CRITICAL: Colors.BOLD + Colors.RED,
    }

    AGENT_EMOJIS = {
        "Orchestrator": "🎼",
        "Researcher": "🔍",
        "Analyzer": "🧠",
        "Intelligence": "🔮",
        "ContentCreator": "✍️",
        "HealthCheck": "🩺",
        "Monetization": "💰",
        "Creativity": "🎨",
        "Advertising": "📢",
    }

    def format(self, record):
        color = self.LEVEL_COLORS.get(record.levelno, Colors.WHITE)
        emoji = self.AGENT_EMOJIS.get(record.name, "🤖")

        # Original format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        timestamp = self.formatTime(record, self.datefmt)

        # We need to handle potential message formatting arguments if they exist
        # But getMessage() handles that.

        log_fmt = (
            f"{Colors.BOLD}{Colors.WHITE}[{timestamp}]{Colors.RESET} "
            f"{emoji}  {Colors.BOLD}{record.name:<15}{Colors.RESET} "
            f"{color}{record.levelname:<8}{Colors.RESET} "
            f"{record.getMessage()}"
        )

        if record.exc_info:
            # format the exception
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
            if record.exc_text:
                log_fmt += f"\n{record.exc_text}"

        return log_fmt
