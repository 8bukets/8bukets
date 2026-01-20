import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys
import html

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

def sanitize_markdown(text):
    """Sanitize text for use in Markdown tables."""
    if text is None:
        return ""
    # Escape HTML characters and pipes
    return html.escape(str(text)).replace('|', r'\|')

def generate_report(data, output_file):
    total_posts = len(data)

    # Initialize counters and trackers
    domain_counts = Counter()
    category_counts = Counter()
    author_counts = Counter()
    year_counts = Counter()

    min_date = None
    max_date = None

    unique_domains = set()

    # Single pass iteration
    for p in data:
        # 1. Domain Analysis
        external_link = p.get('external_link')
        if external_link:
            domain = get_domain(external_link)
            domain_counts[domain] += 1
            unique_domains.add(domain)

        # 2. Category Analysis
        cats = p.get('categories', []) or []
        if cats:
            category_counts.update(cats)

        # 3. Date Analysis
        dt_str = p.get('datetime')
        if dt_str:
            try:
                # Handle ISO format
                dt = datetime.fromisoformat(dt_str)

                # Track min/max dates
                if min_date is None or dt < min_date:
                    min_date = dt
                if max_date is None or dt > max_date:
                    max_date = dt

                # Track year
                year_counts[dt.year] += 1
            except ValueError:
                pass

        # 4. Author Analysis
        author = p.get('author')
        if author:
            author_counts[author] += 1

    # Prepare data for report

    # Domains: top 10 by count
    top_domains = domain_counts.most_common(10)

    # Categories: top 10 by count
    top_categories = category_counts.most_common(10)

    # Dates: range and years sorted by year descending
    if min_date and max_date:
        start_date = min_date.strftime('%Y-%m-%d')
        end_date = max_date.strftime('%Y-%m-%d')
        # Sort years descending (key is year)
        sorted_years = sorted(year_counts.items(), key=lambda x: x[0], reverse=True)
    else:
        start_date = "N/A"
        end_date = "N/A"
        sorted_years = []

    # Authors: all by count descending (most_common does this)
    sorted_authors = author_counts.most_common()

    # Generate Markdown
    md = []

    # Header & TOC
    md.append('<a name="top"></a>')
    md.append("# 📊 Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    md.append("\n## 📑 Table of Contents")
    md.append("- [General Statistics](#general-statistics)")
    md.append("- [Top 10 Referenced Domains](#top-10-referenced-domains)")
    md.append("- [Top 10 Categories](#top-10-categories)")
    md.append("- [Posts by Year](#posts-by-year)")
    md.append("- [Authors](#authors)")

    # General Stats
    md.append('\n<a name="general-statistics"></a>')
    md.append("## 📈 General Statistics")
    md.append(f"- **Total Posts:** {total_posts:,}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(unique_domains):,}")
    md.append("\n[⬆ Back to Top](#top)")

    # Domains
    md.append('\n<a name="top-10-referenced-domains"></a>')
    md.append("## 🌐 Top 10 Referenced Domains")
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in top_domains:
        md.append(f"| {sanitize_markdown(domain)} | {count:,} |")
    md.append("\n[⬆ Back to Top](#top)")

    # Categories
    md.append('\n<a name="top-10-categories"></a>')
    md.append("## 🏷️ Top 10 Categories")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in top_categories:
        md.append(f"| {sanitize_markdown(cat)} | {count:,} |")
    md.append("\n[⬆ Back to Top](#top)")

    # Years
    md.append('\n<a name="posts-by-year"></a>')
    md.append("## 📅 Posts by Year")
    md.append("| Year | Count |")
    md.append("| :--- | :---: |")
    for year, count in sorted_years:
        # Visualize with a simple bar
        # Scale: max count is 100%
        # max_count = max(y[1] for y in sorted_years) if sorted_years else 1
        # bar_len = int((count / max_count) * 20)
        # bar = "█" * bar_len + "░" * (20 - bar_len)
        # md.append(f"| {year} | {count:,} |")
        # Keeping it simple for now as per original, just adding formatting
        md.append(f"| {year} | {count:,} |")
    md.append("\n[⬆ Back to Top](#top)")

    # Authors
    md.append('\n<a name="authors"></a>')
    md.append("## ✍️ Authors")
    for author, count in sorted_authors:
        md.append(f"- **{sanitize_markdown(author)}**: {count:,} posts")
    md.append("\n[⬆ Back to Top](#top)")

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
