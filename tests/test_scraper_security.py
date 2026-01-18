import unittest
from unittest.mock import patch, MagicMock
import socket
import sys
import os

# Add root directory to path to import scrape_informatic
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# We will patch scrape_informatic when we import it, or if it's already imported
# But since we are modifying it, we expect the function is_safe_url to be there.
# However, for TDD, we might want to see it fail first.
# But I can't import is_safe_url if it doesn't exist.
# So I will define the test assuming the function exists, but I'll write the function immediately after.

# For now, I'll assume I can import scrape_informatic
import scrape_informatic

class TestScraperSecurity(unittest.TestCase):

    def test_is_safe_url_public_ip(self):
        """Test that public IPs are considered safe."""
        # Mock socket.getaddrinfo to return a public IP
        with patch('socket.getaddrinfo') as mock_getaddrinfo:
            # 8.8.8.8 is Google DNS (public)
            mock_getaddrinfo.return_value = [(socket.AF_INET, socket.SOCK_STREAM, 6, '', ('8.8.8.8', 80))]

            url = "http://google.com"
            self.assertTrue(scrape_informatic.is_safe_url(url))

    def test_is_safe_url_localhost(self):
        """Test that localhost is unsafe."""
        with patch('socket.getaddrinfo') as mock_getaddrinfo:
            # 127.0.0.1
            mock_getaddrinfo.return_value = [(socket.AF_INET, socket.SOCK_STREAM, 6, '', ('127.0.0.1', 80))]

            url = "http://localhost"
            self.assertFalse(scrape_informatic.is_safe_url(url))

    def test_is_safe_url_private_ip(self):
        """Test that private IPs are unsafe."""
        with patch('socket.getaddrinfo') as mock_getaddrinfo:
            # 192.168.1.1
            mock_getaddrinfo.return_value = [(socket.AF_INET, socket.SOCK_STREAM, 6, '', ('192.168.1.1', 80))]

            url = "http://192.168.1.1"
            self.assertFalse(scrape_informatic.is_safe_url(url))

    def test_is_safe_url_aws_metadata(self):
        """Test that AWS metadata IP is unsafe."""
        with patch('socket.getaddrinfo') as mock_getaddrinfo:
            # 169.254.169.254
            mock_getaddrinfo.return_value = [(socket.AF_INET, socket.SOCK_STREAM, 6, '', ('169.254.169.254', 80))]

            url = "http://169.254.169.254/latest/meta-data/"
            self.assertFalse(scrape_informatic.is_safe_url(url))

    def test_is_safe_url_bad_scheme(self):
        """Test that non-http/https schemes are unsafe."""
        url = "file:///etc/passwd"
        # Should fail before DNS resolution
        self.assertFalse(scrape_informatic.is_safe_url(url))

        url = "ftp://example.com"
        self.assertFalse(scrape_informatic.is_safe_url(url))

    def test_is_safe_url_dns_failure(self):
        """Test behavior when DNS resolution fails."""
        with patch('socket.getaddrinfo') as mock_getaddrinfo:
            mock_getaddrinfo.side_effect = socket.gaierror("Name or service not known")

            url = "http://nonexistent.domain"
            # If DNS fails, it should probably be considered unsafe or just fail gracefully.
            # Usually return False to be safe.
            self.assertFalse(scrape_informatic.is_safe_url(url))

if __name__ == '__main__':
    unittest.main()
