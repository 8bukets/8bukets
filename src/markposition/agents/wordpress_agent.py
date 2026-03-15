from markposition.agents.base_agent import BaseAgent
import os
import aiohttp
import json
import base64

class WordPressAgent(BaseAgent):
    """
    Autonomous publishing agent for WordPress.
    Connects to markposition.wordpress.com (or any WP instance) via REST API.
    """
    execution_stage = 13 # Final publishing stage

    def __init__(self):
        super().__init__("WordPressAgent")
        self.wp_url = os.getenv("WP_URL", "https://markposition.wordpress.com/wp-json/wp/v2")
        self.wp_user = os.getenv("WP_USER")
        self.wp_password = os.getenv("WP_PASSWORD")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Executing Autonomous WordPress Publishing...")

        # 1. Extract content from previous stage
        content_html = context.get("generated_content_html")
        content_text = context.get("generated_content")
        title = context.get("top_pattern", "Daily Market Intelligence Report")

        if not content_html and not content_text:
             self.logger.warning("No content generated. Skipping WordPress publishing.")
             return {"wp_published": False, "wp_error": "No content available."}

        # 2. Build WordPress Post Payload
        payload = {
            "title": title,
            "content": content_html if content_html else f"<pre>{content_text}</pre>",
            "status": "publish", # Can be 'draft' for review
            "categories": [1], # Default category
            "tags": []
        }

        # Map intelligence categories to WP tags (simplified)
        for cat in context.get("market_patterns", []):
             if ":" in cat:
                  payload["tags"].append(cat.split(":")[1].split("(")[0].strip())

        # 3. Publish to WordPress
        if not self.wp_user or not self.wp_password:
             self.logger.info("WordPress credentials not provided. Simulating publish...")
             self.logger.info(f"Simulated Post: {title} -> {self.wp_url}/posts")
             return {"wp_published": "SIMULATED", "wp_url_target": self.wp_url}

        # Handle Auth (Application Passwords)
        auth_str = f"{self.wp_user}:{self.wp_password}"
        encoded_auth = base64.b64encode(auth_str.encode()).decode()
        headers = {
            "Authorization": f"Basic {encoded_auth}",
            "Content-Type": "application/json"
        }

        try:
            async with self.session.post(f"{self.wp_url}/posts", json=payload, headers=headers) as resp:
                if resp.status in [200, 201]:
                    post_data = await resp.json()
                    self.logger.info(f"Published successfully: {post_data.get('link')}")
                    return {"wp_published": True, "wp_post_link": post_data.get('link')}
                else:
                    error_msg = await resp.text()
                    self.logger.error(f"Failed to publish to WordPress (Status: {resp.status}): {error_msg}")
                    return {"wp_published": False, "wp_error": f"Status {resp.status}"}
        except Exception as e:
            self.logger.error(f"Error connecting to WordPress API: {e}")
            return {"wp_published": False, "wp_error": str(e)}
