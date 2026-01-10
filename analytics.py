"""
Analytics module for Markposition.

Generates a Markdown report from scraped JSON data.
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
    """Extracts the domain from a URL."""
    if not url:
        return None
    try:
        return urlparse(url).netloc.replace('www.', '')
    except Exception: # pylint: disable=broad-exception-caught
        return None

def create_bar(count, total, length=20):
    """Generates a visual ASCII progress bar."""
    if total == 0:
        return ""
    filled_len = int(round(length * count / float(total)))
    progress_bar = '█' * filled_len + '░' * (length - filled_len)
    percent = round((count / total) * 100, 1)
    return f"`{progress_bar}` {percent}%"

def generate_report(data, output_file):
    """Generates the Markdown report."""
    total_posts = len(data)

    # 1. Domain Analysis
    domains = [get_domain(p.get('external_link')) for p in data if p.get('external_link')]
    domain_counts = Counter(domains).most_common(10)
    max_domain_count = domain_counts[0][1] if domain_counts else 0

    # 2. Category Analysis
    all_categories = []
    for p in data:
        cats = p.get('categories', [])
        if cats:
            all_categories.extend(cats)
    category_counts = Counter(all_categories).most_common(10)
    max_cat_count = category_counts[0][1] if category_counts else 0

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
        max_year_count = max(y[1] for y in year_counts) if year_counts else 0
    else:
        start_date = "N/A"
        end_date = "N/A"
        year_counts = []
        max_year_count = 0

    # 4. Author Analysis
    authors = [p.get('author') for p in data if p.get('author')]
    author_counts = Counter(authors).most_common()

    # Generate Markdown
    md = []
    md.append("# 📊 Markposition Analytics Report")
    md.append(f"\n_Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_")

    md.append("\n## 📈 Executive Summary")
    md.append("| Metric | Value |")
    md.append("| :--- | :--- |")
    md.append(f"| 📝 **Total Posts** | **{total_posts}** |")
    md.append(f"| 📅 **Date Range** | {start_date} to {end_date} |")
    md.append(f"| 🌐 **Unique Domains** | {len(set(domains))} |")
    md.append(f"| 👥 **Active Authors** | {len(author_counts)} |")

    md.append("\n## 🔗 Top 10 Referenced Domains")
    md.append("| Domain | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for domain, count in domain_counts:
        progress_bar = create_bar(count, max_domain_count)
        md.append(f"| {domain} | {count} | {progress_bar} |")

    md.append("\n## 🏷️ Top 10 Categories")
    md.append("| Category | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for cat, count in category_counts:
        progress_bar = create_bar(count, max_cat_count)
        md.append(f"| {cat} | {count} | {progress_bar} |")

    md.append("\n## 🗓️ Posts by Year")
    md.append("| Year | Count | Activity |")
    md.append("| :--- | :---: | :--- |")
    for year, count in year_counts:
        progress_bar = create_bar(count, max_year_count)
        md.append(f"| {year} | {count} | {progress_bar} |")

    md.append("\n## ✍️ Authors")
    if len(author_counts) > 5:
        md.append("<details>")
        md.append("<summary>Click to see all authors</summary>\n")
        for author, count in author_counts:
            md.append(f"- **{author}**: {count} posts")
        md.append("</details>")
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

    input_data = load_data(args.input)
    generate_report(input_data, args.output)
