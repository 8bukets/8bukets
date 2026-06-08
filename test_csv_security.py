from scraper import OracleNewsScraper
import os
import csv
import logging

# Disable logging
logging.disable(logging.CRITICAL)

def test_csv_security():
    output_json = "test_links.json"
    output_csv = "test_links.csv"
    output_txt = "test_unique_links.txt"

    # Cleanup previous run
    for f in [output_json, output_csv, output_txt]:
        if os.path.exists(f):
            os.remove(f)

    scraper = OracleNewsScraper(output_json, output_csv, output_txt)

    malicious_data = [
        {
            'title': '=cmd|/C calc!A0',
            'date': '+2023-01-01',
            'author': '-Author',
            'categories': ['@Category'],
            'external_link': 'http://example.com',
            'domain': 'example.com',
            'post_url': 'http://example.com/post'
        }
    ]

    normal_data = [
         {
            'title': 'Normal Title',
            'date': '2023-01-01',
            'author': 'Author',
            'categories': ['Category'],
            'external_link': 'http://example.com',
            'domain': 'example.com',
            'post_url': 'http://example.com/post'
        }
    ]

    print("Running save_data with malicious input...")
    scraper.save_data(malicious_data)

    print(f"Reading {output_csv} to verify sanitization...")
    with open(output_csv, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        row = next(reader)

        # Verify sanitization
        # The writer writes sanitized strings, so if we read them back with csv.reader,
        # we should see the single quote if it was added.

        errors = []
        if not row[0].startswith("'="):
            errors.append(f"Title not sanitized: {row[0]}")
        if not row[1].startswith("'+"):
             errors.append(f"Date not sanitized: {row[1]}")
        if not row[2].startswith("'-"):
             errors.append(f"Author not sanitized: {row[2]}")
        if not row[3].startswith("'@"):
             errors.append(f"Categories not sanitized: {row[3]}")

        if errors:
            print("FAILED: Sanitization check failed.")
            for e in errors:
                print(f"  - {e}")
            exit(1)
        else:
            print("PASSED: Malicious input correctly sanitized.")

    # Verify normal data is not affected
    print("Running save_data with normal input...")
    scraper.save_data(normal_data)

    with open(output_csv, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        row = next(reader)

        if row[0].startswith("'"):
            print(f"FAILED: Normal title unnecessarily sanitized: {row[0]}")
            exit(1)

    print("PASSED: Normal input not affected.")

    # Cleanup
    for f in [output_json, output_csv, output_txt]:
        if os.path.exists(f):
            os.remove(f)

if __name__ == "__main__":
    test_csv_security()
