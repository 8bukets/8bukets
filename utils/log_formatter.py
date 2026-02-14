import logging

class ColorFormatter(logging.Formatter):
    """
    Custom formatter to add colors and emojis to log messages.
    """

    # ANSI escape codes
    RESET = "\033[0m"
    BOLD = "\033[1m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Log Level Colors
    LEVEL_COLORS = {
        logging.DEBUG: BLUE,
        logging.INFO: GREEN,
        logging.WARNING: YELLOW,
        logging.ERROR: RED,
        logging.CRITICAL: BOLD + RED
    }

    # Log Level Emojis
    LEVEL_EMOJIS = {
        logging.DEBUG: "🐛",
        logging.INFO: "ℹ️",
        logging.WARNING: "⚠️",
        logging.ERROR: "❌",
        logging.CRITICAL: "🚨"
    }

    # Agent Emojis Mapping
    AGENT_EMOJIS = {
        "SystemOrchestrator": "⚙️",
        "Analysis Agent": "🔍",
        "Health Check Agent": "🏥",
        "Research Agent": "📚",
        "Intelligence Agent": "🧠",
        "Creativity Agent": "🎨",
        "Content Agent": "📝",
        "Monetization Agent": "💰",
        "MarkPositionScraper": "🕷️"
    }

    def format(self, record):
        # Determine color and emoji for the level
        color = self.LEVEL_COLORS.get(record.levelno, self.RESET)
        level_emoji = self.LEVEL_EMOJIS.get(record.levelno, "")

        # Determine emoji for the logger/agent
        # We check if the logger name is a known agent or if the message contains agent name
        agent_emoji = self.AGENT_EMOJIS.get(record.name, "")

        # Fallback: Check message for agent name if not in logger name
        if not agent_emoji:
            for agent_name, emoji in self.AGENT_EMOJIS.items():
                if f"[{agent_name}]" in record.msg:
                    agent_emoji = emoji
                    break

        # Format the timestamp
        timestamp = self.formatTime(record, self.datefmt)

        # Construct the log message
        # Format: [Time] [Emoji] [Level] - [Message]
        # We use Cyan for timestamp
        log_fmt = f"{self.CYAN}{timestamp}{self.RESET} "

        if agent_emoji:
            log_fmt += f"{agent_emoji} "

        log_fmt += f"{color}{record.levelname}{self.RESET} - {record.getMessage()}"

        return log_fmt
