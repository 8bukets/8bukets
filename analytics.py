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

    md.append("\n## General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(set(domains))}")

    md.append("\n## Top 10 Referenced Domains")
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in domain_counts:
        md.append(f"| {escape_markdown(domain)} | {count} |")

    md.append("\n## Top 10 Categories")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in category_counts:
        md.append(f"| {escape_markdown(cat)} | {count} |")

    md.append("\n## Posts by Year")
    md.append("| Year | Count |")
    md.append("| :--- | :---: |")
    for year, count in year_counts:
        md.append(f"| {year} | {count} |")

    md.append("\n## Authors")
    for author, count in author_counts:
        md.append(f"- {escape_markdown(author)}: {count} posts")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    # CLI Visual Summary
    use_colors = sys.stdout.isatty()

    class Colors:
        HEADER = '\033[95m' if use_colors else ''
        BLUE = '\033[94m' if use_colors else ''
        GREEN = '\033[92m' if use_colors else ''
        ENDC = '\033[0m' if use_colors else ''
        BOLD = '\033[1m' if use_colors else ''

    def create_bar_chart(label, value, max_val, width=20):
        if max_val == 0:
            bar_len = 0
        else:
            bar_len = int((value / max_val) * width)
        bar_visual = '█' * bar_len
        return f"{label:<25} {Colors.BLUE}|{bar_visual:<{width}}|{Colors.ENDC} {value}"

    print(f"\n{Colors.HEADER}{Colors.BOLD}📊 Report generated: {output_file}{Colors.ENDC}")
    print(f"{Colors.GREEN}✔ Total Posts: {total_posts} | "
          f"Date Range: {start_date} to {end_date}{Colors.ENDC}\n")

    print(f"{Colors.BOLD}Top Linked Domains:{Colors.ENDC}")
    if domain_counts:
        max_count = domain_counts[0][1]
        for domain_name, dom_count in domain_counts[:5]:
            print(create_bar_chart(domain_name, dom_count, max_count))
    print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
