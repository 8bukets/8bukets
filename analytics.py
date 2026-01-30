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

SECTIONS = {
    "stats": {"title": "General Statistics", "emoji": "📈", "slug": "general-statistics"},
    "domains": {"title": "Top 10 Referenced Domains", "emoji": "🌐", "slug": "top-10-referenced-domains"},
    "categories": {"title": "Top 10 Categories", "emoji": "📂", "slug": "top-10-categories"},
    "years": {"title": "Posts by Year", "emoji": "📅", "slug": "posts-by-year"},
    "authors": {"title": "Authors", "emoji": "✍️", "slug": "authors"},
}

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
            # Match original behavior: include None if get_domain returns it
            # Original: domains = [get_domain(...) for ... if external_link]
            # Counter(domains)
            domain_counts[domain] += 1
            unique_domains.add(domain)

        # 2. Category Analysis
        cats = p.get('categories', [])
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
    md.append("# 📊 Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Table of Contents
    md.append(f"\n## <a name='table-of-contents'></a>Table of Contents")
    for key, info in SECTIONS.items():
        md.append(f"- [{info['emoji']} {info['title']}](#{info['slug']})")

    # Helper for section headers
    def section_header(key):
        info = SECTIONS[key]
        return f"\n## <a name='{info['slug']}'></a>{info['emoji']} {info['title']}"

    def back_to_top():
        return "\n[Back to Top](#table-of-contents)"

    md.append(section_header("stats"))
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(unique_domains)}")
    md.append(back_to_top())

    md.append(section_header("domains"))
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in top_domains:
        md.append(f"| {domain} | {count} |")
    md.append(back_to_top())

    md.append(section_header("categories"))
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in top_categories:
        md.append(f"| {cat} | {count} |")
    md.append(back_to_top())

    md.append(section_header("years"))
    md.append("| Year | Count |")
    md.append("| :--- | :---: |")
    for year, count in sorted_years:
        md.append(f"| {year} | {count} |")
    md.append(back_to_top())

    md.append(section_header("authors"))
    for author, count in sorted_authors:
        md.append(f"- {author}: {count} posts")
    md.append(back_to_top())

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
