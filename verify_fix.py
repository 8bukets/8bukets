import csv
import os
from scraper import OracleNewsScraper

def test_csv_injection_fix():
    output_json = "test_links.json"
    output_csv = "test_links.csv"
    output_txt = "test_unique_links.txt"

    # Clean up previous runs
    if os.path.exists(output_csv):
        os.remove(output_csv)

    scraper = OracleNewsScraper(output_json, output_csv, output_txt)

    malicious_post = {
        'title': '=1+1',
        'date': '@today',
        'author': '+attacker',
        'categories': ['-bad'],
        'external_link': 'http://example.com',
        'domain': 'example.com',
        'post_url': 'http://example.com/post'
    }

    scraper.save_data([malicious_post])

    # Read CSV and verify fix
    with open(output_csv, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        row = next(reader)

        print(f"Row content: {row}")

        # Check sanitization
        sanitized = True
        if not row[0].startswith("'="):
            print("Fix Verification Failed: Title not sanitized correctly")
            sanitized = False
        if not row[1].startswith("'@"):
            print("Fix Verification Failed: Date not sanitized correctly")
            sanitized = False
        if not row[2].startswith("'+"):
            print("Fix Verification Failed: Author not sanitized correctly")
            sanitized = False
        if not row[3].startswith("'-"):
             print("Fix Verification Failed: Categories not sanitized correctly")
             sanitized = False

        if sanitized:
            print("TEST PASSED: Data successfully sanitized.")
        else:
            print("TEST FAILED: Data not sanitized.")

    # Clean up
    for f in [output_json, output_csv, output_txt]:
        if os.path.exists(f):
            os.remove(f)

if __name__ == "__main__":
    test_csv_injection_fix()
