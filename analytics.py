import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys
import html

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

def sanitize_markdown(text):
    """Sanitize text for Markdown tables to prevent injection."""
    if text is None:
        return ""
    text = str(text)
    # Escape HTML characters
    text = html.escape(text)
    # Escape pipes
    text = text.replace('|', '&#124;')
    # Remove newlines to keep table structure
    text = text.replace('\n', ' ').replace('\r', '')
    return text

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
        dt_str = p.get('datetime') or p.get('date')
        if dt_str:
            try:
                # Handle ISO format
                dt = datetime.fromisoformat(dt_str)
            except ValueError:
                try:
                    # Handle YYYY-MM-DD
                    dt = datetime.strptime(dt_str, '%Y-%m-%d')
                except ValueError:
                    continue
            dates.append(dt)

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
    md.append("# 📈 Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Anchors
    anchor_stats = "general-statistics"
    anchor_domains = "top-10-referenced-domains"
    anchor_cats = "top-10-categories"
    anchor_years = "posts-by-year"
    anchor_authors = "authors"

    # Table of Contents
    md.append("\n## Table of Contents")
    md.append(f"- [📊 General Statistics](#{anchor_stats})")
    md.append(f"- [🌐 Top 10 Referenced Domains](#{anchor_domains})")
    md.append(f"- [🏷️ Top 10 Categories](#{anchor_cats})")
    md.append(f"- [📅 Posts by Year](#{anchor_years})")
    md.append(f"- [✍️ Authors](#{anchor_authors})")

    md.append(f"\n## <a id='{anchor_stats}'></a>📊 General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(set(domains))}")

    md.append(f"\n## <a id='{anchor_domains}'></a>🌐 Top 10 Referenced Domains")
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in domain_counts:
        md.append(f"| {sanitize_markdown(domain)} | {count} |")

    md.append(f"\n## <a id='{anchor_cats}'></a>🏷️ Top 10 Categories")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in category_counts:
        md.append(f"| {sanitize_markdown(cat)} | {count} |")

    md.append(f"\n## <a id='{anchor_years}'></a>📅 Posts by Year")
    md.append("| Year | Count |")
    md.append("| :--- | :---: |")
    for year, count in year_counts:
        md.append(f"| {year} | {count} |")

    md.append(f"\n## <a id='{anchor_authors}'></a>✍️ Authors")
    for author, count in author_counts:
        md.append(f"- {sanitize_markdown(author)}: {count} posts")

    # Footer
    md.append("\n---\n")
    md.append("Generated with ❤️ by Palette")

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
