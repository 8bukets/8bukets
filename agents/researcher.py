from .base_agent import BaseAgent
import subprocess
import sys
import json
import os
import logging
from typing import List, Dict

class ResearcherAgent(BaseAgent):
    def __init__(self):
        super().__init__("Researcher")

    def perform_task(self, data):
        # Data can specify limits or targets
        limit = data.get('limit', 1) if data else 1
        output_file = data.get('output_file', 'data.json') if data else 'data.json'

        self.logger.info(f"Scraping content (limit {limit} pages)...")

        results = {}

        # Scrape Blog Content and Check Google Listings in parallel
        self.logger.info("Checking Google Listings...")
        search_output = "google_search_results.json"

        # Define commands
        cmd_blog = [sys.executable, "scrape_informatic.py", "-n", str(limit), "-o", output_file]
        cmd_google = [sys.executable, "google_search_scraper.py", "-o", search_output]

        # Cleanup stale files
        if os.path.exists(output_file):
            try:
                os.remove(output_file)
            except OSError:
                pass
        if os.path.exists(search_output):
            try:
                os.remove(search_output)
            except OSError:
                pass

        p_blog = None
        p_google = None

        try:
            # Start Blog Scraper
            p_blog = subprocess.Popen(cmd_blog)
        except Exception as e:
            self.logger.error(f"Failed to start blog scraper: {e}")

        try:
            # Start Google Scraper
            p_google = subprocess.Popen(cmd_google)
        except Exception as e:
            self.logger.error(f"Failed to start google scraper: {e}")

        # Wait for processes and check return codes
        blog_success = False
        if p_blog:
            p_blog.wait()
            if p_blog.returncode == 0:
                blog_success = True
            else:
                self.logger.error(f"Blog scraper failed with return code {p_blog.returncode}")

        google_success = False
        if p_google:
            p_google.wait()
            if p_google.returncode == 0:
                google_success = True
            else:
                self.logger.error(f"Google scraper failed with return code {p_google.returncode}")

        # Process Results
        # 1. Blog Content
        results['blog_posts'] = []
        if blog_success and os.path.exists(output_file):
            try:
                with open(output_file, 'r', encoding='utf-8') as f:
                    results['blog_posts'] = json.load(f)
            except Exception as e:
                self.logger.error(f"Failed to read blog results: {e}")

        # 2. Google Listings
        results['google_listings'] = []
        if google_success and os.path.exists(search_output):
            try:
                with open(search_output, 'r', encoding='utf-8') as f:
                    results['google_listings'] = json.load(f)
            except Exception as e:
                self.logger.error(f"Failed to read google results: {e}")

        return results
