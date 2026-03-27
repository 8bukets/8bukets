
import pytest
from scraper import OracleNewsScraper

@pytest.fixture
def scraper():
    return OracleNewsScraper("test.json", "test.csv", "test.txt")

def test_parse_page_single_comment(scraper):
    html = """
    <html>
        <body>
            <!-- rc92v0
            <section>
                <ul>
                    <li class="rc92w3">
                        <div class="rc92-dt">Oct 15, 2025</div>
                        <h5><a href="/news/test-article.html">Test Article</a></h5>
                    </li>
                </ul>
            </section>
            -->
            <div>Other content</div>
        </body>
    </html>
    """

    posts = scraper.parse_page(html)
    assert len(posts) == 1
    assert posts[0]['title'] == 'Test Article'

def test_parse_page_multiple_comments(scraper):
    html = """
    <html>
        <body>
            <!-- Copyright 2025 -->
            <div>Header</div>
            <!-- rc92v0
            <section>
                <ul>
                    <li class="rc92w3">
                        <div class="rc92-dt">Oct 16, 2025</div>
                        <h5><a href="/news/article-2.html">Article 2</a></h5>
                    </li>
                </ul>
            </section>
            -->
            <!-- Footer -->
        </body>
    </html>
    """

    posts = scraper.parse_page(html)
    assert len(posts) == 1
    assert posts[0]['title'] == 'Article 2'
