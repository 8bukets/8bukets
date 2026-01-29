import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys

# Define Sections with Emojis
SECTIONS = {
    "stats": ("General Statistics", "📊"),
    "domains": ("Top 10 Referenced Domains", "🔗"),
    "categories": ("Top 10 Categories", "📂"),
    "years": ("Posts by Year", "📅"),
    "authors": ("Authors", "✍️")
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

    # --- Markdown Generation ---
    md = []

    # Title
    md.append("# Wordpress Blog Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    md.append("\n---") # Visual separator

    # Table of Contents
    md.append(f"\n<a name='table-of-contents'></a>")
    md.append("# Table of Contents")
    for section_id, (title, emoji) in SECTIONS.items():
        md.append(f"- [{title} {emoji}](#{section_id})")

    # Helper to add section
    def add_section(section_id, content_lines):
        title, emoji = SECTIONS[section_id]
        md.append(f"\n<a name='{section_id}'></a>")
        md.append(f"## {title} {emoji}")
        md.extend(content_lines)
        md.append(f"\n[Back to Top](#table-of-contents)")

    # Stats
    stats_content = [
        f"- **Total Posts:** {total_posts}",
        f"- **Date Range:** {start_date} to {end_date}",
        f"- **Unique Domains Linked:** {len(set(domains))}"
    ]
    add_section("stats", stats_content)

    # Domains
    domain_content = []
    domain_content.append("| Domain | Count |")
    domain_content.append("| :--- | :---: |")
    for domain, count in domain_counts:
        domain_content.append(f"| {domain} | {count} |")
    add_section("domains", domain_content)

    # Categories
    cat_content = []
    cat_content.append("| Category | Count |")
    cat_content.append("| :--- | :---: |")
    for cat, count in category_counts:
        cat_content.append(f"| {cat} | {count} |")
    add_section("categories", cat_content)

    # Years
    year_content = []
    year_content.append("| Year | Count |")
    year_content.append("| :--- | :---: |")
    for year, count in year_counts:
        year_content.append(f"| {year} | {count} |")
    add_section("years", year_content)

    # Authors
    author_content = []
    for author, count in author_counts:
        author_content.append(f"- {author}: {count} posts")
    add_section("authors", author_content)

    return '\n'.join(md)

def generate_report(data, output_file):
    markdown_content = generate_markdown_content(data)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)

    print(f"Report generated: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for WordPress blog data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
