# Markposition Scraper & Analytics

A robust, asynchronous toolset for scraping and analyzing data from `https://markposition.wordpress.com/`.

## Features

### Scraper (`scraper.py`)
*   **High Performance**: Built with `aiohttp` and `asyncio` for concurrent fetching, significantly faster than synchronous scrapers.
*   **Robust**: Handles network errors and pagination automatically (stops on 404 or empty pages).
*   **Smart Extraction**:
    *   Prioritizes content links, then embedded iframes (e.g., YouTube), then title URLs.
    *   Extracts metadata: Title, Date, Author, Categories, External Link, Domain, Post URL.
*   **Data Cleaning**: Normalizes text fields.
*   **Multiple Outputs**: JSON, CSV, and TXT (unique links).

### Analytics (`analytics.py`)
*   **Insightful Reports**: Generates a Markdown report (`REPORT.md`) summarizing the scraped data.
*   **Metrics**:
    *   Total posts and date range.
    *   Top referenced domains.
    *   Top categories.
    *   Posting frequency by year.
    *   Author statistics.

## Requirements

*   Python 3.7+
*   `aiohttp`
*   `beautifulsoup4`
*   `requests` (legacy dependency, optional for analytics)

Install dependencies:

```bash
pip install aiohttp beautifulsoup4 requests
```

## Usage

### 1. Scrape Data

Run the asynchronous scraper to fetch data:

```bash
python3 scraper.py
```

**Options:**
*   `--json`: Output JSON filename (default: `links.json`)
*   `--csv`: Output CSV filename (default: `links.csv`)
*   `--txt`: Output TXT filename for unique links (default: `unique_links.txt`)
*   `--limit`: Limit the number of pages to scrape (e.g., `--limit 5`).
*   `--concurrency`: Number of concurrent requests (default: 5).

### 2. Generate Report

Run the analytics script to process the JSON data:

```bash
python3 analytics.py
```

**Options:**
*   `--input`: Input JSON file (default: `links.json`)
*   `--output`: Output Markdown file (default: `REPORT.md`)

## Output Files

*   `links.json`: Full dataset in JSON format.
*   `links.csv`: Tabular dataset.
*   `unique_links.txt`: Sorted list of unique extracted URLs.
*   `REPORT.md`: Statistical summary of the data.
