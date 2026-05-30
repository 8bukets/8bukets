from .base_agent import BaseAgent, Blackboard

class ReActAgent(BaseAgent):
    """
    An agent implementing the ReAct (Reasoning and Acting) framework.
    It takes knowledge and intelligence insights, performs reasoning, and proposes actionable steps.
    """
    def __init__(self):
        super().__init__("ReActAgent",
                         dependencies=["intelligence_insights", "ai_agents_definitions", "agent_use_cases", "agent_best_practices", "google_cloud_tools_list", "react_framework_details", "agent_taxonomy"],
                         provides=["react_reasoning", "react_actions", "react_agent_deployment_config"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Executing ReAct (Reasoning + Acting) logic...")

        insights = blackboard.get("intelligence_insights", [])
        definitions = blackboard.get("ai_agents_definitions", {})
        use_cases = blackboard.get("agent_use_cases", {})
        best_practices = blackboard.get("agent_best_practices", [])
        tools_list = blackboard.get("google_cloud_tools_list", [])
        react_details = blackboard.get("react_framework_details", {})
        taxonomy = blackboard.get("agent_taxonomy", {})

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
        if action_log or react_details:
            reasoning_log.append("Reasoning: Specific actions determined or React knowledge found, configuring React Agent deployment.")
            if "DEPLOY_REACT_AGENT" not in action_log:
                action_log.append("DEPLOY_REACT_AGENT")

            # Dynamically determine deployment target based on best practices and knowledge
            deployment_target = "Cloud Run"
            if "deployment_strategy" in react_details and "Next.js" in react_details["deployment_strategy"]:
                deployment_target = "Vercel"
            elif any("Next.js" in bp for bp in best_practices) or any("Vercel" in bp for bp in best_practices):
                deployment_target = "Vercel"

            taxonomy_mode = "BACKGROUND" if taxonomy.get("background_processes") else "INTERACTIVE"

            # Check if any specific use case is active (e.g., customer, security)
            active_use_cases = list(use_cases.keys()) if isinstance(use_cases, dict) else []

            scale_tier = "STANDARD"
            auto_scaling = {"min_replicas": 1, "max_replicas": 3}
            if len(insights) > 5 or any("High concentration" in i for i in insights):
                scale_tier = "GLOBAL_EDGE"
                auto_scaling = {"min_replicas": 5, "max_replicas": 50, "regions": ["us-central1", "europe-west1", "asia-east1"]}
                reasoning_log.append("Reasoning: High data volume or concentration detected, configuring GLOBAL_EDGE scaling tier.")
            elif len(insights) > 2:
                scale_tier = "ENTERPRISE"
                auto_scaling = {"min_replicas": 3, "max_replicas": 10}
                reasoning_log.append("Reasoning: Moderate data volume detected, configuring ENTERPRISE scaling tier.")

            deployment_config = {
                "agent_type": "ReactAgent",
                "frontend_framework": "Next.js",
                "backend_framework": "Node.js",
                "deployment_target": deployment_target,
                "active_use_cases": active_use_cases,
                "orchestration_mode": "SYNCHRONIZED",
                "taxonomy_mode": taxonomy_mode,
                "status": "READY_FOR_DEPLOYMENT",
                "tools_integration": tools_list,
                "react_framework_details": react_details,
                "scale_tier": scale_tier,
                "auto_scaling": auto_scaling
            }

        # Prepare payload
        payload = {
            "react_reasoning": reasoning_log,
            "react_actions": action_log,
            "react_agent_deployment_config": deployment_config
        }

        self.logger.info(f"ReAct reasoning complete. Proposed actions: {action_log}")
        return payload
