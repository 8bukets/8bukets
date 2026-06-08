import time
import subprocess
import shutil
import sys
import os

def run_benchmark():
    input_file = "links.json"
    output_file = "REPORT_test.md"

    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found. Run generate_data.py first.")
        sys.exit(1)

    print(f"Running analytics.py on {input_file}...")

    start_time = time.perf_counter()

    # Run the analytics script as a subprocess to ensure clean state
    result = subprocess.run(
        [sys.executable, "analytics.py", "--input", input_file, "--output", output_file],
        capture_output=True,
        text=True
    )

    end_time = time.perf_counter()
    duration = end_time - start_time

    if result.returncode != 0:
        print("Error running analytics.py:")
        print(result.stderr)
        sys.exit(1)

    print(f"Success! Time taken: {duration:.4f} seconds")
    with open("benchmark_result.txt", "w") as f:
        f.write(f"{duration:.4f}")

    # Verify output exists
    if not os.path.exists(output_file):
        print(f"Error: {output_file} was not generated.")
        sys.exit(1)

    # Copy report for verification if requested
    if len(sys.argv) > 1 and sys.argv[1] == "--baseline":
        shutil.copy(output_file, "REPORT_baseline.md")
        print("Saved REPORT_baseline.md")

    return duration

if __name__ == "__main__":
    run_benchmark()
