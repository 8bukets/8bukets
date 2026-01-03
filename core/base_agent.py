import json
import logging
import os
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class BaseAgent(ABC):
    def __init__(self, name, dna_path='data/dna.json'):
        self.name = name
        self.dna_path = dna_path
        self.logger = logging.getLogger(name)

    def load_dna(self):
        try:
            with open(self.dna_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            # Return a default structure to prevent crashes if file is missing
            return {
                "system_stats": {"iq": 25, "generation": 0, "total_revenue": 0.0},
                "parameters": {"bid_aggressiveness": 0.5, "creativity_level": 0.5, "cooperation_factor": 0.5},
                "policy": {"robots_txt_compliance": True}
            }

    def get_parameter(self, key, default=None):
        dna = self.load_dna()
        return dna.get('parameters', {}).get(key, default)

    def get_stat(self, key, default=None):
        dna = self.load_dna()
        return dna.get('system_stats', {}).get(key, default)

    @abstractmethod
    def run_cycle(self, context):
        """
        Executes one cycle of the agent's task.
        :param context: A dictionary shared across agents for the current cycle.
        """
        pass

    def log(self, message):
        self.logger.info(message)
