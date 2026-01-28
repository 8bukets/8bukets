import json
import os
import subprocess
import sys

def create_dummy_data(filename):
    data = [
        {
            "title": "Test Post 1",
            "date": "Oct 15, 2025",
            "datetime": "2025-10-15T00:00:00",
            "author": "Oracle",
            "categories": ["News", "Cloud"],
            "external_link": "https://www.oracle.com/news/test1",
            "domain": "oracle.com",
            "post_url": "https://www.oracle.com/news/test1"
        },
        {
            "title": "Test Post 2",
            "date": "Sep 30, 2025",
            "datetime": "2025-09-30T00:00:00",
            "author": "Oracle",
            "categories": ["Announcement"],
            "external_link": "https://www.google.com/search",
            "domain": "google.com",
            "post_url": "https://www.google.com/search"
        }
    ]
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)
    print(f"Created {filename}")

def run_analytics(input_file, output_file):
    print(f"Running analytics.py...")
    result = subprocess.run(
        [sys.executable, 'analytics.py', '--input', input_file, '--output', output_file],
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        print(f"Error running analytics.py: {result.stderr}")
        sys.exit(1)
    print(f"Generated {output_file}")

def verify_report(filename):
    print(f"Verifying {filename}...")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Checklist
    checks = {
        "TOC Anchor": "<a name='table-of-contents'></a>",
        "TOC Header": "## Table of Contents",
        "TOC Link (General)": "- [General Statistics](#general-statistics)",
        "Section Anchor (General)": "<a name='general-statistics'></a>",
        "Emoji Header (General)": "## 📈 General Statistics",
        "Back to Top": "[Back to Top](#table-of-contents)",
        "Emoji Header (Domains)": "## 🔗 Top 10 Referenced Domains",
    }

    failed = False
    for name, expected in checks.items():
        if expected in content:
            print(f"✅ {name} found.")
        else:
            print(f"❌ {name} NOT found.")
            failed = True

    if failed:
        print("Verification FAILED.")
        sys.exit(1)
    else:
        print("Verification PASSED.")

def main():
    input_file = "dummy_links.json"
    output_file = "REPORT_TEST.md"

    create_dummy_data(input_file)
    try:
        run_analytics(input_file, output_file)
        verify_report(output_file)
    finally:
        # Cleanup
        if os.path.exists(input_file):
            os.remove(input_file)
        if os.path.exists(output_file):
            os.remove(output_file)

if __name__ == "__main__":
    main()
