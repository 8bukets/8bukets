import os
import json
import requests
import logging
from agents.base import BaseAgent

logger = logging.getLogger(__name__)

class HealthCheckAgent(BaseAgent):
    def __init__(self):
        super().__init__("HealthCheckAgent")

    def check_site(self, url):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                logger.info(f"[{self.name}] Site {url} is reachable.")
                return True
            else:
                logger.warning(f"[{self.name}] Site {url} returned status {response.status_code}.")
                return False
        except Exception as e:
            logger.error(f"[{self.name}] Failed to reach site {url}: {e}")
            return False

    def check_data_integrity(self, filepath):
        if not os.path.exists(filepath):
            logger.warning(f"[{self.name}] Data file {filepath} does not exist.")
            return False
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if not isinstance(data, list):
                    logger.error(f"[{self.name}] Data file {filepath} is not a list.")
                    return False
                logger.info(f"[{self.name}] Data file {filepath} is valid JSON with {len(data)} records.")
                return True
        except Exception as e:
            logger.error(f"[{self.name}] Data file {filepath} is corrupt: {e}")
            return False

    def run(self, url=None, data_file=None):
        site_status = True
        data_status = True

        if url:
            site_status = self.check_site(url)

        if data_file:
            data_status = self.check_data_integrity(data_file)

        return site_status and data_status
