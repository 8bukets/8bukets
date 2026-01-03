from typing import List, Dict, Any
from .base_agent import BaseAgent

class AutonomousIntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("Autonomous Intelligence Agent")

    def run(self, data: List[Dict[str, Any]], dna: Dict[str, Any] = None, feedback: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Evolves the DNA based on feedback.
        """
        if not dna or not feedback:
            return {"status": "No DNA or Feedback provided", "dna_update": None}

        current_iq = dna.get("system_iq", 25)
        performance_score = feedback.get("market_score", 0)

        # Evolution Logic
        new_dna = dna.copy()

        # IQ Growth (Self-learning)
        # If performance was good, IQ grows slightly
        if performance_score > 0.5:
            new_dna["system_iq"] = min(200, current_iq + 1)

        # Adaptive Bidding
        current_aggressiveness = new_dna["bid_strategy"]["aggressiveness"]
        if performance_score < 0.4:
            # Underperforming, try being more aggressive
            new_dna["bid_strategy"]["aggressiveness"] = min(1.0, current_aggressiveness + 0.1)
        elif performance_score > 0.8:
            # Overperforming, maybe optimize budget (slightly lower aggressiveness to save cost)
            new_dna["bid_strategy"]["aggressiveness"] = max(0.1, current_aggressiveness - 0.05)

        # Content Strategy Evolution
        current_creativity = new_dna["content_strategy"]["creativity_weight"]
        if feedback.get("engagement_score", 0) < 0.5:
             new_dna["content_strategy"]["creativity_weight"] = min(1.0, current_creativity + 0.1)

        new_dna["last_performance_score"] = performance_score

        return {
            "status": "Evolved",
            "previous_iq": current_iq,
            "new_iq": new_dna["system_iq"],
            "new_dna": new_dna
        }

    def format_report(self, results: Dict[str, Any]) -> str:
        if results.get("status") != "Evolved":
            return f"## {self.name} Report\nStatus: {results.get('status')}"

        return f"""## {self.name} Report
**Evolution Status:** {results['status']}
**IQ Evolution:** {results['previous_iq']} -> {results['new_iq']}
**Key DNA Updates:**
- Bid Aggressiveness: {results['new_dna']['bid_strategy']['aggressiveness']:.2f}
- Creativity Weight: {results['new_dna']['content_strategy']['creativity_weight']:.2f}
"""
