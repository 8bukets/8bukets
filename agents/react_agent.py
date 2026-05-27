from .base_agent import BaseAgent, Blackboard

class ReActAgent(BaseAgent):
    """
    An agent implementing the ReAct (Reasoning and Acting) framework.
    It takes knowledge and intelligence insights, performs reasoning, and proposes actionable steps.
    """
    def __init__(self):
        super().__init__("ReActAgent",
                         dependencies=["intelligence_insights", "ai_agents_definitions", "agent_use_cases", "agent_best_practices"],
                         provides=["react_reasoning", "react_actions", "react_agent_deployment_config"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Executing ReAct (Reasoning + Acting) logic...")

        insights = blackboard.get("intelligence_insights", [])
        definitions = blackboard.get("ai_agents_definitions", {})
        use_cases = blackboard.get("agent_use_cases", {})
        best_practices = blackboard.get("agent_best_practices", [])

        reasoning_log = []
        action_log = []

        # 1. Reasoning Phase
        if "reasoning" in str(definitions.get("features", "")).lower():
            reasoning_log.append("ReAct feature 'Reasoning' confirmed in knowledge base.")

        if best_practices:
            reasoning_log.append("Integrating Agent Best Practices into reasoning logic.")
            if any("serverless" in bp.lower() for bp in best_practices):
                reasoning_log.append("Best Practice: Serverless deployment (e.g., Cloud Run/Vercel) identified as optimal.")

        has_creative_use_case = "creative" in use_cases and use_cases["creative"]
        has_code_use_case = "code" in use_cases and use_cases["code"]

        if has_creative_use_case:
            reasoning_log.append("Reasoning: Creative agent use case detected. Suggesting enhanced content generation.")

        if has_code_use_case:
            reasoning_log.append("Reasoning: Code agent use case detected. Suggesting integration with coding environments.")

        if insights:
            reasoning_log.append(f"Analyzing {len(insights)} intelligence insights for actionable items.")
            for insight in insights:
                if "High concentration" in insight:
                    reasoning_log.append("Reasoning: High concentration detected, requires focused ad targeting.")
                elif "efficiency" in insight.lower() or "decision-making" in insight.lower():
                    reasoning_log.append("Reasoning: Strategic benefits identified, should optimize workflow.")

        # 2. Acting Phase
        deployment_config = {}

        if reasoning_log:
            if "High concentration" in str(reasoning_log):
                action_log.append("DEPLOY_FOCUSED_AD_CAMPAIGN")
            if "efficiency" in str(reasoning_log).lower():
                action_log.append("OPTIMIZE_WORKFLOW_DECISION_MAKING")
            if has_creative_use_case:
                action_log.append("DEPLOY_CREATIVE_REACT_AGENT")
            if has_code_use_case:
                action_log.append("DEPLOY_CODE_REACT_AGENT")

            if not action_log:
                 action_log.append("CONTINUE_MONITORING")
        else:
            reasoning_log.append("Reasoning: No specific insights to act upon.")
            action_log.append("CONTINUE_MONITORING")

        if any("DEPLOY_" in action for action in action_log):
            target = "Cloud Run"
            if any("Vercel" in bp for bp in best_practices) or any("serverless" in bp.lower() for bp in best_practices):
                target = "Vercel / Cloud Run"

            deployment_config = {
                "agent_type": "ReactAgent",
                "framework": "Next.js",
                "deployment_target": target,
                "status": "READY_FOR_DEPLOYMENT",
                "active_use_cases": [k for k, v in use_cases.items() if v]
            }

        # Prepare payload
        payload = {
            "react_reasoning": reasoning_log,
            "react_actions": action_log,
            "react_agent_deployment_config": deployment_config
        }

        self.logger.info(f"ReAct reasoning complete. Proposed actions: {action_log}")
        return payload
