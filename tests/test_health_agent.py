import unittest
import os
from agents.health_agent import HealthAgent
from bs4 import BeautifulSoup

class TestHealthAgent(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test_index.html'
        with open(self.test_file, 'w') as f:
            f.write("<html><head></head><body><header></header><main></main><footer></footer></body></html>")
        self.agent = HealthAgent(filepath=self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists('robots.txt'):
             # We don't want to delete the real robots.txt if it exists, but for this test we might mock it
             pass

    def test_check_integrity_success(self):
        self.assertTrue(self.agent.check_integrity())

    def test_check_integrity_failure(self):
        with open(self.test_file, 'w') as f:
            f.write("<html><body></body></html>") # Missing head, header, main, footer

        # Capture stdout to avoid clutter
        import io
        import sys
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        self.assertFalse(self.agent.check_integrity())

        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
