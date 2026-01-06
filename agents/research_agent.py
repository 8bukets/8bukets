import logging
from collections import defaultdict

logger = logging.getLogger("ResearchAgent")

class ResearchAgent:
    def __init__(self):
        pass

    def identify_trends(self, analysis_results):
        """Identifies trends by grouping articles with similar keywords."""
        if not analysis_results:
            return {}

        trends = defaultdict(list)

        # Simple clustering: If an article contains a top keyword, add it to that trend
        top_keywords = [k[0] for k in analysis_results.get("top_keywords", [])]

        for article in analysis_results.get("articles", []):
            assigned = False
            for keyword in article["keywords"]:
                if keyword in top_keywords:
                    trends[keyword].append(article["title"])
                    assigned = True
                    # An article can belong to multiple trends, but let's just pick relevant ones

            # If no top keyword found, maybe put in "General" or skip
            if not assigned:
                trends["General"].append(article["title"])

        # Filter out small trends
        major_trends = {k: v for k, v in trends.items() if len(v) > 1}

        logger.info(f"📈 Identified {len(major_trends)} major trends.")
        return major_trends
