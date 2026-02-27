import pytest
from markposition.scraper import MarkPositionScraperAsync

@pytest.fixture
def scraper():
    return MarkPositionScraperAsync(
        output_json="test_links.json",
        output_csv="test_links.csv",
        output_txt="test_unique_links.txt"
    )

def test_clean_text(scraper):
    assert scraper.clean_text("  hello   world  ") == "hello world"
    assert scraper.clean_text("hello\xa0world") == "hello world"
    assert scraper.clean_text("") == ""
    assert scraper.clean_text(None) == ""

def test_is_url(scraper):
    assert scraper.is_url("https://google.com") is True
    assert scraper.is_url("http://example.org/path?q=1") is True
    assert scraper.is_url("not a url") is False
    assert scraper.is_url("  https://google.com  ") is True

def test_extract_domain(scraper):
    assert scraper.extract_domain("https://www.google.com/search") == "google.com"
    assert scraper.extract_domain("http://sub.domain.co.uk/page") == "sub.domain.co.uk"
    assert scraper.extract_domain("not a url") is None
    assert scraper.extract_domain(None) is None
