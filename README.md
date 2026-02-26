# Markposition Scraper & Analytics

A robust, asynchronous toolset for scraping and analyzing data from `https://markposition.wordpress.com/`.

## Features

### Orchestrator (`run_system.py`)
*   **Dynamic Agent Discovery**: Automatically detects and loads agents from the `agents/` folder.
*   **Concurrent Stage-Based Execution**: Runs independent agents in parallel stages using `asyncio.gather`.
*   **SQLAlchemy Persistence**: Uses SQLite for cross-cycle memory management.
*   **Rich CLI Dashboard**: Real-time progress monitoring and summary reports.

### Scraper (`scraper.py`)
*   **High Performance**: Built with `aiohttp` and `asyncio` for concurrent fetching.
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

## Configuration & Deployment

### Environment Variables
The system can be configured using environment variables. See `.env.example` for available options.

### Docker
Deploy the autonomous system instantly:
```bash
docker-compose up --build
```

## Usage

### 1. Run Full Autonomous System

Executes the scraper followed by the concurrent agent pipeline and generates a daily report:

```bash
python3 run_system.py
```

### 2. Scrape Data Individually

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
