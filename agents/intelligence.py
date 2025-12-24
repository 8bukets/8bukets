from .base_agent import BaseAgent
from learning_module import LearningModule
import datetime

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("Intelligence")
        self.brain = LearningModule()

    def perform_task(self, data):
        # Data is a mix of Analyzer result and now potentially Advertising result
        analyzer_data = data.get("analysis", {})
        ad_data = data.get("advertising", {})

        sentiment = analyzer_data.get("average_sentiment", 0)
        keywords = analyzer_data.get("top_keywords", [])
        categories = analyzer_data.get("top_categories", [])

        # Evolve: Update knowledge base
        top_cat_name = categories[0][0] if categories else "Unknown"
        self.brain.update_stats(
            datetime.datetime.now().strftime("%Y-%m-%d"),
            sentiment,
            top_cat_name
        )

        # Get historical context
        history = self.brain.get_insights()

        insights = []

        # 1. Sentiment Strategy vs History
        if isinstance(history, dict):
            hist_avg = history.get("historical_average_sentiment", 0)
            if sentiment > hist_avg:
                insights.append("Current sentiment is improving over historical average.")
            else:
                insights.append("Current sentiment is dipping. Investigating engagement drivers.")

        # 2. Ad-Driven Strategy
        target = ad_data.get("target_audience", "General")
        insights.append(f"Align content tone for: {target}.")

        antigravity_picks = [item['keyword'] for item in ad_data.get("bid_strategy", []) if "Antigravity" in item['strategy']]
        if antigravity_picks:
            insights.append(f"Focus on 'Antigravity' keywords for ROI: {', '.join(antigravity_picks)}.")

        # 3. Content Focus Recommendation
        recommended_focus = keywords[0][0] if keywords else "General"
        if antigravity_picks:
            recommended_focus = antigravity_picks[0]

        return {
            "insights": insights,
            "recommended_focus": recommended_focus,
            "evolution_status": f"Learning from {history.get('data_points', 0) if isinstance(history, dict) else 0} historical cycles."
        }
