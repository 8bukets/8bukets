from agents.base_agent import BaseAgent
import random

class ContentAgent(BaseAgent):
    def __init__(self, name: str = "Content"):
        super().__init__(name)

    async def process(self, data: dict) -> dict:
        """
        Expects 'insights' from AnalysisAgent.
        """
        insights = data.get("insights", {})
        self.log("Generating content strategy based on insights...")

        top_cats = [c[0] for c in insights.get("top_categories", [])]
        top_domains = [d[0] for d in insights.get("top_domains", [])]

        # Generate a "content strategy"
        strategy = []
        if top_cats:
            strategy.append(f"Focus on high-performing categories: {', '.join(top_cats)}.")
        else:
            strategy.append("Explore new categories as current data is sparse.")

        if top_domains:
            strategy.append(f"Curate more content from trusted sources like: {', '.join(top_domains)}.")

        # "Create" some titles
        generated_titles = []
        templates = [
            "The Future of {cat}",
            "Why {domain} is Leading the Way",
            "Top 5 Trends in {cat}",
            "Deep Dive: {cat} Analysis"
        ]

        for _ in range(3):
            cat = random.choice(top_cats) if top_cats else "Tech"
            domain = random.choice(top_domains) if top_domains else "The Web"
            template = random.choice(templates)
            title = template.format(cat=cat, domain=domain)
            generated_titles.append(title)

        content_pack = {
            "strategy_brief": " ".join(strategy),
            "suggested_titles": generated_titles
        }

        self.log(f"Generated {len(generated_titles)} content ideas.")
        return {"status": "success", "content": content_pack}

class CreativityAgent(BaseAgent):
    def __init__(self, name: str = "Creativity"):
        super().__init__(name)

    async def process(self, data: dict) -> dict:
        """
        Adds 'flair' or 'antigravity' to content.
        Expects 'content' from ContentAgent.
        """
        content = data.get("content", {})
        titles = content.get("suggested_titles", [])

        self.log("Infusing creativity and defying gravity...")

        creative_titles = []
        emojis = ["🚀", "✨", "🔥", "💡", "🛡️", "🤖"]

        for title in titles:
            emoji = random.choice(emojis)
            # "Antigravity" effect: reverse words or something fun?
            # Let's just add a 'Google Antigravity' reference occasionally.
            if random.random() > 0.7:
                title = f"{title} (Zero G Edition)"

            creative_titles.append(f"{emoji} {title}")

        content["creative_titles"] = creative_titles
        self.log("Creativity infusion complete.")
        return {"status": "success", "creative_content": content}
