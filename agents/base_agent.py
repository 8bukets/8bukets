import logging

class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.INFO)
        # Removed individual handler setup to prevent duplicate logs
        # and rely on the root logger's configuration (ColorFormatter)

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
