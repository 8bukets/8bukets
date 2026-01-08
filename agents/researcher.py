"""
This module contains the ResearcherAgent which is responsible for gathering data
from various sources including blog scraping and Google search.
"""
import subprocess
import sys
import json
import os
from concurrent.futures import ThreadPoolExecutor
from .base_agent import BaseAgent

class ResearcherAgent(BaseAgent):
    """
    Agent responsible for conducting research by scraping blog content and Google listings.
    """
    def __init__(self):
        super().__init__("Researcher")

    def _scrape_blog(self, limit, output_file):
        """Helper to run the blog scraper."""
        try:
            cmd = [sys.executable, "scrape_informatic.py", "-n", str(limit), "-o", output_file]
            subprocess.run(cmd, check=True)
            if os.path.exists(output_file):
                with open(output_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except subprocess.CalledProcessError as e:
            self.logger.error("Blog scraping failed with exit code %s", e.returncode)
        except (IOError, json.JSONDecodeError) as e:
            self.logger.error("Blog scraping output error: %s", e)
        except Exception as e: # pylint: disable=broad-exception-caught
            self.logger.error("Blog scraping failed: %s", e)
        return []

    def _scrape_google(self, search_output):
        """Helper to run the google scraper."""
        try:
            cmd = [sys.executable, "google_search_scraper.py", "-o", search_output]
            subprocess.run(cmd, check=True)
            if os.path.exists(search_output):
                with open(search_output, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except subprocess.CalledProcessError as e:
            self.logger.error("Google search scraping failed with exit code %s", e.returncode)
        except (IOError, json.JSONDecodeError) as e:
            self.logger.error("Google search scraping output error: %s", e)
        except Exception as e: # pylint: disable=broad-exception-caught
            self.logger.error("Google search scraping failed: %s", e)
        return []

    def perform_task(self, data):
        # Data can specify limits or targets
        limit = data.get('limit', 1) if data else 1
        output_file = data.get('output_file', 'data.json') if data else 'data.json'
        search_output = "google_search_results.json"

        self.logger.info(
            "Scraping content (limit %s pages) and checking Google listings in parallel...",
            limit
        )

        results = {}

        # Use ThreadPoolExecutor to run subprocesses in parallel
        # Note: subprocess.run releases the GIL, so threads are effective here.
        with ThreadPoolExecutor(max_workers=2) as executor:
            future_blog = executor.submit(self._scrape_blog, limit, output_file)
            future_google = executor.submit(self._scrape_google, search_output)

            results['blog_posts'] = future_blog.result()
            results['google_listings'] = future_google.result()

        return results
