"""
Module for analyzing Markposition scraped data and generating a Markdown report.
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
    """Extract domain from a URL."""
    if not url:
        return None
    try:
        return urlparse(url).netloc.replace('www.', '')
    except Exception: # pylint: disable=broad-except
        return None

def generate_report(posts_data, output_file):
    """Generate a Markdown report from the analyzed data."""
    total_posts = len(posts_data)

    # 1. Domain Analysis
    domains = [get_domain(p.get('external_link')) for p in posts_data if p.get('external_link')]
    domain_counts = Counter(domains).most_common(10)

    # 2. Category Analysis
    all_categories = []
    for p in posts_data:
        cats = p.get('categories', [])
        if cats:
            all_categories.extend(cats)
    category_counts = Counter(all_categories).most_common(10)

    # 3. Date Analysis
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
    else:
        start_date = "N/A"
        end_date = "N/A"
        year_counts = []

    # 4. Author Analysis
    authors = [p.get('author') for p in posts_data if p.get('author')]
    author_counts = Counter(authors).most_common()

    # Generate Markdown
    md_lines = []
    md_lines.append("# Markposition Analytics Report")
    md_lines.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    md_lines.append("\n## 📊 Executive Summary")
    md_lines.append("| Metric | Value |")
    md_lines.append("| :--- | :--- |")
    md_lines.append(f"| **Total Posts** | {total_posts} 📝 |")
    md_lines.append(f"| **Date Range** | {start_date} to {end_date} 📅 |")
    md_lines.append(f"| **Unique Domains** | {len(set(domains))} 🔗 |")
    if author_counts:
        top_author = author_counts[0][0]
        md_lines.append(f"| **Primary Author** | {top_author} ✍️ |")

    md_lines.append("\n<details>")
    md_lines.append("<summary><strong>🏆 Top 10 Referenced Domains</strong></summary>\n")
    md_lines.append("| Domain | Count |")
    md_lines.append("| :--- | :---: |")
    for domain, count in domain_counts:
        md_lines.append(f"| {domain} | {count} |")
    md_lines.append("</details>")

    md_lines.append("\n<details>")
    md_lines.append("<summary><strong>📂 Top 10 Categories</strong></summary>\n")
    md_lines.append("| Category | Count |")
    md_lines.append("| :--- | :---: |")
    for cat, count in category_counts:
        md_lines.append(f"| {cat} | {count} |")
    md_lines.append("</details>")

    md_lines.append("\n## 📈 Posts by Year")
    md_lines.append("| Year | Count | Distribution |")
    md_lines.append("| :--- | :---: | :--- |")
    max_count = max((c for _, c in year_counts), default=0)
    for year, count in year_counts:
        bar_len = int((count / max_count) * 20) if max_count else 0
        progress_bar = "█" * bar_len
        md_lines.append(f"| {year} | {count} | `{progress_bar}` |")

    md_lines.append("\n<details>")
    md_lines.append("<summary><strong>👥 Authors</strong></summary>\n")
    for author, count in author_counts:
        md_lines.append(f"- {author}: {count} posts")
    md_lines.append("</details>")

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
