from .base_agent import BaseAgent
import asyncio
from analytics import generate_report, load_data
import os
import json

class AnalyzeAgent(BaseAgent):
    def __init__(self, shared_state):
        super().__init__("AnalyzeAgent", shared_state)

    async def perform_task(self):
        # check if there is new data to analyze
        if self.shared_state.get('new_data_available', False):
            self.log("🔍 Detecting new data. Running analysis...")
            try:
                # Assuming data is in links.json for now, mirroring the existing analytics.py usage
                if os.path.exists("links.json"):
                    data = load_data("links.json")
                    generate_report(data, "REPORT.md")
                    self.log("📊 Analysis complete. Report generated.")
                    self.shared_state['new_data_available'] = False

                    # Notify Content Agent
                    if 'ContentAgent' in self.shared_state['agents']:
                        self.send_message(self.shared_state['agents']['ContentAgent'], {
                            'type': 'analysis_result',
                            'summary': f"Analyzed {len(data)} items."
                        })
            except Exception as e:
                self.logger.error(f"Analysis failed: {e}")

        await asyncio.sleep(5)
