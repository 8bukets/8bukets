import requests
from bs4 import BeautifulSoup
import json
import logging

logger = logging.getLogger("AIKnowledgeScraper")

def scrape_ai_agents_knowledge():
    url = "https://cloud.google.com/discover/what-are-ai-agents"
    logger.info(f"Fetching AI Agent knowledge from {url}...")
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"Error fetching AI Agent knowledge: {e}")
        return False

    soup = BeautifulSoup(resp.content, "html.parser")

    # Capture all relevant headings as section markers
    # Including h1, h2, h3 to get more granular and complete sections (like Benefits and Use Cases)
    headings = soup.find_all(["h1", "h2", "h3", "h4"])
    all_tags = soup.find_all(True)
    data = {}

    for i, header in enumerate(headings):
        section_title = header.get_text(strip=True)
        # Break when we hit the footer navigation or additional resources sections
        if section_title in ["Additional resources", "Take the next step", "Accelerate your digital transformation", "Why Google", "Products and pricing", "Solutions", "Resources", "Engage"]:
            break

        section_id = header.get("id")
        if not section_id:
            section_id = section_title.lower().replace(" ", "-").replace("?", "")

        next_header = headings[i+1] if i+1 < len(headings) else None

        try:
            start_idx = all_tags.index(header)
            end_idx = all_tags.index(next_header) if next_header else len(all_tags)
        except ValueError:
            continue

        section_content = []
        processed_tags = set()

        for j in range(start_idx + 1, end_idx):
            tag = all_tags[j]
            if tag in processed_tags:
                continue

            # Sub-headings within a section (h4)
            if tag.name == "h4":
                section_content.append(f"### {tag.get_text(strip=True)}")
            # Content tags
            elif tag.name in ["p", "li", "table", "pre", "h5", "h6"]:
                if tag.name == "table":
                    rows = []
                    header_count = 0
                    for k, tr in enumerate(tag.find_all("tr")):
                        cells = [th_td.get_text(separator=" ", strip=True) for th_td in tr.find_all(["th", "td"])]
                        if not any(cells): continue # Skip empty rows
                        rows.append(" | ".join(cells))
                        if k == 0 or header_count == 0:
                            header_count = len(cells)

                    if rows and header_count > 1:
                        # Add Markdown table separator
                        separator = " | ".join(["---"] * header_count)
                        rows.insert(1, separator)

                    section_content.append("\n".join(rows))
                elif tag.name == "pre":
                    section_content.append(f"```\n{tag.get_text(strip=True)}\n```")
                elif tag.name == "li":
                    # Use separator to avoid text concatenation
                    text = tag.get_text(separator=" ", strip=True)
                    section_content.append(f"- {text}")
                else:
                    text = tag.get_text(separator=' ', strip=True)
                    if text:
                        section_content.append(text)

                # Mark all descendants as processed to avoid duplicates
                for descendant in tag.find_all(True):
                    processed_tags.add(descendant)

        if section_content:
            data[section_id] = {
                "title": section_title,
                "content": "\n\n".join(section_content)
            }

    data["compile-definition"] = {
        "title": "What does Compile mean?",
        "content": "To compile means to gather information from various sources and arrange it into a structured format, such as a report, list, book, or file. In computing, it refers to translating human-readable source code into machine-readable, executable instructions.\n\n### Key Definitions of Compile\n\n- **Gathering Information**: To collect and put together data, facts, or documents (e.g., to compile a report or compile a list).\n- **Creating Works**: To produce a book, anthology, or database from various materials.\n- **Computing**: To convert high-level programming code (like C++ or Java) into machine code, allowing a computer to execute the program.\n\n### Usage Examples\n\n- \"She is compiling a list of clients for the newsletter.\"\n- \"It took years to compile the dictionary.\"\n- \"The developer needs to compile the code before running the application.\"\n\n### Synonyms\n\nAssemble, Collect, Gather, Compose, Accumulate, Organize, Synthesize\n\n### Contextual Usage\n\n- **General**: Focuses on the act of assembling information or materials (e.g., compile a report).\n- **Computing**: Focuses on the automatic transformation of code using a tool known as a compiler."
    }

    # Save to JSON
    json_path = "ai_agents_knowledge.json"
    try:
        # Merge with existing data to ensure cumulative knowledge integration
        if os.path.exists(json_path):
            try:
                with open(json_path, "r", encoding="utf-8") as f:
                    existing_data = json.load(f)
                # Update existing with new, but keep what's not in new
                existing_data.update(data)
                data = existing_data
            except Exception as e:
                logger.warning(f"Failed to load existing knowledge for merging: {e}")

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        logger.info(f"Saved merged AI Agent knowledge to {json_path}")

        # Save to Markdown for documentation reference
        md_path = "ai_agents_knowledge.md"
        with open(md_path, "w", encoding="utf-8") as f:
            f.write("# What are AI Agents?\n\n")
            f.write(f"Scraped from [{url}]({url})\n\n")
            for section_id, section_data in data.items():
                f.write(f"## {section_data['title']}\n\n")
                f.write(f"{section_data['content']}\n\n")
        return True
    except Exception as e:
        logger.error(f"Failed to save AI Agent knowledge files: {e}")
        return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    scrape_ai_agents_knowledge()
