import json
import argparse
from collections import Counter
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

def create_ascii_bar(value, max_value, width=20):
    if max_value == 0:
        return '░' * width
    fill_len = int((value / max_value) * width)
    return '█' * fill_len + '░' * (width - fill_len)

def escape_markdown(text):
    if text is None:
        return ""
    text = str(text)
    return text.replace('|', '&#124;')

def generate_report(data, output_file):
    total_posts = len(data)

    # 1. Domain Analysis
    # Optimization: Use pre-computed 'domain' field instead of re-parsing 'external_link'
    domains = [p.get('domain') for p in data if p.get('domain')]
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
    md.append("# <a id='markposition-analytics-report'></a>Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Table of Contents
    md.append("\n## Table of Contents")
    md.append("- [📊 General Statistics](#general-statistics)")
    md.append("- [🌐 Top 10 Referenced Domains](#top-10-referenced-domains)")
    md.append("- [📂 Top 10 Categories](#top-10-categories)")
    md.append("- [📅 Posts by Year](#posts-by-year)")
    md.append("- [✍️ Authors](#authors)")

    md.append("\n## <a id='general-statistics'></a>📊 General Statistics")
    if domain_counts:
        top_domain = domain_counts[0]
        md.append(f"> 💡 **Highlight:** The most referenced domain is **{top_domain[0]}** with {top_domain[1]} citations.")

    md.append(f"\n- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(set(domains))}")
    md.append("\n[Back to Top](#markposition-analytics-report)")

    md.append("\n## <a id='top-10-referenced-domains'></a>🌐 Top 10 Referenced Domains")
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in domain_counts:
        md.append(f"| {domain} | {count} |")
    md.append("\n[Back to Top](#markposition-analytics-report)")

    md.append("\n## <a id='top-10-categories'></a>📂 Top 10 Categories")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in category_counts:
        md.append(f"| {cat} | {count} |")
    md.append("\n[Back to Top](#markposition-analytics-report)")

    md.append("\n## <a id='posts-by-year'></a>📅 Posts by Year")
    md.append("| Year | Count |")
    md.append("| :--- | :---: |")
    for year, count in year_counts:
        md.append(f"| {year} | {count} |")
    md.append("\n[Back to Top](#markposition-analytics-report)")
    # Max values for charts
    max_domain_count = domain_counts[0][1] if domain_counts else 0
    max_category_count = category_counts[0][1] if category_counts else 0
    max_year_count = max([c for y, c in year_counts]) if year_counts else 0

    md.append("\n## Top 10 Referenced Domains")
    md.append("| Domain | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for domain, count in domain_counts:
        bar = create_ascii_bar(count, max_domain_count)
        md.append(f"| {escape_markdown(domain)} | {count} | {bar} |")

    md.append("\n## Top 10 Categories")
    md.append("| Category | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for cat, count in category_counts:
        bar = create_ascii_bar(count, max_category_count)
        md.append(f"| {escape_markdown(cat)} | {count} | {bar} |")

    md.append("\n## Posts by Year")
    md.append("| Year | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for year, count in year_counts:
        bar = create_ascii_bar(count, max_year_count)
        md.append(f"| {year} | {count} | {bar} |")

    md.append("\n## <a id='authors'></a>✍️ Authors")
    for author, count in author_counts:
        md.append(f"- {author}: {count} posts")
    md.append("\n[Back to Top](#markposition-analytics-report)")
        md.append(f"- {escape_markdown(author)}: {count} posts")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    print(f"✨ Report generated: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
