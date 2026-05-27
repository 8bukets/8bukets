import os
import json
import re
from .base_agent import BaseAgent, Blackboard

class KnowledgeAgent(BaseAgent):
    """
    KnowledgeAgent: Provides structured AI agent knowledge (definitions, use cases, benefits)
    from the synthesized data to the Blackboard.
    """
    def __init__(self):
        super().__init__("KnowledgeAgent",
                         dependencies=[],
                         provides=[
                             "ai_agent_knowledge",
                             "ai_agents_definitions",
                             "agent_best_practices",
                             "agent_use_cases",
                             "google_cloud_tools_list",
                             "react_framework_details",
                             "agent_taxonomy"
                         ])

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Providing structured AI agent knowledge to the ecosystem...")

        # Support both potential paths
        knowledge_files = ["data/knowledge/ai_agents_knowledge.json", "data/ai_agents_knowledge.json", "ai_agents_knowledge.json"]
        knowledge_data = {}
        
        selected_file = None
        for kf in knowledge_files:
            if os.path.exists(kf):
                selected_file = kf
                break

        if not selected_file:
            self.logger.warning("No AI agent knowledge file found.")
            return {
                "ai_agent_knowledge": {},
                "ai_agents_definitions": {},
                "agent_best_practices": [],
                "agent_use_cases": {},
                "google_cloud_tools_list": [],
                "react_framework_details": {},
                "agent_taxonomy": {}
            }

        try:
            with open(selected_file, "r", encoding="utf-8") as f:
                knowledge = json.load(f)
            
            # 1. Processing for HEAD branch (list format)
            if isinstance(knowledge, list):
                knowledge_list = knowledge
                knowledge_dict = {} # Mock dict for base branch processing if needed
            else:
                knowledge_dict = knowledge
                knowledge_list = [] # Mock list for head branch processing if needed

            # Synthesized summary for HEAD
            synthesized = {
                "entries": knowledge_list if knowledge_list else [knowledge_dict],
                "all_definitions": [d for entry in (knowledge_list if knowledge_list else [knowledge_dict]) for d in entry.get("definitions", []) if isinstance(entry, dict)],
                "all_use_cases": [u for entry in (knowledge_list if knowledge_list else [knowledge_dict]) for u in entry.get("use_cases", []) if isinstance(entry, dict)],
                "all_benefits": [b for entry in (knowledge_list if knowledge_list else [knowledge_dict]) for b in entry.get("benefits", []) if isinstance(entry, dict)],
                "all_tools": list(set([t for entry in (knowledge_list if knowledge_list else [knowledge_dict]) for t in entry.get("google_cloud_tools", []) if isinstance(entry, dict)]))
            }

            # 2. Processing for BASE branch (dict format from Scraper)
            if not knowledge_dict and knowledge_list:
                # Convert list back to dict for the legacy logic if possible
                # This might be tricky if the schema changed significantly.
                # Assuming the dict version is the one with keys like 'what-is-an-ai-agent'
                pass
            
            # Helper to extract bullet points
            def extract_bullet(text, marker):
                if not text: return ""
                for line in text.split("\n"):
                    if line.startswith(f"- {marker}"):
                        return line.split(":", 1)[1].strip() if ":" in line else line
                return ""

            how_they_work = knowledge_dict.get("how-do-ai-agents-work", {}).get("content", "")

            definitions = {
                "ai_agent": knowledge_dict.get("what-is-an-ai-agent", {}).get("content", ""),
                "features": knowledge_dict.get("key-features-of-an-ai-agent", {}).get("content", ""),
                "differences": knowledge_dict.get("what-is-the-difference-between-ai-agents-ai-assistants-and-bots", {}).get("content", "") + "\n\n" + knowledge_dict.get("key-differences", {}).get("content", ""),
                "interaction_types": knowledge_dict.get("based-on-interaction", {}).get("content", ""),
                "agent_count_types": knowledge_dict.get("based-on-number-of-agents", {}).get("content", ""),
                "types": knowledge_dict.get("what-are-the-types-of-agents-in-ai", {}).get("content", "") + "\n\n" + knowledge_dict.get("based-on-interaction", {}).get("content", "") + "\n\n" + knowledge_dict.get("based-on-number-of-agents", {}).get("content", ""),
                "challenges": knowledge_dict.get("challenges-with-using-ai-agents", {}).get("content", ""),
                "jules_tools": knowledge_dict.get("jules-tools", {}).get("content", ""),
                "deployment": knowledge_dict.get("deploy-ai-agents-for-scale-and-efficiency-with-cloud-run", {}).get("content", ""),
                "how_they_work": how_they_work,
                "persona_definition": extract_bullet(how_they_work, "Persona"),
                "memory_definition": extract_bullet(how_they_work, "Memory"),
                "tools_definition": extract_bullet(how_they_work, "Tools"),
                "model_definition": extract_bullet(how_they_work, "Model"),
                "use_cases": {
                    "customer": knowledge_dict.get("customer-agents", {}).get("content", ""),
                    "employee": knowledge_dict.get("employee-agents", {}).get("content", ""),
                    "creative": knowledge_dict.get("creative-agents", {}).get("content", ""),
                    "data": knowledge_dict.get("data-agents", {}).get("content", ""),
                    "code": knowledge_dict.get("code-agents", {}).get("content", ""),
                    "security": knowledge_dict.get("security-agents", {}).get("content", "")
                },
                "benefits": "\n\n".join([
                    knowledge_dict.get("benefits-of-using-ai-agents", {}).get("content", ""),
                    knowledge_dict.get("efficiency-and-productivity", {}).get("content", ""),
                    knowledge_dict.get("improved-decision-making", {}).get("content", ""),
                    knowledge_dict.get("enhanced-capabilities", {}).get("content", ""),
                    knowledge_dict.get("social-interaction-and-simulation", {}).get("content", "")
                ]),
                "google_cloud_tools": knowledge_dict.get("google-cloud-and-ai-agents", {}).get("content", ""),
                "react-agent-deployment-logic": knowledge_dict.get("react-agent-deployment-logic", {}).get("content", "")
            }

            use_cases = definitions.get("use_cases", {})

            # Extract tools list
            tools_content = definitions.get("google_cloud_tools", "")
            tools_list = []
            if tools_content:
                for line in tools_content.split("\n"):
                    if line.startswith("- "):
                        match = re.search(r"^- ([\w\s\(\)-]{1,60}?)(?:\s+(?:Secure platform|Create AI|Build hybrid|Build Google-quality|Curated collection|Open-source|An AI|A fully managed|Provides a|Unified|Single|End-to-end|Speech|Language|Custom|Omnichannel|Description)|$)", line)
                        if match:
                            tool_name = match.group(1).strip()
                            if tool_name.endswith('App'):
                                tool_name = tool_name[:-3].strip()
                            if tool_name.endswith('Platform'):
                                tool_name = tool_name

                            # Clean up the specific merged strings found in the JSON file
                            if "PlatformCreate AI" in line:
                                tool_name = "Gemini Enterprise Agent Platform"

                            if tool_name and len(tool_name.split()) <= 6:
                                tools_list.append(tool_name)
                        else:
                            parts = line.split(" ", 2)
                            if len(parts) >= 2:
                                tools_list.append(parts[1])

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
                "ai_agent_knowledge": synthesized,
                "ai_agents_definitions": definitions,
                "agent_best_practices": best_practices,
                "agent_use_cases": use_cases,
                "google_cloud_tools_list": tools_list,
                "additional_resources": definitions.get("additional_resources", ""),
                "react_framework_details": {
                    "features": definitions.get("features", ""),
                    "deployment_strategy": "Orchestrate React components using Next.js for seamless AI integration.",
                    "react-agent-deployment-logic": definitions.get("react-agent-deployment-logic", "")
                },
                "agent_taxonomy": {
                    "interactive_partners": "Assisting with tasks like customer service via direct conversation.",
                    "background_processes": "Automating routine tasks and optimizing processes behind the scenes."
                }
            }

        except Exception as e:
            self.logger.error(f"Error processing knowledge: {e}")
            return {
                "ai_agent_knowledge": {},
                "ai_agents_definitions": {},
                "agent_best_practices": [],
                "agent_use_cases": {},
                "google_cloud_tools_list": [],
                "react_framework_details": {},
                "agent_taxonomy": {}
            }
