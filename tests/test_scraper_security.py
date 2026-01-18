import unittest
from unittest.mock import patch
from scraper import OracleNewsScraper
import socket

class TestScraperSecurity(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.scraper = OracleNewsScraper("x", "x", "x")

    @patch('asyncio.AbstractEventLoop.getaddrinfo')
    async def test_is_safe_url_public(self, mock_getaddrinfo):
        """Test that public URLs are considered safe."""
        # Mock public IP (8.8.8.8)
        # return of getaddrinfo is list of (family, type, proto, canonname, sockaddr)
        # sockaddr is (address, port) for AF_INET
        mock_getaddrinfo.return_value = [
            (socket.AF_INET, socket.SOCK_STREAM, 6, '', ('8.8.8.8', 80))
        ]

        result = await self.scraper.is_safe_url("https://www.oracle.com")
        self.assertTrue(result, "Public URL should be safe")

    @patch('asyncio.AbstractEventLoop.getaddrinfo')
    async def test_is_safe_url_localhost_ip(self, mock_getaddrinfo):
        """Test that localhost IP is unsafe."""
        # Mock localhost IP
        mock_getaddrinfo.return_value = [
            (socket.AF_INET, socket.SOCK_STREAM, 6, '', ('127.0.0.1', 80))
        ]

        result = await self.scraper.is_safe_url("http://127.0.0.1")
        self.assertFalse(result, "127.0.0.1 should be unsafe")

    @patch('asyncio.AbstractEventLoop.getaddrinfo')
    async def test_is_safe_url_localhost_name(self, mock_getaddrinfo):
        """Test that localhost hostname is unsafe."""
        # Mock localhost resolution
        mock_getaddrinfo.return_value = [
            (socket.AF_INET, socket.SOCK_STREAM, 6, '', ('127.0.0.1', 80))
        ]

        result = await self.scraper.is_safe_url("http://localhost")
        self.assertFalse(result, "localhost should be unsafe")

    @patch('asyncio.AbstractEventLoop.getaddrinfo')
    async def test_is_safe_url_private_ip(self, mock_getaddrinfo):
        """Test that private IPs are unsafe."""
        # Mock private IP
        mock_getaddrinfo.return_value = [
            (socket.AF_INET, socket.SOCK_STREAM, 6, '', ('192.168.1.1', 80))
        ]

        result = await self.scraper.is_safe_url("http://192.168.1.1")
        self.assertFalse(result, "Private IP should be unsafe")

    @patch('asyncio.AbstractEventLoop.getaddrinfo')
    async def test_is_safe_url_ipv6_loopback(self, mock_getaddrinfo):
        """Test that IPv6 loopback is unsafe."""
        # Mock IPv6 loopback
        # sockaddr for AF_INET6 is (address, port, flow info, scope id)
        mock_getaddrinfo.return_value = [
            (socket.AF_INET6, socket.SOCK_STREAM, 6, '', ('::1', 80, 0, 0))
        ]

        result = await self.scraper.is_safe_url("http://localhost")
        self.assertFalse(result, "IPv6 loopback should be unsafe")

    async def test_is_safe_url_bad_scheme(self):
        """Test that non-http/https schemes are unsafe."""
        # No DNS resolution needed here
        result = await self.scraper.is_safe_url("ftp://example.com")
        self.assertFalse(result, "FTP scheme should be unsafe")

    async def test_is_safe_url_file_scheme(self):
        """Test that file scheme is unsafe (prevents local file access)."""
        result = await self.scraper.is_safe_url("file:///etc/passwd")
        self.assertFalse(result, "File scheme should be unsafe")

if __name__ == '__main__':
    unittest.main()
