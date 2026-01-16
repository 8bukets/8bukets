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

def analyze_data(data):
    # 1. Domain Analysis
    # Use generator to count without intermediate list
    domain_counter = Counter(p.get('domain') for p in data if p.get('domain'))
    domain_counts = domain_counter.most_common(10)

    # 2. Category Analysis
    # Nested generator to flatten categories without intermediate list
    # Use (p.get('categories') or []) to handle None if 'categories' key exists but is null
    category_counts = Counter(
        cat for p in data for cat in (p.get('categories') or [])
    ).most_common(10)

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
        # Use generator for years
        year_counts = Counter(d.year for d in dates).most_common()
        year_counts.sort(key=lambda x: x[0], reverse=True)
    else:
        start_date = "N/A"
        end_date = "N/A"
        year_counts = []

    # 4. Author Analysis
    # Use generator
    author_counts = Counter(p.get('author') for p in data if p.get('author')).most_common()

    return {
        'total_posts': len(data),
        'start_date': start_date,
        'end_date': end_date,
        'unique_domains': len(domain_counter), # Count unique keys in Counter
        'domain_counts': domain_counts,
        'category_counts': category_counts,
        'year_counts': year_counts,
        'author_counts': author_counts
    }

def generate_report(data, output_file):
    stats = analyze_data(data)

    # Generate Markdown
    md = []
    md.append("# Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    md.append("\n## General Statistics")
    md.append(f"- **Total Posts:** {stats['total_posts']}")
    md.append(f"- **Date Range:** {stats['start_date']} to {stats['end_date']}")
    md.append(f"- **Unique Domains Linked:** {stats['unique_domains']}")

    md.append("\n## Top 10 Referenced Domains")
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in stats['domain_counts']:
        md.append(f"| {domain} | {count} |")

    md.append("\n## Top 10 Categories")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in stats['category_counts']:
        md.append(f"| {cat} | {count} |")

    md.append("\n## Posts by Year")
    md.append("| Year | Count |")
    md.append("| :--- | :---: |")
    for year, count in stats['year_counts']:
        md.append(f"| {year} | {count} |")

    md.append("\n## Authors")
    for author, count in stats['author_counts']:
        md.append(f"- {author}: {count} posts")

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
