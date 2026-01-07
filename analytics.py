"""
Analytics module for Markposition.

Generates statistical reports from scraped JSON data, including analysis of domains,
categories, posting dates, and authors. Outputs a Markdown report and a console summary.
"""

import json
import argparse
from collections import Counter
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

def generate_report(scraped_data, output_file):
    """Generates a Markdown report and prints a summary to the console."""
    total_posts = len(scraped_data)

    # 1. Domain Analysis
    domains = [p.get('domain') for p in scraped_data if p.get('domain')]
    domain_counts = Counter(domains).most_common(10)

    # 2. Category Analysis
    all_categories = []
    for p in scraped_data:
        cats = p.get('categories', [])
        if cats:
            all_categories.extend(cats)
    category_counts = Counter(all_categories).most_common(10)

    # 3. Date Analysis
    dates = []
    for p in scraped_data:
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
    authors = [p.get('author') for p in scraped_data if p.get('author')]
    author_counts = Counter(authors).most_common()

    # Generate Markdown
    md_content = []
    md_content.append("# 📊 Markposition Analytics Report")
    md_content.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    md_content.append("\n## 📈 General Statistics")
    md_content.append(f"- **Total Posts:** {total_posts}")
    md_content.append(f"- **Date Range:** {start_date} to {end_date}")
    md_content.append(f"- **Unique Domains Linked:** {len(set(domains))}")

    md_content.append("\n## 🌐 Top 10 Referenced Domains")
    md_content.append("| Domain | Count |")
    md_content.append("| :--- | :---: |")
    for domain, count in domain_counts:
        md_content.append(f"| {domain} | {count} |")

    md_content.append("\n## 🏷️ Top 10 Categories")
    md_content.append("| Category | Count |")
    md_content.append("| :--- | :---: |")
    for cat, count in category_counts:
        md_content.append(f"| {cat} | {count} |")

    md_content.append("\n## 📅 Posts by Year")
    md_content.append("| Year | Count |")
    md_content.append("| :--- | :---: |")
    for year, count in year_counts:
        md_content.append(f"| {year} | {count} |")

    md_content.append("\n## ✍️ Authors")
    for author, count in author_counts:
        md_content.append(f"- {author}: {count} posts")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_content))

    # Print Console Summary
    print("\n📊 Markposition Analytics Summary")
    print("---------------------------------")
    print(f"✅ Total Posts: {total_posts}")
    print(f"📅 Date Range: {start_date} to {end_date}")
    print(f"🌐 Unique Domains: {len(set(domains))}")
    if author_counts:
        top_author = author_counts[0]
        print(f"✍️  Top Author: {top_author[0]} ({top_author[1]} posts)")
    print(f"\n📄 Full report saved to: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data_input = load_data(args.input)
    generate_report(data_input, args.output)
