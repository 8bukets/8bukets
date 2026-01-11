import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys

# UX Visual Constants
EMOJI = {
    'STATS': '📊',
    'DOMAIN': '🌐',
    'CATEGORY': '🏷️',
    'DATE': '📅',
    'AUTHOR': '✍️',
    'TIME': '⏰',
    'CHECK': '✅'
}

def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

def get_domain(url):
    if not url:
        return None
    try:
        return urlparse(url).netloc.replace('www.', '')
    except:
        return None

def generate_report(data, output_file):
    total_posts = len(data)

    # 1. Domain Analysis
    domains = [get_domain(p.get('external_link')) for p in data if p.get('external_link')]
    domain_counts = Counter(domains).most_common(10)
    unique_domains = len(set(domains))

    # 2. Category Analysis
    all_categories = []
    for p in data:
        cats = p.get('categories', [])
        if cats:
            all_categories.extend(cats)
    category_counts = Counter(all_categories).most_common(10)

    # 3. Date Analysis
    dates = []
    for p in data:
        dt_str = p.get('datetime')
        if dt_str:
            try:
                # Handle ISO format
                dt = datetime.fromisoformat(dt_str)
                dates.append(dt)
            except ValueError:
                pass

    if dates:
        dates.sort()
        start_date = dates[0].strftime('%Y-%m-%d')
        end_date = dates[-1].strftime('%Y-%m-%d')
        years = [d.year for d in dates]
        year_counts = Counter(years).most_common()
        year_counts.sort(key=lambda x: x[0], reverse=True)
    else:
        start_date = "N/A"
        end_date = "N/A"
        year_counts = []

    # 4. Author Analysis
    authors = [p.get('author') for p in data if p.get('author')]
    author_counts = Counter(authors).most_common()

    # Generate Markdown
    md = []
    md.append("# Markposition Analytics Report")
    md.append(f"\n> Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Executive Summary
    md.append(f"\n## {EMOJI['STATS']} Executive Summary")
    md.append("| Metric | Value |")
    md.append("| :--- | :--- |")
    md.append(f"| {EMOJI['CHECK']} Total Posts | **{total_posts}** |")
    md.append(f"| {EMOJI['DATE']} Date Range | {start_date} to {end_date} |")
    md.append(f"| {EMOJI['DOMAIN']} Unique Domains | {unique_domains} |")
    md.append(f"| {EMOJI['AUTHOR']} Active Authors | {len(author_counts)} |")

    # Detailed Sections with Collapsible Details
    md.append(f"\n## {EMOJI['DOMAIN']} Top Referenced Domains")
    md.append("<details>")
    md.append("<summary>Click to view top 10 domains</summary>\n")
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in domain_counts:
        md.append(f"| {domain} | {count} |")
    md.append("</details>")

    md.append(f"\n## {EMOJI['CATEGORY']} Top Categories")
    md.append("<details>")
    md.append("<summary>Click to view top 10 categories</summary>\n")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in category_counts:
        md.append(f"| {cat} | {count} |")
    md.append("</details>")

    md.append(f"\n## {EMOJI['DATE']} Posting Activity by Year")
    md.append("<details>")
    md.append("<summary>Click to view yearly breakdown</summary>\n")
    md.append("| Year | Count |")
    md.append("| :--- | :---: |")
    for year, count in year_counts:
        md.append(f"| {year} | {count} |")
    md.append("</details>")

    md.append(f"\n## {EMOJI['AUTHOR']} Authors")
    md.append("<details>")
    md.append("<summary>Click to view author stats</summary>\n")
    for author, count in author_counts:
        md.append(f"- **{author}**: {count} posts")
    md.append("</details>")

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
