import requests
from bs4 import BeautifulSoup
import json
import logging
import os

logger = logging.getLogger("GoogleAdsScraper")
logging.basicConfig(level=logging.INFO)

URLS = [
    "https://support.google.com/google-ads/answer/2459326?hl=en&ref_topic=10289453&sjid=5167206403107665975-EU",
    "https://business.google.com/uk/ad-tools/bidding/",
    "https://business.google.com/uk/resources/",
    "https://developers.google.com/ad-manager",
    "https://developers.google.com/ad-manager/dynamic-ad-insertion",
    "https://developers.google.com/ad-manager/dynamic-ad-insertion/full-service",
    "https://developers.google.com/ad-manager/dynamic-ad-insertion/pod-serving",
    "https://developers.google.com/ad-manager/api/start",
    "https://admanager.google.com/home/resources/",
    "https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/overview"
]

def scrape_google_ads_docs():
    data = {}
    md_content = "# Google Ads & Ad Manager Documentation\n\n"

    for url in URLS:
        logger.info(f"Fetching Google Ads docs from {url}...")
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            continue

        soup = BeautifulSoup(resp.content, "html.parser")
        main_content = soup.find("article") or soup.find("main") or soup.find("body")

        if not main_content:
            logger.warning(f"Could not find main content for {url}")
            continue

        headings = main_content.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])

        # Determine the page title
        h1 = main_content.find("h1")
        page_title = h1.get_text(strip=True) if h1 else url

        page_data = {
            "title": page_title,
            "url": url,
            "content": []
        }

        md_content += f"## {page_title}\n\n"
        md_content += f"Source: [{url}]({url})\n\n"

        extracted_text = []

        # Simple extraction logic: grab all text under headings, paragraphs, and list items
        # A more complex one would group by headings, but since the structure varies wildly
        # across support, business, developers, and cloud subdomains, we'll extract the main text.
        for elem in main_content.find_all(["h1", "h2", "h3", "p", "li"]):
            text = elem.get_text(separator=' ', strip=True)
            if not text:
                continue

            if elem.name in ["h1", "h2", "h3"]:
                md_prefix = "#" * int(elem.name[1])
                md_content += f"{md_prefix} {text}\n\n"
                extracted_text.append({"type": elem.name, "text": text})
            elif elem.name == "p":
                md_content += f"{text}\n\n"
                extracted_text.append({"type": "p", "text": text})
            elif elem.name == "li":
                md_content += f"- {text}\n"
                extracted_text.append({"type": "li", "text": text})

        page_data["content"] = extracted_text
        data[url] = page_data

        md_content += "\n---\n\n"

    json_path = "google_ads_docs.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    logger.info(f"Saved Google Ads docs JSON to {json_path}")

    md_path = "google_ads_docs.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    logger.info(f"Saved Google Ads docs Markdown to {md_path}")

    return True

if __name__ == "__main__":
    scrape_google_ads_docs()
