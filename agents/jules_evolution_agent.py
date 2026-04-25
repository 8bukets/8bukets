import asyncio
import os
import json
from .base_agent import BaseAgent, Blackboard

try:
    import google.generativeai as genai
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

class JulesEvolutionAgent(BaseAgent):
    """The Lead Evolution Coordinator: Orchestrates high-level system transformation with autonomous deep planning capabilities."""
    def __init__(self):
        super().__init__("JulesEvolutionAgent",
                         dependencies=["system_evolution", "meta_optimizations", "sigma_performance_report"],
                         provides=["evolution_strategy", "collaboration_nexus", "autonomous_decision", "deep_plan"])

        self.api_key = os.getenv("GEMINI_API_KEY")
        if HAS_GENAI and self.api_key:
            genai.configure(api_key=self.api_key)
            # Using Gemini 1.5 Flash for rapid autonomous reasoning
            self.model = genai.GenerativeModel('gemini-1.5-flash')
        else:
            self.model = None
            self.logger.warning("GEMINI_API_KEY missing or google.generativeai not installed. JulesEvolutionAgent will operate in fallback static mode.")

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Coordinating system-wide autonomous evolution via Deep Planning...")

        evolution = blackboard.get("system_evolution", {})
        sigma = blackboard.get("sigma_performance_report", {})

        target_version = evolution.get("parameter_shifts", {}).get("current_version", "1.0")

        decision_data = {
            "autonomous_decision": None,
            "deep_plan": None
        }

        if self.model:
            # Perform Deep Planning
            decision_data = await self._perform_deep_planning(sigma, target_version)
        else:
            self.logger.info("Operating in static fallback mode due to missing LLM configuration.")
            decision_data["deep_plan"] = "Static fallback plan: increase concurrency."
            decision_data["autonomous_decision"] = {"action": "UPDATE_PARAMETER", "key": "system_concurrency", "value": 10}

        # Build the 'Collaboration Nexus' - a shared strategy for specialized agents
        strategy = {
            "target_version": target_version,
            "optimization_priority": "AUTONOMOUS_DEEP_PLANNING",
            "required_collaborators": ["GitHubEvolutionAgent", "Architect"],
            "nexus_active": True,
            "decision": decision_data["autonomous_decision"]
        }

        # Simulate orchestration overhead
        await asyncio.sleep(0.1)
        self.logger.info(f"Nexus established. Deep plan formulated: {decision_data['deep_plan']}")

        return {
            "evolution_strategy": strategy,
            "collaboration_nexus": "ACTIVE",
            "autonomous_decision": decision_data["autonomous_decision"],
            "deep_plan": decision_data["deep_plan"]
        }

    async def _perform_deep_planning(self, sigma_report: dict, version: str) -> dict:
        """Uses the LLM to question assumptions and formulate an autonomous plan."""

        prompt = f"""
        You are the 'JulesEvolutionAgent', the Lead Evolution Coordinator of a massive 170-agent DAG architecture.
        Your goal is to perform 'Deep Planning'.

        Current System State:
        - Target Version: {version}
        - Sigma Performance Report: {json.dumps(sigma_report)}

        Instructions:
        1. Analyze the performance report.
        2. Ask yourself clarifying questions internally to identify bottlenecks or areas for improvement.
        3. Formulate a specific, actionable decision to evolve the system (e.g., changing a configuration parameter).

        You must output your response in valid JSON format with exactly two keys:
        - "deep_plan": A string describing your reasoning and the questions you asked yourself.
        - "autonomous_decision": A JSON object representing the action to take. For example: {{"action": "UPDATE_PARAMETER", "key": "system_concurrency", "value": 8}}

        Output only the JSON.
        """

        try:
            # We run the synchronous Gemini call in an executor to avoid blocking the asyncio event loop
            loop = asyncio.get_running_loop()
            response = await loop.run_in_executor(None, self.model.generate_content, prompt)

            # Clean up potential markdown formatting from the response
            response_text = response.text.strip()
            if response_text.startswith("```json"):
                response_text = response_text[7:]
            if response_text.endswith("```"):
                response_text = response_text[:-3]

            parsed_response = json.loads(response_text)
            self.logger.info("Successfully executed Deep Planning using LLM.")
            return parsed_response

        except Exception as e:
            self.logger.error(f"Deep Planning failed: {e}. Falling back to default plan.")
            return {
                "deep_plan": f"Deep planning encountered an error: {e}. Defaulting to safe parameter bump.",
                "autonomous_decision": {"action": "UPDATE_PARAMETER", "key": "search_depth", "value": 2}
            }

    async def review(self, blackboard: Blackboard):
        nexus = blackboard.get("collaboration_nexus")
        decision = blackboard.get("autonomous_decision")

        feedback = []
        if nexus == "ACTIVE":
            feedback.append("Evolution strategy is synchronized across all specialized agents.")

        if decision:
            feedback.append(f"Autonomous decision generated: {json.dumps(decision)}")
            # Propose the autonomous decision to the Architect
            if decision.get("action") == "UPDATE_PARAMETER":
                await blackboard.propose_improvement(
                    agent_name="JulesEvolutionAgent",
                    improvement={decision.get("key"): decision.get("value")}
                )
        else:
            feedback.append("Evolution coordination pending autonomous decision.")

        return feedback
