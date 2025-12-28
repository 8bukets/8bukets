import random
from bs4 import BeautifulSoup
import os

class AdAgent:
    def __init__(self, filepath='index.html'):
        self.filepath = filepath
        self.bids = [
            {"advertiser": "SportsGear Pro", "bid": 0.50, "content": "Get 50% off on all football boots!"},
            {"advertiser": "BetWin365", "bid": 1.20, "content": "Join now and get a $100 bonus."},
            {"advertiser": "HealthyLife", "bid": 0.30, "content": "Vitamins for peak performance."},
            {"advertiser": "TechStream", "bid": 0.80, "content": "Watch live sports in 4K anywhere."}
        ]

    def run_auction(self):
        """Simulate a programmatic ad auction."""
        print("[AdAgent] Initiating Real-Time Bidding (RTB)...")
        # Simulate slight variance in bids
        for bid in self.bids:
            bid['current_bid'] = bid['bid'] * random.uniform(0.9, 1.2)

        # Select winner
        winner = max(self.bids, key=lambda x: x['current_bid'])
        print(f"[AdAgent] Auction Winner: {winner['advertiser']} with bid ${winner['current_bid']:.2f}")
        return winner

    def optimize_targeting(self, winner):
        """Simulate targeting optimization."""
        # In a real agent, this would analyze user cookies/behavior
        print(f"[AdAgent] Optimizing ad targeting for audience segment: Sports Enthusiasts")
        return winner['content']

    def place_ad(self, soup=None):
        """Inject the winning ad into the page."""
        should_save = False
        if soup is None:
            if not os.path.exists(self.filepath):
                print(f"[AdAgent] Error: {self.filepath} not found.")
                return
            should_save = True

        winner = self.run_auction()
        ad_content = self.optimize_targeting(winner)

        if soup is None:
            with open(self.filepath, 'r') as f:
                soup = BeautifulSoup(f, 'html.parser')

        ad_slot = soup.find(id='ad-slot-top')
        if ad_slot:
            # Create ad HTML
            ad_html = f"""
            <div class="programmatic-ad" style="background: #e0f7fa; padding: 1.5rem; border: 1px dashed #006064; text-align: center; border-radius: 8px;">
                <p style="font-weight: bold; color: #006064;">Sponsored by {winner['advertiser']}</p>
                <h3 style="margin: 0.5rem 0;">{ad_content}</h3>
                <button style="background: #00838f; color: white; border: none; padding: 0.5rem 1rem; cursor: pointer; border-radius: 4px;">Shop Now</button>
                <p style="font-size: 0.7rem; color: #999; margin-top: 0.5rem;">Ad served autonomously by AdAgent v1.0</p>
            </div>
            """

            # Clear previous ad and insert new one
            ad_slot.clear()
            ad_slot.append(BeautifulSoup(ad_html, 'html.parser'))
            # Ensure it's visible
            if 'style' in ad_slot.attrs:
                ad_slot['style'] = ad_slot['style'].replace('display: none;', 'display: block;')
            else:
                ad_slot['style'] = 'display: block;'

            if should_save:
                with open(self.filepath, 'w') as f:
                    f.write(str(soup))
            print("[AdAgent] Ad placement successful.")
        else:
            print("[AdAgent] Error: Ad slot #ad-slot-top not found.")

if __name__ == "__main__":
    agent = AdAgent()
    agent.place_ad()
