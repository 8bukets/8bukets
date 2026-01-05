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

def create_bar_chart(value, max_value, width=20):
    if max_value == 0:
        return "░" * width
    filled_length = int(width * value / max_value)
    bar = "█" * filled_length + "░" * (width - filled_length)
    return bar

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
    else:
        start_date = "N/A"
        end_date = "N/A"
        year_counts = []

    # 4. Author Analysis
    authors = [p.get('author') for p in data if p.get('author')]
    author_counts = Counter(authors).most_common()

    # Generate Markdown
    md = []
    md.append("# Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    md.append("\n## General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(set(domains))}")

    # Top 10 Referenced Domains
    md.append("\n## Top 10 Referenced Domains")
    if domain_counts:
        max_domain_count = domain_counts[0][1]
        md.append("| Domain | Count | % | Distribution |")
        md.append("| :--- | :---: | :---: | :--- |")
        for domain, count in domain_counts:
            pct = (count / len(domains)) * 100 if domains else 0
            bar = create_bar_chart(count, max_domain_count)
            md.append(f"| {domain} | {count} | {pct:.1f}% | {bar} |")
    else:
        md.append("No domains found.")

    # Top 10 Categories
    md.append("\n## Top 10 Categories")
    if category_counts:
        max_cat_count = category_counts[0][1]
        md.append("| Category | Count | % | Distribution |")
        md.append("| :--- | :---: | :---: | :--- |")
        for cat, count in category_counts:
            pct = (count / len(all_categories)) * 100 if all_categories else 0
            bar = create_bar_chart(count, max_cat_count)
            md.append(f"| {cat} | {count} | {pct:.1f}% | {bar} |")
    else:
        md.append("No categories found.")

    # Posts by Year
    md.append("\n## Posts by Year")
    if year_counts:
        max_year_count = max(count for _, count in year_counts)
        md.append("| Year | Count | % | Distribution |")
        md.append("| :--- | :---: | :---: | :--- |")
        for year, count in year_counts:
            pct = (count / total_posts) * 100 if total_posts else 0
            bar = create_bar_chart(count, max_year_count)
            md.append(f"| {year} | {count} | {pct:.1f}% | {bar} |")
    else:
        md.append("No date data available.")

    # Authors
    md.append("\n## Authors")
    if author_counts:
        max_author_count = author_counts[0][1]
        md.append("| Author | Count | % | Distribution |")
        md.append("| :--- | :---: | :---: | :--- |")
        for author, count in author_counts:
            pct = (count / total_posts) * 100 if total_posts else 0
            bar = create_bar_chart(count, max_author_count)
            md.append(f"| {author} | {count} | {pct:.1f}% | {bar} |")
    else:
        md.append("No authors found.")

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
