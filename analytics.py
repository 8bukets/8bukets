"""
Analytics module for Markposition data.
Generates a Markdown report with statistics and visualizations.
"""
import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys

def load_data(filepath):
    """Load JSON data from file."""
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

def draw_bar(count, max_count, width=15):
    """Generate an ASCII bar chart."""
    if max_count == 0:
        return ""
    filled = int((count / max_count) * width)
    return "█" * filled + "░" * (width - filled)

def generate_report(posts_data, output_file):
    """Generate a Markdown report from posts data."""
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
        start_date, end_date = "N/A", "N/A"
        year_counts = []

    # 4. Author Analysis
    authors = [p.get('author') for p in posts_data if p.get('author')]
    author_counts = Counter(authors).most_common()

    # Generate Markdown
    md = []
    md.append("# 🎨 Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    md.append("\n## 📊 Executive Summary")
    md.append("| Metric | Value |")
    md.append("| :--- | :--- |")
    md.append(f"| **Total Posts** | {total_posts} |")
    md.append(f"| **Date Range** | {start_date} to {end_date} |")
    md.append(f"| **Unique Domains** | {len(set(domains))} |")

    md.append("\n## 🌐 Top 10 Referenced Domains")
    if domain_counts:
        max_d = domain_counts[0][1]
        md.append("| Domain | Count | Distribution |")
        md.append("| :--- | :---: | :--- |")
        for domain, count in domain_counts:
            md.append(f"| {domain} | {count} | {draw_bar(count, max_d)} |")

    md.append("\n## 📂 Top 10 Categories")
    if category_counts:
        max_c = category_counts[0][1]
        md.append("| Category | Count | Distribution |")
        md.append("| :--- | :---: | :--- |")
        for cat, count in category_counts:
            md.append(f"| {cat} | {count} | {draw_bar(count, max_c)} |")

    md.append("\n## 📅 Posts by Year")
    if year_counts:
        max_y = max(c for _, c in year_counts)
        md.append("| Year | Count | Distribution |")
        md.append("| :--- | :---: | :--- |")
        for year, count in year_counts:
            md.append(f"| {year} | {count} | {draw_bar(count, max_y)} |")

    md.append("\n## ✍️ Authors")
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
