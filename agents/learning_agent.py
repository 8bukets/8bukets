from .base_agent import BaseAgent
from typing import Dict
import json
import os

DNA_FILE = "dna.json"

class LearningAgent(BaseAgent):
    def __init__(self):
        super().__init__("Learning Agent")

    def process(self, market_feedback: Dict) -> Dict:
        self.log("Analyzing feedback and evolving DNA...")

        try:
            with open(DNA_FILE, 'r') as f:
                dna = json.load(f)
        except FileNotFoundError:
            self.log("DNA file not found, initializing default.")
            dna = {"system_iq": 25, "bid_aggressiveness": 0.5}

        # Evolutionary Logic
        score = market_feedback.get("market_score", 0)

        # IQ Growth
        if score > 75:
            dna["system_iq"] += 1
            self.log("High performance! IQ increased.")

        # Parameter Mutation
        if "Increase" in market_feedback.get("feedback", ""):
            dna["bid_aggressiveness"] = min(1.0, dna.get("bid_aggressiveness", 0.5) + 0.05)
        else:
            # Stabilize
            dna["bid_aggressiveness"] = max(0.1, dna.get("bid_aggressiveness", 0.5) - 0.01)

        dna["evolution_generation"] = dna.get("evolution_generation", 1) + 1

        # Save evolved DNA
        with open(DNA_FILE, 'w') as f:
            json.dump(dna, f, indent=4)

        return dna
