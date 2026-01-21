import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys

EMOJI_MAP = {
    "General Statistics": "📊",
    "Top 10 Referenced Domains": "🌐",
    "Top 10 Categories": "🍷",
    "Posts by Year": "📅",
    "Authors": "✒️"
}

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

    # Domains: top 10 by count
    top_domains = domain_counts.most_common(10)

    # Categories: top 10 by count
    top_categories = category_counts.most_common(10)

    # Dates: range and years sorted by year descending
    if min_date and max_date:
        start_date = min_date.strftime('%Y-%m-%d')
        end_date = max_date.strftime('%Y-%m-%d')
        # Sort years descending (key is year)
        sorted_years = sorted(year_counts.items(), key=lambda x: x[0], reverse=True)
    else:
        start_date = "N/A"
        end_date = "N/A"
        sorted_years = []

    # Authors: all by count descending (most_common does this)
    sorted_authors = author_counts.most_common()

    # Generate Markdown
    # We will build parts separately to avoid magic indices

    # 1. Header Part
    md_header = []
    md_header.append(f"<a name=\"top\"></a>")
    md_header.append("# Markposition Analytics Report")
    md_header.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # 2. Body Part (collecting TOC entries as we go)
    md_body = []
    toc_lines = ["\n## Table of Contents"]

    def add_header(title):
        slug = title.lower().replace(" ", "-")
        emoji = EMOJI_MAP.get(title, "")

        # Add to TOC
        toc_lines.append(f"- [{title}](#{slug})")

        # Add to content
        md_body.append(f"\n<a name=\"{slug}\"></a>")
        md_body.append(f"## {emoji} {title}".strip())

    def add_back_to_top():
        md_body.append(f"\n[Back to Top](#top)")

    add_header("General Statistics")
    md_body.append(f"- **Total Posts:** {total_posts:,}")
    md_body.append(f"- **Date Range:** {start_date} to {end_date}")
    md_body.append(f"- **Unique Domains Linked:** {len(unique_domains):,}")
    add_back_to_top()

    add_header("Top 10 Referenced Domains")
    md_body.append("| Domain | Count |")
    md_body.append("| :--- | :---: |")
    for domain, count in top_domains:
        md_body.append(f"| {domain} | {count:,} |")
    add_back_to_top()

    add_header("Top 10 Categories")
    md_body.append("| Category | Count |")
    md_body.append("| :--- | :---: |")
    for cat, count in top_categories:
        md_body.append(f"| {cat} | {count:,} |")
    add_back_to_top()

    add_header("Posts by Year")
    md_body.append("| Year | Count |")
    md_body.append("| :--- | :---: |")
    for year, count in sorted_years:
        md_body.append(f"| {year} | {count:,} |")
    add_back_to_top()

    add_header("Authors")
    for author, count in sorted_authors:
        md_body.append(f"- {author}: {count:,} posts")
    add_back_to_top()

    # Combine parts
    final_md = md_header + toc_lines + md_body

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(final_md))

    print(f"Report generated: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
