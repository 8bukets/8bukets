import logging
from agents.analyze_agent import AnalyzeAgent

logger = logging.getLogger("IntelligenceAgent")

class IntelligenceAgent(AnalyzeAgent):
    def synthesize_strategy(self, analysis_data):
        """Synthesizes high-level insights from analysis."""
        if not analysis_data:
            return "No data to synthesize."

        positive_count = sum(1 for a in analysis_data['articles'] if a['sentiment'] > 0)
        negative_count = sum(1 for a in analysis_data['articles'] if a['sentiment'] < 0)

        strategy = {
            "market_mood": "Positive" if positive_count > negative_count else "Negative",
            "focus_areas": [k[0] for k in analysis_data['top_keywords'][:3]],
            "recommendation": "Focus on identified positive trends."
        }
        return strategy
