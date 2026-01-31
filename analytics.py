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

def generate_report(data, output_file):
    total_posts = len(data)

    # Initialize lists for batch processing (faster than incremental Counter updates in Python)
    domains = []
    all_categories = []
    years = []
    authors = []

    min_date = None
    max_date = None

    # Single pass loop O(N)
    for p in data:
        # Domain
        domain = p.get('domain')
        if domain:
            domains.append(domain)

        # Categories
        cats = p.get('categories')
        if cats:
            all_categories.extend(cats)

        # Date
        dt_str = p.get('datetime')
        if dt_str:
            try:
                # Handle ISO format
                dt = datetime.fromisoformat(dt_str)
                if min_date is None or dt < min_date:
                    min_date = dt
                if max_date is None or dt > max_date:
                    max_date = dt
                years.append(dt.year)
            except ValueError:
                pass

        # Author
        author = p.get('author')
        if author:
            authors.append(author)

    # Create counters efficiently using C-optimized constructors
    domain_counts = Counter(domains)
    category_counts = Counter(all_categories)
    year_counts = Counter(years)
    author_counts = Counter(authors)

    # Prepare report data
    top_domains = domain_counts.most_common(10)
    top_categories = category_counts.most_common(10)

    # Sort years descending
    sorted_years = sorted(year_counts.items(), key=lambda x: x[0], reverse=True)

    # Sort authors by count descending (default most_common)
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
