from core.base_agent import BaseAgent

class HealthCheckAgent(BaseAgent):
    def __init__(self):
        super().__init__("HealthCheckAgent")

    def run_cycle(self, context):
        self.log("Running system diagnostic...")

        # Verify critical files exist
        health_status = "Healthy"
        issues = []

        if not context.get('produced_content'):
            health_status = "Degraded"
            issues.append("No content produced in cycle")

        if not context.get('financials'):
            health_status = "Warning"
            issues.append("No financial data generated")

        context['system_health'] = {
            "status": health_status,
            "issues": issues
        }
        self.log(f"System Health: {health_status}")
