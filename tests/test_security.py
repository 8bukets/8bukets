import os
import unittest
import shutil
import subprocess
import sys

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.test_dir = "tests/temp_test_dir"
        self.victim_dir = "tests/victim"
        os.makedirs(self.test_dir, exist_ok=True)
        os.makedirs(self.victim_dir, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)
        shutil.rmtree(self.victim_dir, ignore_errors=True)
        # Cleanup any files created in CWD (which is where sanitized files go)
        if os.path.exists("vuln_check.json"):
            os.remove("vuln_check.json")
        if os.path.exists("vuln_search.json"):
            os.remove("vuln_search.json")

    def test_path_traversal_prevention_scrape_informatic(self):
        """
        Verify that scrape_informatic.py sanitizes the output path.
        """
        scraper_script = os.path.abspath("scrape_informatic.py")
        relative_exploit_path = "../victim/vuln_check.json"

        cmd = [
            sys.executable,
            scraper_script,
            "-o", relative_exploit_path,
            "-n", "1"
        ]

        try:
            subprocess.run(cmd, cwd=self.test_dir, capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError:
             pass

        victim_file = os.path.join(self.victim_dir, "vuln_check.json")
        self.assertFalse(os.path.exists(victim_file), "Vulnerability in scrape_informatic! File written to victim directory.")

        sanitized_file = os.path.join(self.test_dir, "vuln_check.json")
        if os.path.exists(sanitized_file):
            print("Sanitization worked (scrape_informatic): File written to CWD.")

    def test_path_traversal_prevention_google_search(self):
        """
        Verify that google_search_scraper.py sanitizes the output path.
        """
        scraper_script = os.path.abspath("google_search_scraper.py")
        relative_exploit_path = "../victim/vuln_search.json"

        # We use a dummy query and limit 1 to be fast
        cmd = [
            sys.executable,
            scraper_script,
            "dummy query",
            "-o", relative_exploit_path,
            "-n", "1"
        ]

        try:
            subprocess.run(cmd, cwd=self.test_dir, capture_output=True, text=True, check=True)
        except subprocess.CalledProcessError:
             pass

        victim_file = os.path.join(self.victim_dir, "vuln_search.json")
        self.assertFalse(os.path.exists(victim_file), "Vulnerability in google_search_scraper! File written to victim directory.")

        sanitized_file = os.path.join(self.test_dir, "vuln_search.json")
        if os.path.exists(sanitized_file):
            print("Sanitization worked (google_search_scraper): File written to CWD.")

if __name__ == '__main__':
    unittest.main()
