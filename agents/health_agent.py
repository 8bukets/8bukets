from agents.base_agent import BaseAgent
import os
import shutil

class HealthCheckAgent(BaseAgent):
    def __init__(self):
        super().__init__("HealthCheck")

    async def run(self, context: dict):
        self.log("Performing health checks...")

        health_status = {"healthy": True, "issues": []}

        # Check files
        expected_files = ["links.json", "links.csv"]
        for f in expected_files:
            if not os.path.exists(f):
                health_status["healthy"] = False
                health_status["issues"].append(f"Missing file: {f}")
            else:
                size = os.path.getsize(f)
                if size == 0:
                    health_status["healthy"] = False
                    health_status["issues"].append(f"Empty file: {f}")

        # Check report generation
        report = context.get("report_file")
        if report and not os.path.exists(report):
            health_status["healthy"] = False
            health_status["issues"].append("Report was not generated.")

        # Disk usage check (basic)
        try:
            total, used, free = shutil.disk_usage(".")
            if free < 1024 * 1024 * 10: # Less than 10MB
                health_status["healthy"] = False
                health_status["issues"].append("Low disk space.")
        except:
            pass

        if health_status["healthy"]:
            self.log("System is HEALTHY.")
        else:
            self.log(f"System UNHEALTHY: {', '.join(health_status['issues'])}")

        context["health"] = health_status
