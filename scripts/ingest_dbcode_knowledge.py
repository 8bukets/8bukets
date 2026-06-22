import os
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://dbcode.io/"
REPO_URL = "https://github.com/dbcodeio/public"

def ingest_dbcode_knowledge():
    print(f"🤖 [Ingest] Fetching DBCode knowledge from {URL}...")

    try:
        response = requests.get(URL, timeout=20)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        data = {}

        # Basic metadata
        title = soup.title.string.strip() if soup.title else "DBCode - SQL & Database Client for VS Code"

        # Extract features from the landing page
        for header in soup.find_all(['h2', 'h3']):
            section_title = header.get_text().strip()
            if not section_title:
                continue

            section_id = header.get('id') or section_title.lower().replace(' ', '-').replace('?', '').replace(',', '')

            # Get text until next header
            content_parts = []
            next_node = header.find_next_sibling()
            while next_node and next_node.name not in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                text = next_node.get_text().strip()
                if text:
                    content_parts.append(text)
                next_node = next_node.find_next_sibling()

            if content_parts:
                data[section_id] = {
                    "title": section_title,
                    "content": "\n\n".join(content_parts)
                }

        # Add knowledge from the provided prompt text (Manual Additions)
        manual_additions = {
            "overview": {
                "title": "Overview",
                "content": "DBCode is a modern database client for VS Code, Cursor, and Windsurf - with first-class Copilot and MCP integration. Browse schemas, edit data, visualize queries, and manage 50+ databases without leaving your editor. SQL Notebooks, auto-generated ER diagrams, and secure report sharing."
            },
            "supported-databases": {
                "title": "Supported Databases",
                "content": "PostgreSQL, MySQL, SQL Server, SQLite, Oracle, MongoDB, Redis, DuckDB, Snowflake, BigQuery, Databricks, ClickHouse, Cassandra, Elasticsearch, Neo4j, Firebase, DynamoDB, MariaDB, and 50+ more engines including warehouses, lakehouses, and file formats."
            },
            "key-features": {
                "title": "Key Features",
                "content": "- Data Viewing & Editing: VS Code database GUI - filter, sort, group, and edit data directly.\n- Copilot Integration: Natural language to SQL queries.\n- Entity Relationship Diagrams: Auto-generated from live schema. Export as PDF, HTML, or PNG.\n- Foreign Key Navigation: Navigate relationships without writing JOINs.\n- SQL Editor: Full editor with intellisense, autocomplete, and inline signature help.\n- Secure Report Sharing: Encrypted database report sharing.\n- Database Notebooks: SQL and Python cells in VS Code Notebooks with Jupyter kernel integration.\n- Execution Plans: Visualize EXPLAIN and ANALYZE output as interactive node graphs."
            },
            "pricing": {
                "title": "Pricing",
                "content": "Core features are free, forever. Some advanced features require a subscription."
            }
        }

        # Merge manual additions
        data.update(manual_additions)

        target_dir = "data/knowledge"
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        json_path = os.path.join(target_dir, "dbcode_knowledge.json")
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

        md_path = os.path.join(target_dir, "dbcode_knowledge.md")
        signature = f"All the best - {URL}"

        md_content = f"# {title}\n\nScraped from [{URL}]({URL}) and [{REPO_URL}]({REPO_URL})\n\n"
        for key, sec in data.items():
            md_content += f"## {sec['title']}\n\n{sec['content']}\n\n"

        md_content += f"---\n{signature}\n"

        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

        # Update system_knowledge.json
        system_knowledge_path = os.path.join(os.getcwd(), 'data/knowledge/system_knowledge.json')
        if os.path.exists(system_knowledge_path):
            try:
                with open(system_knowledge_path, 'r', encoding='utf-8') as f:
                    system_knowledge = json.load(f)

                if "ai_agents_structured" not in system_knowledge:
                    system_knowledge["ai_agents_structured"] = []

                # Remove existing entry for this URL to avoid duplication
                system_knowledge["ai_agents_structured"] = [
                    item for item in system_knowledge["ai_agents_structured"] if item.get("url") != URL
                ]

                new_entry = {
                    "url": URL,
                    "title": title,
                    "sections": [
                        {"header": sec["title"], "content": sec["content"].split('\n\n')}
                        for sec in data.values()
                    ]
                }

                system_knowledge["ai_agents_structured"].append(new_entry)

                with open(system_knowledge_path, 'w', encoding='utf-8') as f:
                    json.dump(system_knowledge, f, indent=4, ensure_ascii=False)
                print(f"✅ [Ingest] Integrated DBCode knowledge into system_knowledge.json")
            except Exception as e:
                print(f"❌ [Ingest] Failed to integrate with system_knowledge.json: {e}")

        print(f"Updated knowledge files successfully.")
        return True
    except Exception as e:
        print(f"Failed to ingest DBCode knowledge: {e}")
        return False

if __name__ == "__main__":
    ingest_dbcode_knowledge()
