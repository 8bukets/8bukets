from .base_agent import BaseAgent
from textblob import Word
from textblob import TextBlob

class CreativityAgent(BaseAgent):
    def __init__(self):
        super().__init__("Creativity")

    def perform_task(self, data):
        # Data is top keywords from Analyzer
        keywords = data.get("top_keywords", [])
        ideas = []

        for word, count in keywords[:3]:
            # Simple creativity: finding synsets/definitions (simulated creativity)
            try:
                w = Word(word)
                synonyms = w.synsets
                if synonyms:
                    idea = f"Explore the concept of '{synonyms[0].lemmas()[0].name()}' related to {word}."
                    ideas.append(idea)
                else:
                    ideas.append(f"Write a deep dive on '{word}'.")
            except Exception:
                ideas.append(f"Brainstorming failed for {word}.")

        return {"creative_ideas": ideas}
