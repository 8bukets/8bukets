import json
import argparse
from collections import Counter
from datetime import datetime
import sys

class Colors:
    _is_tty = sys.stdout.isatty()

    HEADER = '\033[95m' if _is_tty else ''
    OKBLUE = '\033[94m' if _is_tty else ''
    OKCYAN = '\033[96m' if _is_tty else ''
    OKGREEN = '\033[92m' if _is_tty else ''
    WARNING = '\033[93m' if _is_tty else ''
    FAIL = '\033[91m' if _is_tty else ''
    ENDC = '\033[0m' if _is_tty else ''
    BOLD = '\033[1m' if _is_tty else ''
    UNDERLINE = '\033[4m' if _is_tty else ''

def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{Colors.FAIL}Error: File '{filepath}' not found.{Colors.ENDC}")
        sys.exit(1)

def generate_report(data, output_file):
    total_posts = len(data)

    # 1. Domain Analysis
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
    md.append("# Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    md.append("\n## General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(set(domains))}")

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

    # Print Summary to Console
    print(f"\n{Colors.HEADER}{Colors.BOLD}Markposition Analytics Report{Colors.ENDC}")
    print(f"{Colors.HEADER}-----------------------------{Colors.ENDC}")
    print(f"{Colors.OKCYAN}Total Posts:{Colors.ENDC}      {total_posts}")
    print(f"{Colors.OKCYAN}Date Range:{Colors.ENDC}       {start_date} to {end_date}")
    print(f"{Colors.OKCYAN}Unique Domains:{Colors.ENDC}   {len(set(domains))}")
    if category_counts:
        top_cat, top_cat_count = category_counts[0]
        print(f"{Colors.OKCYAN}Top Category:{Colors.ENDC}     {top_cat} ({top_cat_count})")

    print(f"\n{Colors.OKGREEN}✔ Report generated successfully: {output_file}{Colors.ENDC}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
