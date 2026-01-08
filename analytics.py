"""
Analytics module for processing scraped WordPress blog data.
Generates a Markdown report with key statistics and insights.
"""
import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys

def load_data(filepath):
    """Load JSON data from the specified file path."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

def get_domain(url):
    """Extract the domain name from a URL."""
    if not url:
        return None
    try:
        return urlparse(url).netloc.replace('www.', '')
    except (ValueError, AttributeError):
        return None

def generate_report(report_data, output_file):
    """Generate a Markdown analytics report from the data."""
    total_posts = len(report_data)

    # 1. Domain Analysis
    domains = [
        get_domain(p.get('external_link'))
        for p in report_data
        if p.get('external_link')
    ]
    domain_counts = Counter(domains).most_common(10)

    # 2. Category Analysis
    all_categories = []
    for p in report_data:
        cats = p.get('categories', [])
        if cats:
            all_categories.extend(cats)
    category_counts = Counter(all_categories).most_common(10)

    # 3. Date Analysis
    dates = []
    for p in report_data:
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
    authors = [p.get('author') for p in report_data if p.get('author')]
    author_counts = Counter(authors).most_common()

    # Generate Markdown
    md = []
    md.append("# 📊 Wordpress Blog Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Executive Summary
    md.append("\n## 🚀 Executive Summary")
    md.append("| Metric | Value |")
    md.append("| :--- | :--- |")
    md.append(f"| **Total Posts** | {total_posts} |")
    md.append(f"| **Date Range** | {start_date} to {end_date} |")
    md.append(f"| **Unique Domains** | {len(set(domains))} |")
    md.append(f"| **Top Domain** | {domain_counts[0][0] if domain_counts else 'N/A'} |")
    md.append(f"| **Top Category** | {category_counts[0][0] if category_counts else 'N/A'} |")

    md.append("\n## 🌐 Top 10 Referenced Domains")
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in domain_counts:
        md.append(f"| {domain} | {count} |")

    md.append("\n## 🏷️ Top 10 Categories")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in category_counts:
        md.append(f"| {cat} | {count} |")

    md.append("\n## 📅 Posts by Year")
    md.append("<details>")
    md.append("<summary>Click to view posts by year</summary>\n")
    md.append("| Year | Count |")
    md.append("| :--- | :---: |")
    for year, count in year_counts:
        md.append(f"| {year} | {count} |")
    md.append("\n</details>")

    md.append("\n## ✍️ Authors")
    md.append("<details>")
    md.append(f"<summary>View all {len(author_counts)} authors</summary>\n")
    for author, count in author_counts:
        md.append(f"- {author}: {count} posts")
    md.append("\n</details>")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    print(f"✨ Report successfully generated: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate analytics report for WordPress blog data"
    )
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data_payload = load_data(args.input)
    generate_report(data_payload, args.output)
