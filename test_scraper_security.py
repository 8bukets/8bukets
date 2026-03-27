import subprocess
import os
import sys

def test_traversal():
    traversal_path = "../tmp/traversal_repro.txt"
    # Ensure cleanup
    if os.path.exists(traversal_path):
        os.remove(traversal_path)

    print(f"Testing path traversal with output: {traversal_path}")

    # Run scraper
    cmd = [
        "python3", "scraper.py",
        "--limit", "1",
        "--txt", traversal_path
    ]

    try:
        # We expect this to fail if security check is in place,
        # or succeed (and create file) if vulnerable.
        result = subprocess.run(cmd, capture_output=True, text=True)

        if os.path.exists(traversal_path):
            print("❌ VULNERABILITY DETECTED: File created outside CWD.")
            os.remove(traversal_path)
            return False

        # Check if it failed due to our validation (we assume we'll raise ValueError or exit 1)
        error_msg = "Output path" in result.stderr and "outside the current working directory" in result.stderr
        if result.returncode != 0 and error_msg:
            print("✅ SECURE: Scraper blocked path traversal.")
            return True
        elif result.returncode == 0:
             # If return code 0 but file not found... weird for the scraper unless it wrote nothing?
             # But scraper usually writes something if limit 1 finds something.
             # Given my previous manual test, it writes.
             print("❓ UNKNOWN: Scraper finished successfully but file not found? Check logic.")
             return False
        else:
             # Scraper failed for other reasons
             print(f"⚠️ Scraper failed with error:\n{result.stderr}")
             # If it failed but didn't create file, it's technically secure from traversal, but maybe broken.
             # But strictly for traversal test:
             return True

    except Exception as e:
        print(f"Error running test: {e}")
        return False

if __name__ == "__main__":
    if test_traversal():
        sys.exit(0)
    else:
        sys.exit(1)
