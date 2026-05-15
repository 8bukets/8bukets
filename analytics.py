import json
import argparse
from collections import Counter
from datetime import datetime
import sys
import html

class Colors:
    GREEN = '\033[92m'
    RESET = '\033[0m'

def sanitize_markdown(text):
    """Sanitize text for Markdown tables to prevent injection."""
    if not isinstance(text, str):
        text = str(text)
    # Escape HTML characters
    text = html.escape(text)
    # Replace pipes with HTML entity to prevent table breakage
    return text.replace('|', '&#124;')

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class UXFormatter:
    @staticmethod
    def info(msg: str):
        print(f"{Colors.BLUE}ℹ️  {msg}{Colors.ENDC}")

    @staticmethod
    def success(msg: str):
        print(f"{Colors.GREEN}✅ {msg}{Colors.ENDC}")

    @staticmethod
    def warning(msg: str):
        print(f"{Colors.YELLOW}⚠️  {msg}{Colors.ENDC}")

    @staticmethod
    def error(msg: str):
        print(f"{Colors.RED}❌ {msg}{Colors.ENDC}")

def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        UXFormatter.error(f"File '{filepath}' not found.")
        sys.exit(1)

def create_ascii_bar(count, max_value, max_width=20):
    if max_value == 0:
        return ""

    filled_len = int((count / max_value) * max_width)
    if filled_len == 0 and count > 0:
        filled_len = 1
    return "█" * filled_len
def create_ascii_bar(value, max_value, width=20):
    if max_value == 0:
        return ""
    bar_length = int((value / max_value) * width)
    if value > 0 and bar_length == 0:
        return "▏"
    return "█" * bar_length

def generate_report(data, output_file):
    total_posts = len(data)

    # 1. Domain Analysis
    domains = [p.get('domain') for p in data if p.get('domain')]
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

    if dates:
        dates.sort()
        start_date = dates[0].strftime('%Y-%m-%d')
        end_date = dates[-1].strftime('%Y-%m-%d')
        years = [d.year for d in dates]
        year_counts = Counter(years).most_common()
        year_counts.sort(key=lambda x: x[0], reverse=True)
        max_year_count = max(count for year, count in year_counts) if year_counts else 0
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
    md.append("# 📈 Markposition Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Table of Contents
    md.append("\n## Table of Contents")
    md.append("- [General Statistics](#general-statistics)")
    md.append("- [Top 10 Referenced Domains](#top-10-referenced-domains)")
    md.append("- [Top 10 Categories](#top-10-categories)")
    md.append("- [Posts by Year](#posts-by-year)")
    md.append("- [Authors](#authors)")

    md.append("\n## 📊 General Statistics")
    md.append(f"- **Total Posts:** {total_posts}")
    md.append(f"- **Date Range:** {start_date} to {end_date}")
    md.append(f"- **Unique Domains Linked:** {len(set(domains))}")
    md.append("\n[Back to Top](#table-of-contents)")

    # Helper to get max count for bars
    max_domain_count = domain_counts[0][1] if domain_counts else 0
    max_cat_count = category_counts[0][1] if category_counts else 0
    max_year_count = max([c for _, c in year_counts]) if year_counts else 0

    md.append("\n## 🌐 Top 10 Referenced Domains")
    md.append("| Domain | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for domain, count in domain_counts:
        bar = create_ascii_bar(count, max_domain_count)
        md.append(f"| {domain} | {count} | {bar} |")

    md.append("\n## 🏷️ Top 10 Categories")
    md.append("| Category | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for cat, count in category_counts:
        bar = create_ascii_bar(count, max_cat_count)
        md.append(f"| {cat} | {count} | {bar} |")

    md.append("\n## 📅 Posts by Year")
    md.append("| Year | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for year, count in year_counts:
        bar = create_ascii_bar(count, max_year_count)
        md.append(f"| {year} | {count} | {bar} |")

    md.append("\n## 🌐 Top 10 Referenced Domains")
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in domain_counts:
        md.append(f"| {sanitize_markdown(domain)} | {count} |")
    md.append("\n## 🔗 Top 10 Referenced Domains")
    md.append("| Domain | Count |")
    md.append("| :--- | :---: |")
    for domain, count in domain_counts:
        md.append(f"| {domain} | {count} |")
    md.append("\n[Back to Top](#table-of-contents)")

    md.append("\n## 📂 Top 10 Categories")
    md.append("| Category | Count |")
    md.append("| :--- | :---: |")
    for cat, count in category_counts:
        md.append(f"| {sanitize_markdown(cat)} | {count} |")
        md.append(f"| {cat} | {count} |")
    md.append("\n[Back to Top](#table-of-contents)")

    md.append("\n## 📅 Posts by Year")
    md.append("| Year | Count |")
    md.append("| :--- | :---: |")
    for year, count in year_counts:
        md.append(f"| {year} | {count} |")
    md.append("\n[Back to Top](#table-of-contents)")
    md.append("\n## 📊 General Statistics")
    md.append(f"- 📝 **Total Posts:** {total_posts}")
    md.append(f"- 📅 **Date Range:** {start_date} to {end_date}")
    md.append(f"- 🔗 **Unique Domains Linked:** {len(set(domains))}")

    md.append("\n## 🌐 Top 10 Referenced Domains")
    md.append("| Domain | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for domain, count in domain_counts:
        bar = create_ascii_bar(count, max_domain_count)
        md.append(f"| {domain} | {count} | {bar} |")

    md.append("\n## 📂 Top 10 Categories")
    md.append("| Category | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for cat, count in category_counts:
        bar = create_ascii_bar(count, max_category_count)
        md.append(f"| {cat} | {count} | {bar} |")

    md.append("\n## 📅 Posts by Year")
    md.append("| Year | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    for year, count in year_counts:
        bar = create_ascii_bar(count, max_year_count)
        md.append(f"| {year} | {count} | {bar} |")

    md.append("\n## ✍️ Authors")
    for author, count in author_counts:
        md.append(f"- {sanitize_markdown(author)}: {count} posts")

    md.append("\n---\nGenerated with ❤️ by Palette")
        md.append(f"- {author}: {count} posts")
    md.append("\n[Back to Top](#table-of-contents)")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md))

    UXFormatter.success(f"Report generated: {output_file}")

    # Print summary to console
    print(f"\n{Colors.BOLD}Summary:{Colors.ENDC}")
    print(f"- Total Posts: {total_posts}")
    print(f"- Unique Domains: {len(set(domains))}")
    print(f"- Date Range: {start_date} to {end_date}")
    print(f"{Colors.GREEN}Report generated: {output_file}{Colors.RESET}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    args = parser.parse_args()

    data = load_data(args.input)
    generate_report(data, args.output)
