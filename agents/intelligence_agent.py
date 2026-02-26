from .base_agent import BaseAgent
from textblob import TextBlob

class IntelligenceAgent(BaseAgent):
    execution_stage = 3
    def __init__(self):
        super().__init__("IntelligenceAgent")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Running Intelligence (NLP Enabled)...")

        # Synthesize findings
        analysis = context.get("analysis_stats", {})
        research = context.get("research_notes", [])

        insights = []
        sentiments = []

        # NLP Analysis of Titles
        for item in data[:50]: # Sample for performance
            title = item.get("title", "")
            if title:
                blob = TextBlob(title)
                sentiments.append(blob.sentiment.polarity)

        avg_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0
        sentiment_label = "Positive" if avg_sentiment > 0.1 else "Negative" if avg_sentiment < -0.1 else "Neutral"

        insights.append(f"Content Sentiment: {sentiment_label} (Score: {round(avg_sentiment, 2)})")

        # Insight 1: Dominance
        top_cats = analysis.get("top_categories", {})
        if "Ad Ads Advertise" in top_cats:
            insights.append("High concentration of advertising-related content.")

        # Insight 2: Context
        if any("google" in note.lower() for note in research):
            insights.append("Google ecosystem is a primary focus area.")

        return {
            "intelligence_insights": insights,
            "sentiment_score": avg_sentiment
        }
