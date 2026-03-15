from .base_agent import BaseAgent
import collections

class PatternAgent(BaseAgent):
    execution_stage = 4 # Runs after Analysis/Intelligence
    def __init__(self):
        super().__init__("PatternAgent")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Extracting market patterns...")

        # 1. Category Patterns
        categories = []
        for item in data:
            categories.extend(item.get("categories", []))

        cat_counts = collections.Counter(categories)
        top_patterns = [f"Dominant Category: {cat} ({count} occurrences)" for cat, count in cat_counts.most_common(3)]

        # 2. Domain Patterns
        domains = [item.get("domain") for item in data if item.get("domain")]
        domain_counts = collections.Counter(domains)
        domain_patterns = [f"Frequent Domain: {dom} ({count} posts)" for dom, count in domain_counts.most_common(3)]

        # 3. Temporal Patterns (simplified)
        dates = [item.get("date") for item in data if item.get("date")]
        # Just count posts per month/year if possible

        all_patterns = top_patterns + domain_patterns

        # Persistence
        for pattern in all_patterns:
            self.add_vector_insight(f"Market Pattern: {pattern}", {"type": "pattern_recognition"})

        return {
            "market_patterns": all_patterns,
            "top_pattern": all_patterns[0] if all_patterns else "None detected"
        }
