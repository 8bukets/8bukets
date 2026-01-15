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

def create_bar_chart(input_data, width=30):
    """Generates an ASCII bar chart for the given data (list of (label, value) tuples)."""
    if not input_data:
        return ""

    max_val = max(item[1] for item in input_data) if input_data else 0
    chart = []
    for label, value in input_data:
        if max_val > 0:
            bar_len = int((value / max_val) * width)
        else:
            bar_len = 0
        bar_str = '█' * bar_len
        empty = '░' * (width - bar_len)
        # Truncate label if too long
        display_label = (label[:23] + '..') if len(str(label)) > 25 else f"{str(label):<25}"
        chart.append(
            f"{display_label} {Colors.BLUE}{bar_str}{Colors.ENDC}"
            f"{Colors.CYAN}{empty}{Colors.ENDC} {value}"
        )
    return "\n".join(chart)

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
    md.append("# Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    md.append("\n## General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(unique_domains)}")

    md.append("\n## Top 10 Referenced Domains")
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in top_domains:
        md.append(f"| {domain} | {count} |")

    md.append("\n## Top 10 Categories")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in top_categories:
        md.append(f"| {cat} | {count} |")

    md.append("\n## Posts by Year")
    md.append("| Year | Count |")
    md.append("| :--- | :---: |")
    for year, count in sorted_years:
        md.append(f"| {year} | {count} |")

    md.append("\n## Authors")
    for author, count in sorted_authors:
        md.append(f"- {author}: {count} posts")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    # UX Improvement: Visual Summary to Console
    print(f"\n{Colors.GREEN}{Colors.BOLD}✨ Report generated successfully!{Colors.ENDC}")
    print(f"{Colors.BOLD}📁 File:{Colors.ENDC} {output_file}")

    print(f"\n{Colors.HEADER}📊 Quick Summary:{Colors.ENDC}")
    print(f"  • {Colors.BOLD}Total Posts:{Colors.ENDC} {total_posts}")
    print(f"  • {Colors.BOLD}Date Range:{Colors.ENDC}  {start_date} to {end_date}")
    print(f"  • {Colors.BOLD}Unique Domains:{Colors.ENDC} {len(unique_domains)}")

    print(f"\n{Colors.BOLD}🏆 Top 5 Domains:{Colors.ENDC}")
    print(create_bar_chart(domain_counts.most_common(5)))

    print(f"\n{Colors.CYAN}💡 Pro tip: Open {output_file} for full analysis "
          f"including authors and categories.{Colors.ENDC}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
