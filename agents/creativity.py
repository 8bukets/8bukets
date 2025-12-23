from agents.base import BaseAgent
import logging
import random

logger = logging.getLogger(__name__)

class CreativityAgent(BaseAgent):
    def __init__(self):
        super().__init__("CreativityAgent")

    def run(self, keywords):
        logger.info(f"[{self.name}] Generating creative ideas...")
        if not keywords:
            return []

        top_kws = [k[0] for k in keywords[:5]]
        ideas = []

        templates = [
            "Top 10 {} trends for this season",
            "Why {} is taking over the market",
            "The ultimate guide to buying {}",
            "Hidden gems in the {} category",
            "How to save money on {}"
        ]

        for _ in range(3):
            kw = random.choice(top_kws)
            template = random.choice(templates)
            ideas.append(template.format(kw))

        return ideas
