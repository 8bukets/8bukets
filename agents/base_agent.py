import logging
import sys
import os

# Add root directory to path if needed for cli_utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from cli_utils import ColoredFormatter
except ImportError:
    ColoredFormatter = None

class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            if ColoredFormatter:
                formatter = ColoredFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            else:
                formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
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
