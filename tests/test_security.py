import unittest
from unittest.mock import MagicMock, patch
import sys
import os

# Add root directory to sys.path so we can import scrape_informatic
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import scrape_informatic

class TestSecurity(unittest.TestCase):
    @patch('scrape_informatic.requests.Session')
    def test_timeout_present_in_get_requests(self, MockSession):
        """
        Security Test:
        Verifies that requests.Session.get() is called with a 'timeout' parameter.
        Missing timeout can lead to Denial of Service (DoS) if the server hangs.
        """
        # Setup
        session_instance = MockSession.return_value
        session_instance.get.return_value.status_code = 200
        # Mocking content to be valid HTML to pass soup parsing
        session_instance.get.return_value.content = b"<html><body><article><h2>Title</h2></article></body></html>"

        # Execute
        # We run scrape for 1 page to trigger the network call
        scrape_informatic.scrape("test_output_security.json", max_pages=1)

        # Verify
        # Check that get() was called at least once
        self.assertTrue(session_instance.get.called, "Session.get() was not called.")

        # Check arguments of the first call to get()
        # call_args returns (args, kwargs)
        args, kwargs = session_instance.get.call_args

        # Assert timeout is in kwargs
        self.assertIn('timeout', kwargs, "SECURITY FAILURE: requests.get() call is missing 'timeout' parameter! Risk of indefinite hang (DoS).")

        # Check timeout value is reasonable (e.g., between 5 and 60 seconds)
        timeout_val = kwargs['timeout']
        self.assertGreaterEqual(timeout_val, 5, "Timeout value is too short (< 5s).")
        self.assertLessEqual(timeout_val, 60, "Timeout value is too long (> 60s).")

if __name__ == '__main__':
    unittest.main()
