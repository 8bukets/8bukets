# Promotion Tool

A command-line tool to automate the promotion of WordPress blogs. It fetches content from an RSS feed, generates social media posts with intelligent hashtags, downloads images, and performs health checks.

## Features

- **Automated Copywriting**: Generates tweets with hashtags derived from titles and content.
- **Image Downloading**: Automatically fetches featured images for easy posting.
- **SEO Health Check**: Verifies homepage metadata (OG tags, description).
- **Broken Link Checker**: Scans post content for dead links before you share them.
- **Export**: Saves a comprehensive Markdown report.

## Installation

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Basic usage:
```bash
python promote_site.py
```

Advanced usage:
```bash
python promote_site.py --url https://yourblog.wordpress.com --output report.md --download-images --check-links
```

### Arguments

- `--url`: The base URL of the site (default: `https://draagsterblocks.wordpress.com/`)
- `--feed`: Custom RSS feed URL (optional).
- `--output`: Path to save the report (e.g., `report.md`).
- `--download-images`: Enable downloading of featured images to `images/` folder.
- `--check-links`: specific flag to check for broken links in the post content.
