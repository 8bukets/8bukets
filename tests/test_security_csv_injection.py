import csv
import os
import unittest
from scraper import MarkPositionScraperAsync

class TestSecurity(unittest.TestCase):
    def test_csv_injection_mitigation(self):
        # Setup
        json_file = "test_links_security.json"
        csv_file = "test_links_security.csv"
        txt_file = "test_unique_links_security.txt"

        scraper = MarkPositionScraperAsync(json_file, csv_file, txt_file)

        # Malicious data - fields starting with =, +, -, @
        posts = [
            {
                'title': '=cmd|/C calc!A0',
                'date': '2023-01-01',
                'author': '@attacker',
                'categories': ['+category'],
                'external_link': '-http://evil.com',
                'domain': 'evil.com',
                'post_url': 'http://example.com/post'
            }
        ]

        # Open files as expected by save_batch
        with open(json_file, 'w', encoding='utf-8') as json_f, \
             open(csv_file, 'w', newline='', encoding='utf-8') as csv_f, \
             open(txt_file, 'w', encoding='utf-8') as txt_f:

            csv_writer = csv.writer(csv_f)
            # Write header
            csv_writer.writerow(['Title', 'Date', 'Author', 'Categories', 'External Link', 'Domain', 'Post URL'])

            json_f.write('[')
            scraper.save_batch(posts, json_f, csv_writer, txt_f, set(), True)
            json_f.write(']')

        # Verification
        with open(csv_file, 'r', newline='', encoding='utf-8') as csv_f:
            reader = csv.reader(csv_f)
            header = next(reader)
            row = next(reader)

            # Assertions
            self.assertTrue(row[0].startswith("'="), "Title should be sanitized")
            self.assertTrue(row[2].startswith("'@"), "Author should be sanitized")
            self.assertTrue(row[3].startswith("'+"), "Categories should be sanitized")
            self.assertTrue(row[4].startswith("'-"), "External Link should be sanitized")

            self.assertEqual(row[0], "'=cmd|/C calc!A0")
            self.assertEqual(row[2], "'@attacker")
            self.assertEqual(row[3], "'+category")
            self.assertEqual(row[4], "'-http://evil.com")

        # Cleanup
        self.addCleanup(self._cleanup_files, [json_file, csv_file, txt_file])

    def _cleanup_files(self, files):
        for f in files:
            if os.path.exists(f):
                os.remove(f)

if __name__ == "__main__":
    unittest.main()
