from .base_agent import BaseAgent
from typing import Dict, Any
import json
import os

class LearningAgent(BaseAgent):
    def __init__(self):
        super().__init__("Learning Agent")
        self.memory_file = "agent_memory.json"

    def load_state(self) -> Dict:
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    return json.load(f)
            except:
                return self._default_state()
        return self._default_state()

    def _default_state(self):
        return {
            "system_iq": 25,
            "total_runs": 0,
            "successful_runs": 0
        }

    def save_state(self, state: Dict):
        with open(self.memory_file, 'w') as f:
            json.dump(state, f, indent=4)

    def improve_iq(self, success: bool = True):
        state = self.load_state()
        state["total_runs"] += 1

        if success:
            state["successful_runs"] += 1
            # Simple learning curve: +1 IQ per successful run
            state["system_iq"] += 1
            self.log(f"🧠 System IQ increased to {state['system_iq']}!")

        self.save_state(state)
        return state["system_iq"]

    def get_iq(self) -> int:
        return self.load_state().get("system_iq", 25)
