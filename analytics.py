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

    @staticmethod
    def colorize(text, color):
        if sys.stdout.isatty():
            return f"{color}{text}{Colors.ENDC}"
        return text

def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(Colors.colorize(f"Error: File '{filepath}' not found.", Colors.FAIL))
        sys.exit(1)

def get_domain(url):
    if not url:
        return None
    try:
        return urlparse(url).netloc.replace('www.', '')
    except:
        return None

def print_summary_box(stats):
    # Calculate box width
    width = 50
    horizontal = "─" * (width - 2)

    print(Colors.colorize(f"\n┌{horizontal}┐", Colors.CYAN))
    print(Colors.colorize(f"│ {'ANALYTICS SUMMARY'.center(width - 4)} │", Colors.CYAN + Colors.BOLD))
    print(Colors.colorize(f"├{horizontal}┤", Colors.CYAN))

    # Stats rows
    rows = [
        ("Total Posts", str(stats['total_posts'])),
        ("Date Range", f"{stats['start_date']} to {stats['end_date']}"),
        ("Top Domain", f"{stats['top_domain'][0]} ({stats['top_domain'][1]})" if stats['top_domain'] else "N/A"),
        ("Top Category", f"{stats['top_category'][0]} ({stats['top_category'][1]})" if stats['top_category'] else "N/A"),
        ("Unique Domains", str(stats['unique_domains']))
    ]

    for label, value in rows:
        # Truncate value if too long to fit
        max_val_len = width - 4 - len(label) - 2 # 2 for ": "
        if len(value) > max_val_len:
            value = value[:max_val_len-1] + "…"

        line = f"│ {Colors.colorize(label, Colors.GREEN)}: {value}"
        # Adjust padding calculation to account for color codes length being invisible
        # But here we added color codes to 'line', so standard len() is wrong.
        # We need to construct the visual string length separately.
        padding = " " * (width - 4 - len(label) - 2 - len(value))
        print(f"{line}{padding} {Colors.colorize('│', Colors.CYAN)}")

    print(Colors.colorize(f"└{horizontal}┘", Colors.CYAN))
    print(f"\nReport generated: {Colors.colorize(stats['output_file'], Colors.BLUE)}")

def generate_report(data, output_file):
    total_posts = len(data)

    # 1. Domain Analysis
    domains = [get_domain(p.get('external_link')) for p in data if p.get('external_link')]
    domain_counts = Counter(domains).most_common(10)
    unique_domains = len(set(domains))

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
    md.append(f"- **Unique Domains Linked:** {unique_domains}")

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

    # Print Summary Box
    stats = {
        "total_posts": total_posts,
        "start_date": start_date,
        "end_date": end_date,
        "unique_domains": unique_domains,
        "top_domain": domain_counts[0] if domain_counts else None,
        "top_category": category_counts[0] if category_counts else None,
        "output_file": output_file
    }
    print_summary_box(stats)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
