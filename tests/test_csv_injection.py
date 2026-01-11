import unittest
import csv
import os
import tempfile
from scraper import MarkPositionScraperAsync

class TestCSVInjection(unittest.TestCase):
    def setUp(self):
        # Create temporary files for output
        self.temp_json = tempfile.NamedTemporaryFile(delete=False)
        self.temp_csv = tempfile.NamedTemporaryFile(delete=False)
        self.temp_txt = tempfile.NamedTemporaryFile(delete=False)
        self.scraper = MarkPositionScraperAsync(
            output_json=self.temp_json.name,
            output_csv=self.temp_csv.name,
            output_txt=self.temp_txt.name
        )

    def tearDown(self):
        # Clean up temp files
        os.unlink(self.temp_json.name)
        os.unlink(self.temp_csv.name)
        os.unlink(self.temp_txt.name)

    def test_csv_injection(self):
        # Mock data with potential CSV injection payload
        malicious_data = [
            {
                'title': '=1+1',  # Payload
                'date': '2023-01-01',
                'author': '@attacker', # Payload
                'categories': ['+category'], # Payload
                'external_link': '-http://evil.com', # Payload
                'domain': 'evil.com',
                'post_url': 'http://example.com/post'
            }
        ]

        # Save data
        self.scraper.save_data(malicious_data)

        # Read back and check if sanitized
        with open(self.temp_csv.name, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            row = next(reader)

            # Current behavior (before fix): payloads are written as is
            # After fix: they should be prepended with '

            # This assertion confirms if the sanitization is applied.
            # I will check if it starts with ' if it started with special chars

            title = row[0]
            author = row[2]
            # categories in CSV are ", ".join(list)
            categories = row[3]
            external_link = row[4]

            # In this test, we WANT to fail if it's NOT sanitized, or we can check the behavior.
            # To serve as a reproduction script, I should assert the DANGEROUS state if I want to prove it exists.
            # But normally I want to write a test that passes when FIXED.

            # Let's assert that it IS sanitized (which will fail now)
            self.assertTrue(title.startswith("'="), f"Title not sanitized: {title}")
            self.assertTrue(author.startswith("'@"), f"Author not sanitized: {author}")
            self.assertTrue(categories.startswith("'+"), f"Categories not sanitized: {categories}")
            self.assertTrue(external_link.startswith("'-"), f"External link not sanitized: {external_link}")

if __name__ == '__main__':
    unittest.main()
