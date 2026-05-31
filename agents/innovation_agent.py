from agents.base_agent import BaseAgent

class InnovationAgent(BaseAgent):
    def __init__(self):
        super().__init__("Innovation")

    async def run(self, context: dict):
        self.log("Brainstorming system innovations and code integrations...")

        data = context.get("raw_data", [])
        analysis = context.get("analysis", {})
        top_domains = analysis.get("top_domains", [])

        domain_list = [d[0] for d in top_domains]

        innovations = []

        # Pattern Matching for Code Ideas
        if any("youtube" in d for d in domain_list):
            innovations.append({
                "trigger": "High volume of YouTube content",
                "idea": "Integrate `youtube-transcript-api` or `pytube` to extract video metadata and captions automatically.",
                "complexity": "Medium"
            })

        if any("spotify" in d for d in domain_list):
            innovations.append({
                "trigger": "Spotify links detected",
                "idea": "Integrate `spotipy` to fetch audio features (tempo, key) for linked tracks.",
                "complexity": "Medium"
            })

        if any("wordpress" in d for d in domain_list):
            innovations.append({
                "trigger": "WordPress ecosystem",
                "idea": "Implement `python-wordpress-xmlrpc` to post summarized findings back to a WordPress blog.",
                "complexity": "High"
            })

        if len(data) > 100:
            innovations.append({
                "trigger": "Large dataset (>100 items)",
                "idea": "Implement `pandas` for advanced dataframes and `matplotlib` for generating visual charts in the report.",
                "complexity": "Low"
            })

        # Curiosity / "High Interest" generic ideas
        innovations.append({
            "trigger": "Curiosity Protocol",
            "idea": "Implement Sentiment Analysis (VADER) to tag content as Positive/Negative/Neutral.",
            "complexity": "Low"
        })

        context["innovations"] = innovations
        self.log(f"Generated {len(innovations)} innovation ideas.")
