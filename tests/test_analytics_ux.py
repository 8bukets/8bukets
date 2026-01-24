import os
import sys
import json
import pytest

# Add parent directory to path so we can import analytics
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import analytics

def test_report_ux_elements(tmp_path):
    # Create dummy data
    data = [
        {
            "title": "Test Post",
            "date": "May 20, 2023",
            "datetime": "2023-05-20T12:00:00+00:00",
            "author": "Test Author",
            "categories": ["Test Cat"],
            "external_link": "https://example.com",
            "domain": "example.com",
            "post_url": "https://markposition.wordpress.com/test"
        }
    ]

    output_file = tmp_path / "REPORT.md"

    # Generate report
    analytics.generate_report(data, str(output_file))

    # Read report
    with open(output_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Check for UX elements
    assert "## Table of Contents" in content
    assert "<a id='top'></a>" in content
    assert "📊 General Statistics" in content
    assert "🔗 Top 10 Referenced Domains" in content
    assert "📂 Top 10 Categories" in content
    assert "📅 Posts by Year" in content
    assert "✍️ Authors" in content
    assert "<details>" in content
    assert "<summary>View Authors List</summary>" in content
    assert "[⬆️ Back to Top](#top)" in content
