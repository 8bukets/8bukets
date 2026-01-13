"""
Analytics module for processing scraped data and generating a Markdown report.
Includes visual enhancements like ASCII bar charts.
"""
import json
import argparse
import math
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys

def load_data(filepath):
    """Load JSON data from the specified filepath."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

def get_domain(url):
    """Extract domain from a given URL."""
    if not url:
        return None
    try:
        return urlparse(url).netloc.replace('www.', '')
    except Exception: # pylint: disable=broad-except
        return None

def create_bar_chart(value, max_value, max_width=20):
    """Generates an ASCII bar chart."""
    if not max_value:
        return ""
    width = int(math.ceil((value / max_value) * max_width))
    return "█" * width + "░" * (max_width - width)

def generate_report(report_data, output_file):
    """Generates a Markdown report from the analyzed data."""
    total_posts = len(report_data)

    # 1. Domain Analysis
    domains = [get_domain(p.get('external_link')) for p in report_data if p.get('external_link')]
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
    md.append("# 📊 Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    md.append("\n## 📈 General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(set(domains))}")

    md.append("\n## 🌐 Top 10 Referenced Domains")
    max_domain = domain_counts[0][1] if domain_counts else 1
    md.append("| Domain | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for domain, count in domain_counts:
        chart_bar = create_bar_chart(count, max_domain)
        md.append(f"| {domain} | {count} | {chart_bar} |")

    md.append("\n## 📂 Top 10 Categories")
    max_cat = category_counts[0][1] if category_counts else 1
    md.append("| Category | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for cat, count in category_counts:
        chart_bar = create_bar_chart(count, max_cat)
        md.append(f"| {cat} | {count} | {chart_bar} |")

    md.append("\n## 📅 Posts by Year")
    max_year = year_counts[0][1] if year_counts else 1
    md.append("| Year | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for year, count in year_counts:
        chart_bar = create_bar_chart(count, max_year)
        md.append(f"| {year} | {count} | {chart_bar} |")

    md.append("\n## ✍️ Authors")
    max_auth = author_counts[0][1] if author_counts else 1
    md.append("| Author | Posts | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for author, count in author_counts:
        chart_bar = create_bar_chart(count, max_auth)
        md.append(f"| {author} | {count} | {chart_bar} |")

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
