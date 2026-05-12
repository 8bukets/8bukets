import os
import json
import re
from .base_agent import BaseAgent, Blackboard

class SystemAuditAgent(BaseAgent):
    """
    Autonomously audits the system for PII leaks, security vulnerabilities,
    and compliance with architectural standards.
    """
    def __init__(self):
        super().__init__("SystemAuditAgent",
                         dependencies=["sigma_performance_report", "system_evolution"],
                         provides=["audit_report"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Executing Autonomous System Audit...")

        findings = []
        pii_patterns = [
            r"\b\d{10,11}\b",  # Potential OIB/ID
            r"\b\+?[\d\s-]{10,}\b"  # Potential Phone
        ]

        # 1. Audit results/ for PII
        results_dir = "results"
        if os.path.exists(results_dir):
            for filename in os.listdir(results_dir):
                if filename.endswith(".md") or filename.endswith(".log"):
                    filepath = os.path.join(results_dir, filename)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                        for pattern in pii_patterns:
                            if re.search(pattern, content) and "[REDACTED]" not in content and "[SENSITIVE_DATA_RESTRICTED]" not in content:
                                findings.append(f"Potential PII detected in {filename}")

        # 2. Check security config
        evolution = blackboard.get("system_evolution", {})
        if evolution.get("parameter_shifts", {}).get("system_concurrency", 0) > 100:
            findings.append("System concurrency is dangerously high (>100). Recommend caution.")

        # 3. Check for mandatory files
        mandatory_files = ["AGENTS.md", "LICENSE", ".gitignore"]
        for f in mandatory_files:
            if not os.path.exists(f):
                findings.append(f"Missing mandatory file: {f}")

        status = "SECURE" if not findings else "WARNING"
        self.logger.info(f"Audit Complete. Status: {status}. Findings: {len(findings)}")

        return {
            "audit_report": {
                "status": status,
                "findings": findings,
                "timestamp": os.path.getmtime(results_dir) if os.path.exists(results_dir) else 0
            }
        }

    async def review(self, blackboard: Blackboard):
        report = blackboard.get("audit_report", {})
        if report.get("status") == "WARNING":
            return [f"System Audit Warning: {f}" for f in report.get("findings", [])]
        return ["System architecture and data privacy standards are verified."]
