import pytest
import requests_mock
from seo_analyzer import SEOAnalyzer

HTML_PERFECT = """
<html>
    <head>
        <title>Perfect SEO Title For This Webpage Example</title>
        <meta name="description" content="This is a perfect meta description that is exactly the right length to show up well in Google search results without being truncated or too short." />
    </head>
    <body>
        <h1>Main Heading</h1>
        <img src="test.jpg" alt="Description of image" />
        <a href="#">Descriptive Link</a>
    </body>
</html>
"""

HTML_POOR = """
<html>
    <head>
        <title>Short</title>
        <!-- No Meta Description -->
    </head>
    <body>
        <!-- No H1 -->
        <h2>Subheading</h2>
        <img src="test.jpg" /> <!-- No Alt -->
        <a href="#">click here</a>
    </body>
</html>
"""

def test_analyzer_perfect_score(requests_mock):
    url = "http://example.com"
    requests_mock.get(url, text=HTML_PERFECT)

    analyzer = SEOAnalyzer(url)
    report = analyzer.run()

    assert report["score"] == 100
    assert len(report["issues"]) == 0
    assert len(report["passed"]) > 0

def test_analyzer_poor_score(requests_mock):
    url = "http://example.com/poor"
    requests_mock.get(url, text=HTML_POOR)

    analyzer = SEOAnalyzer(url)
    report = analyzer.run()

    assert report["score"] < 100

    issues = [i["message"] for i in report["issues"]]
    assert any("Title is too short" in i for i in issues)
    assert any("Missing meta description" in i for i in issues)
    assert any("Missing <h1> tag" in i for i in issues)
    assert any("missing 'alt' text" in i for i in issues)
    assert any("generic text" in i for i in issues)

def test_fetch_failure(requests_mock):
    url = "http://example.com/fail"
    requests_mock.get(url, status_code=404)

    analyzer = SEOAnalyzer(url)
    report = analyzer.run()

    assert report["score"] == 0
    assert report["issues"][0]["severity"] == "critical"
