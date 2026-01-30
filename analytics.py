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

def generate_markdown_content(data):
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

    # Define Sections
    # Key: (Emoji, Title, Slug)
    sections_info = [
        ("stats", "📊", "General Statistics", "general-statistics"),
        ("domains", "🔗", "Top 10 Referenced Domains", "top-10-referenced-domains"),
        ("categories", "📂", "Top 10 Categories", "top-10-categories"),
        ("years", "📅", "Posts by Year", "posts-by-year"),
        ("authors", "✍️", "Authors", "authors"),
    ]

    md = []
    md.append("# Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Table of Contents
    md.append(f"\n<a name='table-of-contents'></a>")
    md.append("## Table of Contents")
    for _, emoji, title, slug in sections_info:
        md.append(f"- [{emoji} {title}](#{slug})")

    # Helper to add back to top
    back_to_top = "\n[Back to Top](#table-of-contents)"

    # Generate Sections

    # 1. General Statistics
    emoji, title, slug = sections_info[0][1], sections_info[0][2], sections_info[0][3]
    md.append(f"\n<a name='{slug}'></a>")
    md.append(f"## {emoji} {title}")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(set(domains))}")
    md.append(back_to_top)

    # 2. Domains
    emoji, title, slug = sections_info[1][1], sections_info[1][2], sections_info[1][3]
    md.append(f"\n<a name='{slug}'></a>")
    md.append(f"## {emoji} {title}")
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in domain_counts:
        md.append(f"| {domain} | {count} |")
    md.append(back_to_top)

    # 3. Categories
    emoji, title, slug = sections_info[2][1], sections_info[2][2], sections_info[2][3]
    md.append(f"\n<a name='{slug}'></a>")
    md.append(f"## {emoji} {title}")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in category_counts:
        md.append(f"| {cat} | {count} |")
    md.append(back_to_top)

    # 4. Years
    emoji, title, slug = sections_info[3][1], sections_info[3][2], sections_info[3][3]
    md.append(f"\n<a name='{slug}'></a>")
    md.append(f"## {emoji} {title}")
    md.append("| Year | Count |")
    md.append("| :--- | :---: |")
    for year, count in year_counts:
        md.append(f"| {year} | {count} |")
    md.append(back_to_top)

    # 5. Authors
    emoji, title, slug = sections_info[4][1], sections_info[4][2], sections_info[4][3]
    md.append(f"\n<a name='{slug}'></a>")
    md.append(f"## {emoji} {title}")
    for author, count in author_counts:
        md.append(f"- {author}: {count} posts")
    md.append(back_to_top)

    return '\n'.join(md)

def generate_report(data, output_file):
    content = generate_markdown_content(data)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Report generated: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
