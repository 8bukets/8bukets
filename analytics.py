import json
import argparse
from collections import Counter
from urllib.parse import urlparse
from datetime import datetime
import sys
import re

def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return [] # Return empty list instead of exit for robustness

def get_domain(url):
    if not url:
        return None
    try:
        return urlparse(url).netloc.replace('www.', '')
    except:
        return None

def analyze_keywords(data, top_n=10):
    """Extracts top keywords from titles."""
    stop_words = {
        'the', 'and', 'in', 'of', 'for', 'a', 'to', 'on', 'with', 'at', 'by',
        'from', 'is', 'it', 'your', 'my', 'webshop', 'online', 'store', 'shop',
        'official', 'website', 'site', 'hr', 'com', 'eu', 'collection', 'new',
        'sale', 'best', 'buy', 'free', 'shipping', 'delivery', 'price', 'deals',
        'offer', 'discount', 'save', 'get', 'up', 'off', 'all', 'more'
    }

    all_words = []
    for p in data:
        title = p.get('title', '').lower()
        # Remove special chars
        words = re.findall(r'\b\w+\b', title)
        for w in words:
            if w not in stop_words and len(w) > 2:
                all_words.append(w)

    return Counter(all_words).most_common(top_n)

def detect_new_posts(current_data, prev_data):
    """Identifies posts present in current but not in prev."""
    if not prev_data:
        return []

    prev_urls = {p.get('post_url') for p in prev_data if p.get('post_url')}
    new_posts = []

    for p in current_data:
        if p.get('post_url') and p.get('post_url') not in prev_urls:
            new_posts.append(p)

    return new_posts

def generate_report(data, output_file, prev_data=None):
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

    # 5. Intelligent Analysis
    top_keywords = analyze_keywords(data)
    new_posts = detect_new_posts(data, prev_data) if prev_data else []

    # Generate Markdown
    md = []
    md.append("# Webshop Analytics Report")
    md.append(f"\n**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    md.append("\n## Daily Insights")
    if new_posts:
        md.append(f"**🚀 {len(new_posts)} New Posts Detected!**")
        for p in new_posts[:5]: # List top 5
            md.append(f"- [{p.get('title', 'Untitled')}]({p.get('post_url')})")
        if len(new_posts) > 5:
            md.append(f"- ...and {len(new_posts) - 5} more.")
    else:
        md.append("No new posts detected since last run.")

    md.append("\n### Trending Keywords")
    md.append("| Keyword | Frequency |")
    md.append("| :--- | :---: |")
    for kw, count in top_keywords:
        md.append(f"| {kw} | {count} |")

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

    print(f"Report generated: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate analytics report for Webshop data")
    parser.add_argument("--input", default="links.json", help="Input JSON file")
    parser.add_argument("--output", default="REPORT.md", help="Output Markdown report file")
    parser.add_argument("--prev", help="Previous JSON file for comparison", required=False)
    args = parser.parse_args()

    data = load_data(args.input)
    prev_data = load_data(args.prev) if args.prev else None

    generate_report(data, args.output, prev_data)
