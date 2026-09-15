import unittest
import os
import shutil
import tempfile
from utils import validate_output_path, is_safe_url

class TestSecurity(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        self.original_cwd = os.getcwd()
        os.chdir(self.test_dir)

    def tearDown(self):
        # Restore CWD and remove temp dir
        os.chdir(self.original_cwd)
        shutil.rmtree(self.test_dir)

    def test_valid_paths(self):
        """Test that paths inside the current directory are allowed."""
        valid_paths = [
            "data.json",
            "subdir/data.csv",
            "./report.md",
            "a/b/c/output.txt"
        ]

        for path in valid_paths:
            try:
                result = validate_output_path(path)
                # Ensure the result is an absolute path starting with test_dir
                self.assertTrue(result.startswith(self.test_dir))
            except ValueError as e:
                self.fail(f"Valid path '{path}' raised ValueError: {e}")

    def test_path_traversal(self):
        """Test that paths outside the current directory are rejected."""
        # Note: These checks depend on the filesystem structure, but ../ should always go up.
        invalid_paths = [
            "../secret.txt",
            "../../etc/passwd",
            "/tmp/evil.json",
            "/etc/shadow",
            "subdir/../../outside.txt"
        ]

        for path in invalid_paths:
            with self.assertRaises(ValueError, msg=f"Path '{path}' should have failed"):
                validate_output_path(path)

class TestSSRFProtection(unittest.TestCase):
    def test_safe_urls_allowed(self):
        safe_urls = [
            "https://artmusicpage.wordpress.com/",
            "http://example.com/page/2/",
            "https://93.184.216.34/blog",  # public IP literal, not private/loopback
        ]
        for url in safe_urls:
            self.assertTrue(is_safe_url(url), f"Expected '{url}' to be considered safe")

    def test_unsafe_schemes_rejected(self):
        unsafe = ["file:///etc/passwd", "ftp://example.com", "javascript:alert(1)", "gopher://x"]
        for url in unsafe:
            self.assertFalse(is_safe_url(url), f"Expected '{url}' to be rejected (bad scheme)")

    def test_localhost_and_loopback_rejected(self):
        unsafe = [
            "http://localhost/",
            "http://127.0.0.1/",
            "https://127.0.0.1:8080/admin",
            "http://[::1]/",
        ]
        for url in unsafe:
            self.assertFalse(is_safe_url(url), f"Expected '{url}' to be rejected (loopback)")

    def test_private_and_link_local_ips_rejected(self):
        unsafe = [
            "http://10.0.0.5/",
            "http://192.168.1.1/",
            "http://169.254.169.254/latest/meta-data/",  # cloud metadata endpoint
        ]
        for url in unsafe:
            self.assertFalse(is_safe_url(url), f"Expected '{url}' to be rejected (private/link-local)")

    def test_malformed_url_rejected(self):
        self.assertFalse(is_safe_url(""))
        self.assertFalse(is_safe_url("not a url"))


if __name__ == '__main__':
    unittest.main()
