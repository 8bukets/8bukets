import pytest
from scraper import MarkPositionScraperAsync

@pytest.mark.asyncio
async def test_unsafe_links_extraction():
    unsafe_html = """
    <article class="post">
        <h1 class="entry-title"><a href="http://example.com/1">Post 1</a></h1>
        <div class="entry-content">
            <a href="javascript:alert('XSS')">Javascript Link</a>
        </div>
    </article>
    <article class="post">
        <h1 class="entry-title"><a href="http://example.com/2">Post 2</a></h1>
        <div class="entry-content">
            <a href="file:///etc/passwd">File Link</a>
        </div>
    </article>
    <article class="post">
        <h1 class="entry-title"><a href="http://example.com/3">Post 3</a></h1>
        <div class="entry-content">
            <a href="http://example.com/newline\ninjection">Newline Link</a>
        </div>
    </article>
    <article class="post">
        <h1 class="entry-title"><a href="http://example.com/4">Post 4</a></h1>
        <div class="entry-content">
            <a href="   https://valid.com/page  ">Valid Link with spaces</a>
        </div>
    </article>
    """
    scraper = MarkPositionScraperAsync("test.json", "test.csv", "test.txt")
    posts = await scraper.parse_page(unsafe_html)

    links = [p.get('external_link') for p in posts]

    assert len(links) == 4
    assert links[0] is None, f"Javascript link should be None, got {links[0]}"
    assert links[1] is None, f"File link should be None, got {links[1]}"
    assert links[2] == "http://example.com/newlineinjection", f"Newline link should be cleaned, got {links[2]}"
    assert links[3] == "https://valid.com/page", f"Spaced link should be cleaned, got {links[3]}"
