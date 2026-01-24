import os
import json
import pytest
import analytics

def test_generate_report_structure(tmp_path):
    # Setup dummy data
    data = [
        {
            "title": "Test Post",
            "date": "October 5, 2022",
            "datetime": "2022-10-05T07:47:49+02:00",
            "author": "Test Author",
            "categories": ["Test Category"],
            "external_link": "https://example.com",
            "domain": "example.com",
            "post_url": "https://test.wordpress.com/post"
        }
    ]

    output_file = tmp_path / "TEST_REPORT.md"

    # Run generation
    analytics.generate_report(data, str(output_file))

    # Read result
    with open(output_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Verify enhancements
    # 1. Top Anchor
    assert "<a id='top'></a>" in content

    # 2. Table of Contents
    assert "## 📑 Table of Contents" in content
    assert "[General Statistics](#stats)" in content

    # 3. Emojis in Headers
    assert "## 📈 General Statistics" in content
    assert "## 🌐 Top 10 Referenced Domains" in content

    # 4. Explicit Anchors
    assert "<a id='stats'></a>" in content
    assert "<a id='domains'></a>" in content

    # 5. Back to Top links
    assert "[⬆️ Back to Top](#top)" in content
