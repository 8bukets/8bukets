from .base_agent import BaseAgent, Blackboard

class CreativityAgent(BaseAgent):
    def __init__(self):
        super().__init__("CreativityAgent", dependencies=["intelligence_insights", "ai_agents_definitions"], provides=["creative_concepts"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Running Creativity Session...")

        insights = blackboard.get("intelligence_insights", [])
        knowledge = blackboard.get("ai_agents_definitions", {})

        concepts = [
            "5 Trends Shaping the Future",
            "Why Your Strategy Needs a Reboot",
            "Monetization: Beyond the Basics"
        ]

        if any("advertising" in str(insight).lower() for insight in insights):
            concepts.append("Deep Dive: High concentration of advertising-related content.")

        agent_types = knowledge.get("types", "").lower()
        if "background agents" in agent_types:
            concepts.append("Efficiency Playbook: Automating with Background Agents")
        if "interactive partners" in agent_types:
            concepts.append("User Engagement: Building Interactive Partner Agents")

        use_cases = knowledge.get("use_cases", {})
        if use_cases:
            if use_cases.get("code"):
                concepts.append("The Future of Dev: Accelerating with Code Agents")
            if use_cases.get("security"):
                concepts.append("Autonomous Defense: Protecting the Perimeter with Security Agents")
            if use_cases.get("data"):
                concepts.append("Data Insights: Unleashing Data Agents on Complex Analytics")

        # NEW ENHANCEMENT: Map concepts directly to Work Orders as suggested by 8bukets intelligence
        executable_orders = []
        for i, concept in enumerate(concepts):
            executable_orders.append({
                "id": f"AUTO_CREATIVE_EXEC_{i}",
                "type": "CONTENT_CREATION",
                "description": concept,
                "status": "pending"
            })

        # Blackboard doesn't have a sync set() method natively in BaseAgent,
        # but agents return dicts which are merged into blackboard asynchronously.

        return {"creative_concepts": concepts, "creative_work_orders": executable_orders}
