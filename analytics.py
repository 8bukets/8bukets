"""
Analytics module for Markposition.

Generates a Markdown report summarizing scraped data, including
statistics on posts, domains, categories, and authors.
"""

import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys
import math

def load_data(filepath):
    """Load JSON data from a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

def get_domain(url):
    """Extract the domain from a URL."""
    if not url:
        return None
    try:
        return urlparse(url).netloc.replace('www.', '')
    except Exception: # pylint: disable=broad-except
        return None

def generate_bar_chart(value, max_value, length=20):
    """Generate an ASCII bar chart for a given value."""
    if max_value == 0:
        return "░" * length

    # Calculate ratio
    ratio = value / max_value
    filled_length = math.ceil(ratio * length)

    bar_chars = "█" * filled_length
    empty = "░" * (length - filled_length)
    return f"{bar_chars}{empty}"

def generate_report(report_data, output_file):
    """Generate a Markdown report from the provided data."""
    total_posts = len(report_data)

    # Initialize counters and trackers
    domain_counts = Counter()
    category_counts = Counter()
    author_counts = Counter()
    year_counts = Counter()

    min_date = None
    max_date = None

    unique_domains = set()

    # Single pass iteration
    for p in report_data:
        # 1. Domain Analysis
        external_link = p.get('external_link')
        if external_link:
            domain = get_domain(external_link)
            domain_counts[domain] += 1
            unique_domains.add(domain)

        # 2. Category Analysis
        cats = p.get('categories', [])
        if cats:
            category_counts.update(cats)

        # 3. Date Analysis
        dt_str = p.get('datetime')
        if dt_str:
            try:
                # Handle ISO format
                dt = datetime.fromisoformat(dt_str)

                # Track min/max dates
                if min_date is None or dt < min_date:
                    min_date = dt
                if max_date is None or dt > max_date:
                    max_date = dt

                # Track year
                year_counts[dt.year] += 1
            except ValueError:
                pass

        # 4. Author Analysis
        author = p.get('author')
        if author:
            author_counts[author] += 1

    # Prepare data for report

    # Domains: top 10 by count
    top_domains = domain_counts.most_common(10)
    max_domain_count = top_domains[0][1] if top_domains else 0

    # Categories: top 10 by count
    top_categories = category_counts.most_common(10)
    max_category_count = top_categories[0][1] if top_categories else 0

    # Dates: range and years sorted by year descending
    if min_date and max_date:
        start_date = min_date.strftime('%Y-%m-%d')
        end_date = max_date.strftime('%Y-%m-%d')
        # Sort years descending (key is year)
        sorted_years = sorted(year_counts.items(), key=lambda x: x[0], reverse=True)
        max_year_count = max(year_counts.values()) if year_counts else 0
    else:
        start_date = "N/A"
        end_date = "N/A"
        sorted_years = []
        max_year_count = 0

    # Authors: all by count descending (most_common does this)
    sorted_authors = author_counts.most_common()

    # Generate Markdown
    md = []
    md.append("# 📊 Markposition Analytics Report")
    md.append(f"\n_Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_")

    md.append("\n## 📈 Executive Summary")
    md.append("| Metric | Value |")
    md.append("| :--- | :--- |")
    md.append(f"| **Total Posts** | {total_posts} |")
    md.append(f"| **Date Range** | {start_date} to {end_date} |")
    md.append(f"| **Unique Domains** | {len(unique_domains)} |")
    md.append(f"| **Active Authors** | {len(author_counts)} |")

    md.append("\n## 🌐 Top 10 Referenced Domains")
    md.append("| Domain | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for domain, count in top_domains:
        chart = generate_bar_chart(count, max_domain_count)
        md.append(f"| {domain} | {count} | `{chart}` |")

    md.append("\n## 🏷️ Top 10 Categories")
    md.append("| Category | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for cat, count in top_categories:
        chart = generate_bar_chart(count, max_category_count)
        md.append(f"| {cat} | {count} | `{chart}` |")

    md.append("\n## 📅 Posts by Year")
    md.append("| Year | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for year, count in sorted_years:
        chart = generate_bar_chart(count, max_year_count)
        md.append(f"| {year} | {count} | `{chart}` |")

    md.append("\n## ✍️ Authors")
    if len(sorted_authors) > 5:
        md.append("<details>")
        md.append(f"<summary>View all {len(sorted_authors)} authors</summary>\n")
        md.append("| Author | Posts |")
        md.append("| :--- | :---: |")
        for author, count in sorted_authors:
            md.append(f"| {author} | {count} |")
        md.append("\n</details>")
    else:
        md.append("| Author | Posts |")
        md.append("| :--- | :---: |")
        for author, count in sorted_authors:
            md.append(f"| {author} | {count} |")

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
