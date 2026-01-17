import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys
from itertools import chain

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
    # Optimization: Use generator expression to avoid creating intermediate list in memory
    domains = (get_domain(p.get('external_link')) for p in data if p.get('external_link'))
    domain_counts = Counter(domains).most_common(10)

    # 2. Category Analysis
    # Optimization: Use chain.from_iterable to avoid creating a large intermediate list of all categories
    # chain.from_iterable efficiently iterates over the sublists without building a single flat list first
    all_categories = chain.from_iterable((p.get('categories') or []) for p in data)
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
    # Optimization: Use generator expression to avoid creating intermediate list
    authors = (p.get('author') for p in data if p.get('author'))
    author_counts = Counter(authors).most_common()

    # Generate Markdown
    md = []
    md.append("# Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    md.append("\n## General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    # Note: len(set(domains)) would consume the generator if we reused it, but we already consumed it in Counter.
    # To get unique domains count efficiently without storing all domains, we can use the keys from domain_counts if we had the full counter.
    # But domain_counts is only top 10.
    # So we strictly speaking need to iterate again or store the counter.

    # Re-calculating unique domains count.
    # Since we need the count of unique items, we have to iterate again or store the set.
    # The original code did: len(set(domains)).
    # But now 'domains' is a generator that is already exhausted by Counter(domains).
    # So we need to re-create the generator or keep the full Counter object.

    # Let's verify what the original code did.
    # original: domains = [list]... domain_counts = Counter(domains).most_common(10) ... len(set(domains))

    # To preserve functionality and memory efficiency:
    # We can create a full Counter first.

    domains_gen = (get_domain(p.get('external_link')) for p in data if p.get('external_link'))
    full_domain_counts = Counter(domains_gen)
    domain_counts = full_domain_counts.most_common(10)
    unique_domains_count = len(full_domain_counts)

    md.append(f"- **Unique Domains Linked:** {unique_domains_count}")

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

    print(f"Report generated: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
