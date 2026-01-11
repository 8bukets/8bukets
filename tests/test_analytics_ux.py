import unittest
import json
import os
import sys
from datetime import datetime

# Add root directory to path so we can import analytics
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import analytics

class TestAnalyticsUX(unittest.TestCase):
    def setUp(self):
        self.test_json = 'tests/test_links.json'
        self.test_report = 'tests/TEST_REPORT_UX.md'

        # Create sample data
        data = []
        # Add 10 posts for 2023
        for i in range(10):
            data.append({
                "title": f"Post {i}",
                "date": "2023-01-01",
                "datetime": "2023-01-01T12:00:00+00:00",
                "author": "Author A",
                "categories": ["Cat A"],
                "external_link": "https://example.com/page1",
                "domain": "example.com",
                "post_url": "https://markposition.wordpress.com/post1"
            })
        # Add 5 posts for 2022
        for i in range(5):
             data.append({
                "title": f"Post {i}",
                "date": "2022-01-01",
                "datetime": "2022-01-01T12:00:00+00:00",
                "author": "Author B",
                "categories": ["Cat B"],
                "external_link": "https://google.com/page1",
                "domain": "google.com",
                "post_url": "https://markposition.wordpress.com/post2"
            })

        with open(self.test_json, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    def tearDown(self):
        if os.path.exists(self.test_json):
            os.remove(self.test_json)
        if os.path.exists(self.test_report):
            os.remove(self.test_report)

    def test_report_structure(self):
        # Run the generator
        data = analytics.load_data(self.test_json)
        analytics.generate_report(data, self.test_report)

        # Read the output
        with open(self.test_report, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for UX elements
        self.assertIn("📊 Markposition Analytics Report", content) # Emoji in title
        self.assertIn("## 📈 Executive Summary", content) # Executive summary section
        self.assertIn("## 🌐 Top 10 Referenced Domains", content)
        self.assertIn("## 🏷️ Top 10 Categories", content)
        self.assertIn("## 📅 Posts by Year", content)
        self.assertIn("## ✍️ Authors", content)

        # Check for ASCII bar charts
        # Depending on implementation, bars might look like █ or ░
        # We expect at least some bars
        self.assertTrue("█" in content or "░" in content)

if __name__ == '__main__':
    unittest.main()
