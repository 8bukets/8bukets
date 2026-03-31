
import pytest
import asyncio
from bs4 import BeautifulSoup, SoupStrainer
from scraper import MarkPositionScraperAsync

@pytest.mark.asyncio
async def test_parse_page_structure():
    html_content = """
    <!DOCTYPE html>
    <html>
    <body>
        <article class="post">
            <h1 class="entry-title"><a href="http://example.com/1">Post 1</a></h1>
            <time class="entry-date" datetime="2023-01-01">Jan 1, 2023</time>
        </article>
        <article class="other">
            <h1>Ignored</h1>
        </article>
    </body>
    </html>
    """

    scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")
    posts = await scraper.parse_page(html_content)

    assert len(posts) == 1
    assert posts[0]['title'] == "Post 1"
    assert posts[0]['datetime'] == "2023-01-01"

@pytest.mark.asyncio
async def test_soup_strainer_optimization():
    # Verify that SoupStrainer is actually filtering
    html_content = """
    <html>
    <body>
        <div id="sidebar">Sidebar Content</div>
        <article class="post">Content</article>
    </body>
    </html>
    """

    strainer = SoupStrainer('article', class_='post')
    soup = BeautifulSoup(html_content, 'lxml', parse_only=strainer)

    # The sidebar should not be in the soup (or at least not searchable in the same way if it was strained out)
    # Actually, if strained, finding 'div' might return None or empty depending on how it's used.
    # But more importantly, the 'article' should be found.

    assert len(soup.find_all('article', class_='post')) == 1
    assert len(soup.find_all('div', id='sidebar')) == 0  # Should be 0 if strained correctly
