import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys
from utils import validate_output_path

def create_ascii_bar(count, max_count, bar_length=20):
    """
    Generate an ASCII progress bar for visualizing distributions.

    Args:
        count (int): The current value.
        max_count (int): The maximum value for scaling.
        bar_length (int): Total character length of the bar.

    Returns:
        str: A string representing the progress bar visually.
    """
    if max_count == 0:
        return ""
    filled_length = int(round(bar_length * count / float(max_count)))
    bar = '█' * filled_length + '░' * (bar_length - filled_length)
    return bar

def escape_markdown(text):
    """Escape pipes to prevent breaking Markdown tables."""
    if text is None:
        return ""
    return str(text).replace('|', '&#124;')

def load_data(filepath):
    """
    Load scraped JSON data from a file.

    Args:
        filepath (str): Path to the JSON data file.

    Returns:
        List[Dict]: Parsed data. Exits the program if file is missing.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)

def get_domain(url):
    """
    Extract domain from a given URL string.

    Args:
        url (str): The URL.

    Returns:
        str or None: The parsed domain or None if parsing fails.
    """
    if not url:
        return None
    try:
        return urlparse(url).netloc.replace('www.', '')
    except:
        return None

def generate_report(data, output_file, dry_run=False):
    """
    Generate analytics report from scraped data and write it to a Markdown file.

    Args:
        data (List[Dict]): The scraped JSON data.
        output_file (str): The path to the output Markdown file.
        dry_run (bool): If True, do not write the report to a file.
    """
    total_posts = len(data)

    # 1. Domain Analysis
    domains = []
    for p in data:
        # Optimization: Use pre-calculated domain if available
        d = p.get('domain')
        if d:
            domains.append(d)
        elif p.get('external_link'):
            domains.append(get_domain(p.get('external_link')))

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
        dt = None
        if dt_str:
            try:
                # Handle ISO format
                dt = datetime.fromisoformat(dt_str)
            except ValueError:
                pass

        # Fallback to parsing the 'date' field if 'datetime' is missing or failed
        if dt is None:
            date_str = p.get('date')
            if date_str:
                try:
                    # e.g., "October 5, 2022"
                    dt = datetime.strptime(date_str, "%B %d, %Y")
                except ValueError:
                    pass

        if dt:
            dates.append(dt)

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
    md.append("| Domain | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    max_domain_count = domain_counts[0][1] if domain_counts else 0
    for domain, count in domain_counts:
        bar = create_ascii_bar(count, max_domain_count)
        md.append(f"| {escape_markdown(domain)} | {count} | {bar} |")

    md.append("\n## Top 10 Categories")
    md.append("| Category | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    max_cat_count = category_counts[0][1] if category_counts else 0
    for cat, count in category_counts:
        bar = create_ascii_bar(count, max_cat_count)
        md.append(f"| {escape_markdown(cat)} | {count} | {bar} |")

    md.append("\n## Posts by Year")
    md.append("| Year | Count | Distribution |")
    md.append("| :--- | :---: | :--- |")
    max_year_count = max([c for _, c in year_counts]) if year_counts else 0
    for year, count in year_counts:
        bar = create_ascii_bar(count, max_year_count)
        md.append(f"| {year} | {count} | {bar} |")

    md.append("\n## Authors")
    for author, count in author_counts:
        md.append(f"- {author}: {count} posts")

    if dry_run:
        print(f"Dry run enabled. Would have generated report at: {output_file}")
    else:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(md))
        print(f"Report generated: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Markposition data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    parser.add_argument("--dry-run", action="store_true", help="Run without writing any output files")
    args = parser.parse_args()

    # Validate output path
    output_path = validate_output_path(args.output)

    data = load_data(args.input)
    generate_report(data, output_path, dry_run=args.dry_run)
