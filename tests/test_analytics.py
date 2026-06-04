import unittest
import sys
import os
import json
from datetime import datetime
import tempfile

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analytics import generate_report

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        self.test_data = [
            {
                'domain': 'google.com',
                'categories': ['Tech', 'News'],
                'datetime': '2023-01-01T10:00:00',
                'author': 'Alice'
            },
            {
                'domain': 'google.com',
                'categories': ['Tech'],
                'datetime': '2023-01-02T10:00:00',
                'author': 'Bob'
            },
            {
                'domain': 'example.com',
                'categories': ['Life'],
                'datetime': '2022-12-31T10:00:00',
                'author': 'Alice'
            }
        ]
        self.output_file = tempfile.NamedTemporaryFile(delete=False).name

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_generate_report(self):
        generate_report(self.test_data, self.output_file)

        with open(self.output_file, 'r') as f:
            content = f.read()

        # Check Domains
        self.assertIn('| google.com | 2 |', content)
        self.assertIn('| example.com | 1 |', content)

        # Check Categories
        self.assertIn('| Tech | 2 |', content)
        self.assertIn('| News | 1 |', content)
        self.assertIn('| Life | 1 |', content)

        # Check Years
        self.assertIn('| 2023 | 2 |', content)
        self.assertIn('| 2022 | 1 |', content)

        # Check Authors
        self.assertIn('- Alice: 2 posts', content)
        self.assertIn('- Bob: 1 posts', content)

        # Check Date Range
        self.assertIn('2022-12-31 to 2023-01-02', content)

if __name__ == '__main__':
    unittest.main()
