import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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

    # Determine Highlight
    highlight = "No significant data found."
    if year_counts:
        # Find the year with the most posts (max by count)
        most_active_year_entry = sorted(year_counts, key=lambda x: x[1], reverse=True)[0]
        highlight = f"**{most_active_year_entry[0]}** was the most active year with **{most_active_year_entry[1]}** posts."
    elif domain_counts:
        top_dom, top_dom_count = domain_counts[0]
        highlight = f"**{top_dom}** is the top referenced source with **{top_dom_count}** links."


    # Generate Markdown
    md = []
    md.append("# 📈 Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Table of Contents
    md.append("\n## Table of Contents")
    md.append("- [📊 General Statistics](#general-statistics)")
    md.append("- [🔗 Top Referenced Domains](#top-referenced-domains)")
    md.append("- [📂 Top Categories](#top-categories)")
    md.append("- [📅 Posts by Year](#posts-by-year)")
    md.append("- [✍️ Authors](#authors)")

    md.append(f"\n> 💡 **Highlight:** {highlight}")

    # General Stats
    md.append("\n## 📊 General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(set(domains))}")
    md.append("\n[Back to Top](#table-of-contents)")

    # Top Domains
    md.append("\n## 🔗 Top Referenced Domains")
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in domain_counts:
        md.append(f"| {domain} | {count} |")
    md.append("\n[Back to Top](#table-of-contents)")
        md.append(f"| {escape_markdown(domain)} | {count} |")

    # Top Categories
    md.append("\n## 📂 Top Categories")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in category_counts:
        md.append(f"| {cat} | {count} |")
    md.append("\n[Back to Top](#table-of-contents)")
        md.append(f"| {escape_markdown(cat)} | {count} |")

    # Posts by Year
    md.append("\n## 📅 Posts by Year")
    md.append("| Year | Count |")
    md.append("| :--- | :---: |")
    for year, count in year_counts:
        md.append(f"| {year} | {count} |")
    md.append("\n[Back to Top](#table-of-contents)")

    # Authors
    md.append("\n## ✍️ Authors")
    for author, count in author_counts:
        md.append(f"- {author}: {count} posts")
    md.append("\n[Back to Top](#table-of-contents)")
        md.append(f"- {escape_markdown(author)}: {count} posts")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    # Improved Console Feedback with TTY check
    use_color = sys.stdout.isatty()

    file_display = f"\033[1m{output_file}\033[0m" if use_color else output_file

    print(f"\n✨ Report successfully generated: {file_display}")
    print(f"   📊 Analyzed {total_posts} posts")
    if year_counts:
         most_active = sorted(year_counts, key=lambda x: x[1], reverse=True)[0]
         print(f"   📅 Most active year: {most_active[0]} ({most_active[1]} posts)")
    print(f"   💡 Tip: Open {output_file} to view detailed insights.\n")
    # Console Summary
    print(f"\n{Colors.HEADER}📊 Analytics Summary{Colors.ENDC}")
    print(f"{Colors.BLUE}Total Posts:{Colors.ENDC} {total_posts}")
    print(f"{Colors.BLUE}Date Range:{Colors.ENDC} {start_date} to {end_date}")

    if domain_counts:
        top_domain, count = domain_counts[0]
        print(f"{Colors.BLUE}Top Domain:{Colors.ENDC} {top_domain} ({count} refs)")

    print(f"\n{Colors.GREEN}✨ Report generated: {output_file}{Colors.ENDC}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
