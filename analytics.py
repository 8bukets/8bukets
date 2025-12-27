import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def sanitize_markdown_cell(text):
    if not isinstance(text, str):
        return str(text)
    return text.replace("\\", "\\\\").replace("|", "\\|").replace("\n", " ")


def print_summary(total_posts, start_date, end_date,
                  unique_domains, top_domain, top_category, output_file):
    print(f"\n{Colors.HEADER}📊 Markposition Analytics Report{Colors.ENDC}")
    print(f"{Colors.BLUE}{'-'*30}{Colors.ENDC}")

    print(f"{Colors.BOLD}📅 Date Range:{Colors.ENDC} "
          f"{start_date} to {end_date}")
    print(f"{Colors.BOLD}📝 Total Posts:{Colors.ENDC} {total_posts}")
    print(f"{Colors.BOLD}🔗 Unique Domains:{Colors.ENDC} {unique_domains}")

    if top_domain:
        print(f"\n{Colors.CYAN}🏆 Top Domain:{Colors.ENDC} "
              f"{top_domain[0]} ({top_domain[1]})")
    if top_category:
        print(f"{Colors.CYAN}📂 Top Category:{Colors.ENDC} "
              f"{top_category[0]} ({top_category[1]})")

    print(f"\n{Colors.GREEN}✅ Report generated:{Colors.ENDC} "
          f"{output_file}\n")


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
    except Exception:
        return None


def generate_report(data, output_file):
    total_posts = len(data)

    # 1. Domain Analysis
    domains = [
        get_domain(p.get('external_link'))
        for p in data if p.get('external_link')
    ]
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
    md.append(
        f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    md.append("\n## General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(set(domains))}")

    md.append("\n## Top 10 Referenced Domains")
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in domain_counts:
        safe_domain = sanitize_markdown_cell(domain)
        md.append(f"| {safe_domain} | {count} |")

    md.append("\n## Top 10 Categories")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in category_counts:
        md.append(f"| {sanitize_markdown_cell(cat)} | {count} |")

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

    print_summary(
        total_posts,
        start_date,
        end_date,
        len(set(domains)),
        domain_counts[0] if domain_counts else None,
        category_counts[0] if category_counts else None,
        output_file
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate analytics report for Markposition data"
    )
    parser.add_argument(
        "--input", default="links.json", help="Input JSON file"
    )
    parser.add_argument(
        "--output", default="REPORT.md", help="Output Markdown report file"
    )
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
