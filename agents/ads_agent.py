from core.base_agent import BaseAgent

class AdsAgent(BaseAgent):
    def __init__(self):
        super().__init__("AdsAgent")

    def run_cycle(self, context):
        # This agent creates the actual ad creative based on the campaign
        campaign = context.get('ad_campaign', {})

        self.log("Generating ad creatives...")

        ad_creative = {
            "headline": f"Discover {campaign.get('targeting', {}).get('keywords', ['Tech'])[0]} Solutions",
            "body": "Autonomous AI optimization for your business.",
            "cta": "Learn More"
        }

        context['ad_creative'] = ad_creative
        self.log(f"Creative ready: {ad_creative['headline']}")
