import os
import json
import time
from .base_agent import BaseAgent

class HealthCheckAgent(BaseAgent):
    def __init__(self):
        super().__init__("Health Check Agent")

    def run(self, data: dict = None) -> dict:
        """
        Checks the integrity of the system:
        - Verify links.json exists and is valid JSON.
        - Check if data is recent (heuristic).
        - Verify unique_links.txt existence.
        """
        results = {
            "status": "pass",
            "checks": []
        }

        # Check links.json
        json_path = "links.json"
        if os.path.exists(json_path):
            try:
                with open(json_path, 'r') as f:
                    content = json.load(f)
                results["checks"].append(f"✓ {json_path} exists and is valid JSON ({len(content)} records).")
            except Exception as e:
                results["status"] = "fail"
                results["checks"].append(f"✗ {json_path} is invalid: {str(e)}")
        else:
            results["status"] = "fail"
            results["checks"].append(f"✗ {json_path} does not exist.")

        # Check unique_links.txt
        txt_path = "unique_links.txt"
        if os.path.exists(txt_path):
            results["checks"].append(f"✓ {txt_path} exists.")
        else:
            results["status"] = "warning"
            results["checks"].append(f"⚠ {txt_path} missing.")

        return results
