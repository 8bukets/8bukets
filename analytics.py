"""
Analytics module for Markposition scraper.
Generates a Markdown report from JSON data.
"""

import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import math
import sys

def load_data(filepath):
    """Loads JSON data from the specified file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

def get_domain(url):
    """Extracts the domain from a URL."""
    if not url:
        return None
    try:
        return urlparse(url).netloc.replace('www.', '')
    except Exception: # pylint: disable=broad-except
        return None

def create_bar_chart(value, max_value, max_width=20):
    """Creates an ASCII bar chart string."""
    if max_value == 0:
        return ""
    width = math.ceil((value / max_value) * max_width)
    return "█" * width + "░" * (max_width - width)

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
    md_lines = []
    md_lines.append("# 📊 Markposition Analytics Report")
    md_lines.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    md_lines.append("\n## 📈 General Statistics")
    md_lines.append(f"- **Total Posts:** {total_posts}")
    md_lines.append(f"- **Date Range:** {start_date} to {end_date}")
    md_lines.append(f"- **Unique Domains Linked:** {len(set(domains))}")

    md_lines.append("\n## 🌐 Top 10 Referenced Domains")
    md_lines.append("| Domain | Count | Distribution |")
    md_lines.append("| :--- | :---: | :--- |")

    max_domain_count = max((c for _, c in domain_counts), default=0)
    for domain, count in domain_counts:
        bar_chart = create_bar_chart(count, max_domain_count)
        md_lines.append(f"| {domain} | {count} | {bar_chart} |")

    md_lines.append("\n## 📂 Top 10 Categories")
    md_lines.append("| Category | Count | Distribution |")
    md_lines.append("| :--- | :---: | :--- |")

    max_cat_count = max((c for _, c in category_counts), default=0)
    for cat, count in category_counts:
        bar_chart = create_bar_chart(count, max_cat_count)
        md_lines.append(f"| {cat} | {count} | {bar_chart} |")

    md_lines.append("\n## 📅 Posts by Year")
    md_lines.append("| Year | Count | Distribution |")
    md_lines.append("| :--- | :---: | :--- |")

    max_year_count = max((c for _, c in year_counts), default=0)
    for year, count in year_counts:
        bar_chart = create_bar_chart(count, max_year_count)
        md_lines.append(f"| {year} | {count} | {bar_chart} |")

    md_lines.append("\n## ✍️ Authors")
    for author, count in author_counts:
        md_lines.append(f"- {author}: {count} posts")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))

    print(f"Report generated: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    cli_args = parser.parse_args()

    loaded_data = load_data(cli_args.input)
    generate_report(loaded_data, cli_args.output)
