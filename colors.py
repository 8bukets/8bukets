import logging
import sys

class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

class ColoredFormatter(logging.Formatter):
    COLORS = {
        'INFO': Colors.GREEN,
        'WARNING': Colors.YELLOW,
        'ERROR': Colors.RED,
        'CRITICAL': Colors.RED + Colors.BOLD,
        'DEBUG': Colors.BLUE
    }
    EMOJIS = {
        'INFO': 'ℹ️',
        'WARNING': '⚠️',
        'ERROR': '❌',
        'CRITICAL': '🚨',
        'DEBUG': '🐛'
    }

    def format(self, record):
        # Format timestamp first
        record.asctime = self.formatTime(record, self.datefmt)

        color = self.COLORS.get(record.levelname, Colors.RESET)
        emoji = self.EMOJIS.get(record.levelname, '')
        reset = Colors.RESET

        # We handle formatting manually to ensure colors are placed correctly
        # Pattern: Time - Level - Emoji Message
        return f"{reset}{record.asctime} - {color}{record.levelname}{reset} - {emoji} {record.getMessage()}"
