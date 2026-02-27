from .base_agent import BaseAgent
import os
from datetime import datetime

class DocumentationAgent(BaseAgent):
    execution_stage = 10 # Last stage
    def __init__(self):
        super().__init__("DocumentationAgent")

    async def run(self, data: list, context: dict) -> dict:
        self.logger.info("Running Documentation Agent...")

        filename = "SYSTEM_EVOLUTION.md"

        # Collect insights
        status = context.get("autonomous_status", "UNKNOWN")
        evolution = context.get("evolution_notes", [])
        intelligence = context.get("intelligence_insights", [])

        entry = [
            f"\n## {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"- **System Status:** {status}",
            "- **Intelligence Insights:**"
        ]

        for ins in intelligence:
            entry.append(f"  - {ins}")

        if evolution:
            entry.append("- **Autonomous Actions:**")
            for act in evolution:
                entry.append(f"  - {act}")
        else:
            entry.append("- **Autonomous Actions:** None in this cycle.")

        entry_text = "\n".join(entry) + "\n"

        # Append to log
        try:
            mode = "a" if os.path.exists(filename) else "w"
            if mode == "w":
                with open(filename, "w") as f:
                    f.write("# Markposition System Evolution Log\n")
                    f.write("This file is automatically maintained by the DocumentationAgent.\n")

            with open(filename, "a") as f:
                f.write(entry_text)

            self.logger.info(f"Evolution log updated in {filename}")
        except Exception as e:
            self.logger.error(f"Failed to update evolution log: {e}")

        return {"documentation_updated": True}
