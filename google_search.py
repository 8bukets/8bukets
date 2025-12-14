import json
import csv
import sys
import logging
import argparse
import time
from typing import List, Dict
from playwright.sync_api import sync_playwright

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

def run_search(query: str, headless: bool = True) -> List[Dict[str, str]]:
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            viewport={'width': 1280, 'height': 800}
        )
        page = context.new_page()

        try:
            logger.info(f"Navigating to Google...")
            page.goto("https://www.google.com")

            # Handle cookie consent if it appears (common in EU/some regions)
            # Look for "Accept all" or "I agree" buttons
            # This selector is a best guess for the "Accept all" button (L2AGLb is common)
            try:
                accept_button = page.wait_for_selector('button#L2AGLb, div[role="button"]:has-text("Accept all"), div[role="button"]:has-text("I agree")', timeout=3000)
                if accept_button:
                    logger.info("Found cookie consent. Clicking Accept...")
                    accept_button.click()
            except Exception:
                # No consent popup or different structure
                pass

            # Perform search
            logger.info(f"Searching for: {query}")
            search_input = page.wait_for_selector('textarea[name="q"], input[name="q"]')
            search_input.fill(query)
            search_input.press("Enter")

            # Wait for results
            page.wait_for_selector('#search')

            # Parse results
            # Similar logic to BS4 but using Playwright
            # div.g is usually the container for search results
            result_divs = page.query_selector_all('div.g')

            logger.info(f"Found {len(result_divs)} potential result blocks.")

            for div in result_divs:
                item = {}

                # Title and Link
                link_element = div.query_selector('a')
                if link_element:
                    href = link_element.get_attribute('href')
                    if href and href.startswith('http') and 'google.com' not in href:
                        item['link'] = href

                        title_element = link_element.query_selector('h3')
                        if title_element:
                            item['title'] = title_element.inner_text()
                        else:
                            item['title'] = link_element.inner_text()

                # Snippet
                if 'link' in item:
                    # Generic snippet selectors
                    snippet_element = div.query_selector('div[style*="-webkit-line-clamp"]') or \
                                      div.query_selector('.VwiC3b') or \
                                      div.query_selector('.IsZvec')

                    if snippet_element:
                        item['snippet'] = snippet_element.inner_text()
                    else:
                        item['snippet'] = ""

                    results.append(item)

        except Exception as e:
            logger.error(f"Error during search: {e}")
            # Take a screenshot for debugging if needed
            # page.screenshot(path="error_screenshot.png")
        finally:
            browser.close()

    return results

def save_results(results: List[Dict[str, str]], output_prefix: str):
    if not results:
        logger.warning("No results to save.")
        return

    # JSON
    with open(f"{output_prefix}.json", 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    # CSV
    with open(f"{output_prefix}.csv", 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Link', 'Snippet'])
        for res in results:
            writer.writerow([
                res.get('title', ''),
                res.get('link', ''),
                res.get('snippet', '')
            ])

    logger.info(f"Saved {len(results)} results to {output_prefix}.json and {output_prefix}.csv")

def main():
    parser = argparse.ArgumentParser(description="Scrape Google Search results.")
    parser.add_argument("query", nargs="?", default="site:marketing1usa.wordpress.com", help="Search query")
    parser.add_argument("--output", default="google_results", help="Output file prefix")
    parser.add_argument("--headless", action="store_true", default=True, help="Run in headless mode")

    args = parser.parse_args()

    results = run_search(args.query, headless=args.headless)

    if results:
        for i, res in enumerate(results, 1):
            print(f"{i}. {res.get('title')} - {res.get('link')}")
        save_results(results, args.output)
    else:
        logger.info("No results found.")

if __name__ == "__main__":
    main()
