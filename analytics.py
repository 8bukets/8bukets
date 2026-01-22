import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys

def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

def get_domain(url):
    if not url:
        return None
    try:
        return urlparse(url).netloc.replace('www.', '')
    except:
        return None

def calc_pct(count, total):
    if total == 0:
        return "0%"
    return f"{(count / total) * 100:.1f}%"

def generate_report(data, output_file):
    total_posts = len(data)

    # Initialize counters and trackers
    domain_counts = Counter()
    category_counts = Counter()
    author_counts = Counter()
    year_counts = Counter()

    min_date = None
    max_date = None

    unique_domains = set()

    # Single pass iteration
    for p in data:
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
    top_domains = domain_counts.most_common(10)
    top_categories = category_counts.most_common(10)

    # Dates
    if min_date and max_date:
        start_date = min_date.strftime('%Y-%m-%d')
        end_date = max_date.strftime('%Y-%m-%d')
        sorted_years = sorted(year_counts.items(), key=lambda x: x[0], reverse=True)
    else:
        start_date = "N/A"
        end_date = "N/A"
        sorted_years = []

    sorted_authors = author_counts.most_common()

    # Quick Insights
    top_domain_name = top_domains[0][0] if top_domains else "N/A"
    top_cat_name = top_categories[0][0] if top_categories else "N/A"

    # Generate Markdown
    md = []
    md.append("# 📊 Markposition Analytics Report")
    md.append(f"**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # Table of Contents
    md.append("## Table of Contents")
    md.append("- [📈 General Statistics](#-general-statistics)")
    md.append("- [🔗 Top 10 Referenced Domains](#-top-10-referenced-domains)")
    md.append("- [📂 Top 10 Categories](#-top-10-categories)")
    md.append("- [📅 Posts by Year](#-posts-by-year)")
    md.append("- [✍️ Authors](#-authors)")

    md.append("\n## 📈 General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(unique_domains)}")
    md.append(f"- **Top Domain:** {top_domain_name}")
    md.append(f"- **Top Category:** {top_cat_name}")

    md.append("\n## 🔗 Top 10 Referenced Domains")
    md.append("| Domain | Count | % of Posts |")
    md.append("| :--- | :---: | :---: |")
    for domain, count in top_domains:
        md.append(f"| {domain} | {count} | {calc_pct(count, total_posts)} |")

    md.append("\n## 📂 Top 10 Categories")
    md.append("| Category | Count | % of Posts |")
    md.append("| :--- | :---: | :---: |")
    for cat, count in top_categories:
        md.append(f"| {cat} | {count} | {calc_pct(count, total_posts)} |")

    md.append("\n## 📅 Posts by Year")
    md.append("| Year | Count | % of Total |")
    md.append("| :--- | :---: | :---: |")
    for year, count in sorted_years:
        md.append(f"| {year} | {count} | {calc_pct(count, total_posts)} |")

    md.append("\n## ✍️ Authors")
    for author, count in sorted_authors:
        md.append(f"- **{author}**: {count} posts ({calc_pct(count, total_posts)})")

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
