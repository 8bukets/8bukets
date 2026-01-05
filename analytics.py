import json
import argparse
from collections import Counter
from datetime import datetime
import sys

def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

def create_bar_chart(value, max_value, width=20):
    """Generates an ASCII bar chart."""
    if max_value == 0:
        return "░" * width

    filled_len = int((value / max_value) * width)

    # Clamp to width to prevent overflow
    if filled_len > width:
        filled_len = width

    # Ensure at least one block if value > 0
    if value > 0 and filled_len == 0:
        filled_len = 1

    empty_len = width - filled_len
    return "█" * filled_len + "░" * empty_len

def generate_report(data, output_file):
    total_posts = len(data)

    # 1. Domain Analysis
    domains = [p.get('domain') for p in data if p.get('domain')]
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

    md.append("\n## Top 10 Referenced Domains")
    md.append("| Domain | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    max_domain = domain_counts[0][1] if domain_counts else 0
    for domain, count in domain_counts:
        bar = create_bar_chart(count, max_domain)
        md.append(f"| {domain} | {count} | {bar} |")

    md.append("\n## Top 10 Categories")
    md.append("| Category | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    max_cat = category_counts[0][1] if category_counts else 0
    for cat, count in category_counts:
        bar = create_bar_chart(count, max_cat)
        md.append(f"| {cat} | {count} | {bar} |")

    md.append("\n## Posts by Year")
    md.append("| Year | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    max_year = max([count for _, count in year_counts]) if year_counts else 0
    for year, count in year_counts:
        bar = create_bar_chart(count, max_year)
        md.append(f"| {year} | {count} | {bar} |")

    md.append("\n## Authors")
    md.append("| Author | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    max_author = author_counts[0][1] if author_counts else 0
    for author, count in author_counts:
        bar = create_bar_chart(count, max_author)
        md.append(f"| {author} | {count} | {bar} |")

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
