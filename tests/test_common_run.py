import subprocess
import os
import sys
import pytest

def test_common_run_execution():
    """
    Test that the common_run.py script executes the full pipeline successfully.
    """
    # Ensure environment variables are set to avoid LLM errors during automated tests
    env = os.environ.copy()
    env["SYSTEM_AUTH_TOKEN"] = "test_token"
    env["GEMINI_API_KEY"] = "dummy_key"

    # Run the script
    result = subprocess.run(
        [sys.executable, "common_run.py"],
        env=env,
        capture_output=True,
        text=True
    )

    # Output stdout/stderr if the test fails for debugging
    if result.returncode != 0:
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)

    # Assert success
    assert result.returncode == 0, "common_run.py failed to execute."

    # Assert that results are generated (Analytics phase worked)
    assert os.path.exists("REPORT.md") or os.path.exists("results"), "Expected output artifacts not found."

if __name__ == "__main__":
    pytest.main([__file__])
