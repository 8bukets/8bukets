import json
import os
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

MEMORY_FILE = "system_memory.json"

class MemorySystem:
    def __init__(self):
        self.memory = self._load_memory()

    def _load_memory(self) -> Dict[str, Any]:
        if os.path.exists(MEMORY_FILE):
            try:
                with open(MEMORY_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Failed to load memory: {e}")

        # Default/Initial Memory
        return {
            "version": 1.0,
            "iterations": 0,
            "keyword_performance": {}, # "cloud": {"score": 10, "impressions": 100}
            "bid_strategy": {
                "base_bid": 1.50,
                "multipliers": {"Canada": 1.2, "India": 0.9}
            },
            "innovation_level": 0.1, # 0.0 to 1.0 (Antigravity factor)
            "history": [],
            "oracle_ai_knowledge": {}
        }

    def save_memory(self):
        try:
            with open(MEMORY_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.memory, f, indent=4)
            logger.info("Memory saved successfully.")
        except Exception as e:
            logger.error(f"Failed to save memory: {e}")

    def get(self, key: str, default=None):
        return self.memory.get(key, default)

    def update(self, key: str, value: Any):
        self.memory[key] = value

    def increment_iteration(self):
        self.memory["iterations"] += 1
