
import csv
import os
import unittest
from scraper import MarkPositionScraperAsync

class TestCSVInjectionPrevention(unittest.TestCase):
    def setUp(self):
        self.output_csv = "test_safe.csv"
        self.scraper = MarkPositionScraperAsync(
            output_json="dummy.json",
            output_csv=self.output_csv,
            output_txt="dummy.txt"
        )
        self.posts = [
            {
                'title': '=1+1',
                'date': '+2023-01-01',
                'author': '@attacker',
                'categories': ['-category'],
                'external_link': 'http://safe.com',
                'domain': 'safe.com',
                'post_url': 'http://wordpress.com/post'
            }
        ]

    def test_save_data_sanitization(self):
        print("\nTesting scraper CSV sanitization...")
        self.scraper.save_data(self.posts)

        with open(self.output_csv, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Check Title
            self.assertEqual(row[0], "'=1+1")
            print("Title sanitized: " + row[0])

            # Check Date
            self.assertEqual(row[1], "'+2023-01-01")
            print("Date sanitized: " + row[1])

            # Check Author
            self.assertEqual(row[2], "'@attacker")
            print("Author sanitized: " + row[2])

            # Check Categories (joined string should start with single quote because first item starts with -)
            # wait, joined string is "-category". so it should be "'-category"
            self.assertEqual(row[3], "'-category")
            print("Categories sanitized: " + row[3])

    def tearDown(self):
        if os.path.exists(self.output_csv):
            os.remove(self.output_csv)
        if os.path.exists("dummy.json"):
            os.remove("dummy.json")
        if os.path.exists("dummy.txt"):
            os.remove("dummy.txt")

if __name__ == "__main__":
    unittest.main()
