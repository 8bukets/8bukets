"""
Learning Agent module.
Responsible for evolutionary logic (DNA updates).
"""
import json
import random
from .base_agent import BaseAgent

class LearningAgent(BaseAgent):
    """
    LearningAgent analyzes performance and evolves the system parameters.
    """
    def __init__(self):
        super().__init__("LearningAgent")

    def evolve(self, market_feedback):
        """Update system DNA based on feedback."""
        dna = self.load_dna()
        params = dna['parameters']

        revenue = market_feedback['revenue']
        # Simple evolutionary logic

        history = dna.get('history', [])
        prev_revenue = history[-1]['revenue'] if history else 0

        self.log_activity(
            f"Analyzing performance: Current=${revenue:.2f} vs Previous=${prev_revenue:.2f}"
        )

        mutation_rate = 0.1
        if revenue > prev_revenue:
            self.log_activity("Performance improved. Stabilizing parameters.")
            mutation_rate = 0.05
        else:
            self.log_activity("Performance declined/stagnant. Mutating parameters.")
            mutation_rate = 0.2

        # Mutate
        for key in params:
            change = random.uniform(-mutation_rate, mutation_rate)
            params[key] = max(0.1, min(1.0, params[key] + change))

        # Update generation and IQ
        dna['generation'] += 1
        dna['system_iq'] += (0.1 if revenue > prev_revenue else 0)

        # Save history
        history.append({
            "generation": dna['generation'],
            "revenue": revenue,
            "params_snapshot": params.copy()
        })
        # Keep last 10 entries
        dna['history'] = history[-10:]

        self.save_dna(dna)
        self.log_activity(
            f"Evolution complete. Generation {dna['generation']}. New IQ: {dna['system_iq']:.1f}"
        )

    def save_dna(self, dna):
        """Saves the updated DNA to disk."""
        with open(self.dna_path, 'w', encoding='utf-8') as f:
            json.dump(dna, f, indent=4)
