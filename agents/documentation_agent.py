import os
from datetime import datetime
from .base_agent import BaseAgent, Blackboard

class DocumentationAgent(BaseAgent):
    """
    Maintains the SYSTEM_EVOLUTION.md log, tracking the system's growth,
    agent count, and strategic improvements.
    """
    def __init__(self):
        super().__init__("DocumentationAgent",
                         dependencies=["audit_report", "system_evolution", "antigravity_context"],
                         provides=["documentation_status"])
        self.log_file = "SYSTEM_EVOLUTION.md"

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Updating System Evolution Documentation...")

        evolution = blackboard.get("system_evolution", {})
        audit = blackboard.get("audit_report", {})
        antigravity = blackboard.get("antigravity_context", {})

        version = evolution.get("parameter_shifts", {}).get("current_version", "1.0")

        entry = (
            f"## [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Evolution v{version}\n"
            f"- **System Status:** {evolution.get('status', 'STABLE')}\n"
            f"- **Audit Status:** {audit.get('status', 'N/A')}\n"
            f"- **Antigravity Sync:** {antigravity.get('status', 'PENDING')}\n"
            f"- **Agent Population:** {len([k for k in blackboard.get_all().keys() if 'Agent' in k or 'Backup' in k])}\n"
            f"- **Strategic Improvement:** {evolution.get('improvement_summary', 'Incremental optimization of system parameters.')}\n\n"
        )

        try:
            mode = 'a' if os.path.exists(self.log_file) else 'w'
            if mode == 'w':
                header = "# Markposition Autonomous System Evolution Log\n\n"
                entry = header + entry

            with open(self.log_file, mode, encoding='utf-8') as f:
                f.write(entry)

            self.logger.info(f"Documentation updated in {self.log_file}")
            return {"documentation_status": "UPDATED"}
        except Exception as e:
            self.logger.error(f"Failed to update documentation: {e}")
            return {"documentation_status": "FAILED"}
