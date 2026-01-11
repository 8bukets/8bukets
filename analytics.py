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

def make_bar(count, max_count, width=20):
    """Generate a visual progress bar."""
    if max_count == 0:
        return ""
    filled = int((count / max_count) * width)
    return "█" * filled + "░" * (width - filled)

def generate_report(data, output_file):
    total_posts = len(data)

    # 1. Domain Analysis
    domains = [p.get('domain') for p in data if p.get('domain')]
    domain_counts = Counter(domains).most_common(10)
    max_domain_count = domain_counts[0][1] if domain_counts else 0

    # 2. Category Analysis
    all_categories = []
    for p in data:
        cats = p.get('categories', [])
        if cats:
            all_categories.extend(cats)
    category_counts = Counter(all_categories).most_common(10)
    max_cat_count = category_counts[0][1] if category_counts else 0

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
        max_year_count = max(count for _, count in year_counts) if year_counts else 0
    else:
        start_date = "N/A"
        end_date = "N/A"
        year_counts = []
        max_year_count = 0

    # 4. Author Analysis
    authors = [p.get('author') for p in data if p.get('author')]
    author_counts = Counter(authors).most_common()

    # Generate Markdown
    md = []
    md.append(f"# 🎨 Markposition Analytics Report")
    md.append(f"\n_Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_")

    # Executive Summary Table
    md.append("\n## 📊 Executive Summary")
    md.append("| Metric | Value |")
    md.append("| :--- | :--- |")
    md.append(f"| 📝 **Total Posts** | {total_posts} |")
    md.append(f"| 📅 **Date Range** | {start_date} to {end_date} |")
    md.append(f"| 🌐 **Unique Domains** | {len(set(domains))} |")
    md.append(f"| 🏷️ **Unique Categories** | {len(set(all_categories))} |")
    md.append(f"| ✍️ **Active Authors** | {len(set(authors))} |")

    # Top Domains with Collapsible Details and Visual Bars
    md.append("\n<details open>")
    md.append("<summary><h2>🌐 Top 10 Referenced Domains</h2></summary>\n")
    md.append("| Domain | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for domain, count in domain_counts:
        bar = make_bar(count, max_domain_count)
        md.append(f"| {domain} | {count} | `{bar}` |")
    md.append("</details>")

    # Top Categories
    md.append("\n<details>")
    md.append("<summary><h2>🏷️ Top 10 Categories</h2></summary>\n")
    md.append("| Category | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for cat, count in category_counts:
        bar = make_bar(count, max_cat_count)
        md.append(f"| {cat} | {count} | `{bar}` |")
    md.append("</details>")

    # Posts by Year
    md.append("\n<details>")
    md.append("<summary><h2>📅 Posts by Year</h2></summary>\n")
    md.append("| Year | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for year, count in year_counts:
        bar = make_bar(count, max_year_count)
        md.append(f"| {year} | {count} | `{bar}` |")
    md.append("</details>")

    # Authors
    md.append("\n<details>")
    md.append("<summary><h2>✍️ Authors</h2></summary>\n")
    md.append("| Author | Posts |")
    md.append("| :--- | :---: |")
    for author, count in author_counts:
        md.append(f"| {author} | {count} |")
    md.append("</details>")

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
