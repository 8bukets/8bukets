import asyncio
import time
import pytest
from unittest.mock import patch, MagicMock
from scraper import MarkPositionScraperAsync

class TestScraperPerformance:
    @pytest.mark.asyncio
    async def test_parse_page_non_blocking(self):
        """
        Verify that parse_page runs in a thread and does not block the event loop.
        """
        scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

        # Simulate a slow parsing operation (1 second)
        # We patch _parse_page_sync, which is what runs in the thread
        def slow_parse(html):
            time.sleep(1)
            return []

        with patch.object(scraper, '_parse_page_sync', side_effect=slow_parse):
            start_time = time.time()

            # Start the parsing task
            task = asyncio.create_task(scraper.parse_page("<html></html>"))

            # Yield to the event loop. If parse_page blocks, this sleep won't return
            # until parse_page is done (1s). If it's non-blocking, it returns immediately (0.1s).
            await asyncio.sleep(0.1)

            elapsed = time.time() - start_time

            # Wait for task to finish
            await task

            # If elapsed is small (~0.1s), it means the loop was free.
            # If elapsed is large (~1.1s), it means the loop was blocked.
            print(f"Elapsed time for immediate sleep: {elapsed:.4f}s")

            # Assertion: The loop should not be blocked for the full duration of slow_parse
            assert elapsed < 0.5, f"Event loop was blocked! Elapsed: {elapsed:.4f}s"

    @pytest.mark.asyncio
    async def test_parse_page_functionality(self):
        """
        Verify that parse_page still works correctly after refactoring.
        """
        scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

        html = """
        <html><body>
            <article class="post">
                <h1 class="entry-title"><a href="http://example.com/post">Test Title</a></h1>
                <time class="entry-date" datetime="2023-01-01">January 1, 2023</time>
                <div class="author vcard"><span class="fn">Author Name</span></div>
                <div class="entry-content"><a href="http://external.com">External Link</a></div>
            </article>
        </body></html>
        """

        result = await scraper.parse_page(html)

        assert len(result) == 1
        assert result[0]['title'] == "Test Title"
        assert result[0]['author'] == "Author Name"
        assert result[0]['external_link'] == "http://external.com"
