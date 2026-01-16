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

def is_valid_date_str(s):
    """
    Fast check if string looks like YYYY-MM-DD.
    Replica of basic validation logic without expensive datetime parsing.
    """
    if not s or len(s) < 10:
        return False
    # Check YYYY-MM-DD format
    if not (s[0:4].isdigit() and s[4] == '-' and s[5:7].isdigit() and s[7] == '-' and s[8:10].isdigit()):
        return False
    return True

def generate_report(data, output_file):
    total_posts = len(data)

    # 1. Domain Analysis
    # Optimization: Use generator to avoid building intermediate list and memory usage
    domains_gen = (get_domain(p.get('external_link')) for p in data if p.get('external_link'))
    all_domains_counter = Counter(domains_gen)
    domain_counts = all_domains_counter.most_common(10)
    unique_domains_count = len(all_domains_counter)

    # 2. Category Analysis
    # Optimization: Use itertools.chain to flatten list of lists lazily, avoiding large intermediate list
    categories_gen = chain.from_iterable(p.get('categories') or [] for p in data)
    category_counts = Counter(categories_gen).most_common(10)

    # 3. Date Analysis
    # Optimization: Use string manipulation for ISO dates (faster than parsing datetime objects)
    # Filter using fast string check instead of try/except datetime.fromisoformat to preserve validation
    date_strings = [p.get('datetime') for p in data if p.get('datetime') and is_valid_date_str(p.get('datetime'))]

    start_date = "N/A"
    end_date = "N/A"
    year_counts = []

    if date_strings:
        date_strings.sort()
        # ISO format sorts lexicographically correct
        start_date = date_strings[0][:10] # YYYY-MM-DD
        end_date = date_strings[-1][:10]

        # Extract year from string "YYYY..."
        years = (d[:4] for d in date_strings)
        year_counts = Counter(years).most_common()
        year_counts.sort(key=lambda x: x[0], reverse=True)

    # 4. Author Analysis
    # Optimization: Use generator
    authors = (p.get('author') for p in data if p.get('author'))
    author_counts = Counter(authors).most_common()

    # Generate Markdown
    md = []
    md.append("# Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    md.append("\n## General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
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
