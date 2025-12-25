import os
import shutil
from .base_agent import BaseAgent, AgentContext

class HealthAgent(BaseAgent):
    def __init__(self):
        super().__init__("HealthAgent 🏥")

    def run(self, context: AgentContext):
        self.log(context, "Running system health checks...")

        # Check disk space
        total, used, free = shutil.disk_usage(".")
        free_gb = free // (2**30)
        self.log(context, f"Disk Space: {free_gb} GB free.")

        # Check critical files
        critical_files = ["run_system.py", "scraper.py", "agents/base_agent.py"]
        missing = [f for f in critical_files if not os.path.exists(f)]

        if missing:
            self.log(context, f"⚠️ CRITICAL: Missing files: {missing}")
            context.set("system_health", "DEGRADED")
        else:
            self.log(context, "All critical files present.")
            context.set("system_health", "HEALTHY")
