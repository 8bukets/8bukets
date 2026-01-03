import json
import random
from agents.base_agent import BaseAgent

class LearningAgent(BaseAgent):
    """Evolutionary agent that modifies system DNA based on feedback."""

    def __init__(self):
        super().__init__("Learning")
        self.dna_path = "system_dna.json"

    def process(self, market_feedback: dict, current_dna: dict) -> dict:
        """
        Analyzes market feedback and evolves the DNA.
        """
        self.log("Analyzing feedback and evolving DNA...")

        new_dna = current_dna.copy()
        new_dna['generation'] += 1

        # Simple Evolutionary Algorithm
        # If score is good, reinforce current traits (small random variance).
        # If score is bad, mutate traits significantly.

        score = market_feedback.get('net_score', 0)
        mutation_rate = 0.05 if score > 50 else 0.2

        self.log(f"Current Score: {score}. Mutation Rate: {mutation_rate}")

        # Evolve Ads Agent
        ads = new_dna['agents']['programmatic_ads']
        ads['bid_aggressiveness'] = self.mutate(ads['bid_aggressiveness'], mutation_rate)
        ads['ad_frequency'] = self.mutate(ads['ad_frequency'], mutation_rate)

        # Evolve Content Agent
        content = new_dna['agents']['content_creation']
        content['creativity_temperature'] = self.mutate(content['creativity_temperature'], mutation_rate)

        # Evolve IQ (Self-learning simulation)
        new_dna['iq_score'] += 0.25  # Increasing IQ every generation

        # Save new DNA
        self.save_dna(new_dna)

        return new_dna

    def mutate(self, value, rate):
        """Apply random mutation to a float value between 0 and 1 (clamped)."""
        change = random.uniform(-rate, rate)
        new_val = max(0.0, min(1.0, value + change))
        return new_val

    def save_dna(self, dna):
        """Saves the evolved DNA to disk."""
        with open(self.dna_path, 'w', encoding='utf-8') as f:
            json.dump(dna, f, indent=4)
        self.log(f"DNA evolved to Generation {dna['generation']}")
