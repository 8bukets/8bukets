from .base_agent import BaseAgent

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("Intelligence Agent")

    def run(self, data: dict) -> dict:
        """
        Synthesizes findings from Analysis and Research.
        Expects `data` to be a dict containing outputs from previous agents.
        """
        analysis_out = data.get('analysis', {})
        research_out = data.get('research', {})
        monetization_out = data.get('monetization', {})

        top_cats = list(analysis_out.get('top_categories', {}).keys())
        trends = research_out.get('trending_keywords', [])
        value_score = monetization_out.get('total_value_score', 0)

        brief = (
            f"Strategic Brief:\n"
            f"- Market Focus: The content is heavily skewed towards {', '.join(top_cats[:3])}.\n"
            f"- Trending Topics: Key emerging themes include {', '.join(trends[:5])}.\n"
            f"- Commercial Viability: The current dataset has a monetization potential score of {value_score}.\n"
        )

        return {
            "brief": brief,
            "actionable_insight": f"Focus future content on '{trends[0] if trends else 'general tech'}' within the '{top_cats[0] if top_cats else 'tech'}' category."
        }
