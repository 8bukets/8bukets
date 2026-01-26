import logging
import sys

class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.INFO)
        # Only add handler if root logger is not configured (to avoid double logging)
        if not logging.getLogger().handlers and not self.logger.handlers:
            handler = logging.StreamHandler()
            try:
                from cli_utils import ColoredFormatter
                if sys.stdout.isatty():
                    handler.setFormatter(ColoredFormatter())
                else:
                    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
            except ImportError:
                handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

            self.logger.addHandler(handler)

    def run(self, data=None):
        self.logger.info("Starting...")
        try:
            result = self.perform_task(data)
            self.logger.info("Task complete.")
            return result
        except Exception as e:
            self.logger.error(f"Task failed: {e}")
            return None

    def perform_task(self, data):
        raise NotImplementedError("Subclasses must implement perform_task")
