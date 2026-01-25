import pytest
import asyncio
from scraper import MarkPositionScraperAsync

SAMPLE_HTML = """
<!DOCTYPE html>
<html>
<body>
<article class="post category-tech">
    <h1 class="entry-title"><a href="http://example.com/post1">Test Post</a></h1>
    <time class="entry-date" datetime="2023-01-01">January 1, 2023</time>
    <div class="author vcard"><span class="fn">Bolt</span></div>
    <div class="entry-content">
        <a href="http://external.com">External Link</a>
    </div>
</article>
</body>
</html>
"""

@pytest.mark.asyncio
async def test_parse_page():
    scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")
    posts = await scraper.parse_page(SAMPLE_HTML)
    assert isinstance(posts, list)
    assert len(posts) == 1

    post = posts[0]
    assert post["title"] == "Test Post"
    assert post["date"] == "January 1, 2023"
    assert post["author"] == "Bolt"
    assert "Tech" in post["categories"]
    assert post["external_link"] == "http://external.com"

@pytest.mark.asyncio
async def test_clean_text():
    scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")
    assert scraper.clean_text("  hello   world  ") == "hello world"
    assert scraper.clean_text("hello\xa0world") == "hello world"
