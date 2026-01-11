"""
Analytics module for generating Markposition reports.
Parses JSON data and generates a Markdown report with visual statistics.
"""

import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys

def load_data(filepath):
    """Loads JSON data from the specified filepath."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

def get_domain(url):
    """Extracts the domain from a URL, removing 'www.'."""
    if not url:
        return None
    try:
        return urlparse(url).netloc.replace('www.', '')
    except Exception: # pylint: disable=broad-except
        return None

def draw_ascii_bar(count, max_count, width=20):
    """Generates an ASCII bar chart string."""
    if max_count == 0:
        return "░" * width
    filled = int((count / max_count) * width)
    empty = width - filled
    return "█" * filled + "░" * empty

def generate_report(report_data, output_file):
    """Generates a Markdown report from the provided data."""
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
        dt_str = p.get('datetime') or p.get('date') # Handle both keys if present
        if dt_str:
            try:
                # Handle ISO format
                if 'T' in dt_str:
                    dt = datetime.fromisoformat(dt_str)
                else:
                    dt = datetime.strptime(dt_str, '%Y-%m-%d')
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
    md.append("# 🎨 Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Executive Summary
    md.append("\n## 📋 Executive Summary")
    md.append("| Metric | Value | Status |")
    md.append("| :--- | :--- | :---: |")
    md.append(f"| Total Posts | **{total_posts}** | 📝 |")
    md.append(f"| Unique Domains | **{len(set(domains))}** | 🌐 |")
    md.append(f"| Date Range | {start_date} to {end_date} | 📅 |")
    md.append(f"| Active Authors | {len(author_counts)} | 👥 |")

    # Top Domains
    md.append("\n## 🌐 Top 10 Referenced Domains")
    md.append("| Domain | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    max_domain_count = domain_counts[0][1] if domain_counts else 0
    for domain, count in domain_counts:
        ascii_bar = draw_ascii_bar(count, max_domain_count)
        md.append(f"| {domain} | {count} | `{ascii_bar}` |")

    # Categories
    md.append("\n## 📂 Top 10 Categories")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in category_counts:
        md.append(f"| {cat} | {count} |")

    # Posts by Year
    md.append("\n## 📅 Posts by Year")
    md.append("| Year | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    max_year_count = max((c for y, c in year_counts), default=0) if year_counts else 0
    for year, count in year_counts:
        ascii_bar = draw_ascii_bar(count, max_year_count)
        md.append(f"| {year} | {count} | `{ascii_bar}` |")

    # Authors
    md.append("\n## 👥 Authors")
    if len(author_counts) > 10:
        md.append(f"<details><summary>View all {len(author_counts)} authors</summary>\n")
        md.append("| Author | Posts |")
        md.append("| :--- | :---: |")
        for author, count in author_counts:
            md.append(f"| {author} | {count} |")
        md.append("\n</details>")
    else:
        for author, count in author_counts:
            md.append(f"- **{author}**: {count} posts")

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
