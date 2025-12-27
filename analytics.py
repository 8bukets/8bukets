import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys

def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

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

    # Summary Box
    # Define widths for dynamic sizing
    # Minimum width 42 to accommodate title, max determined by content
    # Titles
    t_file = "📂 File:   "
    t_posts = "📝 Posts:  "
    t_range = "📅 Range:  "

    # Values
    v_file = output_file
    v_posts = str(total_posts)
    v_range = f"{start_date} to {end_date}"

    # Calculate content lengths
    # Note: Emojis like 📂, 📝, 📅 take 2 visual spaces but len() counts 1.
    # We add +1 for each emoji line to account for this in padding calculation.

    # Length of "Title + Value"
    len_file = len(t_file) + len(v_file) + 1 # +1 for emoji
    len_posts = len(t_posts) + len(v_posts) + 1 # +1 for emoji
    len_range = len(t_range) + len(v_range) + 1 # +1 for emoji

    # "📊 Analytics Report Ready!"
    # String length: 26 chars. Visual length: 26 + 1 (for 📊) = 27.
    # We need to account for this if we want strict centering or just make box wide enough.

    # Let's set a minimum content width of 40.
    max_content_len = max(40, len_file, len_posts, len_range)

    # Build lines with padding
    def pad_line(title, value, color_val=None):
        content = f"{title}{color_val if color_val else ''}{value}{Colors.ENDC if color_val else ''}"
        # Correct visual length calculation: len(title) + len(value) + 1 (for emoji in title)
        visible_len = len(title) + len(value) + 1
        padding = max_content_len - visible_len
        return f"{Colors.CYAN}│  {content}{' ' * padding}  │{Colors.ENDC}"

    # Borders
    top_border = f"{Colors.CYAN}┌{'─' * (max_content_len + 4)}┐{Colors.ENDC}"
    bot_border = f"{Colors.CYAN}└{'─' * (max_content_len + 4)}┘{Colors.ENDC}"

    # Header line
    # "📊 Analytics Report Ready!" len is 26. Visual is 27.
    # Padding needed: (max_content_len + 4) - (2 (indent) + 27 (visual) + 2 (right border space? no, we want right align))
    # Correct math:
    # Box inner width: max_content_len + 4 (spaces)
    # We print: │  (2 spaces) [TEXT] [PADDING]  (2 spaces) │
    # Total inner width available: max_content_len + 4.
    # Used: 2 (left margin) + 27 (visual text).
    # Remaining for padding: (max_content_len + 4) - 29.
    header_padding = max_content_len + 4 - 29

    print(f"\n{top_border}")
    print(f"{Colors.CYAN}│  📊 Analytics Report Ready!{' ' * header_padding}│{Colors.ENDC}")
    print(f"{Colors.CYAN}│{' ' * (max_content_len + 4)}│{Colors.ENDC}")
    print(pad_line(t_file, v_file, Colors.BOLD))
    print(pad_line(t_posts, v_posts, Colors.GREEN))
    print(pad_line(t_range, v_range))
    print(f"{bot_border}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
