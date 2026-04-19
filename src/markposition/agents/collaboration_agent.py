import os
from .base_agent import BaseAgent, Blackboard

class CollaborationAgent(BaseAgent):
    """Bridge Agent: Exports system metadata and stakeholder information to the Antigravity platform."""
    def __init__(self):
        super().__init__("CollaborationAgent",
                         dependencies=["sigma_performance_report", "system_evolution"],
                         provides=["antigravity_context"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Synchronizing system state with Antigravity platform...")

        # 1. Load mission and rules
        mission = self._load_antigravity_file(".antigravity/mission.md")
        rules = self._load_antigravity_file(".antigravity/rules.md")

        # 2. Extract key metrics from blackboard
        sigma_report = blackboard.get("sigma_performance_report", {})
        evolution_data = blackboard.get("system_evolution", {})

        # 3. Construct export context
        export_context = {
            "platform": "Antigravity",
            "system_version": evolution_data.get("parameter_shifts", {}).get("current_version", "N/A"),
            "sigma_status": sigma_report.get("average_impact_score", 0),
            "mission_statement": mission,
            "integration_rules": rules,
            "stakeholders": self._extract_stakeholders(mission),
            "status": "SYNCED"
        }

        self.logger.info(f"Exported system version v{export_context['system_version']} to Antigravity.")

        return {"antigravity_context": export_context}

    def _load_antigravity_file(self, filepath: str) -> str:
        if not os.path.exists(filepath):
            return "N/A"
        try:
            with open(filepath, 'r') as f:
                return f.read().strip()
        except Exception as e:
            self.logger.error(f"Failed to read {filepath}: {e}")
            return "ERROR"

    def _extract_stakeholders(self, mission_content: str) -> list:
        stakeholders = []
        if "Stakeholder List" in mission_content:
            lines = mission_content.split('\n')
            for line in lines:
                if '@' in line:
                    # Extracts the email address part from a line like "- user@example.com (Role)"
                    parts = line.strip('- ').split()
                    if parts:
                        stakeholders.append(parts[0])
        return stakeholders
