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

def draw_bar(count, max_val, length=20):
    if max_val == 0:
        return "░" * length
    filled = int(count / max_val * length)
    return "█" * filled + "░" * (length - filled)

def generate_report(data, output_file):
    total_posts = len(data)

    # 1. Domain Analysis
    domains = [get_domain(p.get('external_link')) for p in data if p.get('external_link')]
    domain_counts = Counter(domains).most_common(10)

    # 2. Category Analysis
    all_categories = []
    for p in data:
        cats = p.get('categories', [])
        if cats:
            all_categories.extend(cats)
    category_counts = Counter(all_categories).most_common(10)

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
        max_year_count = max(count for _, count in year_counts) if year_counts else 0
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
    # Add top anchor for "Back to Top" links
    md.append('<a name="top"></a>')
    md.append("# Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Table of Contents
    md.append("\n## Table of Contents")
    md.append("- [General Statistics](#general-statistics)")
    md.append("- [Top 10 Referenced Domains](#top-10-referenced-domains)")
    md.append("- [Top 10 Categories](#top-10-categories)")
    md.append("- [Posts by Year](#posts-by-year)")
    md.append("- [Authors](#authors)")

    md.append("\n## General Statistics")
    md.append(f"- **Total Posts:** {total_posts:,}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(set(domains)):,}")

    md.append("\n## Top 10 Referenced Domains")
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in domain_counts:
        md.append(f"| {domain} | {count:,} |")
    md.append("\n[Back to Top](#top)")

    md.append("\n## Top 10 Categories")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in category_counts:
        md.append(f"| {cat} | {count:,} |")
    md.append("\n[Back to Top](#top)")

    md.append("\n## Posts by Year")
    md.append("| Year | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for year, count in year_counts:
        bar = draw_bar(count, max_year_count)
        percent = (count / total_posts * 100) if total_posts > 0 else 0
        md.append(f"| {year} | {count:,} | {bar} {percent:.1f}% |")
    md.append("\n[Back to Top](#top)")

    md.append("\n## Authors")
    for author, count in author_counts:
        md.append(f"- {author}: {count:,} posts")
    md.append("\n[Back to Top](#top)")

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
