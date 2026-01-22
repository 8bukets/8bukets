import unittest
import asyncio
import sys
import os

# Add parent directory to path to import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import OracleNewsScraper

class TestScraperSecurity(unittest.TestCase):
    def setUp(self):
        self.scraper = OracleNewsScraper("test.json", "test.csv", "test.txt")

    def test_malicious_scheme_filtering(self):
        """Test that the scraper rejects non-http/https schemes like javascript:"""
        # A link that satisfies the substring checks but uses a malicious scheme
        malicious_href = "javascript:alert(1)/news/announcement/google-cloud"

        html = f"""
        <html>
            <body>
                <a href="{malicious_href}"><h3>Malicious Bypass</h3></a>
                <a href="/news/announcement/google-cloud-safe"><h3>Safe Link</h3></a>
            </body>
        </html>
        """

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        articles = loop.run_until_complete(self.scraper.parse_page(html))
        loop.close()

        links = [a['external_link'] for a in articles]

        # Verify we got the safe link
        safe_links = [l for l in links if "google-cloud-safe" in l]
        self.assertTrue(len(safe_links) > 0, "Should extract safe link")

        # Verify we blocked the malicious link
        malicious_links = [l for l in links if l.startswith("javascript:")]
        self.assertEqual(len(malicious_links), 0, f"Scraper accepted malicious links: {malicious_links}")

if __name__ == '__main__':
    unittest.main()
