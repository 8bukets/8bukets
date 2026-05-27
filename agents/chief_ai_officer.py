import os
import json
from .base_agent import BaseAgent, Blackboard

class ChiefAIOfficerAgent(BaseAgent):
    """Chief AI Officer that oversees AI strategy, infrastructure optimization, and multi-agent governance."""
    def __init__(self):
        super().__init__("ChiefAIOfficer",
                         dependencies=["system_evolution", "cloud_workflow_status", "market_intelligence", "resource_allocation"],
                         provides=["ai_strategy_status", "infrastructure_optimization", "strategic_directives"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        evolution = blackboard.get("system_evolution", {})
        cloud_status = blackboard.get("cloud_workflow_status", "UNKNOWN")
        market_intel = blackboard.get("market_intelligence", {})
        resource_alloc = blackboard.get("resource_allocation", {})

        self.logger.info("CAIO: Evaluating system telemetry, market intelligence, and multi-agent synthesis...")

        strategy_status = "OPTIMAL"
        infrastructure_opt = {}
        strategic_directives = []

        # Phase 12 Maturity Check
        is_phase_12 = blackboard.get("is_phase_12", False)
        if not is_phase_12:
            try:
                if os.path.exists('AGENTS.md'):
                    with open('AGENTS.md', 'r') as f:
                        if "Phase 12: Autonomous Super-Intelligence (Current)" in f.read():
                            is_phase_12 = True
            except Exception as e:
                self.logger.error(f"CAIO: Maturity check error: {e}")

        if is_phase_12:
            self.logger.info("CAIO: System confirmed at Phase 12. Enabling sentient orchestration protocols.")
            strategic_directives.append("ACTIVATE_SENTIENT_ORCHESTRATION")
        else:
            self.logger.warning("CAIO: System below Phase 12. Mandating roadmap acceleration.")
            strategic_directives.append("ACCELERATE_ROADMAP_UPGRADE")

        if cloud_status == "DEGRADED":
            self.logger.warning("CAIO: Cloud workflow degraded. Triggering infrastructure optimization.")
            strategy_status = "RECOVERY_MODE"
            infrastructure_opt["action"] = "scale_resources"
            infrastructure_opt["target"] = "cloud_workflow"

        # Evaluate resource allocation and trigger proactive reallocation
        if resource_alloc.get("utilization", 0) > 0.85:
            self.logger.warning("CAIO: High resource utilization detected. Proactively reallocating cloud resources.")
            infrastructure_opt["action"] = "proactive_reallocation"
            strategic_directives.append("INITIATE_CLOUD_BURSTING")

        # Evaluate market intelligence and launch new tasks
        if market_intel.get("opportunity_score", 0) > 0.7:
             self.logger.info("CAIO: High market opportunity score detected. Autonomously launching new exploratory tasks.")
             strategy_status = "EXPANSION_MODE"
             strategic_directives.append("LAUNCH_EXPLORATORY_AGENTS")

        # Check system evolution for anomalies
        if evolution.get("status") == "UNSTABLE":
             self.logger.warning("CAIO: System evolution unstable. Mandating strategy review.")
             strategy_status = "REVIEW_REQUIRED"
             infrastructure_opt["action"] = "halt_evolution"
             strategic_directives.append("CONSOLIDATE_SYSTEM_CORE")

        # Phase 12 Compliance & Governance (EU AI Act alignment)
        if "ACTIVATE_SENTIENT_ORCHESTRATION" in strategic_directives:
            self.logger.info("CAIO: Mandating Ethics & Governance framework (EU AI Act compliance).")
            strategic_directives.append("ESTABLISH_ETHICS_FRAMEWORK")
            strategic_directives.append("OPTIMIZE_ROI_TRACKING")
            strategic_directives.append("AI_PORTFOLIO_CONSOLIDATION")

        return {
            "ai_strategy_status": strategy_status,
            "infrastructure_optimization": infrastructure_opt,
            "strategic_directives": strategic_directives
        }
