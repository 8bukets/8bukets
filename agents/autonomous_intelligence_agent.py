from core.base_agent import BaseAgent
import json

class AutonomousIntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("AutonomousIntelligenceAgent")

    def run_cycle(self, context):
        self.log("Evolutionary Architecture: Analyzing feedback to modify DNA...")

        # This agent modifies the 'dna.json' file based on performance
        feedback = context.get('market_feedback', {})
        financials = context.get('financials', {})

        current_dna = self.load_dna()
        if not current_dna:
            return

        # 1. Update IQ (Self-learning/Improving)
        # IQ increases if revenue was generated or quality was high
        quality = feedback.get('quality_score', 0)
        current_iq = current_dna['system_stats']['iq']
        new_iq = current_iq + (quality * 0.1)
        current_dna['system_stats']['iq'] = round(new_iq, 2)

        # 2. Update Total Revenue
        revenue = financials.get('cycle_revenue', 0)
        current_dna['system_stats']['total_revenue'] += revenue

        # 3. Evolve Parameters (DNA Mutation)
        # If clicks were low, increase bid aggressiveness or creativity
        clicks = feedback.get('clicks', 0)
        if clicks < 5:
            self.log("Performance low: Increasing bid aggressiveness and creativity.")
            current_dna['parameters']['bid_aggressiveness'] = min(1.0, current_dna['parameters']['bid_aggressiveness'] + 0.05)
            current_dna['parameters']['creativity_level'] = min(1.0, current_dna['parameters']['creativity_level'] + 0.05)

        # Increment generation
        current_dna['system_stats']['generation'] += 1

        # Save mutated DNA
        self.save_dna(current_dna)
        self.log(f"Evolution Complete. New IQ: {new_iq}, Generation: {current_dna['system_stats']['generation']}")

    def save_dna(self, dna_data):
        try:
            with open(self.dna_path, 'w') as f:
                json.dump(dna_data, f, indent=4)
        except Exception as e:
            self.logger.error(f"Failed to save evolved DNA: {e}")
