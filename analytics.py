import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys
import os

def validate_path(filepath: str) -> str:
    """
    Validates that the filepath is safe and within the current working directory.
    Returns the absolute path if safe, raises ValueError otherwise.
    """
    abs_path = os.path.abspath(filepath)
    cwd = os.path.abspath(os.getcwd())
    if os.path.commonpath([cwd, abs_path]) != cwd:
        raise ValueError(f"Security Error: Path '{filepath}' attempts to access outside the working directory.")
    return abs_path

def create_ascii_bar(count, max_count, bar_length=20):
    """Generate an ASCII progress bar."""
    if max_count == 0:
        return ""
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

    # 1. Domain Analysis
    domains = []
    for p in data:
        # Optimization: Use pre-calculated domain if available
        d = p.get('domain')
        if d:
            domains.append(d)
        elif p.get('external_link'):
            domains.append(get_domain(p.get('external_link')))

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

    most_active_year = "N/A"
    most_active_year_count = 0

    if dates:
        dates.sort()
        start_date = dates[0].strftime('%Y-%m-%d')
        end_date = dates[-1].strftime('%Y-%m-%d')
        years = [d.year for d in dates]
        year_counts = Counter(years).most_common()
        year_counts.sort(key=lambda x: x[0], reverse=True)

        # Determine highlight (most active year)
        if year_counts:
            # Re-sort by count to find the max
            sorted_by_count = sorted(year_counts, key=lambda x: x[1], reverse=True)
            most_active_year = sorted_by_count[0][0]
            most_active_year_count = sorted_by_count[0][1]
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
    md.append("\n## Table of Contents")
    md.append("- [General Statistics](#general-statistics)")
    md.append("- [Top 10 Referenced Domains](#top-10-referenced-domains)")
    md.append("- [Top 10 Categories](#top-10-categories)")
    md.append("- [Posts by Year](#posts-by-year)")
    md.append("- [Authors](#authors)")

    # General Statistics
    md.append("\n## 📊 General Statistics")
    if most_active_year != "N/A":
        md.append(f"> 💡 **Highlight:** The most active year was **{most_active_year}** with **{most_active_year_count}** posts!")

    md.append(f"\n- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(set(domains))}")
    md.append("\n[Back to Top](#table-of-contents)")

    # Top Domains
    md.append("\n## 🔗 Top 10 Referenced Domains")
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in domain_counts:
        md.append(f"| {domain} | {count} |")
    md.append("\n[Back to Top](#table-of-contents)")

    # Top Categories
    md.append("\n## 📂 Top 10 Categories")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in category_counts:
        md.append(f"| {cat} | {count} |")
    md.append("\n[Back to Top](#table-of-contents)")

    # Posts by Year
    md.append("\n## 📅 Posts by Year")
    md.append("| Year | Count |")
    md.append("| :--- | :---: |")
    for year, count in year_counts:
        md.append(f"| {year} | {count} |")
    md.append("\n[Back to Top](#table-of-contents)")
    md.append("\n## Top 10 Referenced Domains")
    md.append("| Domain | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    max_domain_count = domain_counts[0][1] if domain_counts else 0
    for domain, count in domain_counts:
        bar = create_ascii_bar(count, max_domain_count)
        md.append(f"| {escape_markdown(domain)} | {count} | {bar} |")

    md.append("\n## Top 10 Categories")
    md.append("| Category | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    max_cat_count = category_counts[0][1] if category_counts else 0
    for cat, count in category_counts:
        bar = create_ascii_bar(count, max_cat_count)
        md.append(f"| {escape_markdown(cat)} | {count} | {bar} |")

    md.append("\n## Posts by Year")
    md.append("| Year | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    max_year_count = max([c for _, c in year_counts]) if year_counts else 0
    for year, count in year_counts:
        bar = create_ascii_bar(count, max_year_count)
        md.append(f"| {year} | {count} | {bar} |")

    # Authors
    md.append("\n## ✍️ Authors")
    for author, count in author_counts:
        md.append(f"- {author}: {count} posts")
    md.append("\n[Back to Top](#table-of-contents)")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    print(f"Report generated: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    try:
        input_path = validate_path(args.input)
        output_path = validate_path(args.output)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    data = load_data(input_path)
    generate_report(data, output_path)
