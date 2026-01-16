import unittest
from analytics import analyze_data

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        self.test_data = [
            {
                "domain": "example.com",
                "categories": ["Tech", "News"],
                "author": "Alice",
                "datetime": "2023-01-01T10:00:00"
            },
            {
                "domain": "example.org",
                "categories": ["Tech"],
                "author": "Bob",
                "datetime": "2023-01-02T10:00:00"
            },
            {
                "domain": "example.com",
                "categories": None,  # Test None handling
                "author": "Alice",
                "datetime": "2023-02-01T10:00:00"
            }
        ]

    def test_analyze_data(self):
        stats = analyze_data(self.test_data)

        self.assertEqual(stats['total_posts'], 3)
        self.assertEqual(stats['unique_domains'], 2)

        # Check domain counts
        domain_dict = dict(stats['domain_counts'])
        self.assertEqual(domain_dict['example.com'], 2)
        self.assertEqual(domain_dict['example.org'], 1)

        # Check category counts
        cat_dict = dict(stats['category_counts'])
        self.assertEqual(cat_dict['Tech'], 2)
        self.assertEqual(cat_dict['News'], 1)
        # Ensure None categories didn't crash and weren't counted
        self.assertNotIn(None, cat_dict)

        # Check author counts
        auth_dict = dict(stats['author_counts'])
        self.assertEqual(auth_dict['Alice'], 2)
        self.assertEqual(auth_dict['Bob'], 1)

        # Check year counts
        year_dict = dict(stats['year_counts'])
        self.assertEqual(year_dict[2023], 3)

if __name__ == '__main__':
    unittest.main()
