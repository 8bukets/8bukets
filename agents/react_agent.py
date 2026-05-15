from .base_agent import BaseAgent, Blackboard

class ReActAgent(BaseAgent):
    """
    An agent implementing the ReAct (Reasoning and Acting) framework.
    It takes knowledge and intelligence insights, performs reasoning, and proposes actionable steps.
    """
    def __init__(self):
        super().__init__("ReActAgent",
                         dependencies=["intelligence_insights", "ai_agents_definitions", "agent_use_cases", "agent_best_practices", "google_cloud_tools_list"],
                         provides=["react_reasoning", "react_actions", "react_agent_deployment_config"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Executing ReAct (Reasoning + Acting) logic...")

        insights = blackboard.get("intelligence_insights", [])
        definitions = blackboard.get("ai_agents_definitions", {})
        use_cases = blackboard.get("agent_use_cases", {})
        best_practices = blackboard.get("agent_best_practices", [])
        tools_list = blackboard.get("google_cloud_tools_list", [])

        reasoning_log = []
        action_log = []

        # 1. Reasoning Phase
        if "reasoning" in str(definitions.get("features", "")).lower():
            reasoning_log.append("ReAct feature 'Reasoning' confirmed in knowledge base.")

        if insights:
            reasoning_log.append(f"Analyzing {len(insights)} intelligence insights for actionable items.")
            for insight in insights:
                if "High concentration" in insight:
                    reasoning_log.append("Reasoning: High concentration detected, requires focused ad targeting.")
                elif "efficiency" in insight.lower() or "decision-making" in insight.lower():
                    reasoning_log.append("Reasoning: Strategic benefits identified, should optimize workflow.")

        # 2. Acting Phase
        if reasoning_log:
            action_log.append("DEPLOY_FOCUSED_AD_CAMPAIGN")
            action_log.append("OPTIMIZE_WORKFLOW_DECISION_MAKING")
        else:
            reasoning_log.append("Reasoning: No specific insights to act upon.")
            action_log.append("CONTINUE_MONITORING")

        deployment_config = {}
        if "DEPLOY_FOCUSED_AD_CAMPAIGN" in action_log or "OPTIMIZE_WORKFLOW_DECISION_MAKING" in action_log:
            reasoning_log.append("Reasoning: Specific actions determined, configuring React Agent deployment.")

            # Dynamically determine deployment target based on best practices
            deployment_target = "Cloud Run"
            if any("Next.js" in bp for bp in best_practices) or any("Vercel" in bp for bp in best_practices):
                deployment_target = "Vercel"

            # Check if any specific use case is active (e.g., customer, security)
            active_use_cases = list(use_cases.keys()) if isinstance(use_cases, dict) else []

            deployment_config = {
                "agent_type": "ReactAgent",
                "frontend_framework": "Next.js",
                "backend_framework": "Node.js",
                "deployment_target": deployment_target,
                "active_use_cases": active_use_cases,
                "orchestration_mode": "SYNCHRONIZED",
                "status": "READY_FOR_DEPLOYMENT",
                "tools_integration": tools_list
            }

        # Prepare payload
        payload = {
            "react_reasoning": reasoning_log,
            "react_actions": action_log,
            "react_agent_deployment_config": deployment_config
        }

        self.logger.info(f"ReAct reasoning complete. Proposed actions: {action_log}")
        return payload
