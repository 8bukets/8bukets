import os
import sys
import json
import pytest

# Add parent directory to sys.path to allow importing analytics
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analytics import generate_report

@pytest.fixture
def dummy_data_file(tmp_path):
    data = [
        {
            "title": "Post 1",
            "datetime": "2023-01-01T12:00:00",
            "author": "Author A",
            "categories": ["Cat1", "Cat2"],
            "external_link": "https://example.com/post1",
            "domain": "example.com"
        },
        {
            "title": "Post 2",
            "datetime": "2023-02-01T12:00:00",
            "author": "Author B",
            "categories": ["Cat2"],
            "external_link": "https://google.com/post2",
            "domain": "google.com"
        }
    ]
    p = tmp_path / "dummy_links.json"
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f)
    return str(p)

def test_report_ux_enhancements(dummy_data_file, tmp_path):
    output_file = tmp_path / "REPORT_TEST.md"

    # Load data manually since generate_report expects a list, not a file path
    with open(dummy_data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    generate_report(data, str(output_file))

    with open(output_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check for Emojis in headers
    assert "📊 General Statistics" in content
    assert "🌐 Top 10 Referenced Domains" in content
    assert "📂 Top 10 Categories" in content
    assert "📅 Posts by Year" in content
    assert "✍️ Authors" in content

    # Check for Table of Contents
    assert "<a id='table-of-contents'></a>" in content
    assert "## Table of Contents" in content
    assert "[📊 General Statistics](#general-statistics)" in content

    # Check for Back to Top links
    assert "⬆️ Back to Top" in content

    # Check for HTML anchors (optional but good practice)
    assert "<a id='general-statistics'></a>" in content
