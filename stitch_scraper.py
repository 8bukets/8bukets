import json
import os
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def scrape_stitch_docs():
    url = "https://stitch.withgoogle.com/docs/design-md/specification"
    print(f"Fetching {url} using Playwright...")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        # Give the outer page time to load and inject the iframes
        page.wait_for_timeout(5000)

        # The main content is inside nested iframes.
        # The ultimate content is at "https://app-companion-430619.appspot.com/docs/design-md/specification/index.html"
        target_frame = None
        for frame in page.frames:
            if frame.url.endswith("index.html"):
                target_frame = frame
                break

        if target_frame:
            html = target_frame.content()
        else:
            print("Could not find the target iframe. Trying to fetch the inner URL directly...")
            inner_url = "https://app-companion-430619.appspot.com/docs/design-md/specification/index.html"
            page.goto(inner_url)
            page.wait_for_timeout(5000)
            html = page.content()

        browser.close()

    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article") or soup.find("main") or soup.find(id="main-content")

    if not article:
        print("Error: Could not find main article content.")
        return

    data = {
        "title": "The DESIGN.md specification",
        "url": url,
        "content": {}
    }

    # We will process the article sequentially
    current_h2 = "Introduction"
    current_h3 = None

    # initialize the structure
    data["content"][current_h2] = {"text": [], "subsections": {}}

    for child in article.find_all(recursive=False):
        # some articles have an inner div containing the actual content
        if child.name == 'div':
            elements_to_process = child.find_all(recursive=False)
            if not elements_to_process:
                 elements_to_process = [child]
        else:
            elements_to_process = [child]

        # Instead of doing it this way, let's just flatten and iterate over all elements in the article

    # A better approach: iter over all descendants that are block-level
    current_h2 = "Introduction"
    current_h3 = None
    data["content"][current_h2] = {"text": [], "subsections": {}}

    # Actually, the content is mostly inside <div class="content"> or similar. Let's just find all headers and paragraphs
    # in source order.

    for el in article.descendants:
        if el.name in ['h1', 'h2', 'h3', 'p', 'pre', 'ul', 'ol', 'table'] and not el.find_parent(['pre', 'ul', 'ol', 'table']):
            if el.name == 'h1':
                # Skip the title since we already have it
                continue
            elif el.name == 'h2':
                # Extract text, remove any trailing link icons
                header_text = el.get_text(separator=' ', strip=True)
                # Some headers have a 'Section titled XXX' span for screen readers. Let's clean it up.
                header_text = header_text.replace(f"Section titled “{header_text}”", "").strip()
                if "Section titled" in header_text:
                    # More robust cleanup
                    header_text = header_text.split("Section titled")[0].strip()

                current_h2 = header_text
                current_h3 = None
                if current_h2 not in data["content"]:
                    data["content"][current_h2] = {"text": [], "subsections": {}}
            elif el.name == 'h3':
                header_text = el.get_text(separator=' ', strip=True)
                if "Section titled" in header_text:
                    header_text = header_text.split("Section titled")[0].strip()

                current_h3 = header_text
                if current_h3 not in data["content"][current_h2]["subsections"]:
                    data["content"][current_h2]["subsections"][current_h3] = []
            elif el.name in ['p']:
                text = el.get_text(separator=' ', strip=True)
                if text:
                    if current_h3:
                        data["content"][current_h2]["subsections"][current_h3].append(text)
                    else:
                        data["content"][current_h2]["text"].append(text)
            elif el.name == 'pre':
                # Preformatted code blocks. For <pre>, we just want the raw text inside, preserving newlines
                # However the DOM might have divs/spans inside. Let's extract text without adding newlines between every single inline element
                # Using separator='' but replacing block level tags like div with newlines, or just innerText
                # Playwright's page.evaluate is better but we are in bs4.
                # Let's extract the text recursively, inserting newlines for block elements
                def extract_text_preserve_lines(node):
                    if isinstance(node, str):
                        return node
                    res = []
                    for child in node.contents:
                        res.append(extract_text_preserve_lines(child))
                        if getattr(child, 'name', None) in ['div', 'p', 'br', 'li']:
                            res.append('\n')
                    return "".join(res)

                code = extract_text_preserve_lines(el).strip()
                # Clean up multiple newlines that might have been introduced
                code = "\n".join(line.strip() for line in code.splitlines() if line.strip())

                code_block = f"```\n{code}\n```"
                if current_h3:
                    data["content"][current_h2]["subsections"][current_h3].append(code_block)
                else:
                    data["content"][current_h2]["text"].append(code_block)
            elif el.name in ['ul', 'ol']:
                list_items = []
                for li in el.find_all('li', recursive=False):
                    li_text = li.get_text(separator=' ', strip=True)
                    if li_text:
                        list_items.append(f"- {li_text}")

                if list_items:
                    list_text = "\n".join(list_items)
                    if current_h3:
                        data["content"][current_h2]["subsections"][current_h3].append(list_text)
                    else:
                        data["content"][current_h2]["text"].append(list_text)

    # Save JSON
    json_path = "stitch_docs.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"Saved JSON data to {json_path}")

    # Save Markdown
    md_path = "stitch_docs.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"# {data['title']}\n\n")
        f.write(f"Scraped from [{data['url']}]({data['url']})\n\n")

        for h2, h2_content in data["content"].items():
            # Only write H2 if it has content or subsections
            has_content = bool(h2_content["text"]) or bool(h2_content["subsections"])
            if not has_content and h2 == "Introduction":
                continue

            if h2 != "Introduction":
                f.write(f"## {h2}\n\n")

            if h2_content["text"]:
                f.write("\n\n".join(h2_content["text"]) + "\n\n")

            for h3, h3_text_list in h2_content["subsections"].items():
                f.write(f"### {h3}\n\n")
                if h3_text_list:
                    f.write("\n\n".join(h3_text_list) + "\n\n")

    print(f"Saved Markdown data to {md_path}")

if __name__ == "__main__":
    scrape_stitch_docs()
