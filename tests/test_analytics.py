import pytest
import analytics

def test_get_domain():
    assert analytics.get_domain("https://www.google.com/search") == "google.com"
    assert analytics.get_domain("http://sub.domain.co.uk/page") == "sub.domain.co.uk"
    assert analytics.get_domain("not a url") is None
    assert analytics.get_domain(None) is None

def test_create_ascii_bar():
    # max_count = 10, count = 5 -> 50% of 20 chars = 10 chars
    bar = analytics.create_ascii_bar(5, 10, bar_length=20)
    assert bar == '██████████░░░░░░░░░░'

    # max_count = 0
    assert analytics.create_ascii_bar(5, 0) == ""

    # max_count = 10, count = 10
    assert analytics.create_ascii_bar(10, 10, bar_length=10) == '██████████'

def test_escape_markdown():
    assert analytics.escape_markdown("hello | world") == "hello &#124; world"
    assert analytics.escape_markdown("no pipes here") == "no pipes here"
    assert analytics.escape_markdown(None) == ""
    assert analytics.escape_markdown(123) == "123"
