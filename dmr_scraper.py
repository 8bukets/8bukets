import json
import os
import re

def scrape_dmr_docs():
    file_path = "docs/docker_model_runner.md"
    print(f"Reading {file_path}...")

    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by headings starting with ## or #
    # The regex looks for a newline followed by one or more # characters and a space.
    # It keeps the delimiter (the heading) to process it later.
    parts = re.split(r'\n(#{1,3}\s+.*?\n)', '\n' + content)

    # Reconstruct sections
    sections = []

    if len(parts) > 1 and parts[0].strip() == '':
        parts = parts[1:]

    current_title = "Local models with Docker Model Runner"
    current_content = []

    for i in range(0, len(parts), 2):
        heading_line = parts[i].strip()
        text_block = parts[i+1].strip() if i+1 < len(parts) else ""

        # Remove the leading '#'s from the heading to get the clean title
        match = re.match(r'^(#{1,3})\s+(.*)$', heading_line)
        if match:
            clean_title = match.group(2)
        else:
            clean_title = heading_line

        # If it's the very first part, it might be the top-level title
        sections.append({
            "title": clean_title,
            "content": text_block
        })

    # Output to flat JSON with a sections array at the root as per memory rules
    data = {
        "sections": sections
    }

    json_path = "dmr_docs.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Saved JSON data to {json_path}")

    # For the markdown, we can just copy the original file content
    # but the instructions asked the scraper to output `dmr_docs.md`
    # Let's reconstruct it from the sections.
    md_path = "dmr_docs.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Docker Model Runner Documentation\n\n")
        f.write(f"Generated from `{file_path}`\n\n")
        for section in sections:
            # We don't know the exact heading level, but we'll use H2
            f.write(f"## {section['title']}\n\n")
            if section['content']:
                f.write(f"{section['content']}\n\n")
        f.write("\n---\nAll the best - https://markposition.wordpress.com\n")
    print(f"Saved Markdown data to {md_path}")

if __name__ == "__main__":
    scrape_dmr_docs()
