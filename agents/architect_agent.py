from .base_agent import BaseAgent, Blackboard
import json
import os
from datetime import datetime

CONFIG_FILE = "config/evolution_params.json"

class ArchitectAgent(BaseAgent):
    """The System Architect: Analyzes performance and re-codes system parameters for daily improvement."""
    def __init__(self):
        super().__init__("Architect",
                         dependencies=["sigma_performance_report", "telemetry_synthesis", "research_data"],
                         provides=["system_evolution"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Analyzing system architecture for daily improvements...")

        proposals = blackboard.get_proposals()
        current_config = self.config

        # Analyze performance and research
        sigma = blackboard.get("sigma_performance_report", {})
        research = blackboard.get("research_data", {})
        impact = sigma.get("average_impact_score", 0)
        market_trends = research.get("market_trends", [])

        evolution = {
            "version_upgrade": 0.01,
            "parameter_shifts": {},
            "status": "NO_CHANGE"
        }

        # 1. Performance-based Improvement
        if impact > 0:
            # Increase complexity/depth if system is stable
            evolution["parameter_shifts"]["system_concurrency"] = current_config.get("system_concurrency", 5) + 1
            evolution["parameter_shifts"]["seo_impact_threshold"] = round(current_config.get("seo_impact_threshold", 0.5) * 1.05, 2)
            evolution["status"] = "EVOLVED"

        # 2. Market-based Integration
        if market_trends:
            self.logger.info(f"Integrating {len(market_trends)} market trends into architecture...")
            evolution["status"] = "EVOLVED"

            # Increase research depth if market is active
            if len(market_trends) > 5:
                evolution["parameter_shifts"]["research_depth"] = "DEEP"

            # Focus on specific SEO targets if detected
            if any("google" in t.lower() for t in market_trends):
                evolution["parameter_shifts"]["google_seo_focus"] = True
                self.logger.info("Market trend detected: Prioritizing Google SEO Focus.")

        # Incorporate agent proposals
        for p in proposals:
            self.logger.info(f"Reviewing proposal from {p['proposer']}: {p['improvement']}")
            # Simple simulation: accept all improvement suggestions
            for key, value in p['improvement'].items():
                evolution["parameter_shifts"][key] = value

        if evolution["status"] == "EVOLVED":
            new_version = self._apply_evolution(current_config, evolution)
            evolution["parameter_shifts"]["current_version"] = new_version

        return {"system_evolution": evolution}

    def _apply_evolution(self, current, evolution) -> float:
        new_config = current.copy()
        new_config.update(evolution["parameter_shifts"])
        new_version = round(new_config.get("current_version", 1.0) + evolution["version_upgrade"], 2)
        new_config["current_version"] = new_version
        new_config["last_evolution"] = datetime.now().strftime("%Y-%m-%d")

        try:
            with open(CONFIG_FILE, 'w') as f:
                json.dump(new_config, f, indent=4)
            self.logger.info(f"System evolved to version {new_version}")
            return new_version
        except Exception as e:
            self.logger.error(f"Failed to persist evolution: {e}")
            return current.get("current_version", 1.0)
