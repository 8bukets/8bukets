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

    for json_path in JSON_PATHS:
        if not os.path.exists(json_path):
            print(f"File {json_path} does not exist, skipping.")
            continue

        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f, object_pairs_hook=collections.OrderedDict)

            data["gemini-cli-subagents"] = {
                "title": "Gemini CLI Subagents",
                "content": new_content
            }

            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, separators=(',', ': '))
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
