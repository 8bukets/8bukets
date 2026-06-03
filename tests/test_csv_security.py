import sys
import os
import csv
import unittest

# Add root to path so we can import scraper
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scraper import MarkPositionScraperAsync

class TestCSVSecurity(unittest.TestCase):
    def test_csv_sanitization(self):
        csv_file = 'test_security.csv'
        scraper = MarkPositionScraperAsync('dummy.json', csv_file, 'dummy.txt')

        malicious_payload = [
            {
                'title': '=cmd|\'/C calc\'!A0',
                'date': '2023-10-27',
                'author': '+Malicious',
                'categories': ['@Category'],
                'external_link': '-http://evil.com',
                'domain': 'evil.com',
                'post_url': 'http://example.com'
            }
        ]

        scraper.save_data(malicious_payload)

        with open(csv_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            print(f"DEBUG: Title in CSV: {row[0]}")
            print(f"DEBUG: Author in CSV: {row[2]}")

            # Assert that the vulnerability is FIXED (payloads should be escaped with ')
            self.assertEqual(row[0], "'=cmd|'/C calc'!A0", "Security Fix: Title should be escaped")
            self.assertEqual(row[2], "'+Malicious", "Security Fix: Author should be escaped")
            self.assertEqual(row[3], "'@Category", "Security Fix: Categories should be escaped")
            self.assertEqual(row[4], "'-http://evil.com", "Security Fix: External Link should be escaped")

        # Cleanup
        if os.path.exists(csv_file):
            os.remove(csv_file)
        if os.path.exists('dummy.json'):
            os.remove('dummy.json')
        if os.path.exists('dummy.txt'):
            os.remove('dummy.txt')

if __name__ == '__main__':
    unittest.main()
