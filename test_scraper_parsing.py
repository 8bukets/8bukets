import pytest
import asyncio
from scraper import OracleNewsScraper

MOCK_HTML = """
<html>
<body>
    <div id="content">
        <!-- Should be ignored (no google-cloud) -->
        <a href="/news/announcement/test-article-2023-01-01/">
            <h3>Test Article</h3>
        </a>

        <!-- Should be kept -->
        <a href="/news/announcement/another-article-google-cloud-2023-05-20/">
            <h3>Another Article about Google Cloud</h3>
        </a>

        <!-- Should be ignored (wrong path) -->
        <a href="/other/link-google-cloud">Irrelevant Link</a>
    </div>
</body>
</html>
"""

@pytest.mark.asyncio
async def test_parse_page_logic():
    scraper = OracleNewsScraper("test.json", "test.csv", "test.txt")
    articles = await scraper.parse_page(MOCK_HTML)

    assert len(articles) == 1
    article = articles[0]
    assert article['title'] == "Another Article about Google Cloud"
    assert article['date'] == "2023-05-20"
    assert "oracle.com" in article['external_link']
