import random
import datetime
from bs4 import BeautifulSoup
import os

class ContentAgent:
    def __init__(self, filepath='index.html'):
        self.filepath = filepath
        self.topics = [
            ("Football", "United FC scores a last minute winner!", "In a dramatic turn of events, United FC secured 3 points."),
            ("Basketball", "Lakers secure playoff spot.", "LeBron leads the charge as the Lakers dominate."),
            ("Tennis", "Grand Slam final set.", "The world's top two players will meet on Sunday."),
            ("F1", "Red Bull dominates practice session.", "Verstappen looks unstoppable this weekend."),
            ("Cricket", "World Cup upset!", "Underdogs take the victory in a thrilling match.")
        ]

    def research(self):
        """Simulate researching a new topic."""
        print("[ContentAgent] Researching latest sports trends...")
        topic = random.choice(self.topics)
        print(f"[ContentAgent] Discovered interesting story in: {topic[0]}")
        return topic

    def generate_deep_dive(self):
        """Simulate high intelligence 100% deep dive analysis."""
        print("[ContentAgent] Initiating Deep Dive Analysis Protocol...")
        return ("Analysis", "The Future of Sports Analytics", "A comprehensive study on how AI and autonomous agents are reshaping team strategies and player performance metrics.")

    def create_content(self, topic_data, is_deep_dive=False):
        """Create HTML structure for the article."""
        category, title, summary = topic_data
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        special_class = "deep-dive" if is_deep_dive else "generated-content"
        badge = '<span style="background: #6200ea; color: white; padding: 2px 6px; border-radius: 4px; font-size: 0.7rem; margin-left: 5px;">DEEP DIVE</span>' if is_deep_dive else ""

        html = f"""
        <article data-category="{category}" class="{special_class}" style="{'border-left: 4px solid #6200ea;' if is_deep_dive else ''}">
            <span class="tag">{category}</span>{badge}
            <span class="date" style="font-size: 0.8rem; color: #666; display: block; margin-bottom: 0.5rem;">Generated: {timestamp}</span>
            <img src="images/placeholder.webp" alt="{title}" loading="lazy" width="600" height="400" style="width: 100%; height: auto; border-radius: 4px;">
            <h3>{title}</h3>
            <p>{summary}</p>
            <button class="read-more-btn" onclick="toggleReadMore(this)" aria-label="Read more about {title}">Read More</button>
            <p class="more-text" style="display:none;">[Autonomous Intelligence Expansion]: This content was generated based on real-time data analysis of global sports trends. The agent has determined high engagement potential for {category}.</p>
        </article>
        """
        return html

    def publish(self, soup=None):
        """Inject content into the website."""
        should_save = False
        if soup is None:
            if not os.path.exists(self.filepath):
                print(f"[ContentAgent] Error: {self.filepath} not found.")
                return
            should_save = True

        # 20% chance to generate a Deep Dive (Curiosity/Intelligence)
        if random.random() < 0.2:
            topic_data = self.generate_deep_dive()
            new_content = self.create_content(topic_data, is_deep_dive=True)
        else:
            topic_data = self.research()
            new_content = self.create_content(topic_data)

        if soup is None:
            with open(self.filepath, 'r') as f:
                soup = BeautifulSoup(f, 'html.parser')

        # Find the article list container
        article_list = soup.find(id='article-list')
        if article_list:
            # Create new soup object for the new content
            new_tag = BeautifulSoup(new_content, 'html.parser')
            # Prepend to the list (show as newest)
            article_list.insert(0, new_tag)

            if should_save:
                with open(self.filepath, 'w') as f:
                    f.write(str(soup))
            print("[ContentAgent] Successfully published new article.")
        else:
            print("[ContentAgent] Error: #article-list container not found.")

if __name__ == "__main__":
    agent = ContentAgent()
    agent.publish()
