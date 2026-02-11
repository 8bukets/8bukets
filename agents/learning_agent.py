"""
Learning Agent.
Manages the evolutionary aspect of the system by modifying the system DNA
based on simulated market feedback.
"""

import json
from typing import Any, Dict, List
from .base_agent import BaseAgent

class LearningAgent(BaseAgent):
    """
    Evolutionary Learning Agent that modifies system configuration (DNA).
    """
    def __init__(self):
        super().__init__("Evolutionary Learning")

    def run(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Modifies system_dna.json based on market feedback.
        """
        # Extract market feedback from the data stream (passed from MarketSimulationAgent)
        market_score = 0.5  # Default
        for item in data:
            if "market_feedback_score" in item:
                market_score = item["market_feedback_score"]
                break

        current_dna = self.dna.copy()
        learning_rate = current_dna.get("learning_rate", 0.05)

        changes = []

        # Evolutionary Logic:
        # If score is high, reinforce current traits slightly.
        # If score is low, mutate traits to find better fit.

        direction = 1 if market_score > 0.6 else -1
        mutation_magnitude = learning_rate * (1.0 - market_score if direction > 0 else 1.0)

        # Evolve Bid Aggressiveness
        old_bid = current_dna.get("bid_aggressiveness", 0.5)
        new_bid = max(0.1, min(1.0, old_bid + (direction * mutation_magnitude * 0.5)))
        current_dna["bid_aggressiveness"] = new_bid
        if old_bid != new_bid:
            changes.append(f"Bid: {old_bid:.2f}->{new_bid:.2f}")

        # Evolve IQ (Always goes up slowly)
        current_dna["iq_level"] = current_dna.get("iq_level", 25) + 0.1

        # Evolve Generation
        current_dna["generation"] = current_dna.get("generation", 1) + 1

        # Save mutated DNA
        self.save_dna(current_dna)

        return {
            "evolution_status": "DNA Updated",
            "generation": current_dna["generation"],
            "mutations": changes,
            "new_iq": current_dna["iq_level"]
        }

    def save_dna(self, dna: Dict[str, Any]):
        """Saves the DNA to the JSON file."""
        with open("system_dna.json", "w", encoding='utf-8') as f:
            json.dump(dna, f, indent=4)
