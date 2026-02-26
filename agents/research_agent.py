from .base_agent import BaseAgent

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("ResearchAgent")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Running Research...")

        # In a real system, this would define search queries or fetch external data.
        # Here, we simulate researching the top domains found by the AnalysisAgent.

        analysis = context.get("analysis_stats", {})
        top_domains = list(analysis.get("top_domains", {}).keys())

        research_notes = []
        for domain in top_domains[:3]:
            # Simulation
            note = f"Investigated {domain}:Appears to be a key player in the dataset."
            if "google" in domain:
                note += " (Major Ad Tech Platform)"
            elif "amazon" in domain:
                note += " (E-commerce/Ad Tech)"
            research_notes.append(note)

        return {"research_notes": research_notes}
