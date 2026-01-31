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

    # Performance Optimization: Use Generators with Counter
    # This delegates the counting loop to C-optimized code in collections.Counter
    # and avoids creating large intermediate lists.

    # 1. Domain Analysis
    domain_counts = Counter(
        get_domain(p.get('external_link'))
        for p in data
        if p.get('external_link')
    )
    # Remove None if it slipped through
    if None in domain_counts:
        del domain_counts[None]

    # 2. Category Analysis
    category_counts = Counter(
        cat
        for p in data
        for cat in (p.get('categories') or [])
    )

    # 3. Author Analysis
    author_counts = Counter(
        p.get('author')
        for p in data
        if p.get('author')
    )

    # 4. Date Analysis (Requires explicit loop for parsing and range finding)
    year_counts = Counter()
    min_date = None
    max_date = None

    for p in data:
        # Handle both 'datetime' (ISO) and 'date' (YYYY-MM-DD)
        dt_str = p.get('datetime') or p.get('date')
        if dt_str:
            try:
                # Try fromisoformat first (handles ISO and YYYY-MM-DD in recent python)
                dt = datetime.fromisoformat(dt_str)
            except ValueError:
                try:
                    dt = datetime.strptime(dt_str, '%Y-%m-%d')
                except ValueError:
                    dt = None

            if dt:
                year_counts[dt.year] += 1
                if min_date is None or dt < min_date:
                    min_date = dt
                if max_date is None or dt > max_date:
                    max_date = dt

    # Sort results
    top_domains = domain_counts.most_common(10)
    top_categories = category_counts.most_common(10)
    sorted_years = sorted(year_counts.items(), key=lambda x: x[0], reverse=True)
    sorted_authors = author_counts.most_common()

    if min_date and max_date:
        start_date = min_date.strftime('%Y-%m-%d')
        end_date = max_date.strftime('%Y-%m-%d')
    else:
        start_date = "N/A"
        end_date = "N/A"

    # Generate Markdown
    md = []
    md.append("# Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    md.append("\n## General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(domain_counts)}")

    md.append("\n## Top 10 Referenced Domains")
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in top_domains:
        md.append(f"| {domain} | {count} |")

    md.append("\n## Top 10 Categories")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in top_categories:
        md.append(f"| {cat} | {count} |")

    md.append("\n## Posts by Year")
    md.append("| Year | Count |")
    md.append("| :--- | :---: |")
    for year, count in sorted_years:
        md.append(f"| {year} | {count} |")

    md.append("\n## Authors")
    for author, count in sorted_authors:
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
