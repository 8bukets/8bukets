from datetime import datetime
from .base_agent import BaseAgent

class ContentAgent(BaseAgent):
    def __init__(self):
        super().__init__("Content Agent")

    def run(self):
        self.log("Drafting content...")

        # In a real pipeline, this would take input from CreativityAgent
        title = f"The Future of AdTech: Insights for {datetime.now().strftime('%B %Y')}"
        body = (
            "As we analyze the latest trends in the digital advertising space, one thing is clear: "
            "integration and privacy are top of mind. "
            "Our latest data shows a significant shift towards privacy-first platforms. "
            "Stay tuned as we explore these developments."
        )

        self.results = {
            "blog_post_title": title,
            "blog_post_snippet": body,
            "social_media_tweet": f"Just published: {title}. #AdTech #Marketing #Trends"
        }
        self.log("Content drafted.")
