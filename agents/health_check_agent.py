import os
import json
import logging
import time

logger = logging.getLogger("HealthCheckAgent")

class HealthCheckAgent:
    def __init__(self, data_file="links.json", scraper_file="scraper.py"):
        self.data_file = data_file
        self.scraper_file = scraper_file

    def check(self):
        """Performs health checks on the system."""
        report = {
            "status": "healthy",
            "checks": []
        }

        # Check Scraper Existence
        if os.path.exists(self.scraper_file):
            report["checks"].append({"check": "scraper_exists", "status": "pass"})
        else:
            report["checks"].append({"check": "scraper_exists", "status": "fail", "error": "File missing"})
            report["status"] = "unhealthy"

        # Check Data File Existence and Freshness
        if os.path.exists(self.data_file):
            mtime = os.path.getmtime(self.data_file)
            age = time.time() - mtime
            # Try loading it
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if not isinstance(data, list) or len(data) == 0:
                         report["checks"].append({"check": "data_valid", "status": "fail", "error": "Empty or invalid JSON"})
                         report["status"] = "unhealthy"
                    else:
                        report["checks"].append({"check": "data_valid", "status": "pass", "count": len(data)})
            except Exception as e:
                report["checks"].append({"check": "data_valid", "status": "fail", "error": str(e)})
                report["status"] = "unhealthy"

            report["checks"].append({"check": "data_freshness", "status": "pass", "age_seconds": round(age)})
        else:
             report["checks"].append({"check": "data_exists", "status": "fail", "error": "Data file missing"})
             report["status"] = "unhealthy"

        logger.info(f"Health Check Status: {report['status']}")
        return report
