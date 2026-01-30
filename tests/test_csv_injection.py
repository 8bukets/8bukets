import sys
import os
import csv
import json

# Add parent directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

def test_csv_injection():
    # Setup
    json_file = 'tests/temp.json'
    csv_file = 'tests/temp.csv'
    txt_file = 'tests/temp.txt'

    # Cleanup before test
    for f in [json_file, csv_file, txt_file]:
        if os.path.exists(f):
            os.remove(f)

    scraper = MarkPositionScraperAsync(json_file, csv_file, txt_file)

    # Malicious data
    malicious_data = [
        {
            'title': '=cmd| /C calc',
            'date': '+2023-01-01',
            'author': '@attacker',
            'categories': ['-category'],
            'external_link': 'http://example.com',
            'domain': 'example.com',
            'post_url': 'http://wordpress.com/post'
        }
    ]

    # Execute
    scraper.save_data(malicious_data)

    # Verify
    with open(csv_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        row = next(reader)

        # Columns: Title, Date, Author, Categories, External Link, Domain, Post URL
        title = row[0]
        date = row[1]
        author = row[2]
        categories = row[3]

        print(f"Title: {title}")
        print(f"Date: {date}")
        print(f"Author: {author}")
        print(f"Categories: {categories}")

        # Check for sanitization
        sanitized = True
        if not title.startswith("'="):
            print(f"Title is NOT sanitized properly! Got: {title}")
            sanitized = False
        if not date.startswith("'+"):
            print(f"Date is NOT sanitized properly! Got: {date}")
            sanitized = False
        if not author.startswith("'@"):
            print(f"Author is NOT sanitized properly! Got: {author}")
            sanitized = False
        if not categories.startswith("'-"):
            print(f"Categories is NOT sanitized properly! Got: {categories}")
            sanitized = False

        if sanitized:
            print("SUCCESS: CSV Injection prevented.")
            sys.exit(0)
        else:
            print("FAILURE: Vulnerability still present.")
            sys.exit(1)

if __name__ == "__main__":
    test_csv_injection()
