import json
import os
import logging

logger = logging.getLogger(__name__)

class KnowledgeBase:
    """
    Persistent memory for the autonomous system.
    Stores IQ level, experience, and learned parameters.
    """
    def __init__(self, filepath="iq_stats.json"):
        self.filepath = filepath
        self.data = {
            "iq": 25.0,  # Starting IQ as requested
            "cycles": 0,
            "total_experience": 0,
            "learned_strategies": []
        }
        self.load()

    def load(self):
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r') as f:
                    self.data = json.load(f)
            except Exception as e:
                logger.error(f"Failed to load knowledge base: {e}")

    def save(self):
        try:
            with open(self.filepath, 'w') as f:
                json.dump(self.data, f, indent=4)
        except Exception as e:
            logger.error(f"Failed to save knowledge base: {e}")

    def get_iq(self) -> float:
        return self.data.get("iq", 25.0)

    def learn(self, daily_score: float):
        """
        Update IQ based on the success of the daily cycle.
        Algorithm: IQ increases by a fraction of the daily score (diminishing returns).
        """
        current_iq = self.data["iq"]

        # Learning curve: It gets harder to increase IQ as it gets higher
        growth_factor = 0.1 / (1 + (current_iq / 100))
        iq_gain = daily_score * growth_factor

        self.data["iq"] = round(current_iq + iq_gain, 4)
        self.data["cycles"] += 1
        self.data["total_experience"] += daily_score

        # "Self-improving" logic: unlock strategies based on IQ milestones
        self._unlock_strategies()

        self.save()
        return iq_gain

    def _unlock_strategies(self):
        iq = self.data["iq"]
        strategies = self.data["learned_strategies"]

        new_strats = []
        if iq >= 26 and "concurrent_scraping_v2" not in strategies:
            new_strats.append("concurrent_scraping_v2")
        if iq >= 30 and "deep_analysis_v1" not in strategies:
            new_strats.append("deep_analysis_v1")
        if iq >= 50 and "predictive_bidding" not in strategies:
            new_strats.append("predictive_bidding")

        if new_strats:
            self.data["learned_strategies"].extend(new_strats)
            logger.info(f"🧠 NEW NEURAL PATHWAY UNLOCKED: {new_strats}")

    def get_strategy_param(self, param_name, default_value):
        """
        Returns a parameter value scaled by IQ.
        """
        iq = self.data["iq"]

        if param_name == "concurrency":
            # IQ 25 -> 3, IQ 100 -> 10
            return int(default_value + (iq - 25) / 10)

        if param_name == "creativity_level":
            return iq / 10.0

        return default_value
