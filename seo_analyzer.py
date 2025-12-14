import json
import logging
import sys
import argparse
from typing import List, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

INPUT_FILE = "gadgets.json"
REPORT_FILE = "seo_report.md"

def load_data(filepath: str) -> List[Dict]:
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        return []

def analyze_seo(posts: List[Dict]) -> str:
    report = "# SEO Analysis Report\n\n"
    report += f"**Total Posts Analyzed:** {len(posts)}\n\n"

    issues = {
        "short_title": [],
        "long_title": [],
        "missing_alt": [],
        "thin_content": [],
    }

    for post in posts:
        title = post.get('title', '')
        word_count = post.get('word_count', 0)
        image_alt = post.get('image_alt', '')

        # Title Check
        if len(title) < 30:
            issues["short_title"].append(f"- [{title}]({post.get('original_url')}) ({len(title)} chars)")
        elif len(title) > 60:
            issues["long_title"].append(f"- [{title}]({post.get('original_url')}) ({len(title)} chars)")

        # Alt Text Check
        if not image_alt or image_alt == "Missing Alt Text":
            issues["missing_alt"].append(f"- [{title}]({post.get('original_url')})")

        # Thin Content (Excerpt check)
        if word_count < 50: # Arbitrary for excerpt
            issues["thin_content"].append(f"- [{title}]({post.get('original_url')}) ({word_count} words)")

    report += "## Title Length Issues\n"
    report += "Titles should ideally be between 30 and 60 characters to display fully in search results.\n\n"

    if issues["short_title"]:
        report += f"### Too Short ({len(issues['short_title'])})\n"
        report += "\n".join(issues["short_title"][:10]) + "\n"
        if len(issues["short_title"]) > 10: report += f"... and {len(issues['short_title']) - 10} more.\n"

    if issues["long_title"]:
        report += f"\n### Too Long ({len(issues['long_title'])})\n"
        report += "\n".join(issues["long_title"][:10]) + "\n"
        if len(issues["long_title"]) > 10: report += f"... and {len(issues['long_title']) - 10} more.\n"

    report += "\n## Image Accessibility (Alt Text)\n"
    report += "Images should have descriptive alt text for SEO and accessibility.\n\n"
    if issues["missing_alt"]:
        report += f"**Missing Alt Text:** {len(issues['missing_alt'])}\n"
        report += "\n".join(issues["missing_alt"][:10]) + "\n"
        if len(issues["missing_alt"]) > 10: report += f"... and {len(issues['missing_alt']) - 10} more.\n"
    else:
        report += "All images have alt text! Great job.\n"

    report += "\n## Content Length (Excerpt)\n"
    report += "Thin content (under 50 words in excerpt) might indicate a lack of depth or description.\n\n"
    if issues["thin_content"]:
        report += f"**Thin Content:** {len(issues['thin_content'])}\n"
        report += "\n".join(issues["thin_content"][:10]) + "\n"
        if len(issues["thin_content"]) > 10: report += f"... and {len(issues['thin_content']) - 10} more.\n"
    else:
        report += "Content length looks good based on excerpts.\n"

    report += "\n## Recommendations\n"
    report += "1. **Optimize Titles**: Ensure titles are catchy and include relevant keywords (e.g., specific gadget names, 'Review', 'Best of').\n"
    report += "2. **Add Alt Text**: Describe images for search engines.\n"
    report += "3. **Expand Content**: Ensure each post has substantial text content, not just a link.\n"
    report += "4. **Backlinks**: Promote your content on social media and other tech forums to gain backlinks.\n"
    report += "5. **Speed**: Ensure the site loads quickly (check with PageSpeed Insights).\n"

    return report

def main():
    parser = argparse.ArgumentParser(description="Analyze SEO of scraped gadgets data")
    parser.add_argument("--input", type=str, default=INPUT_FILE, help="Input JSON file")
    parser.add_argument("--output", type=str, default=REPORT_FILE, help="Output Report file")

    args = parser.parse_args()

    data = load_data(args.input)
    if not data:
        logger.error("No data to analyze.")
        return

    report = analyze_seo(data)

    try:
        with open(args.output, 'w') as f:
            f.write(report)
        logger.info(f"SEO Report generated: {args.output}")
    except IOError as e:
        logger.error(f"Error saving report: {e}")

if __name__ == "__main__":
    main()
