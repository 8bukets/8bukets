# Markposition Scraper

This is a robust Python script designed to scrape the website `https://markposition.wordpress.com/`. It traverses all available pages (or a specified limit) and extracts detailed information about each post.

## Features

*   **Robustness**: Uses `requests.Session` with retry logic to handle network instability.
*   **Data Cleaning**: Normalizes whitespace and removes non-breaking spaces from extracted text.
*   **Extraction**: Captures:
    *   Title
    *   Date
    *   Author
    *   Categories
    *   External Link (Prioritizes content links, iframes/embeds, then title URLs)
    *   Post URL
*   **Flexible Output**: Supports JSON, CSV, and TXT output formats, configurable via CLI arguments.

## Requirements

*   Python 3.x
*   `requests` library
*   `beautifulsoup4` library

Install dependencies:

```bash
pip install requests beautifulsoup4
```

## Usage

Run the script from the command line:

```bash
python3 scraper.py
```

### Options

You can customize the execution using command-line arguments:

*   `--json`: Specify the output JSON filename (default: `links.json`).
*   `--csv`: Specify the output CSV filename (default: `links.csv`).
*   `--txt`: Specify the output TXT filename for unique links (default: `unique_links.txt`).
*   `--limit`: Limit the number of pages to scrape (useful for testing).

**Example:**

```bash
python3 scraper.py --json my_data.json --csv my_data.csv --limit 5
```

## Output Files

1.  **JSON**: A detailed list of dictionaries containing all extracted fields for each post.
2.  **CSV**: A tabular representation of the data, suitable for spreadsheets.
3.  **TXT**: A sorted list of unique external URLs found across all scraped posts.
