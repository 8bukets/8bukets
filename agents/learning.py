from .base import Agent
import json
import os
import datetime

class LearningAgent(Agent):
    def __init__(self, dna_path="system_dna.json"):
        self.dna_path = dna_path
        super().__init__("LearningAgent")

    def perform_task(self, context=None):
        """
        Context is expected to contain 'market_feedback' from MarketSimulationAgent.
        """
        market_feedback = context.get('market_feedback', {}) if context else {}
        score = market_feedback.get('score', 0)
        feedback_details = market_feedback.get('details', [])

        self.logger.info(f"Received Market Score: {score}")

        # Load DNA
        dna = self.load_dna()
        if not dna:
            dna = self.initialize_default_dna()

        # Evolution Logic
        dna.setdefault('system_stats', {})
        dna['system_stats']['generation'] = dna['system_stats'].get('generation', 0) + 1
        dna['system_stats']['last_evolution'] = datetime.datetime.now().isoformat()
        dna['system_stats']['iq_level'] = dna['system_stats'].get('iq_level', 10)

        # IQ Evolution: If score is good, IQ increases
        if score > 7.0:
            dna['system_stats']['iq_level'] += 1
            self.logger.info("Evolution: IQ Level Increased!")

        # Parameter Tuning based on feedback
        params = dna['parameters']
        learning_rate = params.get('learning_rate', 0.01)

        # Example: If content score was low, increase creativity
        if "content_quality_low" in feedback_details:
            params['creativity_temperature'] = min(1.0, params['creativity_temperature'] + learning_rate)
            self.logger.info("Evolution: Increased Creativity Temperature")

        # Example: If ad performance was low (simulated), adjust bid aggressiveness
        if "ad_revenue_low" in feedback_details:
             # Random mutation for bidding
            if score < 5.0:
                 params['bid_aggressiveness'] *= 1.1 # Try being more aggressive
            else:
                 params['bid_aggressiveness'] *= 0.9 # Optimize for efficiency
            self.logger.info(f"Evolution: Adjusted Bid Aggressiveness to {params['bid_aggressiveness']:.2f}")

        # Save evolved DNA
        self.save_dna(dna)
        self.results['evolved_dna'] = dna

    def initialize_default_dna(self):
        return {
            "system_stats": {
                "iq_level": 25,
                "generation": 0,
                "last_evolution": None
            },
            "parameters": {
                "creativity_temperature": 0.5,
                "bid_aggressiveness": 1.0,
                "risk_tolerance": 0.3,
                "ad_frequency_cap": 3,
                "content_verbosity": 1.0,
                "learning_rate": 0.01
            },
            "market_memory": {
                "successful_keywords": [],
                "failed_strategies": []
            }
        }

    def load_dna(self):
        if not os.path.exists(self.dna_path):
            return self.initialize_default_dna()
        try:
            with open(self.dna_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            self.logger.error(f"Error loading DNA: {e}")
            return self.initialize_default_dna()

    def save_dna(self, dna):
        try:
            with open(self.dna_path, 'w') as f:
                json.dump(dna, f, indent=2)
            self.logger.info("DNA successfully evolved and saved.")
        except Exception as e:
            self.logger.error(f"Error saving DNA: {e}")
