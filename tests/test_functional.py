import pytest
from scraper import MarkPositionScraperAsync

@pytest.mark.asyncio
async def test_parse_page_extracts_data():
    html = """
    <article class="post category-tech">
        <h1 class="entry-title"><a href="http://example.com/post">Test Title</a></h1>
        <time class="entry-date" datetime="2023-01-01T12:00:00">January 1, 2023</time>
        <span class="author vcard"><span class="fn">John Doe</span></span>
        <div class="entry-content">
            <p>Some content</p>
            <a href="http://external.com">External Link</a>
        </div>
    </article>
    """
    scraper = MarkPositionScraperAsync("out.json", "out.csv", "out.txt")

    # New code is sync
    results = scraper.parse_page(html)

    assert len(results) == 1
    post = results[0]
    assert post['title'] == "Test Title"
    assert post['date'] == "January 1, 2023"
    assert post['author'] == "John Doe"
    assert post['external_link'] == "http://external.com"
    assert "Tech" in post['categories']
