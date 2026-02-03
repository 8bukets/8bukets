import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys

# Define Colors for CLI output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"{Colors.RED}❌ Error: File '{filepath}' not found.{Colors.RESET}")
        print(f"{Colors.YELLOW}💡 Tip: Run scraper.py first to generate data.{Colors.RESET}")
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
    domains = [get_domain(p.get('external_link')) for p in data if p.get('external_link')]
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

    # Rich Console Output
    print(f"\n{Colors.GREEN}✨ Report generated successfully!{Colors.RESET}")
    print(f"{Colors.BLUE}📄 Location: {Colors.BOLD}{output_file}{Colors.RESET}")
    print(f"\n{Colors.HEADER}📊 Quick Summary:{Colors.RESET}")
    print(f"  • Total Posts: {Colors.CYAN}{total_posts}{Colors.RESET}")
    print(f"  • Date Range:  {Colors.CYAN}{start_date}{Colors.RESET} to {Colors.CYAN}{end_date}{Colors.RESET}")
    print(f"  • Top Domain:  {Colors.CYAN}{domain_counts[0][0] if domain_counts else 'N/A'}{Colors.RESET}")
    print(f"  • Top Category: {Colors.CYAN}{category_counts[0][0] if category_counts else 'N/A'}{Colors.RESET}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
