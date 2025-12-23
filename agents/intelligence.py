from .base_agent import BaseAgent

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("Intelligence")

    def perform_task(self, data):
        # Data is the output from AnalyzerAgent
        if not data:
            return {"strategy": "No data available."}

        sentiment = data.get("average_sentiment", 0)
        keywords = data.get("top_keywords", [])
        categories = data.get("top_categories", [])

        insights = []

        # Sentiment Strategy
        if sentiment > 0.1:
            insights.append("Content is performing with positive tone. Continue current strategy.")
        elif sentiment < -0.1:
            insights.append("Content tone is negative. Consider publishing more uplifting or solution-oriented content.")
        else:
            insights.append("Content tone is neutral. Experiment with more opinionated pieces.")

        # Keyword Strategy
        if keywords:
            top_word = keywords[0][0]
            insights.append(f"High focus on '{top_word}'. Consider diversifying or deepening this topic.")

        # Category Strategy
        if categories:
            top_cat = categories[0][0]
            insights.append(f"Category '{top_cat}' is dominant. Explore underrepresented categories.")

        return {
            "insights": insights,
            "recommended_focus": keywords[0][0] if keywords else "general"
        }
