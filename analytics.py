import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys
import re

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

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')

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

    # Header
    md.append("# 📊 Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Table of Contents
    md.append("\n<a name='table-of-contents'></a>")
    md.append("## Table of Contents")
    md.append("- [📈 General Statistics](#general-statistics)")
    md.append("- [🔗 Top 10 Referenced Domains](#top-10-referenced-domains)")
    md.append("- [📂 Top 10 Categories](#top-10-categories)")
    md.append("- [📅 Posts by Year](#posts-by-year)")
    md.append("- [✍️ Authors](#authors)")

    # Helper for section with back to top
    def add_section(title, emoji, content_lines):
        slug = slugify(title)
        md.append(f"\n<a name='{slug}'></a>")
        md.append(f"## {emoji} {title}")
        md.extend(content_lines)
        md.append(f"\n[Back to Top](#table-of-contents)")

    # General Statistics
    stats_content = [
        f"- **Total Posts:** {total_posts}",
        f"- **Date Range:** {start_date} to {end_date}",
        f"- **Unique Domains Linked:** {len(set(domains))}"
    ]
    add_section("General Statistics", "📈", stats_content)

    # Top 10 Referenced Domains
    domains_content = [
        "| Domain | Count |",
        "| :--- | :---: |"
    ]
    for domain, count in domain_counts:
        domains_content.append(f"| {domain} | {count} |")
    add_section("Top 10 Referenced Domains", "🔗", domains_content)

    # Top 10 Categories
    cats_content = [
        "| Category | Count |",
        "| :--- | :---: |"
    ]
    for cat, count in category_counts:
        cats_content.append(f"| {cat} | {count} |")
    add_section("Top 10 Categories", "📂", cats_content)

    # Posts by Year
    years_content = [
        "| Year | Count |",
        "| :--- | :---: |"
    ]
    for year, count in year_counts:
        years_content.append(f"| {year} | {count} |")
    add_section("Posts by Year", "📅", years_content)

    # Authors
    authors_content = []
    for author, count in author_counts:
        authors_content.append(f"- {author}: {count} posts")
    add_section("Authors", "✍️", authors_content)

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
