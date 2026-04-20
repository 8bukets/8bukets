import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

def print_summary_box(stats):
    if not sys.stdout.isatty():
        print(f"Report generated: {stats['report_file']}")
        return

    w_label = 14
    w_value = 30
    width = w_label + w_value + 5 # | L... V... | => 1+1+L+1+V+1+1 = L+V+5

    def row(label, value):
        val = str(value)
        if len(val) > w_value:
            val = val[:w_value-3] + "..."
        print(f"| {Colors.GREEN}{label:<{w_label}}{Colors.ENDC} {Colors.BOLD}{val:<{w_value}}{Colors.ENDC}{Colors.CYAN}{Colors.BOLD} |")

    print(f"\n{Colors.CYAN}{Colors.BOLD}+{'-' * (width - 2)}+")
    print(f"|{'ANALYTICS SUMMARY'.center(width - 2)}|")
    print(f"+{'-' * (width - 2)}+")

    row("Total Posts:", stats['total_posts'])
    row("Date Range:", f"{stats['start_date']} to {stats['end_date']}")

    top_dom = stats['top_domain']
    if isinstance(top_dom, tuple): top_dom = f"{top_dom[0]} ({top_dom[1]})"
    row("Top Domain:", top_dom)

    top_cat = stats['top_category']
    if isinstance(top_cat, tuple): top_cat = f"{top_cat[0]} ({top_cat[1]})"
    row("Top Category:", top_cat)

    print(f"+{'-' * (width - 2)}+")
    report_val = stats['report_file']
    if len(report_val) > width - 12:
        report_val = report_val[:width-15] + "..."
    print(f"| Report: {report_val:<{width-12}} |")
    print(f"+{'-' * (width - 2)}+{Colors.ENDC}\n")

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

def create_ascii_bar(count, max_count, bar_length=20):
    if max_count == 0:
        return "░" * bar_length
    filled_len = int((count / max_count) * bar_length)
    empty_len = bar_length - filled_len
    return "█" * filled_len + "░" * empty_len

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
    md.append("# Wordpress Blog Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    md.append("\n## General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(set(domains))}")

    # Helper for max counts
    max_domain_count = domain_counts[0][1] if domain_counts else 0
    max_category_count = category_counts[0][1] if category_counts else 0
    max_year_count = max((count for year, count in year_counts), default=0)

    md.append("\n## Top 10 Referenced Domains")
    md.append("| Domain | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for domain, count in domain_counts:
        bar = create_ascii_bar(count, max_domain_count)
        md.append(f"| {domain} | {count} | {bar} |")

    md.append("\n## Top 10 Categories")
    md.append("| Category | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for cat, count in category_counts:
        bar = create_ascii_bar(count, max_category_count)
        md.append(f"| {cat} | {count} | {bar} |")

    md.append("\n## Posts by Year")
    md.append("| Year | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for year, count in year_counts:
        bar = create_ascii_bar(count, max_year_count)
        md.append(f"| {year} | {count} | {bar} |")

    md.append("\n## Authors")
    for author, count in author_counts:
        md.append(f"- {author}: {count} posts")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    # Prepare stats for summary
    stats = {
        'total_posts': total_posts,
        'start_date': start_date,
        'end_date': end_date,
        'top_domain': domain_counts[0] if domain_counts else ('None', 0),
        'top_category': category_counts[0] if category_counts else ('None', 0),
        'report_file': output_file
    }
    print_summary_box(stats)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for WordPress blog data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
