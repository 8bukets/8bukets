from .base_agent import BaseAgent, Blackboard

class ReActAgent(BaseAgent):
    """
    An agent implementing the ReAct (Reasoning and Acting) framework.
    It takes knowledge and intelligence insights, performs reasoning, and proposes actionable steps.
    """
    def __init__(self):
        super().__init__("ReActAgent",
                         dependencies=["intelligence_insights", "ai_agents_definitions"],
                         provides=["react_reasoning", "react_actions"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Executing ReAct (Reasoning + Acting) logic...")

        insights = blackboard.get("intelligence_insights", [])
        definitions = blackboard.get("ai_agents_definitions", {})

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

        # Prepare payload
        payload = {
            "react_reasoning": reasoning_log,
            "react_actions": action_log
        }

        self.logger.info(f"ReAct reasoning complete. Proposed actions: {action_log}")
        return payload
