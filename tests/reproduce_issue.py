import sys
import os
import csv

# Add current directory to path
sys.path.append(os.getcwd())

try:
    from scraper import OracleNewsScraper
except ImportError:
    # If running from tests/ directory
    sys.path.append(os.path.join(os.getcwd(), '..'))
    from scraper import OracleNewsScraper

def check_csv_injection():
    output_json = 'test_links.json'
    output_csv = 'test_links.csv'
    output_txt = 'test_links.txt'

    scraper = OracleNewsScraper(output_json, output_csv, output_txt)

    malicious_post = {
        'title': '=1+1',
        'date': 'Oct 15, 2025',
        'author': '@Admin',
        'categories': ['+Formula'],
        'external_link': '-link',
        'domain': 'example.com',
        'post_url': 'http://example.com'
    }

    scraper.save_data([malicious_post])

    with open(output_csv, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader)
        row = next(reader)

        # Check title
        title = row[0]
        author = row[2]
        categories = row[3]
        external_link = row[4]

    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Categories: {categories}")
    print(f"External Link: {external_link}")

    # Cleanup
    for f in [output_json, output_csv, output_txt]:
        if os.path.exists(f):
            os.remove(f)

    vulnerable = False
    if title.startswith('='): vulnerable = True
    if author.startswith('@'): vulnerable = True
    if categories.startswith('+'): vulnerable = True
    if external_link.startswith('-'): vulnerable = True

    if vulnerable:
        print("\nRESULT: VULNERABLE (Unsanitized inputs found)")
    else:
        print("\nRESULT: SECURE (Inputs sanitized)")

if __name__ == "__main__":
    check_csv_injection()
