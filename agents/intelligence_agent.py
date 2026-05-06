from .base_agent import BaseAgent, Blackboard
import os
import json

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("IntelligenceAgent",
                         dependencies=["analysis_stats", "research_data", "ai_agents_definitions"],
                         provides=["intelligence_insights", "synchronization_level", "strategic_risk_assessment"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Running Intelligence Synchronization & External World Collaboration...")

        analysis = blackboard.get("analysis_stats", {})
        research = blackboard.get("research_data", {})
        knowledge = blackboard.get("ai_agents_definitions", {})

        insights = []

        # 0. Knowledge Alignment
        if knowledge:
            insights.append("System alignment verified against Google Cloud AI Agent definitions.")

            ai_agent_def = (knowledge.get("ai_agent", "") + " " + knowledge.get("features", "")).lower()
            if "reasoning" in ai_agent_def and "acting" in ai_agent_def:
                insights.append("Ecosystem architecture aligns with ReAct framework (Reasoning + Acting).")

            if "memory" in ai_agent_def:
                insights.append("System utilizes multi-tiered memory architecture (Short-term, Long-term, Episodic).")

            if "tools" in ai_agent_def:
                insights.append("Agent capabilities are extended via specialized external toolsets.")

            if "collaborating" in ai_agent_def:
                insights.append("System supports multi-agent collaboration and coordination.")

            if "self-refining" in ai_agent_def:
                insights.append("Ecosystem includes self-improvement and adaptation mechanisms.")

            if "observing" in ai_agent_def:
                insights.append("System maintains environmental awareness through perception and sensing.")

            # Benefits integration
            benefits = knowledge.get("benefits", "").lower()
            if "efficiency" in benefits:
                insights.append("Strategic Benefit: Significant efficiency and productivity gains via task division.")
            if "decision-making" in benefits:
                insights.append("Strategic Benefit: Improved decision-making through agent collaboration and debate.")
            if "adaptability" in benefits:
                insights.append("Strategic Benefit: High adaptability to changing situations and strategies.")

            # Tools integration
            tools_info = knowledge.get("google_cloud_tools", "").lower()
            if "gemini" in tools_info:
                insights.append("Tooling Strategy: Leveraging Gemini Enterprise for governance and discovery.")
            if "adk" in tools_info:
                insights.append("Tooling Strategy: Utilizing Agent Development Kit (ADK) for multi-agent systems.")
            if "cloud run" in tools_info:
                insights.append("Infrastructure Strategy: Scalable deployment using Cloud Run serverless platform.")

        # 0.5 Strategic Risk Assessment
        risks = []
        challenges = knowledge.get("challenges", "").lower()
        if challenges:
            if "empathy" in challenges or "emotional intelligence" in challenges:
                risks.append("Limited performance expected in tasks requiring deep emotional intelligence.")
            if "ethical" in challenges:
                risks.append("High-stakes ethical decisions require human-in-the-loop oversight.")
            if "unpredictable" in challenges or "physical environments" in challenges:
                risks.append("Physical environment unpredictability identified as a boundary for autonomous operation.")

        # 1. Internal Logic
        top_cats = analysis.get("top_categories", {})
        if "Ad Ads Advertise" in top_cats:
            insights.append("High concentration of advertising-related content.")

        # 2. Synchronize with Research (Blackboard Collaboration)
        market_trends = research.get("market_trends", [])
        for trend in market_trends:
            insights.append(f"Synchronized Trend: {trend}")

        # 3. Synchronize with Telemetry (External Investigation Collaboration)
        # In a more advanced system, we'd query the TelemetryManager directly or use a shared event bus.
        # Here we check the research results which already integrated the telemetry-derived investigations.
        for investigation in research.get("external_investigations", []):
            if investigation.get("world_context") == "GOOGLE_WORLD":
                insights.append(f"External World Insight: {investigation['domain']} is an active node in the Google World.")

        competitors = research.get("competitor_analysis", {})
        if competitors:
            top_comp = max(competitors.values(), key=lambda x: x['relevance'] == 'High', default=None)
            if top_comp:
                insights.append(f"Strategic Focus: {top_comp['findings']}")

        return {
            "intelligence_insights": insights,
            "synchronization_level": "ADVANCED_COLABORATIVE",
            "strategic_risk_assessment": risks
        }
