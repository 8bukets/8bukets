
import pytest
import asyncio
from scraper import MarkPositionScraperAsync
from bs4 import BeautifulSoup

# Sample HTML for testing
SAMPLE_HTML = """
<html>
    <head>
        <title>Test Page</title>
        <script>var x = 1;</script>
    </head>
    <body>
        <div id="content">
            <article class="post">
                <header class="entry-header">
                    <h1 class="entry-title"><a href="http://example.com/post1">Post 1</a></h1>
                    <div class="entry-meta">
                        <span class="posted-on">
                            <time class="entry-date" datetime="2023-01-01T12:00:00+00:00">January 1, 2023</time>
                        </span>
                        <span class="byline">
                            <span class="author vcard"><a class="url fn n" href="#">Author One</a></span>
                        </span>
                    </div>
                </header>
                <div class="entry-content">
                    <p>Some content <a href="http://external.com">External Link</a></p>
                </div>
                <footer class="entry-footer">
                    <span class="cat-links">
                        <a href="#" rel="category tag">Category 1</a>
                    </span>
                </footer>
            </article>

            <article class="post tag-something">
                 <h1 class="entry-title"><a href="http://example.com/post2">Post 2</a></h1>
                 <div class="entry-content">
                     <iframe src="https://youtube.com/video"></iframe>
                 </div>
            </article>

            <div class="sidebar">
                <p>Ignore me</p>
            </div>
        </div>
    </body>
</html>
"""

@pytest.mark.asyncio
async def test_parse_page():
    scraper = MarkPositionScraperAsync(
        output_json="test.json",
        output_csv="test.csv",
        output_txt="test.txt"
    )

    # Parse the sample HTML
    results = await scraper.parse_page(SAMPLE_HTML)

    # Assertions
    assert len(results) == 2, f"Expected 2 posts, got {len(results)}"

    # Check first post
    post1 = results[0]
    assert post1['title'] == "Post 1"
    assert post1['date'] == "January 1, 2023"
    assert post1['datetime'] == "2023-01-01T12:00:00+00:00"
    assert post1['author'] == "Author One"
    assert post1['external_link'] == "http://external.com"
    assert post1['post_url'] == "http://example.com/post1"

    # Check second post
    post2 = results[1]
    assert post2['title'] == "Post 2"
    assert post2['external_link'] == "https://youtube.com/video"

@pytest.mark.asyncio
async def test_parse_page_empty():
    scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")
    results = await scraper.parse_page("<html><body>No posts here</body></html>")
    assert len(results) == 0
