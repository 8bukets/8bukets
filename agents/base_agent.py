import logging
import asyncio
from typing import Dict, Any, List

# Configure colorful logging
class ColorFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

handler = logging.StreamHandler()
handler.setFormatter(ColorFormatter())
logging.basicConfig(level=logging.INFO, handlers=[handler])

class BaseAgent:
    def __init__(self, name: str, shared_state: Dict[str, Any]):
        self.name = name
        self.shared_state = shared_state
        self.logger = logging.getLogger(name)
        self.inbox = asyncio.Queue()

    async def run(self):
        """Main loop for the agent."""
        self.logger.info(f"⚡ {self.name} started.")
        while True:
            # Process inbox messages
            try:
                message = await asyncio.wait_for(self.inbox.get(), timeout=1.0)
                await self.process_message(message)
                self.inbox.task_done()
            except asyncio.TimeoutError:
                # Perform autonomous tasks if no messages
                try:
                    await self.perform_task()
                except Exception as e:
                     self.logger.error(f"Error in perform_task: {e}")
            except Exception as e:
                self.logger.error(f"Error in main loop: {e}")
                await asyncio.sleep(1)

    async def process_message(self, message: Dict[str, Any]):
        """Handle incoming messages."""
        pass

    async def perform_task(self):
        """Perform autonomous recurring tasks."""
        pass

    def send_message(self, target_agent: 'BaseAgent', message: Dict[str, Any]):
        """Send a message to another agent."""
        target_agent.inbox.put_nowait(message)

    def log(self, message: str):
        self.logger.info(message)
