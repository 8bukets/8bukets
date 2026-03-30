from abc import ABC, abstractmethod
import logging
import json
import os
import asyncio
from typing import Any, Dict, List, Set

MEMORY_FILE = "data/memory.json"
CONFIG_FILE = "config/evolution_params.json"

class Blackboard:
    """Shared state management with history tracking and evolutionary proposals."""
    def __init__(self):
        self._data: Dict[str, Any] = {}
        self._history: List[Dict[str, Any]] = []
        self._proposals: List[Dict[str, Any]] = []
        self._lock = asyncio.Lock()

    async def update(self, agent_name: str, updates: Dict[str, Any]):
        async with self._lock:
            self._data.update(updates)
            self._history.append({
                "agent": agent_name,
                "timestamp": asyncio.get_event_loop().time(),
                "keys": list(updates.keys())
            })

    async def propose_improvement(self, agent_name: str, improvement: Dict[str, Any]):
        """Agent proposes a 'Major Improvement' to the system structure or code."""
        async with self._lock:
            self._proposals.append({
                "proposer": agent_name,
                "timestamp": asyncio.get_event_loop().time(),
                "improvement": improvement
            })

    def get_proposals(self) -> List[Dict[str, Any]]:
        return self._proposals

    def get_all(self) -> Dict[str, Any]:
        return self._data.copy()

    def get(self, key: str, default=None) -> Any:
        return self._data.get(key, default)

    def get_history(self) -> List[Dict[str, Any]]:
        return self._history

class BaseAgent(ABC):
    def __init__(self, name: str, dependencies: List[str] = None, provides: List[str] = None):
        self.name = name
        self.dependencies = dependencies or []
        self.provides = provides or []
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        self.config = self._load_config()

    def _load_config(self) -> dict:
        if not os.path.exists(CONFIG_FILE):
            return {}
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}

    def load_memory(self) -> dict:
        """Load global memory from disk."""
        if not os.path.exists(MEMORY_FILE):
            return {}
        try:
            with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            self.logger.error(f"Failed to load memory: {e}")
            return {}

    def save_memory(self, memory: dict):
        """Save global memory to disk."""
        try:
            os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
            with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
                json.dump(memory, f, indent=4)
        except Exception as e:
            self.logger.error(f"Failed to save memory: {e}")

    def update_agent_memory(self, key: str, value: any):
        """Update a specific key in this agent's memory section."""
        full_mem = self.load_memory()
        if self.name not in full_mem:
            full_mem[self.name] = {}
        full_mem[self.name][key] = value
        self.save_memory(full_mem)

    def get_agent_memory(self, key: str, default=None):
        """Retrieve a specific key from this agent's memory."""
        full_mem = self.load_memory()
        return full_mem.get(self.name, {}).get(key, default)

    @abstractmethod
    async def run(self, data: list, blackboard: Blackboard) -> dict:
        """
        Run the agent's task asynchronously.
        :param data: The raw scraped data (list of dicts).
        :param blackboard: The shared state manager.
        :return: A dictionary containing this agent's output to be merged into blackboard.
        """
        pass

    async def review(self, blackboard: Blackboard) -> List[str]:
        """
        Optional: Review the work of other agents.
        :return: A list of suggestions or validations.
        """
        return []

    async def collaborate(self, other_agent_name: str, topic: str, blackboard: Blackboard):
        """Simulate a collaboration request to another agent."""
        self.logger.info(f"Collaborating with {other_agent_name} on '{topic}'...")
        await asyncio.sleep(0.05)
        return blackboard.get(topic)
