from .base_agent import BaseAgent

class HealthCheckAgent(BaseAgent):
    def __init__(self):
        super().__init__("Health Check Agent")

    def run(self, data, context=None):
        self.log("Running health checks...")

        missing_link_count = 0
        missing_domain_count = 0
        total = len(data)

        for p in data:
            if not p.get('external_link'):
                missing_link_count += 1
            if not p.get('domain'):
                missing_domain_count += 1

        report = "### System Health Check\n"
        report += f"- **Total Records:** {total}\n"
        report += f"- **Records Missing External Links:** {missing_link_count}\n"
        report += f"- **Records Missing Domain:** {missing_domain_count}\n"

        if missing_link_count == 0 and missing_domain_count == 0:
            report += "**Status:** HEALTHY\n"
        else:
            report += "**Status:** WARNING - Data integrity issues found.\n"

        self.log("Health check complete.")
        return report
