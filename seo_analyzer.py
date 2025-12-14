import json
import collections
import re
from datetime import datetime
import argparse

def analyze_seo(json_file, output_file):
    print(f"Loading data from {json_file}...")
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {json_file} not found. Please run scraper.py first.")
        return

    print(f"Analyzing {len(data)} entries...")

    # 1. Title Keyword Analysis
    stop_words = {
        'the', 'and', 'to', 'of', 'a', 'in', 'for', 'on', 'with', 'is', 'at', 'by',
        'from', 'it', 'that', 'this', 'as', 'be', 'or', 'an', 'are', 'was', 'your',
        'more', 'we', 'will', 'can', 'you', 'has', 'have', 'our', 'my', 'home',
        'news', 'best', 'site', 'website', 'official', 'top', 'online', 'free', 'new'
    }

    words = []
    for item in data:
        title = item.get('title', '').lower()
        # Simple tokenization
        tokens = re.findall(r'\b\w+\b', title)
        for token in tokens:
            if token not in stop_words and len(token) > 2:
                words.append(token)

    word_counts = collections.Counter(words)
    top_keywords = word_counts.most_common(20)

    # 2. Posting Frequency Analysis
    dates = []
    missing_dates = 0
    for item in data:
        date_str = item.get('date', '')
        if not date_str or date_str == "No Date":
            missing_dates += 1
            continue

        try:
            # Format: "February 25, 2022"
            dt = datetime.strptime(date_str, '%B %d, %Y')
            dates.append(dt)
        except ValueError:
            pass

    posts_per_year = collections.Counter([d.year for d in dates])
    posts_per_month = collections.Counter([d.strftime('%Y-%m') for d in dates])

    # Generate Report
    print(f"Generating report to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# SEO Analysis Report for malubeach.wordpress.com\n\n")
        f.write(f"**Total Items Scraped:** {len(data)}\n\n")

        f.write("## Top 20 Keywords in Titles\n")
        f.write("Using these keywords in your content and meta descriptions helps Google understand your niche.\n\n")
        f.write("| Keyword | Frequency |\n")
        f.write("| :--- | :---: |\n")
        for word, count in top_keywords:
            f.write(f"| {word} | {count} |\n")
        f.write("\n")

        f.write("## Posting Frequency (Activity)\n")
        f.write("Consistent updates are key for SEO rankings.\n\n")

        if missing_dates > 0:
            f.write(f"**Note:** {missing_dates} posts had no visible date. This often happens with 'sticky' posts or specific theme settings. Ensure your posts display dates if freshness is important.\n\n")

        f.write("### Posts by Year (where date was found)\n")
        if posts_per_year:
            for year, count in sorted(posts_per_year.items(), reverse=True):
                f.write(f"- **{year}**: {count} posts\n")
        else:
            f.write("No dated posts found.\n")
        f.write("\n")

        f.write("### Recent Activity (Last 12 Active Months)\n")
        if posts_per_month:
            sorted_months = sorted(posts_per_month.items(), reverse=True)
            for month, count in sorted_months[:12]:
                 f.write(f"- **{month}**: {count} posts\n")
        else:
             f.write("No dated posts found.\n")

        f.write("\n## Insights\n")
        f.write("- **Content Volume**: ")
        if len(data) > 1000:
            f.write("High. You have a large archive of content, which is good for authority.\n")
        else:
            f.write("Moderate/Low. Consider increasing content volume.\n")

        f.write("- **Keyword Strategy**: Review the top keywords above. Are they relevant to what you want to rank for? ")
        f.write("If 'uncategorized' or generic words appear too often, refine your titles.\n")

    print("Done.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SEO Analyzer")
    parser.add_argument('--input', default='links.json', help='Input JSON file')
    parser.add_argument('--output', default='SEO_REPORT.md', help='Output Report file')
    args = parser.parse_args()

    analyze_seo(args.input, args.output)
