import json
import os
import sys

# Add parent directory to path to import analytics
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analytics import generate_report, load_data

def verify():
    # Use absolute paths or relative to script location
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_file = os.path.join(base_dir, "links.json")
    output_file = os.path.join(base_dir, "VERIFY_REPORT.md")

    if os.path.exists(output_file):
        os.remove(output_file)

    data = load_data(input_file)
    generate_report(data, output_file)

    if not os.path.exists(output_file):
        print("❌ Verification Failed: Report not generated.")
        sys.exit(1)

    with open(output_file, 'r', encoding='utf-8') as f:
        content = f.read()

    expected_sections = [
        "# Markposition Analytics Report",
        "## General Statistics",
        "## Top 10 Referenced Domains",
        "## Top 10 Categories",
        "## Posts by Year",
        "## Authors"
    ]

    for section in expected_sections:
        if section not in content:
            print(f"❌ Verification Failed: Missing section '{section}'")
            sys.exit(1)

    print("✅ Verification Passed: Report structure matches.")
    # Clean up
    if os.path.exists(output_file):
        os.remove(output_file)

if __name__ == "__main__":
    verify()
