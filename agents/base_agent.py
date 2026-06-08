import logging
from ux_utils import configure_ux_logging

class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.logger = configure_ux_logging(self.name)

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
