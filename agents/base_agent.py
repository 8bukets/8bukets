import logging

class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.INFO)
        # Ensure proper logging configuration when running agents independently.
        # If the root logger has handlers (e.g. from orchestrator), we skip adding a new one
        # to avoid duplicate logs.
        if not self.logger.handlers and not logging.getLogger().handlers:
            from utils.colors import ColoredFormatter
            handler = logging.StreamHandler()
            handler.setFormatter(ColoredFormatter())
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
