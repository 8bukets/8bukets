from .base_agent import BaseAgent

class ContentAgent(BaseAgent):
    def __init__(self):
        super().__init__("ContentAgent")

    def run(self, context):
        ideas = context.get('ideas', [])
        self.log("Generating content drafts...")

        drafts = {}
        for idea in ideas:
            # Simple template-based generation
            draft = f"""
            # {idea}

            Welcome to our latest post about {idea}. In this article, we explore the depths of this topic.
            Stay tuned for more updates!
            """
            drafts[idea] = draft.strip()

        self.learn("content_drafts", drafts)
        return {"drafts_count": len(drafts), "drafts": drafts}
