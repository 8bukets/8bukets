import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys

# ANSI Color Codes for Palette UX
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

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

    # Optimization: Aggregate all statistics in a single pass over the data
    # to avoid multiple iterations (O(N) instead of O(4N)) and reduce memory usage.

    # Initialize counters and accumulators
    domain_counter = Counter()
    category_counter = Counter()
    author_counter = Counter()
    year_counter = Counter()
    dates = []

    # Single pass processing
    for p in data:
        # 1. Domain Analysis
        ext_link = p.get('external_link')
        if ext_link:
            domain = get_domain(ext_link)
            domain_counter[domain] += 1

        # 2. Category Analysis
        cats = p.get('categories', [])
        if cats:
            category_counter.update(cats)

        # 3. Date Analysis
        dt_str = p.get('datetime')
        if dt_str:
            try:
                # Handle ISO format
                dt = datetime.fromisoformat(dt_str)
                dates.append(dt)
                year_counter[dt.year] += 1
            except ValueError:
                pass

        # 4. Author Analysis
        author = p.get('author')
        if author:
            author_counter[author] += 1

    # Post-process results

    # Domains
    domain_counts = domain_counter.most_common(10)

    # Categories
    category_counts = category_counter.most_common(10)

    # Dates
    if dates:
        dates.sort()
        start_date = dates[0].strftime('%Y-%m-%d')
        end_date = dates[-1].strftime('%Y-%m-%d')
    else:
        start_date = "N/A"
        end_date = "N/A"

    # Years (sorted by year descending)
    year_counts = sorted(year_counter.items(), key=lambda x: x[0], reverse=True)

    # Authors
    author_counts = author_counter.most_common()

    # Generate Markdown
    md = []
    md.append("# Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    md.append("\n## General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    # len(domain_counter) gives number of unique keys (domains)
    md.append(f"- **Unique Domains Linked:** {len(domain_counter)}")

    md.append("\n## Top 10 Referenced Domains")
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in domain_counts:
        md.append(f"| {domain} | {count} |")

    md.append("\n## Top 10 Categories")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in category_counts:
        md.append(f"| {cat} | {count} |")

    md.append("\n## Posts by Year")
    md.append("| Year | Count |")
    md.append("| :--- | :---: |")
    for year, count in year_counts:
        md.append(f"| {year} | {count} |")

    md.append("\n## Authors")
    for author, count in author_counts:
        md.append(f"- {author}: {count} posts")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    # Palette UX: Console Summary
    print(f"\n{GREEN}{BOLD}✅ Analysis Complete!{RESET}")
    print(f"\n{CYAN}📊 Quick Summary:{RESET}")
    print(f"  • {BOLD}Total Posts:{RESET} {total_posts}")
    print(f"  • {BOLD}Date Range:{RESET} {start_date} to {end_date}")

    top_domain = domain_counts[0] if domain_counts else ("None", 0)
    print(f"  • {BOLD}Top Domain:{RESET} {top_domain[0]} ({top_domain[1]})")

    top_cat = category_counts[0] if category_counts else ("None", 0)
    print(f"  • {BOLD}Top Category:{RESET} {top_cat[0]} ({top_cat[1]})")

    print(f"\n{YELLOW}📝 Full report saved to:{RESET} {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
