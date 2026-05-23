from .base_agent import BaseAgent, Blackboard
import json
import os

class KnowledgeAgent(BaseAgent):
    """
    Agent that provides foundational AI Agent knowledge scraped from Google Cloud.
    """
    def __init__(self):
        super().__init__("KnowledgeAgent",
                         dependencies=[],
                         provides=["ai_agents_definitions", "agent_best_practices", "agent_use_cases", "google_cloud_tools_list", "react_framework_details", "agent_taxonomy"])
        self.knowledge_file = "ai_agents_knowledge.json"

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Loading AI Agent Knowledge from Google Cloud Discover...")

        if not os.path.exists(self.knowledge_file):
            self.logger.error(f"Knowledge file {self.knowledge_file} not found.")
            return {
                "ai_agents_definitions": {},
                "agent_best_practices": []
            }

        try:
            with open(self.knowledge_file, "r", encoding="utf-8") as f:
                knowledge = json.load(f)

            # Extract specific definitions and best practices
            how_they_work = knowledge.get("how-do-ai-agents-work", {}).get("content", "")

            # Helper to extract bullet points
            def extract_bullet(text, marker):
                for line in text.split("\n"):
                    if line.startswith(f"- {marker}"):
                        return line.split(":", 1)[1].strip() if ":" in line else line
                return ""

            definitions = {
                "ai_agent": knowledge.get("what-is-an-ai-agent", {}).get("content", ""),
                "features": knowledge.get("key-features-of-an-ai-agent", {}).get("content", ""),
                "differences": knowledge.get("what-is-the-difference-between-ai-agents-ai-assistants-and-bots", {}).get("content", "") + "\n\n" + knowledge.get("key-differences", {}).get("content", ""),
                "interaction_types": knowledge.get("based-on-interaction", {}).get("content", ""),
                "agent_count_types": knowledge.get("based-on-number-of-agents", {}).get("content", ""),
                "types": knowledge.get("what-are-the-types-of-agents-in-ai", {}).get("content", "") + "\n\n" + knowledge.get("based-on-interaction", {}).get("content", "") + "\n\n" + knowledge.get("based-on-number-of-agents", {}).get("content", ""),
                "challenges": knowledge.get("challenges-with-using-ai-agents", {}).get("content", ""),
                "jules_tools": knowledge.get("jules-tools", {}).get("content", ""),
                "deployment": knowledge.get("deploy-ai-agents-for-scale-and-efficiency-with-cloud-run", {}).get("content", ""),
                "how_they_work": how_they_work,
                "persona_definition": extract_bullet(how_they_work, "Persona"),
                "memory_definition": extract_bullet(how_they_work, "Memory"),
                "tools_definition": extract_bullet(how_they_work, "Tools"),
                "model_definition": extract_bullet(how_they_work, "Model"),
                "use_cases": {
                    "customer": knowledge.get("customer-agents", {}).get("content", ""),
                    "employee": knowledge.get("employee-agents", {}).get("content", ""),
                    "creative": knowledge.get("creative-agents", {}).get("content", ""),
                    "data": knowledge.get("data-agents", {}).get("content", ""),
                    "code": knowledge.get("code-agents", {}).get("content", ""),
                    "security": knowledge.get("security-agents", {}).get("content", "")
                },
                "benefits": "\n\n".join([
                    knowledge.get("benefits-of-using-ai-agents", {}).get("content", ""),
                    knowledge.get("efficiency-and-productivity", {}).get("content", ""),
                    knowledge.get("improved-decision-making", {}).get("content", ""),
                    knowledge.get("enhanced-capabilities", {}).get("content", ""),
                    knowledge.get("social-interaction-and-simulation", {}).get("content", "")
                ]),
                "google_cloud_tools": knowledge.get("google-cloud-and-ai-agents", {}).get("content", "")
            }

            use_cases = definitions.get("use_cases", {})

            # Extract tools list
            tools_content = definitions.get("google_cloud_tools", "")
            tools_list = []
            if tools_content:
                # Tools are typically in bullet points: "- ToolName Description"
                import re
                for line in tools_content.split("\n"):
                    if line.startswith("- "):
                        # Regex to capture the first few words which usually form the tool name
                        # Stops at known description start markers or after 4 words
                        # Updated to handle more markers found in the content, including joined words from scraping
                        match = re.search(r"^- ([\w\s\(\)-]{1,60}?)(?:(?:\s+|[A-Z])(?:Secure platform|Create AI|Build hybrid|Build Google-quality|Curated collection|Open-source|An AI|A fully managed|Provides a|Unified|Single|End-to-end|Speech|Language|Custom|Omnichannel)|$)", line)
                        if match:
                            tool_name = match.group(1).strip()
                            if tool_name and len(tool_name.split()) <= 6:
                                tools_list.append(tool_name)

            best_practices = [
                "Use Jules Tools CLI for terminal-based session management and TUI dashboard.",
                "Focus on reasoning, acting, observing, and planning.",
                "Implement self-refining capabilities for continuous improvement.",
                "Ensure robust memory management (short-term, long-term, episodic, consensus).",
                "Utilize appropriate tools for environment interaction.",
                "Maintain a consistent persona (role, personality, communication style) appropriate to the assigned role.",
                "Leverage serverless platforms like Cloud Run for scalable and cost-effective deployment.",
                "Design specialized agents for specific domains like Code, Security, or Data.",
                "Distinguish between AI Agents (autonomous), AI Assistants (collaborative), and Bots (rule-based).",
                "Orchestrate React agents dynamically through Next.js for robust frontend deployments."
            ]

            return {
                "ai_agents_definitions": definitions,
                "agent_best_practices": best_practices,
                "agent_use_cases": use_cases,
                "google_cloud_tools_list": tools_list,
                "react_framework_details": {
                    "features": definitions.get("features", ""),
                    "deployment_strategy": "Orchestrate React components using Next.js for seamless AI integration."
                },
                "agent_taxonomy": {
                    "interactive_partners": "Assisting with tasks like customer service via direct conversation.",
                    "background_processes": "Automating routine tasks and optimizing processes behind the scenes."
                }
            }
        except Exception as e:
            self.logger.error(f"Failed to load knowledge: {e}")
            return {
                "ai_agents_definitions": {},
                "agent_best_practices": [],
                "agent_use_cases": {},
                "google_cloud_tools_list": [],
                "react_framework_details": {},
                "agent_taxonomy": {}
            }
