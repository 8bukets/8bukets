from .base_agent import BaseAgent
import subprocess
import sys
import json
import os

class ResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__("Researcher")

    def perform_task(self, data):
        # Data can specify limits or targets
        limit = data.get('limit', 1) if data else 1
        output_file = data.get('output_file', 'data.json') if data else 'data.json'

        self.logger.info(f"Scraping content (limit {limit} pages)...")

        # We assume scrape_informatic.py is in the root directory
        cmd = [sys.executable, "scrape_informatic.py", "-n", str(limit), "-o", output_file]
        subprocess.run(cmd, check=True)

        # Load the data to return it
        if os.path.exists(output_file):
            with open(output_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
