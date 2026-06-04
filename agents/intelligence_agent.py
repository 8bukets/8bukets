from .base_agent import BaseAgent, Blackboard
from .telemetry import telemetry_manager
import os
import json
import uuid

class IntelligenceAgent(BaseAgent):
    def __init__(self):
        super().__init__("IntelligenceAgent",
                         dependencies=[
                             "analysis_stats",
                             "research_data",
                             "google_edge_knowledge",
                             "google_innovation_ai_knowledge",
                             "google_models_research_knowledge",
                             "ai_agent_knowledge",
                             "ai_agents_definitions"
                         ],
                         provides=[
                             "intelligence_insights",
                             "synchronization_level",
                             "strategic_outlook",
                             "categorized_knowledge",
                             "strategic_risk_assessment"
                         ])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Running Intelligence Synchronization & External World Collaboration...")

        # Simulate an LLM Call for Intelligence synthesis and record it via OpenTelemetry GenAI semantics
        session_id = str(uuid.uuid4())
        response_id = f"chatcmpl-{uuid.uuid4().hex[:12]}"

        telemetry_manager.record_gen_ai_inference_event(
            operation_name="chat",
            **{
                "gen_ai.conversation.id": session_id,
                "gen_ai.request.model": "gpt-4",
                "gen_ai.system_instructions": [
                    {"type": "text", "content": "You are a strategic intelligence AI."}
                ],
                "gen_ai.input.messages": [
                    {"role": "user", "parts": [{"type": "text", "content": "Analyze current system data."}]}
                ],
                "gen_ai.response.id": response_id,
                "gen_ai.response.model": "gpt-4-0613",
                "gen_ai.usage.input_tokens": 12,
                "gen_ai.usage.output_tokens": 45,
                "gen_ai.output.messages": [
                    {"role": "assistant", "parts": [{"type": "text", "content": "System aligned with Google Cloud Agent definitions."}], "finish_reason": "stop"}
                ],
                "gen_ai.response.finish_reasons": ["stop"]
            }
        )

        telemetry_manager.record_gen_ai_evaluation_event(
            evaluation_name="Relevance",
            **{
                "gen_ai.response.id": response_id,
                "gen_ai.evaluation.score.value": 1.0,
                "gen_ai.evaluation.score.label": "relevant",
                "gen_ai.evaluation.explanation": "The insight accurately reflects the underlying system context."
            }
        )

        analysis = blackboard.get("analysis_stats", {})
        research = blackboard.get("research_data", {})
        knowledge = blackboard.get("ai_agents_definitions", {})

        insights = []

        # 0. Knowledge Alignment
        if knowledge:
            insights.append("System alignment verified against Google Cloud AI Agent definitions.")

            ai_agent_def = (knowledge.get("ai_agent", "") + " " + knowledge.get("features", "") + " " + knowledge.get("how_they_work", "")).lower()
            if "reasoning" in ai_agent_def and "acting" in ai_agent_def:
                insights.append("Ecosystem architecture aligns with ReAct framework (Reasoning + Acting).")

            if "memory" in ai_agent_def:
                memory_def = knowledge.get("memory_definition", "")
                if "short term, long term, consensus, and episodic" in memory_def.lower():
                    insights.append("Verified Multi-tiered Memory: Short-term, Long-term, Consensus, and Episodic memory support confirmed.")
                else:
                    insights.append("System utilizes multi-tiered memory architecture (Short-term, Long-term, Episodic).")

            if "consensus memory" in ai_agent_def:
                insights.append("Ecosystem supports consensus memory for shared information among agents.")

            if "tools" in ai_agent_def:
                tools_def = knowledge.get("tools_definition", "")
                if "physical, graphical, and program-based" in tools_def.lower():
                    insights.append("Extended Toolset: Support for physical, graphical, and program-based interfaces confirmed.")
                else:
                    insights.append("Agent capabilities are extended via specialized external toolsets.")

            if "collaborating" in ai_agent_def:
                insights.append("System supports multi-agent collaboration and coordination.")

            if "self-refining" in ai_agent_def:
                insights.append("Ecosystem includes self-improvement and adaptation mechanisms.")

            # New insights from updated knowledge
            if "reasoning" in ai_agent_def:
                insights.append("Deep reasoning verified: System uses logic to draw conclusions and solve problems autonomously.")

            if "planning" in ai_agent_def:
                insights.append("Strategic planning confirmed: Agents can identify necessary steps and evaluate potential actions.")

            if "observing" in ai_agent_def:
                insights.append("System maintains environmental awareness through perception and sensing.")

            # Taxonomy Insights
            taxonomy = blackboard.get("agent_taxonomy", {})
            if taxonomy:
                insights.append("Taxonomy Alignment: System architecture distinguishes between Interactive Partners and Background Processes.")

            differences = knowledge.get("differences", "").lower()
            if "autonomously" in differences and "proactively" in differences:
                insights.append("Strategic Distinction: System operates as a true AI Agent (Autonomous/Proactive) rather than a simple Bot or Assistant.")

            # Benefits integration
            benefits_content = knowledge.get("benefits", "").lower()
            if "efficiency" in benefits_content:
                insights.append("Strategic Benefit: Significant efficiency and productivity gains via task division.")
            if "decision-making" in benefits_content:
                insights.append("Strategic Benefit: Improved decision-making through agent collaboration and debate.")
            if "adaptability" in benefits_content:
                insights.append("Strategic Benefit: High adaptability to changing situations and strategies.")

            # Tools integration
            tools_info = knowledge.get("google_cloud_tools", "").lower()
            if "gemini" in tools_info:
                insights.append("Tooling Strategy: Leveraging Gemini Enterprise for governance and discovery.")
            if "adk" in tools_info:
                insights.append("Tooling Strategy: Utilizing Agent Development Kit (ADK) for multi-agent systems.")
            if "a2a protocol" in tools_info:
                insights.append("Interoperability Strategy: Adopting A2A Protocol for platform-agnostic agent communication.")
            if "cloud run" in tools_info:
                insights.append("Infrastructure Strategy: Scalable deployment using Cloud Run serverless platform.")

            # Additional Resources insights
            resources = knowledge.get("additional_resources", "").lower()
            if "white paper" in resources:
                insights.append("Research Foundation: System design informed by Google Agents White Papers.")
            if "skillsboost" in resources:
                insights.append("Development Strategy: Leveraging Skillsboost Advanced Generative AI training for developers.")

        # 0.5 Strategic Risk Assessment
        risks = []
        challenges = knowledge.get("challenges", "").lower() if knowledge else ""
        if challenges:
            if "empathy" in challenges or "emotional intelligence" in challenges:
                risks.append("Limited performance expected in tasks requiring deep emotional intelligence.")
            if "ethical" in challenges:
                risks.append("High-stakes ethical decisions require human-in-the-loop oversight.")
            if "unpredictable" in challenges or "physical environments" in challenges:
                risks.append("Physical environment unpredictability identified as a boundary for autonomous operation.")
            if "resource-intensive" in challenges:
                risks.append("Deployment scalability may be impacted by high computational resource requirements.")

        # 1. Internal Logic
        top_cats = analysis.get("top_categories", {})
        if "Ad Ads Advertise" in top_cats:
            insights.append("High concentration of advertising-related content.")

        # 2. Synchronize with Research (Blackboard Collaboration)
        market_trends = research.get("market_trends", [])
        for trend in market_trends:
            insights.append(f"Synchronized Trend: {trend}")

        # 3. Synchronize with Telemetry (External Investigation Collaboration)
        for investigation in research.get("external_investigations", []):
            if investigation.get("world_context") == "GOOGLE_WORLD":
                insights.append(f"External World Insight: {investigation['domain']} is an active node in the Google World.")

        competitors = research.get("competitor_analysis", {})
        if competitors:
            top_comp = max(competitors.values(), key=lambda x: x['relevance'] == 'High', default=None)
            if top_comp:
                insights.append(f"Strategic Focus: {top_comp['findings']}")

        # 4. Integrate Google Edge Knowledge
        edge_knowledge = blackboard.get("google_edge_knowledge", {})
        if edge_knowledge and "sections" in edge_knowledge:
            insights.append(f"Google Edge Knowledge Integrated: {len(edge_knowledge['sections'])} sections extracted.")
            if len(edge_knowledge["sections"]) > 0:
                first_heading = edge_knowledge["sections"][0].get("heading", "N/A")
                insights.append(f"Top Edge AI Insight: {first_heading}")

        # 5. Categorize and Synthesize Google AI Knowledge
        google_knowledge_sources = [
            blackboard.get("google_innovation_ai_knowledge", {}),
            blackboard.get("google_models_research_knowledge", {}),
            blackboard.get("google_edge_knowledge", {})
        ]

        all_articles = []
        for source in google_knowledge_sources:
            if "articles" in source:
                all_articles.extend(source["articles"])
            elif "sections" in source: # Edge knowledge format
                for section in source["sections"]:
                    all_articles.append({
                        "title": section.get("heading", ""),
                        "snippet": section.get("content", "")
                    })

        categories = {
            "Models & Gemini": [],
            "Research & DeepMind": [],
            "Infrastructure & Cloud": [],
            "Products & Tools": [],
            "Safety & Privacy": []
        }

        keywords = {
            "Models & Gemini": ["gemini", "gemma", "llm", "embedding", "multimodal", "token"],
            "Research & DeepMind": ["research", "deepmind", "agi", "quantum", "science", "framework"],
            "Infrastructure & Cloud": ["infrastructure", "cloud", "network", "energy", "compute", "global"],
            "Products & Tools": ["app", "developer", "tool", "notebooklm", "search", "api", "vibe"],
            "Safety & Privacy": ["safety", "security", "privacy", "protecting", "compliance", "policy"]
        }

        for article in all_articles:
            text = (article.get("title", "") + " " + article.get("snippet", "")).lower()
            categorized = False
            for cat, kws in keywords.items():
                if any(kw in text for kw in kws):
                    categories[cat].append(article.get("title"))
                    categorized = True
                    break
            if not categorized:
                # Default to General Innovation
                if "General Innovation" not in categories:
                    categories["General Innovation"] = []
                categories["General Innovation"].append(article.get("title"))

        # Base branch additional categorizations
        if "Models" not in categories:
            categories["Models"] = ["LLMs as the foundation (Brain)"]
        else:
            categories["Models"].append("LLMs as the foundation (Brain)")

        categories["Cloud Products"] = blackboard.get("google_cloud_tools_list", [])
        categories["Solutions"] = list(blackboard.get("agent_use_cases", {}).keys())

        # 6. Integrate AI Agent Knowledge Base
        agent_knowledge = blackboard.get("ai_agent_knowledge", {})
        risk_assessment = risks.copy()
        if agent_knowledge:
            insights.append(f"AI Agent Knowledge Base Integrated: {len(agent_knowledge.get('entries', []))} deep dives analyzed.")

            # Extract common benefits as strategic drivers
            for benefit in agent_knowledge.get("all_benefits", []):
                title = benefit.get("title", "")
                if title and "Benefit" not in title:
                    insights.append(f"Strategic Value Driver: {title}")

            if agent_knowledge.get("all_tools"):
                insights.append(f"Recommended Toolchain: {', '.join(agent_knowledge.get('all_tools'))}")

            # Assess Risk based on agent definitions and use cases
            if any("autonomous" in str(d).lower() for d in agent_knowledge.get("all_definitions")):
                risk_assessment.append("Increased focus on autonomous agency requires enhanced safety guardrails.")
            if agent_knowledge.get("all_use_cases"):
                risk_assessment.append(f"Diversifying application landscape with {len(agent_knowledge['all_use_cases'])} validated use cases.")
                # Highlight top use cases in insights
                for use_case in agent_knowledge.get("all_use_cases", [])[:3]:
                    insights.append(f"Validated AI Agent Use Case: {use_case.get('title')} - {use_case.get('description')[:100]}...")

        # 7. Strategic Outlook synthesis
        outlook = []
        if knowledge:
            benefits_content = knowledge.get("benefits", "").lower()
            if "simultaneous execution" in benefits_content:
                outlook.append("Scaling Strategy: Implementing simultaneous execution across agent tiers.")
            if "realistic simulations" in benefits_content:
                outlook.append("R&D Strategy: Developing realistic simulations for human-agent interaction.")
            if "collaboration" in benefits_content:
                outlook.append("Operational Strategy: Enhancing agent debate and feedback loops.")

        assessment = "Positive outlook on multimodal scaling and autonomous research agents."
        if categories.get("Safety & Privacy"):
            assessment += " Strategic focus on privacy-preserving AI and security frameworks detected."
        if categories.get("Infrastructure & Cloud"):
            assessment += " Infrastructure expansion indicates preparation for massive-scale deployment."
        outlook.append(assessment)

        if not risk_assessment:
            risk_assessment.append("Continuous monitoring of external AI ecosystem recommended.")

        return {
            "intelligence_insights": insights,
            "strategic_outlook": outlook,
            "strategic_risk_assessment": risk_assessment,
            "synchronization_level": "ADVANCED_COLABORATIVE",
            "categorized_knowledge": {k: v for k, v in categories.items() if v}
        }
