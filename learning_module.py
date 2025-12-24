import json
import os
import logging

class LearningModule:
    def __init__(self, db_file="knowledge_base.json"):
        self.db_file = db_file
        self.logger = logging.getLogger("LearningModule")
        self.knowledge = self._load_knowledge()

    def _load_knowledge(self):
        if os.path.exists(self.db_file):
            try:
                with open(self.db_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                self.logger.error(f"Failed to load knowledge base: {e}")
                return {}
        return {
            "history": [],
            "keyword_performance": {},
            "strategy_evolution": []
        }

    def _save_knowledge(self):
        try:
            with open(self.db_file, 'w', encoding='utf-8') as f:
                json.dump(self.knowledge, f, indent=4)
        except Exception as e:
            self.logger.error(f"Failed to save knowledge base: {e}")

    def update_stats(self, date, sentiment, top_category):
        entry = {
            "date": date,
            "sentiment": sentiment,
            "category": top_category
        }
        self.knowledge["history"].append(entry)

        # Simple evolution: Keep last 30 entries
        if len(self.knowledge["history"]) > 30:
            self.knowledge["history"].pop(0)

        self._save_knowledge()

    def update_keyword_value(self, keyword, score):
        # Simulate learning: if a keyword appears often, we value it more?
        # Or here we just track it.
        if keyword not in self.knowledge["keyword_performance"]:
            self.knowledge["keyword_performance"][keyword] = 0.0

        # Simple moving average or accumulation
        current = self.knowledge["keyword_performance"][keyword]
        self.knowledge["keyword_performance"][keyword] = (current + score) / 2
        self._save_knowledge()

    def get_insights(self):
        history = self.knowledge["history"]
        if not history:
            return "No historical data for insights."

        sentiments = [h["sentiment"] for h in history]
        avg_hist_sentiment = sum(sentiments) / len(sentiments)

        return {
            "historical_average_sentiment": avg_hist_sentiment,
            "data_points": len(history)
        }
