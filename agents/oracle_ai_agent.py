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
        if not data or 'sections' not in data:
            self.log("No valid Oracle AI data found to process.")
            return {"status": "No data"}

        # Extract structured knowledge
        knowledge_summary = {
            "title": data.get("title", "Oracle AI Knowledge"),
            "key_points": [],
            "features": [],
            "offers": []
        }

        for section in data.get('sections', []):
            heading = section.get('heading', '')
            content = section.get('content', [])

            # Simple heuristic classification
            content_text = " ".join([c for c in content if isinstance(c, str)])

            if "free pricing tier" in content_text.lower() or "free trial" in content_text.lower():
                knowledge_summary["offers"].append({heading: content_text})
            elif "services" in content_text.lower() or "infrastructure" in content_text.lower():
                knowledge_summary["features"].append({heading: content_text})
            else:
                knowledge_summary["key_points"].append(heading)

        # Update the system memory
        if memory_system is not None:
            memory_system.update("oracle_ai_knowledge", knowledge_summary)

        self.log(f"Successfully integrated {len(knowledge_summary['key_points'])} key points and {len(knowledge_summary['features'])} features into system memory.")

        return knowledge_summary
