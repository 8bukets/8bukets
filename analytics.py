import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys
import re
import os

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

    @staticmethod
    def strip(text):
        return re.sub(r'\x1b\[[0-9;]*m', '', text)

def print_summary_box(title, lines):
    # Check if we should use colors
    use_color = sys.stdout.isatty() or os.environ.get('FORCE_COLOR')

    def get_visible_len(s):
        return len(s) + sum(1 for char in s if char in '🚀⏱️📄📊🔗🏆📅')

    stripped_title = Colors.strip(title)
    stripped_lines = [Colors.strip(line) for line in lines]

    max_len = max([get_visible_len(l) for l in stripped_lines] + [get_visible_len(stripped_title)]) if lines else get_visible_len(stripped_title)
    width = max_len + 2 # Padding

    # Border colors
    BORDER = Colors.CYAN if use_color else ''
    RESET = Colors.ENDC if use_color else ''

    # Helper to format line
    def fmt_line(content, raw_content):
        # content is stripped, raw_content has colors
        visible_len = get_visible_len(content)
        padding = width - visible_len + 1
        text = raw_content if use_color else content
        return f"{BORDER}│{RESET} {text}{' ' * padding}{BORDER}│{RESET}"

    print(f"{BORDER}┌{'─' * (width + 2)}┐{RESET}")
    print(fmt_line(stripped_title, title))
    print(f"{BORDER}├{'─' * (width + 2)}┤{RESET}")

    for i, line in enumerate(lines):
        print(fmt_line(stripped_lines[i], line))

    print(f"{BORDER}└{'─' * (width + 2)}┘{RESET}")

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

    # Prepare summary lines for CLI
    summary_lines = []
    summary_lines.append(f"📄 Total Posts: {Colors.GREEN}{total_posts}{Colors.ENDC}")
    summary_lines.append(f"📅 Date Range: {start_date} to {end_date}")
    summary_lines.append("")
    summary_lines.append(f"{Colors.YELLOW}🏆 Top Domains:{Colors.ENDC}")
    for i, (domain, count) in enumerate(domain_counts[:3]):
         summary_lines.append(f"{i+1}. {domain} ({count})")

    print_summary_box("📊 Analytics Summary", summary_lines)
    print(f"\nReport generated: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for WordPress blog data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
