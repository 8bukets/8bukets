import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_intelephense_docs():
    url = "https://intelephense.com/docs"
    print(f"Fetching {url}...")
    try:
        resp = requests.get(url)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return

    soup = BeautifulSoup(resp.content, "html.parser")

    sections_to_scrape = ["getting-started", "installation", "configuration", "best-practice", "type-system", "frameworks-and-libraries"]
    data = {}

    for section_id in sections_to_scrape:
        header = soup.find(id=section_id)
        if header:
            section_title = header.get_text(strip=True)
            content = []
            curr = header.find_next_sibling()

            # Continue until we hit another header that is a main section (h2 or h3 with id in our list)
            # Actually, to get all sub-sections of 'type-system', we shouldn't stop at just ANY h3.
            # We should only stop if we hit an h2, or an h3 that is in our sections_to_scrape list.
            while curr:
                if curr.name == "h2":
                    break
                if curr.name == "h3" and curr.get("id") in sections_to_scrape:
                    break

                # if it's a code block, format it nicely
                if curr.name == "pre":
                    code = curr.get_text(strip=True)
                    content.append(f"```php\n{code}\n```")
                elif curr.name in ["h3", "h4"]:
                    title = curr.get_text(strip=True)
                    content.append(f"### {title}")
                else:
                    text = curr.get_text(separator=' ', strip=True)
                    if text:
                        content.append(text)
                curr = curr.find_next_sibling()

            data[section_id] = {
                "title": section_title,
                "content": "\n\n".join(content)
            }
        else:
            print(f"Warning: Section '{section_id}' not found.")

    # Save to JSON
    json_path = "intelephense_docs.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Saved JSON data to {json_path}")

    # Save to Markdown
    md_path = "intelephense_docs.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Intelephense Documentation\n\n")
        f.write("Scraped from [https://intelephense.com/docs](https://intelephense.com/docs)\n\n")
        for section_id, section_data in data.items():
            f.write(f"## {section_data['title']}\n\n")
            f.write(f"{section_data['content']}\n\n")
    print(f"Saved Markdown data to {md_path}")

if __name__ == "__main__":
    scrape_intelephense_docs()
