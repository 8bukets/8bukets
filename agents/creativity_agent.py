from .base_agent import BaseAgent
import random

class CreativityAgent(BaseAgent):
    def __init__(self):
        super().__init__("Creativity Agent")

    def run(self, data):
        self.log("Brainstorming creative ideas...")

        ideas = [
            "Top 10 listicle based on most frequent domains",
            "Infographic showing the timeline of posts",
            "Podcast episode discussing the 'Intelligence' findings",
            "Twitter thread highlighting the 'Health Check' status",
            "Deep dive video into one of the 'Research' trends"
        ]

        selected_ideas = random.sample(ideas, 2)

        report = "### Creative Spark\n"
        report += "**Suggested Content Formats:**\n"
        for idea in selected_ideas:
            report += f"- {idea}\n"

        self.log("Brainstorming complete.")
        return report
