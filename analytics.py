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

    # Navigation: Table of Contents
    md.append("\n## Table of Contents")
    md.append("- [General Statistics](#general-statistics)")
    md.append("- [Top 10 Referenced Domains](#top-10-referenced-domains)")
    md.append("- [Top 10 Categories](#top-10-categories)")
    md.append("- [Posts by Year](#posts-by-year)")
    md.append("- [Authors](#authors)")

    md.append("\n## General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(set(domains))}")
    md.append("\n[Back to Top](#table-of-contents)")

    md.append("\n## Top 10 Referenced Domains")
    if domain_counts:
        md.append("| Domain | Count | Share |")
        md.append("| :--- | :---: | :---: |")
        for domain, count in domain_counts:
            share = (count / total_posts) * 100 if total_posts > 0 else 0
            md.append(f"| {domain} | {count} | {share:.1f}% |")
    else:
        md.append("\n*No domain data available.*")
    md.append("\n[Back to Top](#table-of-contents)")

    md.append("\n## Top 10 Categories")
    if category_counts:
        md.append("| Category | Count | Share |")
        md.append("| :--- | :---: | :---: |")
        total_cats = len(all_categories)
        for cat, count in category_counts:
            share = (count / total_cats) * 100 if total_cats > 0 else 0
            md.append(f"| {cat} | {count} | {share:.1f}% |")
    else:
        md.append("\n*No category data available.*")
    md.append("\n[Back to Top](#table-of-contents)")

    md.append("\n## Posts by Year")
    if year_counts:
        md.append("| Year | Count | Share |")
        md.append("| :--- | :---: | :---: |")
        for year, count in year_counts:
            share = (count / total_posts) * 100 if total_posts > 0 else 0
            md.append(f"| {year} | {count} | {share:.1f}% |")
    else:
        md.append("\n*No date data available.*")
    md.append("\n[Back to Top](#table-of-contents)")

    md.append("\n## Authors")
    if author_counts:
        for author, count in author_counts:
            md.append(f"- **{author}**: {count} posts")
    else:
        md.append("\n*No author data available.*")
    md.append("\n[Back to Top](#table-of-contents)")

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
