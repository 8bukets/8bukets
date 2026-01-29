import time
import sys
import os
import re

# Add root to path so we can import scraper
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import OracleNewsScraper

def benchmark():
    scraper = OracleNewsScraper("links.json", "links.csv", "unique.txt")

    # 1. clean_text benchmark
    text = "  This   is  a   messy \n\n text \t with \xa0 non-breaking spaces.  "
    iterations = 100000

    start_time = time.time()
    for _ in range(iterations):
        scraper.clean_text(text)
    end_time = time.time()

    print(f"clean_text: {iterations} iterations took {end_time - start_time:.4f} seconds")

    # 2. Date extraction benchmark (simulating the regex use in parse_page)
    # We can't easily call parse_page without HTML, so we'll simulate the regex usage pattern
    # which we are about to optimize.
    href = "/news/announcement/oracle-database-at-google-cloud-is-now-available-in-canada-2025-12-11/"

    # In the optimized version, we will access a class attribute.
    # For now, we measure the "current" style (re.search) to confirm baseline,
    # and later this script will measure the "new" style if we update it to use the class attribute
    # OR we just measure re.search vs re.compile().search here.

    # However, to be true to "verifying the code change", we should trust that calling scraper.clean_text
    # will become faster.

    # For date extraction, we can check if the class has the attribute.
    if hasattr(scraper, 'DATE_PATTERN'):
        # Optimized path simulation
        start_time = time.time()
        for _ in range(iterations):
            scraper.DATE_PATTERN.search(href)
        end_time = time.time()
        print(f"date_extraction (optimized): {iterations} iterations took {end_time - start_time:.4f} seconds")
    else:
        # Unoptimized path simulation (current code)
        start_time = time.time()
        for _ in range(iterations):
            re.search(r'(\d{4}-\d{2}-\d{2})', href)
        end_time = time.time()
        print(f"date_extraction (baseline): {iterations} iterations took {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    benchmark()
