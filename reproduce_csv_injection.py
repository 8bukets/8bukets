import csv
import os
import json
from scraper import MarkPositionScraperAsync

def reproduce():
    # Setup
    csv_file = 'reproduce.csv'
    json_file = 'reproduce.json'
    txt_file = 'reproduce.txt'

    scraper = MarkPositionScraperAsync(json_file, csv_file, txt_file)

    # Malicious data
    malicious_posts = [{
        'title': '=cmd|/C calc!A0',
        'date': '2023-01-01',
        'author': '+MaliciousAuthor',
        'categories': ['@Category'],
        'external_link': '-http://evil.com',
        'domain': 'evil.com',
        'post_url': 'http://example.com'
    }]

    # Run save_batch
    with open(json_file, 'w', encoding='utf-8') as json_f, \
         open(csv_file, 'w', newline='', encoding='utf-8') as csv_f, \
         open(txt_file, 'w', encoding='utf-8') as txt_f:

        csv_writer = csv.writer(csv_f)
        scraper.save_batch(malicious_posts, json_f, csv_writer, txt_f, set(), True)

    # Verify
    with open(csv_file, 'r', encoding='utf-8') as f:
        content = f.read()
        print("CSV Content:")
        print(content)

        # Check if the exact dangerous string exists at the START of a cell
        # In CSV, it might look like:
        # '=cmd...,...
        # We want to ensure it is escaped like:
        # ''=cmd...,... (if double quoting) or prepended with '

        # Our sanitization prepends ' so we expect "'=cmd..."

        if "'=cmd|/C calc!A0" in content:
             print("SUCCESS: Payload is sanitized with single quote.")
        elif "=cmd|/C calc!A0" in content:
             # It might be in the content, but we need to check if it's the start of the field.
             # In the raw file, if we see `'=cmd...` that's good.
             # If we see just `=cmd...` at start of line or after comma, that's bad.
             pass

        reader = csv.reader([content.strip()])
        row = next(reader)
        print("Parsed Row:", row)

        if row[0].startswith("'="):
            print("SUCCESS: Title is sanitized.")
        else:
             print(f"FAILURE: Title is NOT sanitized: {row[0]}")

        if row[2].startswith("'+"):
            print("SUCCESS: Author is sanitized.")

        if row[3].startswith("'@"):
            print("SUCCESS: Category is sanitized.")

        if row[4].startswith("'-"):
            print("SUCCESS: External Link is sanitized.")

    # Cleanup
    for f in [csv_file, json_file, txt_file]:
        if os.path.exists(f):
            os.remove(f)

if __name__ == '__main__':
    reproduce()
