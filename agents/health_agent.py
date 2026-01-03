from typing import List, Dict, Any
from .base_agent import BaseAgent
import os
import time

class HealthCheckAgent(BaseAgent):
    def __init__(self):
        super().__init__("Health Check Agent")

    def run(self, data: List[Dict[str, Any]], dna: Dict[str, Any] = None, **kwargs) -> Dict[str, Any]:
        # Check integrity of the data passed
        missing_titles = sum(1 for p in data if not p.get('title'))
        missing_dates = sum(1 for p in data if not p.get('date'))
        missing_links = sum(1 for p in data if not p.get('external_link') and not p.get('post_url'))

        # Check File System Health
        files_to_check = ['links.json', 'links.csv', 'scraper.py']
        file_status = {}
        for f in files_to_check:
            if os.path.exists(f):
                size = os.path.getsize(f)
                mtime = os.path.getmtime(f)
                file_status[f] = {
                    "exists": True,
                    "size_bytes": size,
                    "last_modified_ago_seconds": int(time.time() - mtime)
                }
            else:
                file_status[f] = {"exists": False}

        status = "HEALTHY"
        if missing_titles > len(data) * 0.1 or not file_status['links.json']['exists']:
            status = "DEGRADED"

        return {
            "status": status,
            "data_quality": {
                "missing_titles": missing_titles,
                "missing_dates": missing_dates,
                "missing_links": missing_links,
                "total_records": len(data)
            },
            "system_files": file_status
        }

    def format_report(self, results: Dict[str, Any]) -> str:
        lines = [f"## {self.name} Report"]
        lines.append(f"**System Status:** {results.get('status')}")

        dq = results.get('data_quality', {})
        lines.append("\n### Data Quality Checks")
        lines.append(f"- Missing Titles: {dq.get('missing_titles')}")
        lines.append(f"- Missing Dates: {dq.get('missing_dates')}")

        fs = results.get('system_files', {})
        lines.append("\n### File System Check")
        for fname, stats in fs.items():
            status = "OK" if stats.get('exists') else "MISSING"
            lines.append(f"- {fname}: {status}")

        return "\n".join(lines)
