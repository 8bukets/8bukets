from .base_agent import BaseAgent
from typing import Dict, List
import random

class CreativityAgent(BaseAgent):
    def __init__(self):
        super().__init__("Creativity Agent")

    def process(self, keywords: List[tuple]) -> List[str]:
        self.log("Generating creative headlines...")

        words = [w[0].title() for w in keywords]
        if not words:
            words = ["Cloud", "Future", "Tech"]

        headlines = [
            f"Why {words[0]} is the New Gold",
            f"The Secret Behind Oracle's {words[1] if len(words)>1 else 'Move'}",
            f"10 Things You Didn't Know About {words[0]} and Google"
        ]
        return headlines
