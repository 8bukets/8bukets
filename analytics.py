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

def escape_markdown(text):
    """
    Escapes characters that have special meaning in Markdown and HTML.
    Specifically targets:
    - HTML entities: &, <, >
    - Markdown table separators: |
    """
    if text is None:
        return ""
    text = str(text)

    # HTML escaping
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")

    # Markdown escaping
    # Escape pipe to prevent table injection
    text = text.replace("|", "\\|")

    return text

def generate_report(data, output_file):
    total_posts = len(data)

    # Single pass aggregation
    domains = []
    all_categories = []
    dates = []
    authors = []

    for p in data:
        # Domain Analysis
        # Use pre-computed domain if available, otherwise fallback to parsing external_link
        domain = p.get('domain')
        if domain:
            domains.append(domain)
        elif p.get('external_link'):
            d = get_domain(p['external_link'])
            if d:
                domains.append(d)

        # Category Analysis
        cats = p.get('categories')
        if cats:
            all_categories.extend(cats)

        # Date Analysis
        dt_str = p.get('datetime')
        if dt_str:
            try:
                # Handle ISO format
                dates.append(datetime.fromisoformat(dt_str))
            except ValueError:
                pass

        # Author Analysis
        author = p.get('author')
        if author:
            authors.append(author)

    domain_counts = Counter(domains).most_common(10)
    category_counts = Counter(all_categories).most_common(10)

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

    author_counts = Counter(authors).most_common()

    # Generate Markdown
    md = []
    md.append("# Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Table of Contents
    md.append("\n## <a id='toc'></a>📋 Table of Contents")
    md.append("- [📊 General Statistics](#stats)")
    md.append("- [🔗 Referenced Domains](#domains)")
    md.append("- [🏷️ Top Categories](#categories)")
    md.append("- [📅 Posts by Year](#years)")
    md.append("- [✍️ Authors](#authors)")

    md.append("\n## <a id='stats'></a>📊 General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(set(domains))}")

    md.append("\n## <a id='domains'></a>🔗 Top 10 Referenced Domains")
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in domain_counts:
        md.append(f"| {escape_markdown(domain)} | {count} |")

    md.append("\n## <a id='categories'></a>🏷️ Top 10 Categories")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in category_counts:
        md.append(f"| {escape_markdown(cat)} | {count} |")

    md.append("\n## <a id='years'></a>📅 Posts by Year")
    md.append("| Year | Count |")
    md.append("| :--- | :---: |")
    for year, count in year_counts:
        md.append(f"| {year} | {count} |")

    md.append("\n## <a id='authors'></a>✍️ Authors")
    for author, count in author_counts:
        md.append(f"- {escape_markdown(author)}: {count} posts")

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
