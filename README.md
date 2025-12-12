# Markposition Scraper

This is a Python script designed to scrape the website `https://markposition.wordpress.com/`. It traverses all available pages and extracts information about each post.

## Functionality

The scraper performs the following actions:
1.  **Iterates through pages**: Starts from the homepage and follows pagination (e.g., `/page/2/`, `/page/3/`) until a 404 error is encountered or no more articles are found.
2.  **Extracts Data**: For each post found, it extracts:
    *   **Title**: The title of the blog post.
    *   **Date**: The publication date.
    *   **External Link**: The primary external link referenced in the post. This is determined by:
        *   Checking the first `<a>` tag in the post content.
        *   If missing, checking for an `<iframe>` (e.g., YouTube embed).
        *   If missing, checking if the post title itself is a URL.
    *   **Post URL**: The permalink to the blog post.
3.  **Saves Output**:
    *   `links.json`: A JSON file containing all scraped data (list of dictionaries).
    *   `links.csv`: A CSV file containing the same data in a tabular format.
    *   `unique_links.txt`: A text file containing a sorted list of unique external URLs extracted from the posts.

## Requirements

*   Python 3.x
*   `requests` library
*   `beautifulsoup4` library

You can install the dependencies using pip:

```bash
pip install requests beautifulsoup4
```

## Usage

Run the script from the command line:

```bash
python3 scraper.py
```

The script will output its progress to the console and create the output files in the same directory.
