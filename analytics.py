"""
Analytics module for Markposition data.
Generates a Markdown report summarizing scraped data.
"""

import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys
import math

def load_data(filepath):
    """Loads data from a JSON file."""
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

def draw_bar(count, max_count, width=20):
    """Generates an ASCII bar chart."""
    if max_count == 0:
        return "░" * width
    fill_count = int(math.ceil((count / max_count) * width))
    fill_count = min(fill_count, width) # Cap at width
    return "█" * fill_count + "░" * (width - fill_count)

def get_date_stats(posts_data):
    """Extracts and calculates date statistics."""
    dates = []
    for p in posts_data:
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
        max_year_count = max(count for _, count in year_counts) if year_counts else 0
    else:
        start_date = "N/A"
        end_date = "N/A"
        year_counts = []
        max_year_count = 0

    return start_date, end_date, year_counts, max_year_count

def generate_report(posts_data, output_file): # pylint: disable=too-many-locals
    """Generates a Markdown analytics report."""
    total_posts = len(posts_data)

    # 1. Domain Analysis
    domains = [get_domain(p.get('external_link')) for p in posts_data if p.get('external_link')]
    domain_counts = Counter(domains).most_common(10)
    max_domain_count = domain_counts[0][1] if domain_counts else 0

    # 2. Category Analysis
    all_categories = []
    for p in posts_data:
        cats = p.get('categories', [])
        if cats:
            all_categories.extend(cats)
    category_counts = Counter(all_categories).most_common(10)

    # 3. Date Analysis
    start_date, end_date, year_counts, max_year_count = get_date_stats(posts_data)

    # 4. Author Analysis
    authors = [p.get('author') for p in posts_data if p.get('author')]
    author_counts = Counter(authors).most_common()

    # Generate Markdown
    md_lines = []
    md_lines.append("# Markposition Analytics Report")
    md_lines.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    md_lines.append("\n## General Statistics")
    md_lines.append(f"- **Total Posts:** {total_posts}")
    md_lines.append(f"- **Date Range:** {start_date} to {end_date}")
    md_lines.append(f"- **Unique Domains Linked:** {len(set(domains))}")

    md_lines.append("\n## Top 10 Referenced Domains")
    md_lines.append("| Domain | Count | Distribution |")
    md_lines.append("| :--- | :---: | :--- |")
    for domain, count in domain_counts:
        chart_bar = draw_bar(count, max_domain_count)
        md_lines.append(f"| {domain} | {count} | {chart_bar} |")

    md_lines.append("\n## Top 10 Categories")
    md_lines.append("| Category | Count |")
    md_lines.append("| :--- | :---: |")
    for cat, count in category_counts:
        md_lines.append(f"| {cat} | {count} |")

    md_lines.append("\n## Posts by Year")
    md_lines.append("| Year | Count | Distribution |")
    md_lines.append("| :--- | :---: | :--- |")
    for year, count in year_counts:
        chart_bar = draw_bar(count, max_year_count)
        md_lines.append(f"| {year} | {count} | {chart_bar} |")

    md_lines.append("\n## Authors")
    for author, count in author_counts:
        md_lines.append(f"- {author}: {count} posts")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_lines))

    print(f"Report generated: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
