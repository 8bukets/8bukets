from .base_agent import BaseAgent
import requests

class MonetizationAgent(BaseAgent):
    def __init__(self):
        super().__init__("MonetizationAgent")

    def run(self, context):
        url = context.get('target_url', 'https://malubeach.wordpress.com')
        self.log(f"Checking monetization potential for {url}...")

        has_ads_txt = False
        try:
            response = requests.get(f"{url}/ads.txt", timeout=5)
            if response.status_code == 200:
                has_ads_txt = True
                self.log("Found ads.txt!")
            else:
                self.log("No ads.txt found.")
        except:
            pass

        recommendation = "Enable AdSense" if not has_ads_txt else "Optimize Ad Inventory"
        return {"has_ads_txt": has_ads_txt, "recommendation": recommendation}
