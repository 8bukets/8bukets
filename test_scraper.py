import pytest
import asyncio
from scraper import MarkPositionScraperAsync

SAMPLE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Test Page</title>
</head>
<body>
    <article class="post category-tech">
        <header class="entry-header">
            <h1 class="entry-title">
                <a href="https://example.com/post1" rel="bookmark">Test Post Title</a>
            </h1>
        </header>
        <div class="entry-content">
            <p>Some content here.</p>
            <a href="https://external-domain.com/link">External Link</a>
        </div>
        <footer class="entry-footer">
            <span class="cat-links">
                <a href="https://example.com/category/tech" rel="category tag">Tech</a>
            </span>
            <time class="entry-date" datetime="2023-01-01T12:00:00+00:00">January 1, 2023</time>
            <span class="author vcard">
                <a class="url fn n" href="https://example.com/author/jdoe">John Doe</a>
            </span>
        </footer>
    </article>
</body>
</html>
"""

@pytest.fixture
def sample_html():
    return SAMPLE_HTML

@pytest.mark.asyncio
async def test_parse_page(sample_html):
    scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")

    # Test the synchronous parsing logic
    posts = scraper._parse_page_sync(sample_html)

    assert len(posts) == 1
    post = posts[0]
    assert post['title'] == "Test Post Title"
    assert post['external_link'] == "https://external-domain.com/link"
    assert "Tech" in post['categories']
    assert post['date'] == "January 1, 2023"
