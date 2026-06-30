import os
import json
import re
from datetime import datetime

class KnowledgeIngestor:
    def __init__(self, storage_dir=None):
        self.storage_dir = storage_dir or os.path.join(os.getcwd(), 'data/knowledge')
        self.json_path = os.path.join(self.storage_dir, 'system_knowledge.json')

    def process_content(self, title, content, source):
        sections = []
        lines = content.split('\n')
        current_section = None

        for line in lines:
            header_match = re.match(r'^(#+)\s*(.*)', line)
            if header_match:
                if current_section:
                    sections.append(current_section)
                current_section = {"header": header_match.group(0).strip(), "content": ""}
            elif current_section:
                current_section["content"] += (current_section["content"] + "\n" if current_section["content"] else "") + line.strip()

        if current_section:
            sections.append(current_section)

        # Filter empty sections
        sections = [s for s in sections if s["content"].strip()]

        return {
            "title": title,
            "metadata": {
                "source": source,
                "analyzedAt": datetime.utcnow().isoformat() + "Z",
                "description": "Extracted system knowledge (Python Ingestor)"
            },
            "sections": sections
        }

    def persist(self, new_section):
        if not os.path.exists(self.json_path):
            data = {"typescript_sections": []}
        else:
            with open(self.json_path, 'r') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = {"typescript_sections": []}

        if "typescript_sections" not in data:
            data["typescript_sections"] = []

        # Deduplicate
        updated = False
        for i, section in enumerate(data["typescript_sections"]):
            if section.get("title") == new_section["title"]:
                data["typescript_sections"][i] = new_section
                updated = True
                break

        if not updated:
            data["typescript_sections"].append(new_section)

        with open(self.json_path, 'w') as f:
            json.dump(data, f, indent=4)

        print(f"✅ Integrated '{new_section['title']}' into {self.json_path}")

def main():
    ingestor = KnowledgeIngestor()

    files_to_ingest = [
        ('Chief AI Officer (CAIO) Role', 'caio_user_input.md'),
        ('Chief AI Officer (CAIO) Market Intelligence', 'caio_market_intelligence_2026.md'),
        ('Chief AI Officer (CAIO) Executive Intelligence 2026', 'caio_executive_intelligence_2026.md')
    ]

    for title, filename in files_to_ingest:
        filepath = os.path.join(ingestor.storage_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                content = f.read()
                source = f"user_input://{filename}"
                section = ingestor.process_content(title, content, source)
                ingestor.persist(section)
        else:
            print(f"⚠️ File not found: {filepath}")

if __name__ == "__main__":
    main()
