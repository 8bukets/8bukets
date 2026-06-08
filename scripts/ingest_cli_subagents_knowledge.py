import json
import os
import collections
from pathlib import Path

# Paths to update
JSON_PATHS = [
    "ai_agents_knowledge.json",
    "data/ai_agents_knowledge.json",
    "data/knowledge/ai_agents_knowledge.json"
]

MD_PATHS = [
    "ai_agents_knowledge.md",
    "data/knowledge/ai_agents_knowledge.md"
]

RAW_FILE = "data/raw_subagents_docs.md"

def read_raw_content(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
        return ""

def update_json_files(new_content):
    if not new_content:
        return

    import os
    for json_path in JSON_PATHS:
        if not os.path.exists(json_path):
            print(f"File {json_path} does not exist, skipping.")
            continue

        try:
            import subprocess
            import tempfile
            import os

            # Use tempfile to write the new content safely
            with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8', suffix=".md") as temp_content_file:
                temp_content_file.write(new_content)
                temp_content_path = temp_content_file.name

            node_script = f"""
const fs = require('fs');
const jsonPath = process.argv[2];
const mdPath = process.argv[3];
const data = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
const newContent = fs.readFileSync(mdPath, 'utf8');
data['gemini-cli-subagents'] = {{
    title: "Gemini CLI Subagents",
    content: newContent
}};
fs.writeFileSync(jsonPath, JSON.stringify(data, null, 4));
"""
            with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8', suffix=".js") as script_file:
                script_file.write(node_script)
                script_path = script_file.name

            subprocess.run(['node', script_path, json_path, temp_content_path], check=True)

            os.remove(script_path)
            os.remove(temp_content_path)
            print(f"Updated {json_path}")
        except Exception as e:
            print(f"Failed to update {json_path}: {e}")

def update_md_files(new_content):
    if not new_content:
        return

    for md_path in MD_PATHS:
        if not os.path.exists(md_path):
            print(f"File {md_path} does not exist, skipping.")
            continue

        try:
            with open(md_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Find the signature if it exists, so we can insert before it
            signature = "All the best - https://markposition.wordpress.com"
            new_section = f"\n\n## Gemini CLI Subagents\n\n{new_content}\n\n"

            if signature in content:
                # Remove all occurrences of the signature, trim, append new content, then re-add signature
                cleaned_content = content.replace(f"---{signature}", "").replace(f"---\n{signature}", "").replace(signature, "").strip()
                final_content = cleaned_content + new_section + f"---\n{signature}\n"
            else:
                final_content = content.strip() + new_section

            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(final_content)
            print(f"Updated {md_path}")
        except Exception as e:
            print(f"Failed to update {md_path}: {e}")

if __name__ == "__main__":
    print("Reading raw subagents docs...")
    raw_content = read_raw_content(RAW_FILE)

    if raw_content:
        print("Updating JSON files...")
        update_json_files(raw_content)

        print("Appending to Markdown files...")
        update_md_files(raw_content)

        print("Ingestion complete.")
    else:
        print("No content to ingest.")
