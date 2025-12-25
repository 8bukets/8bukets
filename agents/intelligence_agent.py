from .base_agent import BaseAgent

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("Intelligence Agent")

    def run(self):
        self.log("Synthesizing intelligence...")
        # Simulating intelligence gathering from "Research" data (conceptually)
        # In a real system, this would consume the output of ResearchAgent.
        # Here we re-derive some insights or look for specific patterns.

        competitors = ["google", "facebook", "amazon", "apple", "microsoft"]
        mentions = {comp: 0 for comp in competitors}

        for p in self.data:
            title = p.get('title', '').lower()
            for comp in competitors:
                if comp in title:
                    mentions[comp] += 1

        top_competitor = max(mentions, key=mentions.get)

        self.results = {
            "competitor_mentions": mentions,
            "market_leader_signal": top_competitor,
            "strategic_insight": f"High activity detected for {top_competitor}. Recommend monitoring their latest ad tech updates."
        }
        self.log("Intelligence gathered.")
