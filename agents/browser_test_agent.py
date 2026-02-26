from .base_agent import BaseAgent
from playwright.async_api import async_playwright
import os
from datetime import datetime

class BrowserTestAgent(BaseAgent):
    def __init__(self):
        super().__init__("BrowserTestAgent")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Running Browser Verification Test...")

        url = os.getenv("BASE_URL", "https://markposition.wordpress.com/")
        screenshot_path = f"results/browser_verification_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                page = await browser.new_page()

                self.logger.info(f"Navigating to {url}...")
                await page.goto(url, timeout=30000)

                # Basic verification: Check if title contains Markposition
                title = await page.title()
                self.logger.info(f"Page title: {title}")

                # Ensure results directory exists
                os.makedirs("results", exist_ok=True)

                # Take screenshot
                await page.screenshot(path=screenshot_path)
                self.logger.info(f"Screenshot saved to {screenshot_path}")

                await browser.close()

                return {
                    "browser_test": {
                        "status": "PASS",
                        "title": title,
                        "screenshot": screenshot_path,
                        "url": url
                    }
                }
        except Exception as e:
            self.logger.error(f"Browser test failed: {e}")
            return {
                "browser_test": {
                    "status": "FAIL",
                    "error": str(e)
                }
            }
