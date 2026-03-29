"""
Analytics Module
This module processes link data and generates a Markdown report with visual analytics.
"""

import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys
import math

# ANSI Color Codes for Palette UX
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

def load_data(filepath):
    """Loads JSON data from the specified file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

def get_domain(url):
    """Extracts the domain from a given URL."""
    if not url:
        return None
    try:
        return urlparse(url).netloc.replace('www.', '')
    except Exception: # pylint: disable=broad-except
        return None

def create_bar(value, max_value, width=20):
    """Creates an ASCII progress bar."""
    if max_value == 0:
        return "░" * width
    filled_length = math.ceil((value / max_value) * width)
    return "█" * filled_length + "░" * (width - filled_length)

def generate_report(report_data, output_file):
    """Generates a Markdown report from the provided data."""
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
    md.append("| Metric | Value |")
    md.append("| :--- | :--- |")
    md.append(f"| Total Posts | {total_posts} |")
    md.append(f"| Date Range | {start_date} to {end_date} |")
    md.append(f"| Unique Domains | {len(set(domains))} |")

    md.append("\n## 🌐 Top 10 Referenced Domains")
    md.append("| Domain | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    if domain_counts:
        max_domain = domain_counts[0][1]
        for domain, count in domain_counts:
            dist_bar = create_bar(count, max_domain)
            md.append(f"| {domain} | {count} | {dist_bar} |")
    else:
        md.append("| No data | 0 | |")

    md.append("\n## 🏷️ Top 10 Categories")
    md.append("| Category | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    if category_counts:
        max_cat = category_counts[0][1]
        for cat, count in category_counts:
            dist_bar = create_bar(count, max_cat)
            md.append(f"| {cat} | {count} | {dist_bar} |")
    else:
        md.append("| No data | 0 | |")

    md.append("\n## 📅 Posts by Year")
    md.append("| Year | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    if year_counts:
        max_year = year_counts[0][1]
        for year, count in year_counts:
            dist_bar = create_bar(count, max_year)
            md.append(f"| {year} | {count} | {dist_bar} |")
    else:
        md.append("| No data | 0 | |")

    md.append("\n## 👥 Authors")
    if len(author_counts) > 0:
        md.append("| Author | Count | Distribution |")
        md.append("| :--- | :---: | :--- |")
        max_author = author_counts[0][1]
        for author, count in author_counts:
            dist_bar = create_bar(count, max_author)
            md.append(f"| {author} | {count} | {dist_bar} |")
    else:
        md.append("No author data available.")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    # Palette UX: Console Summary
    print(f"\n{GREEN}{BOLD}✅ Analysis Complete!{RESET}")
    print(f"\n{CYAN}📊 Quick Summary:{RESET}")
    print(f"  • {BOLD}Total Posts:{RESET} {total_posts}")
    print(f"  • {BOLD}Date Range:{RESET} {start_date} to {end_date}")

    top_domain = domain_counts[0] if domain_counts else ("None", 0)
    print(f"  • {BOLD}Top Domain:{RESET} {top_domain[0]} ({top_domain[1]})")

    top_cat = category_counts[0] if category_counts else ("None", 0)
    print(f"  • {BOLD}Top Category:{RESET} {top_cat[0]} ({top_cat[1]})")

    print(f"\n{YELLOW}📝 Full report saved to:{RESET} {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
