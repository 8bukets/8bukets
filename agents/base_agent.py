import logging
import os
import json
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

class Blackboard(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._proposals = []
        self._history = []

    async def update(self, source, value):
        """Merge `value`'s keys into the shared blackboard state.

        `source` names the agent/caller responsible for the update and is
        recorded in the update history (see get_history()); it is not used
        as a nesting key, so downstream agents can read merged keys directly
        via blackboard.get(...).
        """
        self._history.append({"source": source, "data": value})
        dict.update(self, value)

    async def propose_improvement(self, proposer, improvement):
        self._proposals.append({
            "proposer": proposer,
            "improvement": improvement
        })

    def get_proposals(self):
        return self._proposals

    def get_history(self):
        return self._history

    def get_all(self):
        return dict(self)

class BaseAgent(ABC):
    def __init__(self, name, dependencies=None, provides=None):
        self.name = name
        self.dependencies = dependencies or []
        self.provides = provides or []
        self.logger = logging.getLogger(f"Agent.{name}")
        self.config = self._load_config()

    def _load_config(self):
        config_path = "config/evolution_params.json"
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    @abstractmethod
    async def run(self, context: dict):
        """
        Execute the agent's task.
        :param context: A shared dictionary containing data and state.
        """
        pass

    def log(self, message):
        self.logger.info(message)
