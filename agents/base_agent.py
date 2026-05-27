from abc import ABC, abstractmethod
import logging
import json
import os
import asyncio
from datetime import datetime
from typing import Any, Dict, List, Set

MEMORY_FILE = "data/memory.json"
CONFIG_FILE = "config/evolution_params.json"

class Blackboard:
    """Shared state management with history tracking and evolutionary proposals (Consensus Memory)."""
    def __init__(self):
        self._data: Dict[str, Any] = {}
        self._history: List[Dict[str, Any]] = []
        self._proposals: List[Dict[str, Any]] = []
        self._consensus_memory: Dict[str, Any] = {}
        self._lock = asyncio.Lock()

    async def update(self, agent_name: str, updates: Dict[str, Any]):
        async with self._lock:
            self._data.update(updates)
            self._history.append({
                "agent": agent_name,
                "timestamp": asyncio.get_event_loop().time(),
                "keys": list(updates.keys())
            })

    async def update_consensus(self, key: str, value: Any):
        """Update shared information among agents (Consensus Memory)."""
        async with self._lock:
            self._consensus_memory[key] = value

    def get_consensus(self, key: str, default=None) -> Any:
        return self._consensus_memory.get(key, default)

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

    async def report_issue(self, agent_name: str, issue_type: str, details: Dict[str, Any] = None):
        """Allows an agent to report a system issue to the blackboard."""
        async with self._lock:
            issues = self._data.get("system_issues", [])
            issues.append({
                "id": f"issue-{len(issues)+1}",
                "type": issue_type,
                "reporter": agent_name,
                "timestamp": asyncio.get_event_loop().time(),
                "details": details or {}
            })
            self._data["system_issues"] = issues

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

        # Formalized Persona (Google Cloud AI Agent standard)
        self.persona = {
            "role": name,
            "personality": "Professional and analytical autonomous agent",
            "communication_style": "Structured and data-driven"
        }

        # Multi-tiered Memory initialization
        self.short_term_memory: Dict[str, Any] = {} # Per-cycle context
        # Episodic memory is stored in self.name section of global memory (data/memory.json)
        # Long-term memory is also part of global memory or specialized stores.

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

    def update_agent_memory(self, key: str, value: Any, memory_type: str = "long_term"):
        """Update agent memory by type (Short-term, Long-term, Episodic)."""
        if memory_type == "short_term":
            self.short_term_memory[key] = value
        else:
            full_mem = self.load_memory()
            if self.name not in full_mem:
                full_mem[self.name] = {"long_term": {}, "episodic": []}

            if memory_type == "long_term":
                if "long_term" not in full_mem[self.name]:
                     full_mem[self.name]["long_term"] = {}
                full_mem[self.name]["long_term"][key] = value
            elif memory_type == "episodic":
                if "episodic" not in full_mem[self.name]:
                    full_mem[self.name]["episodic"] = []
                full_mem[self.name]["episodic"].append({
                    "timestamp": datetime.now().isoformat(),
                    "event": key,
                    "data": value
                })
            self.save_memory(full_mem)

    def get_agent_memory(self, key: str, default=None, memory_type: str = "long_term"):
        """Retrieve agent memory by type with backward compatibility."""
        if memory_type == "short_term":
            return self.short_term_memory.get(key, default)

        full_mem = self.load_memory()
        agent_mem = full_mem.get(self.name, {})
        if memory_type == "long_term":
            # Backward compatibility: Check nested "long_term" first
            if "long_term" in agent_mem and isinstance(agent_mem["long_term"], dict):
                if key in agent_mem["long_term"]:
                    return agent_mem["long_term"][key]
            # Fallback to flat agent_mem
            return agent_mem.get(key, default)
        elif memory_type == "episodic":
            return agent_mem.get("episodic", [])
        return default

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
