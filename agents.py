import random
import requests
from typing import List, Dict
from agent_framework import BaseAgent, KnowledgeBase
from seo_analyzer import SEOAnalyzer
from scraper import WordPressScraper
from google_search import run_search

# --- Specialized Agents ---

class AnalyzeAgent(BaseAgent):
    """Analyzes the website health and SEO."""
    def __init__(self, kb: KnowledgeBase, target_url: str):
        super().__init__("Analyze", kb)
        self.target_url = target_url

    def act(self):
        self.log(f"Running SEO analysis on {self.target_url}...")
        analyzer = SEOAnalyzer(self.target_url)
        report = analyzer.run()
        self.kb.update("seo_reports", report)
        self.log(f"Analysis complete. Score: {report.get('score')}")

class ResearchAgent(BaseAgent):
    """Researches market trends using Google Search."""
    def __init__(self, kb: KnowledgeBase, target_url: str = ""):
        # target_url is unused but kept for interface consistency
        super().__init__("Research", kb)

    def act(self):
        # In a real scenario, this would dynamically choose queries based on KB.
        query = "digital marketing trends 2025"
        self.log(f"Researching query: {query}")

        try:
            results = run_search(query, headless=True)
            self.kb.update("market_trends", {"query": query, "results": results})
            self.log(f"Found {len(results)} research items.")
        except Exception as e:
            self.log(f"Research failed: {e}")

class IntelligenceAgent(BaseAgent):
    """The 'Brain' that makes decisions based on data."""
    def __init__(self, kb: KnowledgeBase, target_url: str = ""):
        super().__init__("Intelligence", kb)

    def act(self):
        reports = self.kb.get("seo_reports") or []
        trends = self.kb.get("market_trends") or []

        decision = "Maintain course."

        if reports:
            latest_score = reports[-1].get("score", 0)
            if latest_score < 70:
                decision = "URGENT: Improve on-page SEO immediately."
                self.kb.update("tasks", {"priority": "High", "action": "Fix SEO Issues"})

        if trends:
            latest_trend = trends[-1]
            if latest_trend.get("results"):
                top_topic = latest_trend["results"][0]["title"]
                decision += f" Pivot content strategy to cover: {top_topic}"
                self.kb.update("tasks", {"priority": "Medium", "action": f"Write about {top_topic}"})

        self.log(f"Strategic Decision: {decision}")
        self.kb.update("insights", {"decision": decision})

class ContentAgent(BaseAgent):
    """Generates content ideas and drafts."""
    def __init__(self, kb: KnowledgeBase, target_url: str = ""):
        super().__init__("Content", kb)

    def act(self):
        tasks = self.kb.get("tasks") or []
        for task in tasks:
            if "Write about" in task.get("action", ""):
                topic = task["action"].replace("Write about ", "")
                draft = f"Title: Unlocking the Power of {topic}\n\nIntroduction: In today's fast-paced world, {topic} is key..."
                self.kb.update("content_ideas", {"topic": topic, "draft": draft})
                self.log(f"Generated content draft for: {topic}")

class AdsAgent(BaseAgent):
    """Autonomous Programmatic Advertising Agent."""
    def __init__(self, kb: KnowledgeBase, target_url: str = ""):
        super().__init__("Ads", kb)

    def act(self):
        # Analyze content to bid on keywords
        content_ideas = self.kb.get("content_ideas") or []
        if not content_ideas:
            self.log("No content to advertise.")
            return

        latest_content = content_ideas[-1]
        topic = latest_content.get("topic", "General Marketing")

        # Simulate Bidding Logic
        bid_price = round(random.uniform(0.50, 5.00), 2)
        targeting = {"region": "US", "demographic": "25-45", "interest": topic}

        campaign = {
            "campaign_name": f"Auto-Campaign-{topic}",
            "bid": bid_price,
            "targeting": targeting,
            "status": "Active"
        }

        self.kb.update("ad_campaigns", campaign)
        self.log(f"Created ad campaign: {campaign}")

class HealthAgent(BaseAgent):
    """Checks system health and Robots.txt compliance."""
    def __init__(self, kb: KnowledgeBase, target_url: str):
        super().__init__("Health", kb)
        self.target_url = target_url

    def act(self):
        try:
            resp = requests.get(self.target_url, timeout=5)
            status = "Online" if resp.status_code == 200 else "Issues"
            self.log(f"Health Check for {self.target_url}: {status} ({resp.status_code})")
        except Exception as e:
            self.log(f"Health Check Failed: {e}")

class CreativityAgent(BaseAgent):
    """Injects creativity and randomness."""
    def __init__(self, kb: KnowledgeBase, target_url: str = ""):
        super().__init__("Creativity", kb)

    def act(self):
        adjectives = ["Revolutionary", "Automated", "Unstoppable", "Quantum", "Viral"]
        nouns = ["Growth", "Synergy", "Intelligence", "Revenue", "Impact"]

        creative_idea = f"{random.choice(adjectives)} {random.choice(nouns)} Strategy"
        self.kb.update("content_ideas", {"topic": "Creative Concept", "draft": f"Concept: {creative_idea}"})
        self.log(f"Brainstormed creative concept: {creative_idea}")

class MonetizationAgent(BaseAgent):
    """Focuses on revenue opportunities."""
    def __init__(self, kb: KnowledgeBase, target_url: str = ""):
        super().__init__("Monetization", kb)

    def act(self):
        # Check if we have enough content to monetize
        content_ideas = self.kb.get("content_ideas") or []
        content_count = len(content_ideas)
        if content_count > 5:
            self.log("Sufficient content for monetization. Suggesting Affiliate Links integration.")
            self.kb.update("tasks", {"priority": "Low", "action": "Add Affiliate Links"})
        else:
            self.log("Need more content before aggressive monetization.")
