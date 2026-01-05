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

def _generate_ascii_bar(count, total, width=20):
    """Generates an ASCII bar chart representation."""
    if total == 0:
        return "░" * width
    percentage = count / total
    filled_length = int(width * percentage)
    bar = "▓" * filled_length + "░" * (width - filled_length)
    return bar

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
    total_domain_refs = sum(domain_counts.values())

    # Categories: top 10 by count
    top_categories = category_counts.most_common(10)
    total_category_refs = sum(category_counts.values())

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
    total_year_refs = sum(year_counts.values())

    # Authors: all by count descending (most_common does this)
    sorted_authors = author_counts.most_common()

    # Generate Markdown
    md = []
    md.append("# Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    md.append("\n## General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(unique_domains)}")

    md.append("\n## Top 10 Referenced Domains")
    md.append("| Domain | Count | % | Distribution |")
    md.append("| :--- | :---: | :---: | :--- |")
    for domain, count in top_domains:
        pct = (count / total_domain_refs) * 100
        bar = _generate_ascii_bar(count, total_domain_refs)
        md.append(f"| {domain} | {count} | {pct:.1f}% | {bar} |")

    md.append("\n## Top 10 Categories")
    md.append("| Category | Count | % | Distribution |")
    md.append("| :--- | :---: | :---: | :--- |")
    for cat, count in top_categories:
        pct = (count / total_category_refs) * 100
        bar = _generate_ascii_bar(count, total_category_refs)
        md.append(f"| {cat} | {count} | {pct:.1f}% | {bar} |")

    md.append("\n## Posts by Year")
    md.append("| Year | Count | % | Distribution |")
    md.append("| :--- | :---: | :---: | :--- |")
    for year, count in sorted_years:
        pct = (count / total_year_refs) * 100
        bar = _generate_ascii_bar(count, total_year_refs)
        md.append(f"| {year} | {count} | {pct:.1f}% | {bar} |")

    md.append("\n## Authors")
    for author, count in sorted_authors:
        md.append(f"- {author}: {count} posts")

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
