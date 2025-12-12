# Promotion Tool for Draagsterblocks

This tool helps automate the promotion of the `draagsterblocks.wordpress.com` blog (all-about-cookies.com).

## Features

1. **Social Media Draft Generation**: Fetches the latest posts from the RSS feed and generates draft tweets with relevant hashtags.
2. **SEO Analysis**: Checks the homepage for critical SEO metadata (Description, Open Graph tags).

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the script:
   ```bash
   python promote_site.py
   ```

## Requirements

- python 3.x
- feedparser
- requests
- beautifulsoup4
