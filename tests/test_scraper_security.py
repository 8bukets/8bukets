import unittest
import csv
import io
import sys
import os

# Add root directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

class MockFile:
    def write(self, content):
        pass

class TestScraperSecurity(unittest.TestCase):
    def test_csv_injection_prevention(self):
        scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt")

        # Malicious inputs
        dangerous_inputs = [
            "=SUM(1+1)",
            "+1+1",
            "-1-1",
            "@SUM(1+1)"
        ]

        for dangerous_input in dangerous_inputs:
            posts = [{
                'title': dangerous_input,
                'date': '2023-01-01',
                'author': dangerous_input,
                'categories': [dangerous_input],
                'external_link': 'http://example.com',
                'domain': 'example.com',
                'post_url': 'http://example.com/post'
            }]

            output = io.StringIO()
            writer = csv.writer(output)

            # We mock the other file handles as they are not the focus
            scraper.save_batch(posts, MockFile(), writer, MockFile(), set(), True)

            csv_content = output.getvalue().strip()
            # The row is: title, date, author, categories, external_link, domain, post_url

            reader = csv.reader(io.StringIO(csv_content))
            row = next(reader)

            title = row[0]
            author = row[2]
            categories = row[3]

            # Verification: Dangerous fields should now start with single quote
            self.assertTrue(title.startswith("'"), f"Title '{title}' not sanitized for input '{dangerous_input}'")
            self.assertTrue(author.startswith("'"), f"Author '{author}' not sanitized for input '{dangerous_input}'")
            self.assertTrue(categories.startswith("'"), f"Categories '{categories}' not sanitized for input '{dangerous_input}'")

if __name__ == '__main__':
    unittest.main()
