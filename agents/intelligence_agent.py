from core.base_agent import BaseAgent

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("IntelligenceAgent")

    def run_cycle(self, context):
        iq = self.get_stat('iq')
        self.log(f"Processing data with System IQ: {iq}")

        analysis = context.get('analysis_report', {})
        research = context.get('research_data', {})

        # Synthesize a strategy
        strategy = {
            "focus_area": research.get('topic', 'General'),
            "action_plan": "optimize_bids" if "ad_relevance" in analysis.get('identified_gaps', []) else "create_content",
            "complexity_level": iq / 100.0
        }

        context['strategy'] = strategy
        self.log(f"Strategic decision made: {strategy['action_plan']}")
