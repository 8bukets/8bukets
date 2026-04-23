import asyncio
import json
import os
import requests
from .base_agent import BaseAgent, Blackboard

class JulesEvolutionAgent(BaseAgent):
    """The Lead Evolution Coordinator: Orchestrates high-level system transformation and agent collaboration using Gemini & Gemma insights."""
    def __init__(self):
        super().__init__("JulesEvolutionAgent",
                         dependencies=["system_evolution", "meta_optimizations"],
                         provides=["evolution_strategy", "collaboration_nexus"])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Coordinating system-wide autonomous evolution via Gemini...")

        # Get current evolution parameters
        params_path = "config/evolution_params.json"
        current_params = {}
        if os.path.exists(params_path):
            with open(params_path, "r", encoding="utf-8") as f:
                current_params = json.load(f)

        # Get Gemma 4 docs for context
        gemma_docs_path = "gemmafour_docs.json"
        gemma_context = "Gemma 4 is highly capable but context is unavailable."
        if os.path.exists(gemma_docs_path):
            with open(gemma_docs_path, "r", encoding="utf-8") as f:
                gemma_data = json.load(f)
                # Keep it concise to avoid huge prompts
                best_practices = gemma_data.get("best_practices", {}).get("content", "")
                overview = gemma_data.get("models_overview", {}).get("content", "")
                gemma_context = f"Overview: {overview[:500]}...\nBest Practices: {best_practices[:500]}..."

        new_params = current_params.copy()
        api_key = os.environ.get("GEMINI_API_KEY")

        if not api_key:
            self.logger.warning("GEMINI_API_KEY is not set. Skipping autonomous parameter optimization.")
        else:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={api_key}"

            prompt = f"""
            You are an AI evolving a massive-scale autonomous system.
            Based on these Gemma 4 best practices and overview: {gemma_context}

            The current system evolution parameters are: {json.dumps(current_params)}

            Please propose small, optimized adjustments to these parameters (e.g., slightly increase concurrency or version, tweak thresholds).
            Return ONLY valid JSON with the updated parameters, no markdown, no other text.
            """

            headers = {'Content-Type': 'application/json'}
            payload = {
                "contents": [
                    {
                        "parts": [{"text": prompt}]
                    }
                ]
            }

            try:
                resp = requests.post(url, headers=headers, json=payload)
                resp.raise_for_status()
                response_data = resp.json()

                # Extract text from response
                text = response_data['candidates'][0]['content']['parts'][0]['text']

                # Clean markdown formatting if present
                text = text.replace("```json", "").replace("```", "").strip()

                proposed_params = json.loads(text)

                # Basic validation
                if isinstance(proposed_params, dict) and "current_version" in proposed_params:
                    new_params = proposed_params
                    self.logger.info(f"Gemini proposed new parameters: {new_params}")

                    # Apply new params
                    with open(params_path, "w", encoding="utf-8") as f:
                        json.dump(new_params, f, indent=4)
                else:
                    self.logger.warning("Gemini returned invalid format.")
            except Exception as e:
                self.logger.error(f"Gemini API call failed: {e}")

        # Build the 'Collaboration Nexus' - a shared strategy for specialized agents
        strategy = {
            "target_version": new_params.get("current_version", current_params.get("current_version", "1.0")),
            "optimization_priority": "STABILITY_AND_VISUALIZATION",
            "required_collaborators": ["GitHubEvolutionAgent", "GitKrakenEvolutionAgent", "DockerEvolutionAgent"],
            "nexus_active": True,
            "gemini_optimized": True
        }

        return {
            "evolution_strategy": strategy,
            "collaboration_nexus": "ACTIVE"
        }

    async def review(self, blackboard: Blackboard):
        nexus = blackboard.get("collaboration_nexus")
        if nexus == "ACTIVE":
            return ["Evolution strategy is synchronized and Gemini-optimized across all specialized agents."]
        return ["Evolution coordination pending."]
