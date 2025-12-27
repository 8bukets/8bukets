import logging

class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.INFO)
        # Avoid duplicate logging: only add handler if root logger has no handlers
        # and this logger has no handlers.
        if not self.logger.handlers and not logging.getLogger().handlers:
            from utils.logging_utils import ColorFormatter
            handler = logging.StreamHandler()
            handler.setFormatter(ColorFormatter())
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
