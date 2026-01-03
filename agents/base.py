import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

import json
import os

class Agent:
    def __init__(self, name, db_name="wishlist_data.db"):
        self.name = name
        self.db_name = db_name
        self.logger = logging.getLogger(self.name)
        self.results = {}
        self.dna = self.load_dna()
        self.cookie_jar = None # To be injected

    def load_dna(self, dna_path="system_dna.json"):
        """Load the system's DNA configuration."""
        if not os.path.exists(dna_path):
            return {}
        try:
            with open(dna_path, 'r') as f:
                return json.load(f)
        except Exception:
            return {}

    def set_cookie_jar(self, cookie_jar):
        self.cookie_jar = cookie_jar

    def run(self):
        """Execute the agent's main task."""
        self.logger.info("Starting...")
        try:
            self.perform_task()
            self.logger.info("Finished successfully.")
        except Exception as e:
            self.logger.error(f"Failed: {e}")
            self.results['error'] = str(e)
        return self.results

    def perform_task(self):
        """To be implemented by subclasses."""
        raise NotImplementedError
