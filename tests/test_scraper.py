import pytest
from bs4 import BeautifulSoup
from scraper import clean_text, is_url, extract_categories, extract_domain, parse_page_content

def test_clean_text():
    assert clean_text("  Hello   World  ") == "Hello World"
    assert clean_text("No\xa0Breaking\xa0Space") == "No Breaking Space"
    assert clean_text("") == ""
    assert clean_text(None) == ""

def test_is_url():
    assert is_url("https://example.com") is True
    assert is_url("http://example.com") is True
    assert is_url("example.com") is False
    assert is_url("  https://example.com  ") is True

def test_extract_domain():
    assert extract_domain("https://www.example.com/page") == "example.com"
    assert extract_domain("http://sub.example.com") == "sub.example.com"
    assert extract_domain(None) is None
    assert extract_domain("not a url") == ""

def test_extract_categories():
    html = '<article class="post category-tech category-news"><div class="entry-content"></div></article>'
    soup = BeautifulSoup(html, 'html.parser')
    article = soup.find('article')
    categories = extract_categories(article)
    assert "Tech" in categories
    assert "News" in categories
    assert len(categories) == 2

def test_parse_page_content():
    html = """
    <html>
        <body>
            <article class="post category-tech">
                <header class="entry-header">
                    <h1 class="entry-title"><a href="http://example.com/post1">Test Post</a></h1>
                    <div class="entry-meta">
                        <span class="posted-on">
                            <time class="entry-date published" datetime="2023-01-01T12:00:00+00:00">January 1, 2023</time>
                        </span>
                        <span class="byline">
                            <span class="author vcard"><a class="url fn n" href="#">John Doe</a></span>
                        </span>
                    </div>
                </header>
                <div class="entry-content">
                    <p>Some content <a href="https://external.com">Link</a></p>
                </div>
            </article>
        </body>
    </html>
    """
    posts = parse_page_content(html)
    assert len(posts) == 1
    post = posts[0]
    assert post['title'] == "Test Post"
    assert post['date'] == "January 1, 2023"
    assert post['author'] == "John Doe"
    assert "Tech" in post['categories']
    assert post['external_link'] == "https://external.com"
    assert post['domain'] == "external.com"
    assert post['post_url'] == "http://example.com/post1"
