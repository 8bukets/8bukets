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
*   `--dry-run`: Run the scraper without writing to any output files (used for testing and data security).

### 2. Generate Report

Run the analytics script to process the JSON data:

```bash
python3 analytics.py
```

**Options:**
*   `--input`: Input JSON file (default: `links.json`)
*   `--output`: Output Markdown file (default: `REPORT.md`)
*   `--dry-run`: Run the analytics generator without writing the report file.


### 3. Run Autonomous System

Execute the full autonomous swarm cycle (includes scraping, data loading, agent intelligence routing, and reporting):

```bash
python3 run_system.py
```

**Options:**
*   `--loop`: Run the system continuously in a loop.
*   `--skip-scraper`: Skip the scraping phase and use existing data files.
*   `--dry-run`: Run the system without persisting data to databases or writing report files.

## Output Files

*   `links.json`: Full dataset in JSON format.
*   `links.csv`: Tabular dataset.
*   `unique_links.txt`: Sorted list of unique extracted URLs.
*   `REPORT.md`: Statistical summary of the data.

## Autonomous Workflows & GitKraken

The system is designed for fully autonomous operation with integrated version control.

### GitHub Integration
- **`GitHubEvolutionAgent`**: Automatically stages and commits system evolution (data, results, and config) during each cycle.
- **GitHub Actions**: A daily workflow is configured in `.github/workflows/autonomous_cycle.yml` to run the system autonomously.

### Monitoring with GitKraken
To monitor the system's progress using GitKraken:
1.  **Clone the Repository**: Open the repository in GitKraken.
2.  **Pull Updates**: The `GitHubEvolutionAgent` creates commits locally. If a `GITHUB_TOKEN` is provided, it will also push to origin.
3.  **Visualize Evolution**: Use GitKraken's graph view to track daily version increments and data updates.
4.  **Local Sync**: If the system is running on a server, use GitKraken to pull the latest autonomous commits to your local machine for analysis.

For detailed setup instructions, see `autonomous_workflow.md`.
