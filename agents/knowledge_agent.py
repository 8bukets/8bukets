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

        # Support multiple potential paths and merge them
        # prioritize canonical paths
        knowledge_files = [
            "ai_agents_knowledge.json",
            "data/knowledge/ai_agents_knowledge.json",
            "data/ai_agents_knowledge.json"
        ]
        
        knowledge_list = []
        knowledge_dict = {}

        for kf in knowledge_files:
            if os.path.exists(kf):
                try:
                    with open(kf, "r", encoding="utf-8") as f:
                        data_in_file = json.load(f)

                    if isinstance(data_in_file, list):
                        knowledge_list.extend(data_in_file)
                        # Map list items to knowledge_dict for legacy key support
                        for item in data_in_file:
                            if not isinstance(item, dict): continue

                            title = item.get("title", "").lower()
                            url = item.get("url", "").lower()

                            # Convert structured sections to flat content for legacy support
                            content_parts = []
                            for section_type in ["definitions", "use_cases", "benefits"]:
                                for entry in item.get(section_type, []):
                                    if isinstance(entry, dict):
                                        header = entry.get("term", entry.get("title", ""))
                                        body = entry.get("text", entry.get("description", ""))
                                        if header and body:
                                            content_parts.append(f"### {header}\n{body}")

                            content = "\n\n".join(content_parts)
                            if not content and "content" in item:
                                content = item["content"]

                            # Map to legacy slugs
                            if "what is an ai agent" in title or "what-are-ai-agents" in url:
                                knowledge_dict["what-is-an-ai-agent"] = {"content": content}
                            elif "key features" in title:
                                knowledge_dict["key-features-of-an-ai-agent"] = {"content": content}
                            elif "difference" in title and "bot" in title:
                                knowledge_dict["what-is-the-difference-between-ai-agents-ai-assistants-and-bots"] = {"content": content}
                            elif "how" in title and "work" in title:
                                knowledge_dict["how-do-ai-agents-work"] = {"content": content}
                            elif "challenges" in title:
                                knowledge_dict["challenges-with-using-ai-agents"] = {"content": content}
                            elif "use cases" in title:
                                knowledge_dict["use-cases-for-ai-agents"] = {"content": content}
                            elif "benefits" in title:
                                knowledge_dict["benefits-of-using-ai-agents"] = {"content": content}
                            elif "google cloud" in title and "agents" in title:
                                knowledge_dict["google-cloud-and-ai-agents"] = {"content": content}
                            elif "jules" in title:
                                knowledge_dict["jules-tools"] = {"content": content}
                    else:
                        knowledge_dict.update(data_in_file)
                        # Wrap dict items into a list for uniform synthesized view
                        for k, v in data_in_file.items():
                            if isinstance(v, dict) and "content" in v:
                                # Avoid duplicate entries if we already have it from another file
                                if not any(e.get("title") == v.get("title", k) for e in knowledge_list):
                                    knowledge_list.append({
                                        "title": v.get("title", k),
                                        "content": v["content"],
                                        "definitions": [],
                                        "use_cases": [],
                                        "benefits": [],
                                        "google_cloud_tools": []
                                    })
                except Exception as e:
                    self.logger.warning(f"Failed to load {kf}: {e}")

        if not knowledge_list and not knowledge_dict:
            self.logger.warning("No AI agent knowledge found in any file.")
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
            # Synthesized summary
            synthesized = {
                "entries": knowledge_list,
                "all_definitions": [],
                "all_use_cases": [],
                "all_benefits": [],
                "all_tools": []
            }

            for item in knowledge_list:
                if not isinstance(item, dict): continue
                synthesized["all_definitions"].extend(item.get("definitions", []))
                synthesized["all_use_cases"].extend(item.get("use_cases", []))
                synthesized["all_benefits"].extend(item.get("benefits", []))
                synthesized["all_tools"].extend(item.get("google_cloud_tools", []))
            
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

            # Extract tools list from all sources
            tools_list = []

            # 1. From google_cloud_tools content (unstructured/markdown)
            tools_content = definitions.get("google_cloud_tools", "")
            if tools_content:
                for line in tools_content.split("\n"):
                    if line.startswith("- "):
                        # Hardcoded list of expected tools to ensure they are captured even if mashed
                        known_tools = ["Gemini Enterprise App", "Gemini Enterprise Agent Platform", "Customer Experience Agent Studio", "Agent Garden", "Agent Development Kit (ADK)", "A2A Protocol", "Cloud Run"]
                        found_known = False
                        for kt in known_tools:
                            if kt in line:
                                tools_list.append(kt)
                                found_known = True
                                break

                        if not found_known:
                            # Try to match tool name before a description (colon or common description starter)
                            match = re.search(r"^- ([\w\s\(\).]{2,60}?)(?::|\s+(?:Secure platform|Create AI|Build hybrid|Build Google-quality|Curated collection|Open-source|An AI|A fully managed|Provides a|Unified|Single|End-to-end|Speech|Language|Custom|Omnichannel|Description)|$)", line)
                            if match:
                                tool_name = match.group(1).strip()
                                if tool_name and len(tool_name.split()) <= 6:
                                    tools_list.append(tool_name)
                            else:
                                # Fallback: take more words but avoid the whole line if it's very long
                                parts = line[2:].split(" ")
                                if parts:
                                    collected = []
                                    for p in parts[:4]:
                                        if not p: continue
                                        if p.lower() in ["is", "a", "an", "the", "build", "secure"]: break
                                        collected.append(p)
                                    if collected:
                                        tools_list.append(" ".join(collected).strip(",.:"))

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

            # Final tools list merge from all sources
            final_tools = list(set(tools_list + synthesized["all_tools"]))

            return {
                "ai_agent_knowledge": synthesized,
                "ai_agents_definitions": definitions,
                "agent_best_practices": best_practices,
                "agent_use_cases": use_cases,
                "google_cloud_tools_list": sorted(final_tools),
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
