from .base_agent import BaseAgent, Blackboard
import os
import json
from textblob import TextBlob

class IntelligenceAgent(BaseAgent):
    """
    Advanced Intelligence Agent performing sentiment analysis and topic modeling
    on scraped market data to derive strategic insights.
    """
    def __init__(self):
        super().__init__("IntelligenceAgent",
                         dependencies=["analysis_stats", "research_data"],
                         provides=["intelligence_insights", "sentiment_report"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Running Advanced Intelligence & Sentiment Analysis...")

        analysis = blackboard.get("analysis_stats", {})
        research = blackboard.get("research_data", {})

        insights = []
        sentiments = []

        # 1. Sentiment Analysis on Post Titles
        for post in data[:100]:  # Analyze a sample for efficiency
            title = post.get('title', '')
            if title:
                blob = TextBlob(title)
                sentiments.append(blob.sentiment.polarity)

        avg_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0
        sentiment_label = "POSITIVE" if avg_sentiment > 0.1 else "NEGATIVE" if avg_sentiment < -0.1 else "NEUTRAL"

        sentiment_report = {
            "average_polarity": avg_sentiment,
            "overall_sentiment": sentiment_label,
            "sample_size": len(sentiments)
        }

        # 2. Synchronize with Research (Blackboard Collaboration)
        market_trends = research.get("market_trends", [])
        for trend in market_trends:
            insights.append(f"Synchronized Trend: {trend}")

        # 3. Collaborative Intelligence Synthesis
        if sentiment_label == "POSITIVE":
            insights.append("Market sentiment is optimistic; favorable for aggressive expansion.")
        elif sentiment_label == "NEGATIVE":
            insights.append("Caution detected in market sentiment; recommend defensive strategy.")

        for investigation in research.get("external_investigations", []):
            if investigation.get("world_context") == "GOOGLE_WORLD":
                insights.append(f"External World Insight: {investigation['domain']} is an active node in the Google World.")

        return {
            "intelligence_insights": insights,
            "sentiment_report": sentiment_report
        }
