import os
import subprocess
import sys

def verify_report_ux():
    # Ensure links.json exists (using the one in root)
    if not os.path.exists("links.json"):
        print("Error: links.json not found.")
        sys.exit(1)

    # Run analytics.py
    cmd = ["python3", "analytics.py", "--output", "TEST_REPORT.md"]
    subprocess.run(cmd, check=True)

    # Read the generated report
    with open("TEST_REPORT.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Checks
    checks = {
        "Table of Contents": "Table of Contents" in content,
        "Explicit Anchors": "<a name=" in content,
        "Back to Top Links": "[Back to Top](#table-of-contents)" in content,
        "Emojis in Headers": any(emoji in content for emoji in ["📊", "🌐", "🏷️", "📅", "✍️"])
    }

    failed = False
    print("\n--- UX Verification Results ---")
    for name, passed in checks.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {name}")
        if not passed:
            failed = True

    # cleanup
    if os.path.exists("TEST_REPORT.md"):
        os.remove("TEST_REPORT.md")

    if failed:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    verify_report_ux()
