import random
from bs4 import BeautifulSoup
import os

class CreativeAgent:
    def __init__(self, filepath='index.html'):
        self.filepath = filepath
        self.ideas = [
            {
                "type": "Poll",
                "title": "Daily Fan Poll",
                "content": "Who will win the Golden Boot this season?",
                "options": ["Haaland", "Mbappe", "Kane", "Salah"]
            },
            {
                "type": "Trivia",
                "title": "Sports Trivia Challenge",
                "content": "Which country won the first ever World Cup in 1930?",
                "options": ["Brazil", "Uruguay", "Argentina", "Italy"]
            },
            {
                "type": "Spotlight",
                "title": "Fan Spotlight",
                "content": "Meet John D., a season ticket holder for 40 years!",
                "options": []
            }
        ]

    def brainstorm(self):
        """Simulate 100% curiosity and creativity to pick an idea."""
        print("[CreativeAgent] Brainstorming high-interest solutions...")
        idea = random.choice(self.ideas)
        print(f"[CreativeAgent] Generated Idea: {idea['title']} ({idea['type']})")
        return idea

    def implement_idea(self):
        """Code and integrate the idea into the system."""
        if not os.path.exists(self.filepath):
            print(f"[CreativeAgent] Error: {self.filepath} not found.")
            return

        idea = self.brainstorm()

        # Generate HTML based on idea type
        html_content = ""
        if idea['type'] in ["Poll", "Trivia"]:
            options_html = "".join([f'<li style="margin: 5px 0;"><button style="width: 100%; text-align: left; padding: 5px; cursor: pointer;">{opt}</button></li>' for opt in idea['options']])
            html_content = f"""
            <div class="creative-feature" style="background: #e8f5e9; padding: 1rem; margin-top: 1.5rem; border-radius: 8px; border-left: 4px solid #2e7d32;">
                <h4 style="margin-top: 0; color: #1b5e20;">✨ {idea['title']}</h4>
                <p style="font-size: 0.9rem;">{idea['content']}</p>
                <ul style="list-style: none; padding: 0;">{options_html}</ul>
            </div>
            """
        else:
            html_content = f"""
            <div class="creative-feature" style="background: #fff3e0; padding: 1rem; margin-top: 1.5rem; border-radius: 8px; border-left: 4px solid #ef6c00;">
                <h4 style="margin-top: 0; color: #e65100;">★ {idea['title']}</h4>
                <p style="font-size: 0.9rem;">{idea['content']}</p>
            </div>
            """

        with open(self.filepath, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')

        sidebar = soup.find('aside', class_='sidebar')
        if sidebar:
            # Remove old creative features to keep it fresh
            for old_feature in sidebar.find_all(class_='creative-feature'):
                old_feature.decompose()

            # Append new feature
            sidebar.append(BeautifulSoup(html_content, 'html.parser'))

            with open(self.filepath, 'w') as f:
                f.write(str(soup))
            print("[CreativeAgent] Idea successfully coded and integrated into the sidebar.")
        else:
            print("[CreativeAgent] Error: Sidebar not found.")

if __name__ == "__main__":
    agent = CreativeAgent()
    agent.implement_idea()
