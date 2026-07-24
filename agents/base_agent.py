import logging
import os
import json
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

class Blackboard(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._proposals = []

    async def async_update(self, key, value):
        self[key] = value

    async def update(self, key_or_dict, value=None):
        if value is not None:
            self[key_or_dict] = value
        else:
            super().update(key_or_dict)

    async def update_consensus(self, key, value):
        if "consensus" not in self:
            self["consensus"] = {}
        self["consensus"][key] = value

    def get_consensus(self, key, default=None):
        return self.get("consensus", {}).get(key, default)

    async def propose_improvement(self, proposer, improvement):
        self._proposals.append({
            "proposer": proposer,
            "improvement": improvement
        })

    def get_proposals(self):
        return self._proposals

    def get_all(self):
        return dict(self)

class BaseAgent(ABC):
    def __init__(self, name, dependencies=None, provides=None):
        self.name = name
        self.dependencies = dependencies or []
        self.provides = provides or []
        self.logger = logging.getLogger(f"Agent.{name}")
        self.config = self._load_config()
        self.persona = {
            "role": name,
            "personality": "Professional, efficient, and direct",
            "communication_style": "Clear, concise"
        }
        self._short_term_memory = {}

    def _load_config(self):
        config_path = "config/evolution_params.json"
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def get_agent_memory(self, key, default=None, memory_type="long_term"):
        if memory_type == "short_term":
            return self._short_term_memory.get(key, default)

        memory_path = "data/memory.json"
        if not os.path.exists(memory_path):
            return default

        try:
            with open(memory_path, "r", encoding="utf-8") as f:
                memory_data = json.load(f)
        except Exception:
            memory_data = {}

        agent_mem = memory_data.get(self.name, {})

        if memory_type == "episodic":
            return agent_mem.get("episodic", [])

        # For long_term or general memory
        if "long_term" in agent_mem and key in agent_mem["long_term"]:
            return agent_mem["long_term"][key]
        if key in agent_mem:
            return agent_mem[key]

        return default

    def update_agent_memory(self, key, value, memory_type="long_term"):
        if memory_type == "short_term":
            self._short_term_memory[key] = value
            return

        memory_path = "data/memory.json"
        os.makedirs(os.path.dirname(memory_path), exist_ok=True)

        try:
            if os.path.exists(memory_path):
                with open(memory_path, "r", encoding="utf-8") as f:
                    memory_data = json.load(f)
            else:
                memory_data = {}
        except Exception:
            memory_data = {}

        if self.name not in memory_data:
            memory_data[self.name] = {}

        agent_mem = memory_data[self.name]

        if memory_type == "episodic":
            if "episodic" not in agent_mem:
                agent_mem["episodic"] = []
            import datetime
            agent_mem["episodic"].append({
                "timestamp": datetime.datetime.now().isoformat(),
                "event": key,
                "data": value
            })
        else:
            if "long_term" not in agent_mem:
                agent_mem["long_term"] = {}
            agent_mem["long_term"][key] = value
            agent_mem[key] = value

        try:
            with open(memory_path, "w", encoding="utf-8") as f:
                json.dump(memory_data, f, indent=4, ensure_ascii=False)
        except Exception as e:
            self.logger.error(f"Failed to write agent memory to {memory_path}: {e}")

    @abstractmethod
    async def run(self, context: dict):
        """
        Execute the agent's task.
        :param context: A shared dictionary containing data and state.
        """
        pass

    def log(self, message):
        self.logger.info(message)
