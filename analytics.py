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

def create_ascii_bar(count, max_count, bar_length=20):
    if max_count == 0:
        return "░" * bar_length
    filled_len = int((count / max_count) * bar_length)
    empty_len = bar_length - filled_len
    return "█" * filled_len + "░" * empty_len

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
    md.append("# 📈 Wordpress Blog Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Table of Contents
<<<<<<< palette-ux-report-improvements-9630359626298714094
    md.append("\n<a name='table-of-contents'></a>")
    md.append("## 📑 Table of Contents")
    md.append("- [📊 General Statistics](#general-statistics)")
    md.append("- [🔗 Top Referenced Domains](#top-referenced-domains)")
    md.append("- [🏷️ Top Categories](#top-categories)")
    md.append("- [📅 Posts by Year](#posts-by-year)")
    md.append("- [✍️ Authors](#authors)")

    md.append("\n<a name='general-statistics'></a>")
    md.append("## 📊 General Statistics")
=======
    md.append("\n## Table of Contents <a id='table-of-contents'></a>")
    md.append("- [📊 General Statistics](#general-statistics)")
    md.append("- [🔗 Top 10 Referenced Domains](#top-10-referenced-domains)")
    md.append("- [🏷️ Top 10 Categories](#top-10-categories)")
    md.append("- [📅 Posts by Year](#posts-by-year)")
    md.append("- [✍️ Authors](#authors)")

    md.append("\n## 📊 General Statistics <a id='general-statistics'></a>")
>>>>>>> artmusicpage-scraper-13642650452924627148
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(set(domains))}")
    md.append("\n[Back to Top](#table-of-contents)")

<<<<<<< palette-ux-report-improvements-9630359626298714094
    md.append("\n<a name='top-referenced-domains'></a>")
    md.append("## 🔗 Top 10 Referenced Domains")
=======
    md.append("\n## 🔗 Top 10 Referenced Domains <a id='top-10-referenced-domains'></a>")
>>>>>>> artmusicpage-scraper-13642650452924627148
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in domain_counts:
        md.append(f"| {domain} | {count} |")
    md.append("\n[Back to Top](#table-of-contents)")

<<<<<<< palette-ux-report-improvements-9630359626298714094
    md.append("\n<a name='top-categories'></a>")
    md.append("## 🏷️ Top 10 Categories")
=======
    md.append("\n## 🏷️ Top 10 Categories <a id='top-10-categories'></a>")
>>>>>>> artmusicpage-scraper-13642650452924627148
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in category_counts:
        md.append(f"| {cat} | {count} |")
    md.append("\n[Back to Top](#table-of-contents)")

<<<<<<< palette-ux-report-improvements-9630359626298714094
    md.append("\n<a name='posts-by-year'></a>")
    md.append("## 📅 Posts by Year")
=======
    md.append("\n## 📅 Posts by Year <a id='posts-by-year'></a>")
>>>>>>> artmusicpage-scraper-13642650452924627148
    md.append("| Year | Count |")
    md.append("| :--- | :---: |")
    for year, count in year_counts:
        md.append(f"| {year} | {count} |")
    md.append("\n[Back to Top](#table-of-contents)")
<<<<<<< palette-ux-report-improvements-9630359626298714094

    md.append("\n<a name='authors'></a>")
    md.append("## ✍️ Authors")
=======
    # Helper for max counts
    max_domain_count = domain_counts[0][1] if domain_counts else 0
    max_category_count = category_counts[0][1] if category_counts else 0
    max_year_count = max((count for year, count in year_counts), default=0)

    md.append("\n## Top 10 Referenced Domains")
    md.append("| Domain | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for domain, count in domain_counts:
        bar = create_ascii_bar(count, max_domain_count)
        md.append(f"| {domain} | {count} | {bar} |")

    md.append("\n## Top 10 Categories")
    md.append("| Category | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for cat, count in category_counts:
        bar = create_ascii_bar(count, max_category_count)
        md.append(f"| {cat} | {count} | {bar} |")

    md.append("\n## Posts by Year")
    md.append("| Year | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for year, count in year_counts:
        bar = create_ascii_bar(count, max_year_count)
        md.append(f"| {year} | {count} | {bar} |")

    md.append("\n## ✍️ Authors <a id='authors'></a>")
>>>>>>> artmusicpage-scraper-13642650452924627148
    for author, count in author_counts:
        md.append(f"- {author}: {count} posts")
    md.append("\n[Back to Top](#table-of-contents)")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    print(f"Report generated: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for WordPress blog data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
