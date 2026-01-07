from .base_agent import BaseAgent
import asyncio

class ContentAgent(BaseAgent):
    def __init__(self, shared_state):
        super().__init__("ContentAgent", shared_state)

    async def process_message(self, message):
        if message.get('type') == 'analysis_result':
            self.log("📝 Generating content based on analysis...")
            # Simulate content creation
            content = f"New insights report: {message.get('summary')}"
            with open("generated_content.txt", "a") as f:
                f.write(content + "\n")
            self.log("✅ Content saved to generated_content.txt")

    async def perform_task(self):
        await asyncio.sleep(5)
