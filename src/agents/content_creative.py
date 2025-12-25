from .base import BaseAgent
import random

class ContentAgent(BaseAgent):
    def setup(self):
        self.bus.subscribe("analysis_completed", self.create_content)

    def create_content(self, topic, message):
        insight = message["content"].get("insight")
        self.log(f"Creating content based on insight: {insight}")
        title = f"The Future of {random.choice(['Ads', 'AI', 'Tech'])}"
        body = f"Based on recent analysis ({insight}), we conclude that..."
        content = {"title": title, "body": body}

        self.publish("content_created", content)
        self.memory.log_experience(self.name, "create_blog_post", "success", 0.85)

    def act(self):
        # Autonomous brainstorming
        if random.random() < 0.2:
            self.log("Brainstorming new content ideas...")

class CreativityAgent(BaseAgent):
    def setup(self):
        self.bus.subscribe("content_created", self.enhance_content)

    def enhance_content(self, topic, message):
        content = message["content"]
        self.log(f"Adding creative flair to '{content['title']}'")
        enhanced_title = f"✨ {content['title']} ✨"
        self.publish("content_enhanced", {"title": enhanced_title, "body": content['body']})
        self.memory.log_experience(self.name, "enhance_content", "success", 0.9)

    def act(self):
        pass
