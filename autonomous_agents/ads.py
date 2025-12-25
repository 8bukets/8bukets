from .base import BaseAgent

class AdAgent(BaseAgent):
    def __init__(self):
        super().__init__("AdsManager")

    def run(self, context):
        content = context.get('generated_content', "")
        if "autonomous" in content.lower():
            bid = 1.50
            target = "Tech Enthusiasts"
        else:
            bid = 0.50
            target = "General"

        context['ad_strategy'] = {
            "bid_amount": bid,
            "target_audience": target
        }
        self.log_activity(f"Ad strategy set: Bid ${bid} for {target}")
