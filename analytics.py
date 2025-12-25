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

    most_active_year = "N/A"
    most_active_year_count = 0

    if dates:
        dates.sort()
        start_date = dates[0].strftime('%Y-%m-%d')
        end_date = dates[-1].strftime('%Y-%m-%d')
        years = [d.year for d in dates]
        year_counts = Counter(years).most_common()
        year_counts.sort(key=lambda x: x[0], reverse=True)
        if year_counts:
             # Find max year
             top_year = max(year_counts, key=lambda x: x[1])
             most_active_year = top_year[0]
             most_active_year_count = top_year[1]
    else:
        start_date = "N/A"
        end_date = "N/A"
        year_counts = []

    # 4. Author Analysis
    authors = [p.get('author') for p in data if p.get('author')]
    author_counts = Counter(authors).most_common()

    top_author = "N/A"
    if author_counts:
        top_author = author_counts[0][0]

    # Generate Markdown
    md = []
    md.append("# 📊 Markposition Analytics Report")
    md.append(f"\n_Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_")

    md.append("\n## 📈 General Overview")
    md.append("| Metric | Value |")
    md.append("| :--- | :--- |")
    md.append(f"| **Total Posts** | {total_posts} |")
    md.append(f"| **Date Range** | {start_date} to {end_date} |")
    md.append(f"| **Unique Domains** | {len(set(domains))} |")
    md.append(f"| **Top Author** | {top_author} |")
    md.append(f"| **Busiest Year** | {most_active_year} ({most_active_year_count} posts) |")

    md.append("\n## 🔗 Top 10 Referenced Domains")
    md.append("| Rank | Domain | Count |")
    md.append("| :---: | :--- | :---: |")
    for i, (domain, count) in enumerate(domain_counts, 1):
        md.append(f"| {i} | {domain} | {count} |")

    md.append("\n## 🏷️ Top 10 Categories")
    md.append("| Rank | Category | Count |")
    md.append("| :---: | :--- | :---: |")
    for i, (cat, count) in enumerate(category_counts, 1):
        md.append(f"| {i} | {cat} | {count} |")

    md.append("\n## 📅 Posting Activity by Year")
    md.append("| Year | Posts |")
    md.append("| :---: | :---: |")
    for year, count in year_counts:
        md.append(f"| {year} | {count} |")

    if author_counts:
        md.append("\n## ✍️ Authors")
        md.append("| Author | Posts |")
        md.append("| :--- | :---: |")
        for author, count in author_counts:
             md.append(f"| {author} | {count} |")

    md.append("\n---\n*🎨 Report enhanced by Palette*")

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
