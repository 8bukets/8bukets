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
        parsed = urlparse(url)
        if not parsed.netloc:
            return None
        return parsed.netloc.replace('www.', '')
    except:
        return None

def generate_report(data, output_file):
    total_posts = len(data)

    # 1. Domain Analysis
    domains = [get_domain(p.get('external_link')) for p in data if p.get('external_link')]
    # Filter out None
    domains = [d for d in domains if d]
    domain_counts = Counter(domains).most_common() # Get all for analysis

    # 2. Category Analysis
    all_categories = []
    for p in data:
        cats = p.get('categories', [])
        if cats:
            all_categories.extend(cats)
    category_counts = Counter(all_categories).most_common()

    # Calculate Category Dominance
    if category_counts:
        top_cat, top_cat_count = category_counts[0]
        dominance_pct = (top_cat_count / total_posts) * 100
        dominance_str = f"{top_cat} ({dominance_pct:.1f}%)"
    else:
        dominance_str = "N/A"

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
        days_active = (dates[-1] - dates[0]).days
    else:
        start_date = "N/A"
        end_date = "N/A"
        year_counts = []
        days_active = 0

    # 4. Author Analysis
    authors = [p.get('author') for p in data if p.get('author')]
    author_counts = Counter(authors).most_common()

    # Generate Markdown
    md = []
    md.append("# 📊 Wordpress Blog Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Executive Summary
    md.append("\n## 🚀 Executive Summary")
    md.append("| Metric | Value | Status |")
    md.append("| :--- | :--- | :---: |")
    md.append(f"| Total Posts | {total_posts} | 📚 |")
    md.append(f"| Date Range | {start_date} to {end_date} | 🗓️ |")
    md.append(f"| Days Active | {days_active} days | ⏱️ |")
    md.append(f"| Unique Domains | {len(set(domains))} | 🔗 |")
    md.append(f"| Category Dominance | {dominance_str} | 🏆 |")

    # Table of Contents
    md.append("\n## 📑 Table of Contents")
    md.append("- [Executive Summary](#-executive-summary)")
    md.append("- [Top Referenced Domains](#-top-referenced-domains)")
    md.append("- [Categories](#-categories)")
    md.append("- [Posts by Year](#-posts-by-year)")
    md.append("- [Authors](#-authors)")

    # Top Domains
    md.append("\n## 🌐 Top Referenced Domains")
    md.append("Top 10 most linked domains in posts.")
    md.append("\n| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in domain_counts[:10]:
        md.append(f"| {domain} | {count} |")

    # Collapsible full list if more than 10
    if len(domain_counts) > 10:
        md.append("\n<details>")
        md.append("<summary>View all domains</summary>\n")
        md.append("| Domain | Count |")
        md.append("| :--- | :---: |")
        for domain, count in domain_counts[10:]:
            md.append(f"| {domain} | {count} |")
        md.append("\n</details>")

    md.append("\n[Back to Top](#-wordpress-blog-analytics-report)")

    # Categories
    md.append("\n## 🏷️ Categories")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in category_counts[:10]:
        md.append(f"| {cat} | {count} |")

    if len(category_counts) > 10:
        md.append("\n<details>")
        md.append("<summary>View all categories</summary>\n")
        md.append("| Category | Count |")
        md.append("| :--- | :---: |")
        for cat, count in category_counts[10:]:
            md.append(f"| {cat} | {count} |")
        md.append("\n</details>")

    md.append("\n[Back to Top](#-wordpress-blog-analytics-report)")

    # Posts by Year
    md.append("\n## 📅 Posts by Year")
    md.append("| Year | Count |")
    md.append("| :--- | :---: |")
    for year, count in year_counts:
        md.append(f"| {year} | {count} |")

    md.append("\n[Back to Top](#-wordpress-blog-analytics-report)")

    # Authors
    md.append("\n## ✍️ Authors")
    if len(author_counts) > 5:
        # Show top 5 then collapse
        md.append("Top 5 contributors:")
        for author, count in author_counts[:5]:
            md.append(f"- **{author}**: {count} posts")

        md.append("\n<details>")
        md.append(f"<summary>View all {len(author_counts)} authors</summary>\n")
        for author, count in author_counts[5:]:
            md.append(f"- {author}: {count} posts")
        md.append("\n</details>")
    else:
        for author, count in author_counts:
            md.append(f"- **{author}**: {count} posts")

    md.append("\n[Back to Top](#-wordpress-blog-analytics-report)")

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
