from .base import BaseAgent
import random

class ResearchAgent(BaseAgent):
    def setup(self):
        self.bus.subscribe("request_research", self.handle_research_request)

    def handle_research_request(self, topic, message):
        query = message["content"].get("query")
        self.log(f"Received research request for: {query}")
        result = self.perform_research(query)
        self.publish("research_completed", {"query": query, "result": result})

    def perform_research(self, query):
        # Simulate researching
        topics = [
            "Programmatic Advertising Trends 2024",
            "AI in Content Creation",
            "High CPM Keywords",
            "Real-time Bidding Strategies"
        ]
        return f"Research data on {query}: Found {random.randint(5, 50)} relevant articles."

    def act(self):
        # Proactive research
        if random.random() < 0.3:
            topic = "Latest Market Trends"
            self.log(f"Initiating autonomous research on {topic}")
            result = self.perform_research(topic)
            self.memory.remember_fact(f"research_{random.randint(1000,9999)}", result)
            self.memory.log_experience(self.name, "autonomous_research", "success", 0.9)

class AnalyzeAgent(BaseAgent):
    def setup(self):
        self.bus.subscribe("research_completed", self.analyze_data)

    def analyze_data(self, topic, message):
        data = message["content"].get("result")
        self.log(f"Analyzing data: {data}")
        insight = f"Insight derived from {data}: Market is bullish."
        self.memory.remember_fact("latest_insight", insight)
        self.publish("analysis_completed", {"insight": insight})
        self.memory.log_experience(self.name, "analyze_research", "success", 0.95)

    def act(self):
        # Periodically review stored facts
        pass
