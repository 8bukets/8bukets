import logging
from typing import Dict, Any, List

# Configure logging to match the project's visual style if possible,
# otherwise default to standard.
logger = logging.getLogger(__name__)

class AgentContext:
    """Shared memory/context for all autonomous agents."""
    def __init__(self):
        self.data: Dict[str, Any] = {}
        self.logs: List[str] = []
        self.config: Dict[str, Any] = {}

    def set(self, key: str, value: Any):
        self.data[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def log_activity(self, agent_name: str, message: str):
        entry = f"[{agent_name}] {message}"
        self.logs.append(entry)
        logger.info(entry)

class BaseAgent:
    """Base class for all autonomous agents."""
    def __init__(self, name: str):
        self.name = name

    def run(self, context: AgentContext):
        """Execute the agent's task."""
        raise NotImplementedError("Agents must implement the run method.")

    def log(self, context: AgentContext, message: str):
        context.log_activity(self.name, message)
