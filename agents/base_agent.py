import logging

class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(self.name)
        # Only set level, do not add handlers as root logger handles propagation
        self.logger.setLevel(logging.INFO)

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
