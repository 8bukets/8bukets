import requests
import json
import os

def scrape_intelephense_docs():
    base_url = "https://raw.githubusercontent.com/bmewburn/intelephense-docs/master/"
    files_to_fetch = ["README.md", "gettingStarted.md", "installation.md", "features.md", "support.md"]

    data = {}

    for filename in files_to_fetch:
        url = f"{base_url}{filename}"
        print(f"Fetching {url}...")
        try:
            resp = requests.get(url)
            resp.raise_for_status()
            content = resp.text

            # Use filename (minus .md) as key
            section_id = filename.replace(".md", "")
            # Properly format the title
            title = section_id.replace("gettingStarted", "Getting Started").title()
            if section_id == "gettingStarted":
                title = "Getting Started"

            data[section_id] = {
                "title": title,
                "content": content
            }
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")

    # Save to JSON
    json_path = "intelephense_docs.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Saved JSON data to {json_path}")

    # Save to Markdown
    md_path = "intelephense_docs.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Intelephense Documentation (from GitHub)\n\n")
        f.write("Source: [bmewburn/intelephense-docs](https://github.com/bmewburn/intelephense-docs)\n\n")
        for section_id, section_data in data.items():
            f.write(f"## {section_data['title']}\n\n")
            f.write(f"{section_data['content']}\n\n")
            f.write("---\n\n")
        f.write("All the best - https://markposition.wordpress.com\n")
    print(f"Saved Markdown data to {md_path}")

if __name__ == "__main__":
    scrape_intelephense_docs()
