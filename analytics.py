import json
import argparse
from collections import Counter
from datetime import datetime
import sys

# Define sections with titles and emojis
SECTIONS = {
    "general": {"title": "General Statistics", "emoji": "📊"},
    "domains": {"title": "Top 10 Referenced Domains", "emoji": "🔗"},
    "categories": {"title": "Top 10 Categories", "emoji": "📂"},
    "years": {"title": "Posts by Year", "emoji": "📅"},
    "authors": {"title": "Authors", "emoji": "✍️"}
}

def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

def slugify(text):
    return text.lower().replace(" ", "-")

def get_section_header(key):
    section = SECTIONS[key]
    title = section["title"]
    emoji = section["emoji"]
    slug = slugify(title)
    # Explicit anchor for reliable linking
    return f'<a name="{slug}"></a>\n## {emoji} {title}'

def get_back_to_top():
    return "\n[Back to Top](#table-of-contents)"

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

    # Table of Contents
    md.append("\n<a name='table-of-contents'></a>\n## Table of Contents")
    for key, section in SECTIONS.items():
        title = section["title"]
        emoji = section["emoji"]
        slug = slugify(title)
        md.append(f"- [{emoji} {title}](#{slug})")

    # General Statistics
    md.append(f"\n{get_section_header('general')}")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(set(domains))}")
    md.append(get_back_to_top())

    # Top Domains
    md.append(f"\n{get_section_header('domains')}")
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in domain_counts:
        md.append(f"| {domain} | {count} |")
    md.append(get_back_to_top())

    # Top Categories
    md.append(f"\n{get_section_header('categories')}")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in category_counts:
        md.append(f"| {cat} | {count} |")
    md.append(get_back_to_top())

    # Posts by Year
    md.append(f"\n{get_section_header('years')}")
    md.append("| Year | Count |")
    md.append("| :--- | :---: |")
    for year, count in year_counts:
        md.append(f"| {year} | {count} |")
    md.append(get_back_to_top())

    # Authors
    md.append(f"\n{get_section_header('authors')}")
    for author, count in author_counts:
        md.append(f"- {author}: {count} posts")
    md.append(get_back_to_top())

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
