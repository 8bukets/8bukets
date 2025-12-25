import logging
import uuid
import json
from typing import Dict, Any, List, Optional
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class KnowledgeBase:
    """
    A shared memory structure for agents to read and write data.
    """
    def __init__(self):
        self._data: Dict[str, Any] = {
            "history": [],
            "insights": {},
            "tasks": [],
            "market_trends": [],
            "content_ideas": [],
            "seo_reports": [],
            "ad_campaigns": []
        }

    def update(self, category: str, data: Any):
        if category not in self._data:
            self._data[category] = []

        if isinstance(self._data[category], list):
            self._data[category].append(data)
        elif isinstance(self._data[category], dict):
            self._data[category].update(data)
        else:
            self._data[category] = data

    def get(self, category: str) -> Any:
        return self._data.get(category)

    def dump(self) -> str:
        return json.dumps(self._data, indent=4, default=str)

class BaseAgent:
    """
    Abstract base class for an autonomous agent.
    """
    def __init__(self, name: str, knowledge_base: KnowledgeBase):
        self.id = str(uuid.uuid4())
        self.name = name
        self.kb = knowledge_base
        self.logger = logging.getLogger(f"Agent-{self.name}")
        self.learning_rate = 0.1
        self.memory: List[str] = []

    def log(self, message: str):
        self.logger.info(message)
        self.memory.append(f"{datetime.now()}: {message}")

    def think(self):
        """Simulate internal processing/decision making."""
        pass

    def act(self):
        """Perform the agent's specific task."""
        raise NotImplementedError("Agents must implement the act method.")

    def collaborate(self):
        """Interact with the shared knowledge base."""
        pass

    def run(self):
        self.log("Starting cycle...")
        self.think()
        self.act()
        self.collaborate()
        self.log("Cycle complete.")
