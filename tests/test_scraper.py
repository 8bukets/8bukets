import pytest
import requests_mock
from scraper import WordPressScraper, Post

HTML_CONTENT = """
<html>
    <body>
        <article class="post">
            <h1 class="entry-title"><a href="http://example.com/post1">Test Post</a></h1>
            <time class="entry-date" datetime="2023-01-01">January 1, 2023</time>
            <div class="entry-content">
                <p>Check this out: <a href="http://external.com">External Link</a></p>
            </div>
        </article>
        <div class="nav-links">
            <span class="page-numbers current">1</span>
            <a class="page-numbers" href="http://example.com/page/2/">2</a>
            <a class="next page-numbers" href="http://example.com/page/2/">Next</a>
        </div>
    </body>
</html>
"""

LAST_PAGE_CONTENT = """
<html>
    <body>
        <article class="post">
            <h1 class="entry-title"><a href="http://example.com/post2">Last Post</a></h1>
            <time class="entry-date" datetime="2023-01-02">January 2, 2023</time>
            <div class="entry-content">
                <p>No links here.</p>
            </div>
        </article>
    </body>
</html>
"""

def test_scraper_initialization():
    scraper = WordPressScraper("http://example.com/")
    assert scraper.base_url == "http://example.com/"

def test_is_url():
    scraper = WordPressScraper("http://example.com/")
    assert scraper.is_url("http://google.com") is True
    assert scraper.is_url("https://google.com") is True
    assert scraper.is_url("not a url") is False

def test_scrape_single_page(requests_mock):
    base_url = "http://example.com/"
    scraper = WordPressScraper(base_url, delay=0)

    requests_mock.get(base_url, text=LAST_PAGE_CONTENT)

    posts = scraper.scrape()

    assert len(posts) == 1
    assert posts[0].title == "Last Post"
    assert posts[0].date == "January 2, 2023"
    assert posts[0].external_link is None

def test_scrape_pagination(requests_mock):
    base_url = "http://example.com/"
    scraper = WordPressScraper(base_url, delay=0)

    requests_mock.get(base_url, text=HTML_CONTENT)
    requests_mock.get(f"{base_url}page/2/", text=LAST_PAGE_CONTENT)

    posts = scraper.scrape()

    assert len(posts) == 2
    assert posts[0].title == "Test Post"
    assert posts[0].external_link == "http://external.com"
    assert posts[1].title == "Last Post"
