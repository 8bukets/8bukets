import requests
from bs4 import BeautifulSoup
import json
import os

def scrape_gemmafour_docs():
    url = "https://ai.google.dev/gemma/docs/core/model_card_4"
    print(f"Fetching {url}...")
    try:
        resp = requests.get(url)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return

    soup = BeautifulSoup(resp.content, "html.parser")

    # The main container for the content is typically the main article or div.
    # In this case, we can iterate over h2 tags directly.
    headings = soup.find_all("h2")
    data = {}

    for header in headings:
        section_id = header.get("id")
        # Ensure we have an ID for the key, else use lowercase title with hyphens
        if not section_id:
            section_id = header.get_text(strip=True).lower().replace(" ", "-")

        section_title = header.get_text(strip=True)
        content = []
        curr = header.find_next_sibling()

        # Stop when we hit the next h2
        while curr:
            if curr.name == "h2":
                break

            # Format the sub-elements nicely
            if curr.name == "pre":
                code = curr.get_text(strip=True)
                content.append(f"```\n{code}\n```")
            elif curr.name in ["h3", "h4"]:
                title = curr.get_text(strip=True)
                content.append(f"### {title}")
            elif curr.name == "ul":
                for li in curr.find_all("li", recursive=False):
                    content.append(f"- {li.get_text(strip=True)}")
            elif curr.name == "ol":
                for idx, li in enumerate(curr.find_all("li", recursive=False)):
                    content.append(f"{idx + 1}. {li.get_text(strip=True)}")
            elif curr.name == "table":
                # Very basic table extraction
                rows = []
                for tr in curr.find_all("tr"):
                    cells = [th_td.get_text(strip=True) for th_td in tr.find_all(["th", "td"])]
                    rows.append(" | ".join(cells))
                content.append("\n".join(rows))
            else:
                # p, div, etc.
                text = curr.get_text(separator=' ', strip=True)
                if text:
                    content.append(text)

            curr = curr.find_next_sibling()

        data[section_id] = {
            "title": section_title,
            "content": "\n\n".join(content)
        }

    # Save to JSON
    json_path = "gemmafour_docs.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Saved JSON data to {json_path}")

    # Save to Markdown
    md_path = "gemmafour_docs.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Gemma 4 Model Card\n\n")
        f.write(f"Scraped from [{url}]({url})\n\n")
        for section_id, section_data in data.items():
            f.write(f"## {section_data['title']}\n\n")
            f.write(f"{section_data['content']}\n\n")
        f.write("\n---\nAll the best - https://markposition.wordpress.com\n")
    print(f"Saved Markdown data to {md_path}")

if __name__ == "__main__":
    scrape_gemmafour_docs()
