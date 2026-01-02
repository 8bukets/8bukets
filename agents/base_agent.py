import logging

# Formatter defined at module level
try:
    from colors import Colors
except ImportError:
    # Fallback if colors.py is missing (though we added it)
    class Colors:
        GREEN = ""
        FAIL = ""
        ENDC = ""

class AgentColoredFormatter(logging.Formatter):
    def format(self, record):
        message = super().format(record)
        prefix = "🚀" if "Starting" in record.msg else "✅" if "complete" in record.msg else "➡️ "
        color = Colors.GREEN if record.levelno == logging.INFO else Colors.FAIL
        return f"{color}{prefix} {message}{Colors.ENDC}"

class BaseAgent:
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.INFO)
        # Prevent duplicate logging since root logger is configured
        self.logger.propagate = False
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = AgentColoredFormatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
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
