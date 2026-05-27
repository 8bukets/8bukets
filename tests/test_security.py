import unittest
from agents.content_agent import ContentAgent

class TestSecurity(unittest.TestCase):
    def test_markdown_injection(self):
        agent = ContentAgent()

        # Malicious input: A title that looks like a Markdown link, contains HTML, and backslashes
        data = [{
            'title': '[Link](http://evil.com) <script> \\',
            'date': '2025-01-01',
            'external_link': 'http://example.com'
        }]

        insights = {
            'strategic_insight': 'Testing',
            'focus_areas': ['Security']
        }

        # Process data
        output = agent.process(data, insights)

        # DEBUG: Print output to see what happens
        print("\nGenerated Output:\n", output)

        # Assertion: The raw markdown link should NOT be present.
        # It should be escaped.
        self.assertNotIn('[Link]', output)
        self.assertNotIn('<script>', output)

        # Assert escaped version is present
        # [ -> \[, ] -> \], ( -> \(, ) -> \), . -> \., < -> \<, > -> \>, \ -> \\
        # Note: '/' is NOT escaped.
        self.assertIn(r'\[Link\]\(http://evil\.com\) \<script\> \\', output)

if __name__ == '__main__':
    unittest.main()
