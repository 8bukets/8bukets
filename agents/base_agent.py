"""
Base Agent class for the autonomous multi-agent system.
"""
import json
import logging
import os

DEFAULT_DNA = {
    "generation": 0,
    "system_iq": 100,
    "parameters": {
        "bid_aggressiveness": 0.5,
        "content_creativity": 0.5,
        "research_depth": 0.5,
        "ad_targeting_precision": 0.5,
        "risk_tolerance": 0.3
    },
    "history": []
}

class BaseAgent:
    """
    Base class for all agents. Handles logging and DNA parameter access.
    """
    def __init__(self, name, dna_path="system_dna.json"):
        self.name = name
        self.dna_path = dna_path
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            ch = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)

    def load_dna(self):
        """Loads the system DNA configuration from JSON. Initializes if missing."""
        if not os.path.exists(self.dna_path):
            self.logger.warning("DNA file not found. Initializing with default DNA.")
            self.save_dna(DEFAULT_DNA)
            return DEFAULT_DNA

        try:
            with open(self.dna_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if not data: # Handle empty file
                    return self._reset_dna()
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            self.logger.error("DNA file corrupt or missing. Resetting.")
            return self._reset_dna()

    def _reset_dna(self):
        """Resets DNA to default values."""
        self.save_dna(DEFAULT_DNA)
        return DEFAULT_DNA

    def save_dna(self, dna):
        """Saves the DNA to disk."""
        with open(self.dna_path, 'w', encoding='utf-8') as f:
            json.dump(dna, f, indent=4)

    def get_parameter(self, key, default=0.5):
        """Retrieves a specific parameter from the DNA."""
        dna = self.load_dna()
        return dna.get("parameters", {}).get(key, default)

    def log_activity(self, message):
        """Logs an activity message."""
        self.logger.info(message)
