from .base_agent import BaseAgent
import json
import os
import random

class AdsAgent(BaseAgent):
    def __init__(self):
        super().__init__("Ads Agent")
        self.memory_file = "ads_memory.json"
        self.knowledge = self.load_memory()

    def load_memory(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    return json.load(f)
            except:
                return {"high_performing_keywords": []}
        return {"high_performing_keywords": []}

    def save_memory(self):
        with open(self.memory_file, 'w') as f:
            json.dump(self.knowledge, f)

    def run(self, data, context=None):
        self.log("Analyzing for Ad Strategy...")

        # 1. Integrate with Context (Collaboration)
        intelligence_insights = ""
        if context and 'Intelligence Agent' in context:
            intelligence_insights = context['Intelligence Agent']
            self.log("Integrating Intelligence insights...")

        # 2. Extract Keywords for Targeting
        keywords = []
        for p in data:
            title_words = p.get('title', '').split()
            keywords.extend([w for w in title_words if len(w) > 5])

        top_keywords = list(set(keywords))[:5]

        # Simulate Learning: Add new keywords to memory
        new_keywords = [k for k in top_keywords if k not in self.knowledge["high_performing_keywords"]]
        if new_keywords:
            self.knowledge["high_performing_keywords"].extend(new_keywords)
            self.save_memory()
            self.log(f"Learned {len(new_keywords)} new potential keywords.")

        # 3. Generate Strategy
        report = "### Programmatic Ads & Targeting Strategy\n"

        if intelligence_insights:
            report += "**Intelligence Integration:**\n"
            report += f"> Used insights to refine bidding against competitors.\n\n"

        report += "**Targeting Keywords:**\n"
        report += ", ".join(self.knowledge["high_performing_keywords"][-10:]) + "\n\n"

        report += "**Bid Strategy:**\n"
        report += "- **High Bid:** Technology, AI, Automation sectors\n"
        report += "- **Medium Bid:** General news\n"
        report += "- **Low Bid:** Retargeting only\n\n"

        report += "**Generated Ad Copy:**\n"
        sample_ad = f"Discover the future of {random.choice(top_keywords) if top_keywords else 'Tech'}. Read the latest analysis now."
        report += f"'{sample_ad}'\n"

        self.log("Ad strategy generated.")
        return report
