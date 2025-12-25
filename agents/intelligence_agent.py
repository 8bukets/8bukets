from .base_agent import BaseAgent

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("Intelligence Agent")

    def run(self, data, context=None):
        self.log("Gathering intelligence...")

        # Identify high-value targets (e.g., .gov or .edu domains, or specific tech giants)
        high_value_domains = ['google', 'amazon', 'facebook', 'apple', 'microsoft']
        found_targets = {}

        for p in data:
            domain = p.get('domain', '')
            if domain:
                for target in high_value_domains:
                    if target in domain:
                        found_targets[target] = found_targets.get(target, 0) + 1

        report = "### Market Intelligence\n"
        report += "**Competitor/Tech Giant Activity:**\n"
        for target, count in found_targets.items():
            report += f"- {target.capitalize()}: {count} links found\n"

        self.log("Intelligence gathering complete.")
        return report
