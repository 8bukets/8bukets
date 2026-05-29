import json
import logging
import os
from typing import Dict, Any, List
from agents.base_agent import BaseAgent

logger = logging.getLogger(__name__)

class OracleAIAgent(BaseAgent):
    def __init__(self, data_file: str = "oracle_ai_docs.json"):
        super().__init__("Oracle AI Agent")
        self.data_file = data_file

    def _load_data(self, data: Any = None) -> Dict:
        if data is not None:
            return data

        if not os.path.exists(self.data_file):
            self.log(f"Data file {self.data_file} not found. Returning empty structure.")
            return {}

        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            self.log(f"Error loading {self.data_file}: {e}")
            return {}

    def process(self, data: Any = None, memory_system: Any = None) -> Dict:
        self.log(f"Processing Oracle AI knowledge...")

        data = self._load_data(data)
        if not data:
            self.log("No valid Oracle AI data found to process.")
            return {"status": "No data"}

        # Handle the legacy schema where the top level is a URL mapping to the actual data
        # Check if the first key is a URL string, and grab the data underneath it
        if data and isinstance(data, dict):
            # If the data doesn't contain 'sections' directly, but has one key (the URL), extract it
            if 'sections' not in data:
                keys = list(data.keys())
                if keys:
                    first_key = keys[0]
                    if isinstance(data[first_key], dict) and 'sections' in data[first_key]:
                        data = data[first_key]

        if not data or 'sections' not in data:
            self.log("No valid Oracle AI data found to process.")
            return {"status": "No data"}

        # Extract structured knowledge
        knowledge_summary = {
            "title": data.get("title", "Oracle AI Knowledge"),
            "key_points": [],
            "features": [],
            "offers": [],
            "database_capabilities": []
        }

        # Process Key Links for database specific features
        for link in data.get('key_links', []):
            text = link.get('text', '')
            url = link.get('url', '')
            if 'database' in text.lower() or 'database' in url.lower():
                knowledge_summary['database_capabilities'].append({"feature": text, "url": url})
            elif 'heatwave' in text.lower() or 'heatwave' in url.lower():
                knowledge_summary['database_capabilities'].append({"feature": text, "url": url})
            elif 'vector search' in text.lower():
                knowledge_summary['database_capabilities'].append({"feature": text, "url": url})

        for section in data.get('sections', []):
            heading = section.get('heading', '')
            content = section.get('content', [])

            # Simple heuristic classification
            content_text = " ".join([c for c in content if isinstance(c, str)])

            if "free pricing tier" in content_text.lower() or "free trial" in content_text.lower():
                knowledge_summary["offers"].append({heading: content_text})
            elif "services" in content_text.lower() or "infrastructure" in content_text.lower() or "action" in heading.lower() or "hands-on" in heading.lower():
                knowledge_summary["features"].append({heading: content_text})
            else:
                knowledge_summary["key_points"].append(heading)

        # Remove duplicate database capabilities by URL
        seen_urls = set()
        unique_db_caps = []
        for cap in knowledge_summary['database_capabilities']:
            if cap['url'] not in seen_urls:
                seen_urls.add(cap['url'])
                unique_db_caps.append(cap)
        knowledge_summary['database_capabilities'] = unique_db_caps

        # Update the system memory
        if memory_system is not None:
            memory_system.update("oracle_ai_knowledge", knowledge_summary)

        self.log(f"Successfully integrated {len(knowledge_summary['key_points'])} key points, {len(knowledge_summary['features'])} features, and {len(knowledge_summary['database_capabilities'])} database capabilities into system memory.")

        return knowledge_summary
