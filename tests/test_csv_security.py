import unittest
import csv
import os
import json
from scraper import MarkPositionScraperAsync

class TestCSVSecurity(unittest.TestCase):
    def setUp(self):
        self.output_json = 'test_links.json'
        self.output_csv = 'test_links.csv'
        self.output_txt = 'test_unique_links.txt'
        self.scraper = MarkPositionScraperAsync(self.output_json, self.output_csv, self.output_txt)

    def tearDown(self):
        if os.path.exists(self.output_json):
            os.remove(self.output_json)
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)
        if os.path.exists(self.output_txt):
            os.remove(self.output_txt)

    def test_csv_injection(self):
        # Malicious data
        malicious_posts = [{
            'title': '=1+1',  # Formula injection
            'date': '2023-01-01',
            'author': '@attacker', # Potential issue in some contexts, mostly formula starters though
            'categories': ['+MaliciousCategory'],
            'external_link': '-http://evil.com',
            'domain': 'evil.com',
            'post_url': 'http://example.com'
        }]

        # Prepare files as they are in scrape()
        with open(self.output_json, 'w', encoding='utf-8') as json_f, \
             open(self.output_csv, 'w', newline='', encoding='utf-8') as csv_f, \
             open(self.output_txt, 'w', encoding='utf-8') as txt_f:

            csv_writer = csv.writer(csv_f)
            # Write header
            csv_writer.writerow(['Title', 'Date', 'Author', 'Categories', 'External Link', 'Domain', 'Post URL'])

            # Initialize JSON
            json_f.write('[')

            seen_links = set()

            # Call save_batch
            self.scraper.save_batch(malicious_posts, json_f, csv_writer, txt_f, seen_links, True)

            # Finalize JSON
            json_f.write('\n]')

        # Read back CSV and check for raw malicious characters at start
        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            print(f"Row content: {row}")

            # Assertions to confirm fix
            # Should be sanitized with single quote
            self.assertTrue(row[0].startswith("'="), f"Title should be sanitized. Got: {row[0]}")
            self.assertTrue(row[2].startswith("'@"), f"Author should be sanitized. Got: {row[2]}")
            self.assertTrue(row[3].startswith("'+"), f"Categories should be sanitized. Got: {row[3]}")
            self.assertTrue(row[4].startswith("'-"), f"External Link should be sanitized. Got: {row[4]}")

if __name__ == '__main__':
    unittest.main()
