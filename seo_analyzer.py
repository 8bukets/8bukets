import requests
from bs4 import BeautifulSoup
import logging
import sys
import json
import argparse
from urllib.parse import urljoin, urlparse
from typing import Dict, List, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

class SEOAnalyzer:
    def __init__(self, url: str):
        self.url = url
        self.soup = None
        self.report: Dict[str, Any] = {
            "url": url,
            "score": 100,
            "issues": [],
            "passed": []
        }

    def fetch_page(self) -> bool:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (compatible; SEOAnalyzer/1.0)'
            }
            response = requests.get(self.url, headers=headers, timeout=10)
            response.raise_for_status()
            self.soup = BeautifulSoup(response.text, 'html.parser')
            return True
        except requests.RequestException as e:
            logger.error(f"Failed to fetch {self.url}: {e}")
            self.report["issues"].append({"severity": "critical", "message": f"Could not access site: {e}"})
            self.report["score"] = 0
            return False

    def analyze_title(self):
        title = self.soup.find('title')
        if not title:
            self._add_issue("high", "Missing <title> tag.")
        else:
            text = title.get_text(strip=True)
            length = len(text)
            if length < 10:
                self._add_issue("medium", f"Title is too short ({length} chars). Aim for 50-60 characters.")
            elif length > 60:
                self._add_issue("medium", f"Title is too long ({length} chars). Google may truncate it.")
            else:
                self._add_pass(f"Title length is optimal ({length} chars): '{text}'")

    def analyze_meta_description(self):
        meta_desc = self.soup.find('meta', attrs={'name': 'description'})
        if not meta_desc:
            self._add_issue("high", "Missing meta description. This is crucial for CTR on search results.")
        else:
            content = meta_desc.get('content', '').strip()
            length = len(content)
            if length < 50:
                self._add_issue("medium", f"Meta description is too short ({length} chars). Aim for 150-160.")
            elif length > 160:
                self._add_issue("medium", f"Meta description is too long ({length} chars). It may be truncated.")
            else:
                self._add_pass(f"Meta description length is optimal ({length} chars).")

    def analyze_headings(self):
        h1s = self.soup.find_all('h1')
        if not h1s:
            self._add_issue("high", "Missing <h1> tag. Every page should have exactly one H1.")
        elif len(h1s) > 1:
            self._add_issue("medium", f"Found {len(h1s)} <h1> tags. Best practice is one per page.")
        else:
            self._add_pass("H1 tag usage is correct.")

        # Check hierarchy
        headings = self.soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        if not headings:
            self._add_issue("low", "No headings found. Structure your content with headers.")

    def analyze_images(self):
        images = self.soup.find_all('img')
        missing_alt = 0
        for img in images:
            if not img.get('alt'):
                missing_alt += 1

        if missing_alt > 0:
            self._add_issue("medium", f"Found {missing_alt} images missing 'alt' text. specific alt text helps image search ranking.")
        elif images:
            self._add_pass(f"All {len(images)} images have alt text.")

    def analyze_links(self):
        links = self.soup.find_all('a', href=True)
        # Basic check for link text
        generic_text = ['click here', 'read more', 'more', 'here']
        poor_links = 0
        for link in links:
            text = link.get_text(strip=True).lower()
            if text in generic_text:
                poor_links += 1

        if poor_links > 0:
            self._add_issue("low", f"Found {poor_links} links with generic text (e.g., 'click here'). Use descriptive anchor text.")

    def _add_issue(self, severity: str, message: str):
        weight = {"critical": 30, "high": 20, "medium": 10, "low": 5}
        self.report["issues"].append({"severity": severity, "message": message})
        self.report["score"] = max(0, self.report["score"] - weight.get(severity, 5))

    def _add_pass(self, message: str):
        self.report["passed"].append(message)

    def run(self):
        if self.fetch_page():
            logger.info(f"Analyzing {self.url}...")
            self.analyze_title()
            self.analyze_meta_description()
            self.analyze_headings()
            self.analyze_images()
            self.analyze_links()

        return self.report

def save_report(report: Dict, filename: str):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4, ensure_ascii=False)
    logger.info(f"Report saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Analyze a webpage for SEO best practices.")
    parser.add_argument("url", nargs="?", default="https://marketing1usa.wordpress.com/", help="URL to analyze")
    parser.add_argument("--output", default="seo_report.json", help="Output file path")

    args = parser.parse_args()

    analyzer = SEOAnalyzer(args.url)
    report = analyzer.run()

    save_report(report, args.output)

    print("\n--- SEO Report Summary ---")
    print(f"Score: {report['score']}/100")
    print("\nIssues:")
    for issue in report['issues']:
        print(f"[{issue['severity'].upper()}] {issue['message']}")
    print("\nGood Practices:")
    for passed in report['passed']:
        print(f"[OK] {passed}")

if __name__ == "__main__":
    main()
