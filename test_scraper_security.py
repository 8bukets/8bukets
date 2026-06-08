from scraper import OracleNewsScraper
import os
import csv
import unittest

class TestSecurity(unittest.TestCase):
    def test_path_traversal(self):
        print("\nTesting Path Traversal...")
        try:
            OracleNewsScraper(
                output_json="../vulnerable.json",
                output_csv="safe.csv",
                output_txt="safe.txt"
            )
            self.fail("Did not raise ValueError for path traversal")
        except ValueError as e:
            print(f"Caught expected error: {e}")
            self.assertIn("traverses outside", str(e))

    def test_csv_injection(self):
        print("\nTesting CSV Injection...")
        json_file = "test_safe.json"
        csv_file = "test_safe.csv"
        txt_file = "test_safe.txt"

        # Cleanup
        for f in [json_file, csv_file, txt_file]:
            if os.path.exists(f): os.remove(f)

        scraper = OracleNewsScraper(json_file, csv_file, txt_file)

        malicious_data = [{
            'title': '=SUM(1+1)',
            'date': '2025-01-01',
            'author': '@Admin',
            'categories': ['+News'],
            'external_link': '-http://evil.com',
            'domain': 'example.com',
            'post_url': 'http://example.com'
        }]

        scraper.save_data(malicious_data)

        # verify csv
        with open(csv_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Row structure: Title, Date, Author, Categories, External Link, Domain, Post URL
            # indices: 0, 1, 2, 3, 4, 5, 6

            self.assertTrue(row[0].startswith("'="), f"Title not sanitized: {row[0]}")
            self.assertTrue(row[2].startswith("'@"), f"Author not sanitized: {row[2]}")
            # Categories are joined by ", ". If the first one starts with +, the string starts with +
            self.assertTrue(row[3].startswith("'+"), f"Categories not sanitized: {row[3]}")
            self.assertTrue(row[4].startswith("'-"), f"External Link not sanitized: {row[4]}")

        print("CSV Injection protection verified.")

        # Cleanup
        for f in [json_file, csv_file, txt_file]:
            if os.path.exists(f): os.remove(f)

if __name__ == '__main__':
    unittest.main()
