import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys

# ANSI Color Codes for Palette UX
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"

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

def generate_ascii_bar(count, max_count, width=20):
    if max_count == 0:
        return ""
    filled = int((count / max_count) * width)
    return "█" * filled + "░" * (width - filled)

def generate_report(data, output_file):
    total_posts = len(data)

    # 1. Domain Analysis
    domains = [get_domain(p.get('external_link')) for p in data if p.get('external_link')]
    domain_counts = Counter(domains).most_common(10)
    max_domain_count = domain_counts[0][1] if domain_counts else 0

    # 2. Category Analysis
    all_categories = []
    for p in data:
        cats = p.get('categories', [])
        if cats:
            all_categories.extend(cats)
    category_counts = Counter(all_categories).most_common(10)
    max_category_count = category_counts[0][1] if category_counts else 0

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

    # Also check 'date' field if datetime is missing or empty list
    if not dates:
        for p in data:
            d_str = p.get('date')
            if d_str:
                try:
                    # Attempt to parse common date formats like "Oct 15, 2025"
                    dt = datetime.strptime(d_str, '%b %d, %Y')
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
        max_year_count = year_counts[0][1] if year_counts else 0
    else:
        start_date = "N/A"
        end_date = "N/A"
        year_counts = []
        max_year_count = 0

    # 4. Author Analysis
    authors = [p.get('author') for p in data if p.get('author')]
    author_counts = Counter(authors).most_common()

    # Generate Markdown
    md = []
    md.append("# 📊 Markposition Analytics Report")
    md.append(f"\n_Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_")

    # Executive Summary
    md.append("\n## 🚀 Executive Summary")
    md.append("| Metric | Value |")
    md.append("| :--- | :--- |")
    md.append(f"| 📝 **Total Posts** | {total_posts} |")
    md.append(f"| 📅 **Date Range** | {start_date} to {end_date} |")
    md.append(f"| 🔗 **Unique Domains** | {len(set(domains))} |")
    md.append(f"| ✍️ **Active Authors** | {len(set(authors))} |")

    # Domains
    md.append("\n## 🌐 Top 10 Referenced Domains")
    md.append("| Domain | Count | Visual |")
    md.append("| :--- | :---: | :--- |")
    for domain, count in domain_counts:
        bar = generate_ascii_bar(count, max_domain_count)
        md.append(f"| {domain} | {count} | `{bar}` |")

    # Categories
    md.append("\n## 🏷️ Top 10 Categories")
    md.append("| Category | Count | Visual |")
    md.append("| :--- | :---: | :--- |")
    for cat, count in category_counts:
        bar = generate_ascii_bar(count, max_category_count)
        md.append(f"| {cat} | {count} | `{bar}` |")

    # Years
    md.append("\n## 🗓️ Posts by Year")
    md.append("| Year | Count | Visual |")
    md.append("| :--- | :---: | :--- |")
    for year, count in year_counts:
        bar = generate_ascii_bar(count, max_year_count)
        md.append(f"| {year} | {count} | `{bar}` |")

    # Authors (Collapsible)
    md.append("\n## ✍️ Authors")
    md.append("<details>")
    md.append(f"<summary>Click to view all {len(author_counts)} authors</summary>\n")
    for author, count in author_counts:
        md.append(f"- **{author}**: {count} posts")
    md.append("</details>")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    # Palette UX: Console Summary
    print(f"\n{GREEN}{BOLD}✅ Analysis Complete!{RESET}")
    print(f"\n{CYAN}📊 Quick Summary:{RESET}")
    print(f"  • {BOLD}Total Posts:{RESET} {total_posts}")
    print(f"  • {BOLD}Date Range:{RESET} {start_date} to {end_date}")

    top_domain = domain_counts[0] if domain_counts else ("None", 0)
    print(f"  • {BOLD}Top Domain:{RESET} {top_domain[0]} ({top_domain[1]})")

    top_cat = category_counts[0] if category_counts else ("None", 0)
    print(f"  • {BOLD}Top Category:{RESET} {top_cat[0]} ({top_cat[1]})")

    print(f"\n{YELLOW}📝 Full report saved to:{RESET} {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
