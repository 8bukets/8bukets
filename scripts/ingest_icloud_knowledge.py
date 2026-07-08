import os
import json
import shutil
import re
from datetime import datetime

def process_markdown(filepath):
    """Processes a markdown file into a structured JSON knowledge format."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)
    title = f"iCloud: {filename}"
    sections = []

    # Naive markdown parsing
    current_header = "Introduction"
    current_content = []

    for line in content.split('\n'):
        if line.startswith('#'):
            if current_content:
                sections.append({
                    "header": current_header,
                    "content": '\n'.join(current_content).strip()
                })
            current_header = line.lstrip('#').strip()
            current_content = []
        else:
            current_content.append(line)

    if current_content:
        sections.append({
            "header": current_header,
            "content": '\n'.join(current_content).strip()
        })

    return {
        "source": f"icloud://{filename}",
        "title": title,
        "description": f"Extracted from iCloud markdown file: {filename}",
        "analyzedAt": datetime.utcnow().isoformat() + "Z",
        "sections": sections
    }

def main():
    icloud_sim_path = os.path.join(os.getcwd(), 'scratch/icloud_sim')
    knowledge_dir = os.path.join(os.getcwd(), 'data/knowledge')

    if not os.path.exists(icloud_sim_path):
        print(f"ℹ️ [iCloud Ingest] Simulation path {icloud_sim_path} does not exist. Skipping.")
        return

    files = os.listdir(icloud_sim_path)
    ingested_count = 0

    for filename in files:
        filepath = os.path.join(icloud_sim_path, filename)
        if not os.path.isfile(filepath):
            continue

        target_filename = re.sub(r'\.(md|json)$', '_knowledge.json', filename)
        if not target_filename.endswith('_knowledge.json'):
            target_filename += '_knowledge.json'

        target_path = os.path.join(knowledge_dir, target_filename)

        try:
            if filename.endswith('.json'):
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # Standardize if needed
                if isinstance(data, dict) and 'sections' not in data:
                    data = {
                        "source": f"icloud://{filename}",
                        "title": data.get('title', f"iCloud: {filename}"),
                        "description": data.get('description', 'Extracted system knowledge from iCloud JSON'),
                        "analyzedAt": datetime.utcnow().isoformat() + "Z",
                        "sections": [{"header": "Content", "content": json.dumps(data, indent=2)}]
                    }

                with open(target_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2)

            elif filename.endswith('.md'):
                data = process_markdown(filepath)
                with open(target_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2)
            else:
                continue

            print(f"✅ [iCloud Ingest] Ingested {filename} -> {target_filename}")
            ingested_count += 1

        except Exception as e:
            print(f"❌ [iCloud Ingest] Failed to process {filename}: {e}")

    print(f"🚀 [iCloud Ingest] Successfully ingested {ingested_count} files.")

if __name__ == "__main__":
    main()
