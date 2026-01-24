import os
import pytest
from analytics import generate_report

def test_generate_report_structure(tmp_path):
    # Dummy data
    data = [
        {
            "title": "Post 1",
            "datetime": "2023-01-01T10:00:00",
            "domain": "example.com",
            "categories": ["Tech"],
            "author": "Author A"
        },
        {
            "title": "Post 2",
            "datetime": "2023-01-02T10:00:00",
            "domain": "test.com",
            "categories": ["Science"],
            "author": "Author B"
        }
    ]

    # Add many authors to test collapsible section
    for i in range(10):
        data.append({
            "title": f"Post {i+3}",
            "datetime": "2023-01-03T10:00:00",
            "author": f"Author {i}"
        })

    output_file = tmp_path / "TEST_REPORT.md"
    generate_report(data, str(output_file))

    with open(output_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Verify TOC
    assert "## Table of Contents" in content
    assert "<a id='general-stats'></a>" in content or "General Statistics" in content # Anchor check logic might change depending on impl

    # Verify Emojis
    assert "📊 General Statistics" in content
    assert "🌐 Top 10 Referenced Domains" in content
    assert "🏷️ Top 10 Categories" in content

    # Verify Collapsible Authors
    assert "<details>" in content
    assert "<summary>" in content
    assert "✍️ Authors" in content
