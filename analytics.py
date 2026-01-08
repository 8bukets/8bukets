"""
Module for generating analytics reports from scraped data.
"""
import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys

def load_data(filepath):
    """Load JSON data from a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

def get_domain(url):
    """Extract domain from URL."""
    if not url:
        return None
    try:
        return urlparse(url).netloc.replace('www.', '')
    except Exception: # pylint: disable=broad-except
        return None

def generate_report(posts_data, output_file):
    """Generate a Markdown report from data."""
    total_posts = len(posts_data)

    # Single pass aggregation
    domain_counter = Counter()
    category_counter = Counter()
    year_counter = Counter()
    author_counter = Counter()

    dates = []

    for p in posts_data:
        # 1. Domain
        ext_link = p.get('external_link')
        if ext_link:
            d = get_domain(ext_link)
            if d:
                domain_counter[d] += 1

        # 2. Category
        cats = p.get('categories')
        if cats:
            for cat in cats:
                category_counter[cat] += 1

        # 3. Date
        dt_str = p.get('datetime')
        if dt_str:
            try:
                dt = datetime.fromisoformat(dt_str)
                dates.append(dt)
                year_counter[dt.year] += 1
            except ValueError:
                pass

        # 4. Author
        a = p.get('author')
        if a:
            author_counter[a] += 1

    domain_counts = domain_counter.most_common(10)
    category_counts = category_counter.most_common(10)

    if dates:
        dates.sort()
        start_date = dates[0].strftime('%Y-%m-%d')
        end_date = dates[-1].strftime('%Y-%m-%d')
    else:
        start_date = "N/A"
        end_date = "N/A"

    year_counts = year_counter.most_common()
    year_counts.sort(key=lambda x: x[0], reverse=True)

    author_counts = author_counter.most_common()

    # Generate Markdown
    md = []
    md.append("# Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    md.append("\n## General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(domain_counter)}")

    md.append("\n## Top 10 Referenced Domains")
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in domain_counts:
        md.append(f"| {domain} | {count} |")

    md.append("\n## Top 10 Categories")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in category_counts:
        md.append(f"| {cat} | {count} |")

    md.append("\n## Posts by Year")
    md.append("| Year | Count |")
    md.append("| :--- | :---: |")
    for year, count in year_counts:
        md.append(f"| {year} | {count} |")

    md.append("\n## Authors")
    for author, count in author_counts:
        md.append(f"- {author}: {count} posts")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    print(f"Report generated: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
