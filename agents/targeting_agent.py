from .base_agent import BaseAgent
from typing import Dict, List, Any

class TargetingAgent(BaseAgent):
    def __init__(self):
        super().__init__("Targeting Agent")

    def process(self, keywords: List[tuple], memory: Dict[str, Any]) -> Dict:
        self.log("Defining targeting segments...")

        # Learn from memory: boost segments that match high-performing keywords
        perf_map = memory.get("keyword_performance", {})

        segments = ["IT Decision Makers", "Cloud Architects", "DBAs"]

        # Dynamic targeting based on scraped keywords
        top_kws = [k[0] for k in keywords[:5]]

        # If "Canada" or "India" is in top keywords, add geo-targeting
        geo_targets = []
        for kw in top_kws:
            if kw.lower() in ["canada", "india", "uk", "usa"]:
                geo_targets.append(kw)

        return {
            "audience_segments": segments,
            "geo_targeting": geo_targets if geo_targets else ["Global"],
            "keyword_targeting": top_kws,
            "exclusion_list": ["Competitors", "Students"]
        }
