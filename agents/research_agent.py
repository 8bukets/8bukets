from .base_agent import BaseAgent
from typing import Dict, List, Any

class ResearchAgent(BaseAgent):
    def __init__(self):
        super().__init__("Research Agent")

    def process(self, data: List[Dict], memory: Dict[str, Any] = None) -> Dict:
        self.log("Synthesizing research...")

        # Simulate research findings based on titles
        findings = []

        if memory and 'oracle_ai_knowledge' in memory:
            oracle_ai_knowledge = memory['oracle_ai_knowledge']

            # Extract from key_points
            for point in oracle_ai_knowledge.get('key_points', []):
                if isinstance(point, str) and 'AI' in point:
                    findings.append(point)

            # Extract from features
            for feature in oracle_ai_knowledge.get('features', []):
                if isinstance(feature, dict):
                    for k, v in feature.items():
                        if isinstance(v, str) and 'AI' in v:
                            findings.append(v)
                        elif isinstance(k, str) and 'AI' in k:
                            findings.append(f"{k}: {v}")

        for item in data:
            title = item.get('title', '')
            if "Canada" in title:
                findings.append("Expansion into Canadian market identified.")
            if "India" in title:
                findings.append("Expansion into Indian market identified.")
            if "Available" in title:
                findings.append("Service availability confirmed in new regions.")

        return {
            "key_findings": findings,
            "research_summary": f"Identified {len(findings)} key strategic moves."
        }
