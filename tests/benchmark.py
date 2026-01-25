import asyncio
import time
import sys
import os
import logging
from unittest.mock import MagicMock

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scraper import MarkPositionScraperAsync

# Create a large HTML sample
LARGE_HTML = """
<html>
<body>
    <div id="content">
""" + """
        <article class="post category-tech">
            <h1 class="entry-title"><a href="http://example.com/post">Sample Post Title</a></h1>
            <time class="entry-date" datetime="2023-01-01">January 1, 2023</time>
            <div class="author vcard"><span class="fn">John Doe</span></div>
            <div class="entry-content">
                <p>Some content here with <a href="http://external.com">External Link</a>.</p>
                <p>More text...</p>
            </div>
        </article>
""" * 200 + """
    </div>
</body>
</html>
"""

async def mock_fetch_page(self, session, page_num):
    # Simulate minimal async delay to yield control
    await asyncio.sleep(0.001)
    return LARGE_HTML

async def run_benchmark():
    print("Preparing benchmark...")
    # Suppress logging for clean output
    logging.getLogger('scraper').setLevel(logging.WARNING)

    scraper = MarkPositionScraperAsync("dummy.json", "dummy.csv", "dummy.txt", concurrency=50)

    # Mock fetch_page
    scraper.fetch_page = mock_fetch_page.__get__(scraper, MarkPositionScraperAsync)

    sem = asyncio.Semaphore(50)
    session = MagicMock()

    print("Starting benchmark with 50 concurrent parses...")
    start_time = time.time()

    tasks = []
    for i in range(50):
        tasks.append(scraper.fetch_and_parse(session, i, sem))

    await asyncio.gather(*tasks)

    end_time = time.time()
    duration = end_time - start_time

    print(f"Total time: {duration:.4f} seconds")
    return duration

if __name__ == "__main__":
    asyncio.run(run_benchmark())
