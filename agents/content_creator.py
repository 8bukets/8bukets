from .base_agent import BaseAgent
import random


class ContentCreatorAgent(BaseAgent):
    def __init__(self):
        super().__init__("ContentCreator")

    def perform_task(self, data):
        # Data is output from IntelligenceAgent
        focus = data.get("recommended_focus", "Technology")
        insights = data.get("insights", [])

        self.logger.info(f"Creating content focused on: {focus}")

        titles = [
            f"The Future of {focus.capitalize()}: What You Need to Know",
            f"5 Ways {focus.capitalize()} is Changing the Industry",
            f"Why {focus.capitalize()} Matters in 2025",
            f"A Beginner's Guide to {focus.capitalize()}"
        ]

        selected_title = random.choice(titles)
        draft = f"# {selected_title}\n\n"
        draft += "## Introduction\n"
        draft += f"In the rapidly evolving world of {focus}, staying ahead is crucial.\n\n"
        draft += "## Key Insights\n"
        for insight in insights:
            draft += f"- {insight}\n"
        draft += "\n## Conclusion\n"
        draft += "Stay tuned for more updates."

        return {"draft_title": selected_title, "draft_content": draft}
