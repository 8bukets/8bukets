from typing import List, Dict, Any, Optional
import json
import logging
import datetime
from .base_agent import BaseAgent
from .robot_txt_agent import RobotTxtAgent
from .analysis_agent import AnalysisAgent
from .research_agent import ResearchAgent
from .intelligence_agent import IntelligenceAgent
from .ads_agent import AdsAgent
from .bid_agent import BidAgent
from .content_agent import ContentAgent
from .health_agent import HealthCheckAgent
from .monetization_agent import MonetizationAgent
from .creativity_agent import CreativityAgent
from .antigravity_agent import AntigravityAgent

logger = logging.getLogger(__name__)

class AutonomousIntelligenceAgent:
    def __init__(self, knowledge_base_file: str = "knowledge_base.json"):
        self.kb_file = knowledge_base_file
        self.knowledge_base = self._load_kb()
        self.agents: List[BaseAgent] = [
            RobotTxtAgent(),
            AnalysisAgent(),
            IntelligenceAgent(),
            AdsAgent(),
            ResearchAgent(),
            BidAgent(),
            ContentAgent(),
            HealthCheckAgent(),
            MonetizationAgent(),
            CreativityAgent(),
            AntigravityAgent()
        ]

    def _load_kb(self) -> Dict[str, Any]:
        kb = {}
        try:
            with open(self.kb_file, 'r', encoding='utf-8') as f:
                kb = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            kb = {"iq": 25, "history": []}

        if "iq" not in kb:
             kb["iq"] = 25  # Starting IQ as requested

        return kb

    def _save_kb(self):
        try:
            with open(self.kb_file, 'w', encoding='utf-8') as f:
                json.dump(self.knowledge_base, f, indent=4)
        except Exception as e:
            logger.error(f"Failed to save KB: {e}")

    async def run(self, data: List[Dict]) -> str:
        shared_context = {}
        report_lines = []
        report_lines.append(f"# Daily Autonomous Report: {datetime.datetime.now().strftime('%Y-%m-%d')}\n")

        current_iq = self.knowledge_base.get("iq", 25)
        report_lines.append(f"**System IQ Level:** {current_iq}\n")

        for agent in self.agents:
            logger.info(f"Coordinator: Running {agent.name}...")
            try:
                # Agents collaborate via shared_context and knowledge_base
                results = await agent.process(data, shared_context, self.knowledge_base)

                # Agents contribute to the report
                report_section = agent.format_report(results)
                report_lines.append(report_section)
                report_lines.append("\n---\n")

                # "Learning" simulation: Update KB with success count or specific agent data if they modified it
                # (In this simple design, we trust agents not to corrupt KB, or we could handle merging)

            except Exception as e:
                logger.error(f"Coordinator: Agent {agent.name} failed: {e}")
                report_lines.append(f"### {agent.name} Failed\nError: {e}\n\n---\n")

        # Self-Improvement / Evolution Step
        self._evolve()
        self._save_kb()

        return "\n".join(report_lines)

    def _evolve(self):
        """Simulate self-improvement and IQ increase."""
        # Increase IQ slightly for every successful run to represent "learning"
        current_iq = self.knowledge_base.get("iq", 25)
        new_iq = current_iq + 0.1  # Small increment
        self.knowledge_base["iq"] = round(new_iq, 2)

        # Log this "evolution"
        entry = {
            "date": datetime.datetime.now().isoformat(),
            "event": "System Evolution",
            "iq_change": f"{current_iq} -> {self.knowledge_base['iq']}"
        }
        if "history" not in self.knowledge_base:
            self.knowledge_base["history"] = []
        self.knowledge_base["history"].append(entry)
        logger.info(f"System evolved. New IQ: {self.knowledge_base['iq']}")
