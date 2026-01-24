import pytest
import asyncio
from scraper import MarkPositionScraperAsync

SAMPLE_HTML = """
<!DOCTYPE html>
<html>
<body>
    <article class="post tag-tech category-technology status-publish">
        <header class="entry-header">
            <h1 class="entry-title">
                <a href="https://example.com/post/1" rel="bookmark">Test Post Title</a>
            </h1>
            <div class="entry-meta">
                <span class="posted-on">
                    <time class="entry-date published" datetime="2023-10-27T10:00:00+00:00">October 27, 2023</time>
                </span>
                <span class="byline">
                    <span class="author vcard">
                        <a class="url fn n" href="https://example.com/author/bolt">Bolt</a>
                    </span>
                </span>
            </div>
        </header>
        <div class="entry-content">
            <p>Some content with a <a href="https://external-domain.com">link</a>.</p>
        </div>
    </article>
</body>
</html>
"""

def test_parse_page():
    scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

    # parse_page is now synchronous
    results = scraper.parse_page(SAMPLE_HTML)

    assert len(results) == 1
    post = results[0]

    assert post['title'] == "Test Post Title"
    assert post['date'] == "October 27, 2023"
    assert post['datetime'] == "2023-10-27T10:00:00+00:00"
    assert post['author'] == "Bolt"
    assert "Technology" in post['categories']
    assert post['external_link'] == "https://external-domain.com"
    assert post['domain'] == "external-domain.com"
