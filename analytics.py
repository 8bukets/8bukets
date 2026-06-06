import json
import os
import argparse
from collections import Counter
from datetime import datetime
import sys
from utils import validate_output_path
from urllib.parse import urlparse

def create_ascii_bar(count, max_count, bar_length=20):
    """Generate an ASCII progress bar."""
    if max_count == 0:
        return "░" * bar_length
    filled_length = int(round(bar_length * count / float(max_count)))
    bar = '█' * filled_length + '░' * (bar_length - filled_length)
    return bar

def escape_markdown(text):
    """Escape pipes to prevent breaking Markdown tables."""
    if text is None:
        return ""
    return str(text).replace('|', '&#124;')

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

    domains = []
    all_categories = []
    dates = []
    authors = []

    # Single pass over data
    for p in data:
        # 1. Domain Analysis
        ext_link = p.get('external_link')
        if ext_link:
            domains.append(p.get('domain') or get_domain(ext_link))

        # 2. Category Analysis
        cats = p.get('categories', [])
        if cats:
            all_categories.extend(cats)

        # 3. Date Analysis
        dt = None
        dt_str = p.get('datetime')
        if dt_str:
            try:
                # Handle ISO format
                dt = datetime.fromisoformat(dt_str)
            except ValueError:
                pass

        # Fallback to parsing the 'date' field if 'datetime' is missing or failed
        if dt is None:
            date_str = p.get('date')
            if date_str:
                try:
                    # e.g., "October 5, 2022"
                    dt = datetime.strptime(date_str, "%B %d, %Y")
                except ValueError:
                    pass

        if dt:
            dates.append(dt)

        # 4. Author Analysis
        author = p.get('author')
        if author:
            authors.append(author)

    domain_counts = Counter(domains).most_common(10)
    top_domain = domain_counts[0][0] if domain_counts else "N/A"
    top_domain_count = domain_counts[0][1] if domain_counts else 0

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

    # Max counts for bars
    max_domain_count = domain_counts[0][1] if domain_counts else 0
    max_category_count = category_counts[0][1] if category_counts else 0
    max_year_count = max((count for year, count in year_counts), default=0)

    # Generate Markdown
    md = []
    md.append("# 📈 Wordpress Blog Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Table of Contents
    md.append("\n<a name='table-of-contents'></a>")
    md.append("## 📑 Table of Contents")
    md.append("- [📊 General Statistics](#general-statistics)")
    md.append("- [🔗 Top Referenced Domains](#top-referenced-domains)")
    md.append("- [🏷️ Top Categories](#top-categories)")
    md.append("- [📅 Posts by Year](#posts-by-year)")
    md.append("- [✍️ Authors](#authors)")

    md.append("\n<a name='general-statistics'></a>")
    md.append("## 📊 General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(set(domains))}")
    if top_domain != "N/A":
        md.append(f"\n> 💡 **Highlight:** The most referenced domain is **{top_domain}** with {top_domain_count} links.")
    md.append("\n[Back to Top](#table-of-contents)")

    md.append("\n<a name='top-referenced-domains'></a>")
    md.append("## 🔗 Top 10 Referenced Domains")
    md.append("| Domain | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for domain, count in domain_counts:
        bar = create_ascii_bar(count, max_domain_count)
        md.append(f"| {escape_markdown(domain)} | {count} | {bar} |")
    md.append("\n[Back to Top](#table-of-contents)")

    md.append("\n<a name='top-categories'></a>")
    md.append("## 🏷️ Top 10 Categories")
    md.append("| Category | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for cat, count in category_counts:
        bar = create_ascii_bar(count, max_category_count)
        md.append(f"| {cat} | {count} | {bar} |")
    md.append("\n[Back to Top](#table-of-contents)")

    md.append("\n<a name='posts-by-year'></a>")
    md.append("## 📅 Posts by Year")
    md.append("| Year | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for year, count in year_counts:
        bar = create_ascii_bar(count, max_year_count)
        md.append(f"| {year} | {count} | {bar} |")
    md.append("\n[Back to Top](#table-of-contents)")

    md.append("\n<a name='authors'></a>")
    md.append("## ✍️ Authors")
    for author, count in author_counts:
        md.append(f"- {author}: {count} posts")
    md.append("\n[Back to Top](#table-of-contents)")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    # Console UX
    if sys.stdout.isatty():
        print(f"\033[92m✨ Report generated successfully: {output_file}\033[0m") # Green text
    else:
        print(f"✨ Report generated successfully: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for WordPress blog data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    # Validate output path
    output_path = validate_output_path(args.output)

    data = load_data(args.input)
    generate_report(data, output_path)
