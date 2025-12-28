## 2024-02-14 - Path Traversal in File Outputs
**Vulnerability:** The scraper accepted arbitrary file paths (e.g., `../../evil.json`) for output, allowing potential arbitrary file overwrite if the script is run with elevated privileges or used in a web wrapper.
**Learning:** Python's `open()` does not validate if the path is within the intended directory. Explicit validation of input filenames is necessary.
**Prevention:** Strictly enforce that output filenames contain no directory components (using `os.path.dirname(f)`) if the intent is to only write to the current working directory.
