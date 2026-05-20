import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys
from utils import validate_output_path

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
    # Optimization: Use pre-calculated domain directly to avoid expensive parsing
    domains = [d for p in data if (d := p.get('domain'))]

    domain_counts = Counter(domains).most_common(10)
    top_domain = domain_counts[0][0] if domain_counts else "N/A"
    top_domain_count = domain_counts[0][1] if domain_counts else 0

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
        dt = None
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
    md.append("# 📊 Markposition Analytics Report")
    md.append("<a name='table-of-contents'></a>")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    md.append("\n## Table of Contents")
    md.append("* [General Statistics](#general-statistics)")
    md.append("* [Top 10 Referenced Domains](#top-10-referenced-domains)")
    md.append("* [Top 10 Categories](#top-10-categories)")
    md.append("* [Posts by Year](#posts-by-year)")
    md.append("* [Authors](#authors)")

    md.append("\n<a name='general-statistics'></a>")
    md.append("## 📈 General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(set(domains))}")
    md.append("\n[Back to Top](#table-of-contents)")

    md.append("\n<a name='top-10-referenced-domains'></a>")
    md.append("## 🌐 Top 10 Referenced Domains")
    # Table of Contents
    md.append("\n## Table of Contents")
    md.append("- [📊 General Statistics](#general-statistics)")
    md.append("- [🌐 Top 10 Referenced Domains](#top-10-referenced-domains)")
    md.append("- [📂 Top 10 Categories](#top-10-categories)")
    md.append("- [📅 Posts by Year](#posts-by-year)")
    md.append("- [✍️ Authors](#authors)")

    # General Statistics
    md.append("\n## 📊 General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(set(domains))}")
    if top_domain != "N/A":
        md.append(f"\n> 💡 **Highlight:** The most referenced domain is **{top_domain}** with {top_domain_count} links.")
    md.append("\n[Back to Top](#table-of-contents)")

    # Domains
    md.append("\n## 🌐 Top 10 Referenced Domains")
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in domain_counts:
        md.append(f"| {domain} | {count} |")
    md.append("\n[Back to Top](#table-of-contents)")

    md.append("\n<a name='top-10-categories'></a>")
    md.append("## 📂 Top 10 Categories")
    # Categories
    md.append("\n## 📂 Top 10 Categories")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in category_counts:
        md.append(f"| {cat} | {count} |")
    md.append("\n[Back to Top](#table-of-contents)")

    md.append("\n<a name='posts-by-year'></a>")
    md.append("## 📅 Posts by Year")
    # Years
    md.append("\n## 📅 Posts by Year")
    md.append("| Year | Count |")
    md.append("| :--- | :---: |")
    for year, count in year_counts:
        md.append(f"| {year} | {count} |")
    md.append("\n[Back to Top](#table-of-contents)")

    md.append("\n<a name='authors'></a>")
    md.append("## ✍️ Authors")
    for author, count in author_counts:
        md.append(f"- {author}: {count} posts")
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
        md.append(f"- **{author}**: {count} posts")
    md.append("\n[Back to Top](#table-of-contents)")

    md.append("\n---\nAll the best - https://markposition.wordpress.com")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    # Console UX
    if sys.stdout.isatty():
        print(f"\033[92m✨ Report generated successfully: {output_file}\033[0m") # Green text
    else:
        print(f"✨ Report generated successfully: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    # Validate output path
    output_path = validate_output_path(args.output)

    data = load_data(args.input)
    generate_report(data, output_path)
