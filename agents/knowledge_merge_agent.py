from .base_agent import BaseAgent, Blackboard
import json
import os
from datetime import datetime
from typing import Dict, Any, List, Union

class KnowledgeMergeAgent(BaseAgent):
    """
    Agent responsible for synthesizing multiple knowledge sources into a unified foundation.
    It merges AI definitions, market research, and technical documentation.
    """
    def __init__(self):
        super().__init__(
            "KnowledgeMergeAgent",
            dependencies=["ai_agents_definitions", "analysis_stats", "research_data"],
            provides=["consolidated_knowledge"]
        )
        self.output_json = "data/knowledge/system_knowledge.json"
        self.output_md = "CONSOLIDATED_KNOWLEDGE.md"
        self.sources = {
            "ai_agents": "ai_agents_knowledge.json",
            "market_data": "links.json",
            "legal_ecosystem": "wilson_sonsini_docs.json",
            "gemma_model": "gemmafour_docs.json",
            "intelephense": "intelephense_docs.json",
            "litert": "litert_docs.json",
            "stitch": "stitch_docs.json",
            "vscode_intelephense": "vscode_intelephense_docs.json",
            "google_ads": "google_ads_docs.json"
        }
        self.strategic_source = "KNOWLEDGE_MERGE.md"

    async def run(self, data: list, blackboard: Blackboard) -> dict:
        self.logger.info("Starting Knowledge Consolidation (Python Layer)...")

        # Load existing unified knowledge to maintain a flat structure
        consolidated = {
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "version": self.config.get("current_version", 1.0),
                "sources_processed": []
            }
        }

        if os.path.exists(self.output_json):
            try:
                with open(self.output_json, "r", encoding="utf-8") as f:
                    existing = json.load(f)
                    if isinstance(existing, dict):
                        # Preserve metadata version if it's higher
                        if existing.get("metadata", {}).get("version", 0) > consolidated["metadata"]["version"]:
                            consolidated["metadata"]["version"] = existing["metadata"]["version"]

                        # Flatten logic: migration from nested structure
                        if "sections" in existing:
                            existing.update(existing.pop("sections"))
                        if "typescript_sections" in existing:
                            existing.update(existing.pop("typescript_sections"))

                        # Use existing as base to preserve everything (flat structure)
                        consolidated.update(existing)
            except Exception as e:
                self.logger.warning(f"Failed to load existing knowledge from {self.output_json}: {e}")

        # Update metadata for current run
        consolidated["metadata"]["generated_at"] = datetime.now().isoformat()

        # 1. Process Structured Knowledge Sources (JSON Dictionaries)
        for key, filepath in self.sources.items():
            if not os.path.exists(filepath):
                self.logger.warning(f"Source file {filepath} not found. Skipping.")
                continue

            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = json.load(f)

                if isinstance(content, dict):
                    # Smart merge for ai_agents if it follows the structured pattern
                    if key == "ai_agents" and "ai_agents_structured" in consolidated:
                        self._merge_ai_agents(consolidated, content)
                    elif key == "market_data":
                        # If market_data is a dict (likely from system_knowledge.json),
                        # we merge it carefully with potentially new content from links.json
                        existing_market = consolidated.get("market_data", {})
                        if isinstance(existing_market, list): existing_market = {"all_entries": existing_market}

                        existing_entries = existing_market.get("all_entries", [])
                        new_entries = content.get("all_entries", []) if isinstance(content, dict) else content

                        if isinstance(new_entries, list):
                            urls = {e.get("post_url") for e in existing_entries if e.get("post_url")}
                            unique_new = [e for e in new_entries if e.get("post_url") not in urls]
                            combined = unique_new + existing_entries
                            consolidated[key] = {
                                "total_entries": len(combined),
                                "recent_entries": combined[:20],
                                "all_entries": combined
                            }
                    else:
                        consolidated[key] = content

                    if filepath not in consolidated["metadata"]["sources_processed"]:
                        consolidated["metadata"]["sources_processed"].append(filepath)
                elif isinstance(content, list):
                    # For market_data (links.json), we want to merge with existing data
                    if key == "market_data":
                        existing_market = consolidated.get("market_data", {})
                        if isinstance(existing_market, list): existing_market = {"all_entries": existing_market}

                        existing_entries = existing_market.get("all_entries", [])

                        # Merge and deduplicate by post_url
                        urls = {e.get("post_url") for e in existing_entries if e.get("post_url")}
                        new_entries = [e for e in content if e.get("post_url") not in urls]

                        combined_entries = new_entries + existing_entries

                        consolidated[key] = {
                            "total_entries": len(combined_entries),
                            "recent_entries": combined_entries[:20],
                            "all_entries": combined_entries
                        }
                    else:
                        consolidated[key] = content

                    if filepath not in consolidated["metadata"]["sources_processed"]:
                        consolidated["metadata"]["sources_processed"].append(filepath)

            except Exception as e:
                self.logger.error(f"Error processing {filepath}: {e}")

        # 2. Add Blackboard Insights
        consolidated["system_insights"] = {
            "analysis_stats": blackboard.get("analysis_stats"),
            "research_trends": blackboard.get("research_data", {}).get("market_trends", []),
            "intelligence_outlook": blackboard.get("strategic_outlook", [])
        }

        # 3. Save Structured Result
        os.makedirs(os.path.dirname(self.output_json), exist_ok=True)
        try:
            with open(self.output_json, "w", encoding="utf-8") as f:
                json.dump(consolidated, f, indent=4, ensure_ascii=False)
            self.logger.info(f"Consolidated JSON saved to {self.output_json}")
        except Exception as e:
            self.logger.error(f"Failed to save consolidated JSON: {e}")

        # 4. Ingest Strategic Mapping (KNOWLEDGE_MERGE.md)
        if os.path.exists(self.strategic_source):
            try:
                with open(self.strategic_source, "r", encoding="utf-8") as f:
                    consolidated["strategic_mapping"] = f.read()
            except Exception as e:
                self.logger.error(f"Failed to read strategic source {self.strategic_source}: {e}")

        # 5. Generate Human-Readable Markdown
        self._generate_markdown(consolidated)

        return {"consolidated_knowledge": consolidated}

    def _merge_ai_agents(self, consolidated: dict, new_agents_data: Union[List[dict], dict]):
        """Deep merge logic for AI agents, similar to merge_knowledge.py"""
        existing_agents = {item["url"]: item for item in consolidated.get("ai_agents_structured", [])}

        # If new_agents_data is a dict (from ai_agents_knowledge.json possibly), convert or handle
        items_to_process = []
        if isinstance(new_agents_data, list):
            items_to_process = new_agents_data
        elif isinstance(new_agents_data, dict):
            # If it's a dict where keys are IDs and values are info
            items_to_process = list(new_agents_data.values())

        for item in items_to_process:
            if not isinstance(item, dict): continue
            url = item.get("url")
            if not url: continue

            if url in existing_agents:
                existing = existing_agents[url]

                # Merge Definitions
                existing_defs = {d["term"]: d["text"] for d in existing.get("definitions", [])}
                for d in item.get("definitions", []):
                    existing_defs[d["term"]] = d["text"]
                existing["definitions"] = [{"term": k, "text": v} for k, v in existing_defs.items()]

                # Merge Tools
                existing_tools = set(existing.get("google_cloud_tools", []))
                existing_tools.update(item.get("google_cloud_tools", []))
                existing["google_cloud_tools"] = sorted(list(existing_tools))

                # Merge Use Cases
                existing_ucs = {u["title"]: u["description"] for u in existing.get("use_cases", [])}
                for u in item.get("use_cases", []):
                    existing_ucs[u["title"]] = u["description"]
                existing["use_cases"] = [{"title": k, "description": v} for k, v in existing_ucs.items()]

                # Merge Benefits
                existing_bens = {b["title"]: b["description"] for b in existing.get("benefits", [])}
                for b in item.get("benefits", []):
                    existing_bens[b["title"]] = b["description"]
                existing["benefits"] = [{"title": k, "description": v} for k, v in existing_bens.items()]
            else:
                existing_agents[url] = item

        consolidated["ai_agents_structured"] = list(existing_agents.values())

    def _generate_markdown(self, consolidated: dict):
        try:
            with open(self.output_md, "w", encoding="utf-8") as f:
                f.write(f"# Consolidated Knowledge Base\n\n")
                f.write(f"**Last Sync (Python):** {consolidated['metadata']['generated_at']}\n")
                f.write(f"**System Version:** {consolidated['metadata']['version']}\n\n")

                # Integrate Strategic Mapping from KNOWLEDGE_MERGE.md
                if "strategic_mapping" in consolidated:
                    f.write("## 🧩 Strategic Identity & Unified Model\n")
                    f.write(consolidated["strategic_mapping"])
                    f.write("\n\n---\n\n")

                f.write("## System Intelligence & Outlook\n")
                insights = consolidated.get("system_insights", {})
                if insights:
                    for item in insights.get("intelligence_outlook", []):
                        f.write(f"- {item}\n")
                else:
                    f.write("Awaiting autonomous intelligence sync...\n")

                f.write("\n## 1. AI Agent Foundation\n")
                ai_data = consolidated.get("ai_agents", {})
                if isinstance(ai_data, dict):
                    for sid, info in ai_data.items():
                        if isinstance(info, dict) and "title" in info:
                            f.write(f"### {info['title']}\n\n{info.get('content', '')}\n\n")

                # Structured AI Agents
                structured_ai = consolidated.get("ai_agents_structured", [])
                if structured_ai:
                    f.write("### Structured AI Agent Knowledge\n")
                    for agent in structured_ai:
                        f.write(f"#### {agent.get('title', 'AI Agent')}\n")
                        f.write(f"URL: {agent.get('url')}\n\n")
                        if agent.get('definitions'):
                            f.write("**Definitions:**\n")
                            for d in agent['definitions']:
                                f.write(f"- *{d['term']}*: {d['text']}\n")
                        f.write("\n")

                f.write("\n## 2. Market Intelligence (Markposition)\n")
                market = consolidated.get("market_data", {})
                f.write(f"Total Market Data Points: {market.get('total_entries', 0)}\n\n")
                for entry in market.get("all_entries", market.get("recent_entries", []))[:50]:
                    f.write(f"- **{entry.get('title', 'N/A')}**: {entry.get('external_link', '')} ({entry.get('date', 'N/A')})\n")

                f.write("\n## 3. Legal & Ecosystem (Wilson Sonsini)\n")
                legal = consolidated.get("legal_ecosystem", {})
                if isinstance(legal, dict):
                    for lid, linfo in legal.items():
                        if isinstance(linfo, dict) and "title" in linfo:
                            f.write(f"### {linfo['title']}\n\n{linfo.get('content', '')}\n\n")

                f.write("\n## 4. Technical Documentation\n")
                for tech_key in ["gemma_model", "intelephense", "litert", "stitch", "vscode_intelephense", "google_ads"]:
                    tech_data = consolidated.get(tech_key, {})
                    if tech_data:
                        title = tech_key.replace("_", " ").title()
                        f.write(f"### {title}\n")
                        # Basic summary as these can be large
                        if isinstance(tech_data, dict):
                            keys_preview = ", ".join(list(tech_data.keys())[:5])
                            f.write(f"Topics covered: {keys_preview}...\n\n")
                        elif isinstance(tech_data, list):
                            f.write(f"Items tracked: {len(tech_data)}\n\n")

                # TypeScript Ingested Knowledge (Flattened structure)
                ts_keys = [k for k in consolidated.keys() if k.startswith("System: ") or k.startswith("Intelephense: ")]
                if ts_keys:
                    f.write("\n## 5. TypeScript Ecosystem Intelligence\n")
                    for key in ts_keys:
                        ts_data = consolidated[key]
                        f.write(f"### {key}\n")
                        if isinstance(ts_data, dict):
                           f.write(f"*Source: {ts_data.get('metadata', {}).get('source', 'Unknown')}*\n\n")
                           for sec in ts_data.get("sections", []):
                               f.write(f"#### {sec['header']}\n{sec['content']}\n\n")

                # Ensure the signature is always present at the very end
                f.write("\n---\nAll the best - https://markposition.wordpress.com\n")

            self.logger.info(f"Consolidated Markdown saved to {self.output_md}")
        except Exception as e:
            self.logger.error(f"Failed to generate Markdown: {e}")

    async def review(self, blackboard: Blackboard) -> List[str]:
        suggestions = []
        if not os.path.exists(self.output_json):
            suggestions.append("Knowledge consolidation artifact is missing.")
        return suggestions
