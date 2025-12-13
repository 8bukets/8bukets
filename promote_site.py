import feedparser
import requests
from bs4 import BeautifulSoup
import warnings
from bs4 import MarkupResemblesLocatorWarning
import argparse
import os
import re
from collections import Counter
import sys

# Filter spurious BS4 warnings
warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

# Common English stop words
STOP_WORDS = {
    'the', 'and', 'to', 'of', 'a', 'in', 'is', 'it', 'you', 'that', 'he', 'was', 'for', 'on', 'are', 'with', 'as', 'i', 'his', 'they',
    'be', 'at', 'one', 'have', 'this', 'from', 'or', 'had', 'by', 'hot', 'word', 'but', 'what', 'some', 'we', 'can', 'out', 'other',
    'were', 'all', 'there', 'when', 'up', 'use', 'your', 'how', 'said', 'an', 'each', 'she', 'which', 'do', 'their', 'time', 'if',
    'will', 'way', 'about', 'many', 'then', 'them', 'write', 'would', 'like', 'so', 'these', 'her', 'long', 'make', 'thing', 'see',
    'him', 'two', 'has', 'look', 'more', 'day', 'could', 'go', 'come', 'did', 'number', 'sound', 'no', 'most', 'people', 'my', 'over',
    'know', 'water', 'than', 'call', 'first', 'who', 'may', 'down', 'side', 'been', 'now', 'find', 'any', 'new', 'work', 'part', 'take',
    'get', 'place', 'made', 'live', 'where', 'after', 'back', 'little', 'only', 'round', 'man', 'year', 'came', 'show', 'every', 'good',
    'me', 'give', 'our', 'under', 'name', 'very', 'through', 'just', 'form', 'sentence', 'great', 'think', 'say', 'help', 'low', 'line',
    'differ', 'turn', 'cause', 'much', 'mean', 'before', 'move', 'right', 'boy', 'old', 'too', 'same', 'tell', 'does', 'set', 'three',
    'want', 'air', 'well', 'also', 'play', 'small', 'end', 'put', 'home', 'read', 'hand', 'port', 'large', 'spell', 'add', 'even', 'land',
    'here', 'must', 'big', 'high', 'such', 'follow', 'act', 'why', 'ask', 'men', 'change', 'went', 'light', 'kind', 'off', 'need', 'house',
    'picture', 'try', 'us', 'again', 'animal', 'point', 'mother', 'world', 'near', 'build', 'self', 'earth', 'father', 'check', 'out',
    'cookie', 'cookies', 'website', 'site', 'web', 'page', 'link', 'click', 'http', 'https', 'com', 'org', 'net'
}

def extract_keywords(text, num=3):
    """Extract top keywords from text excluding stop words."""
    # Clean text: remove special chars and digits
    text = re.sub(r'[^\w\s]', '', text).lower()
    words = [w for w in text.split() if w not in STOP_WORDS and len(w) > 3]
    count = Counter(words)
    return [word for word, _ in count.most_common(num)]

def get_hashtags(title, description=""):
    """Generate relevant hashtags based on keywords in the title and description."""
    title_lower = title.lower()
    tags = ["#web"]

    # Static checking
    if "cookie" in title_lower:
        tags.append("#cookies")
    if "privacy" in title_lower:
        tags.append("#privacy")
    if "google" in title_lower:
        tags.append("#google")
    if "analytics" in title_lower:
        tags.append("#analytics")
    if "rock" in title_lower or "music" in title_lower:
        tags.append("#music")
        tags.append("#rock")
    if "data" in title_lower:
        tags.append("#data")

    # Dynamic keyword extraction from description
    if description:
        soup = BeautifulSoup(description, 'html.parser')
        text_content = soup.get_text()
        keywords = extract_keywords(text_content, num=3)
        for kw in keywords:
            tag = f"#{kw}"
            if tag not in tags:
                tags.append(tag)

    # Default tags if none specific found
    if len(tags) == 1:
         tags.extend(["#blog", "#news"])

    return " ".join(tags[:6]) # Limit to 6 tags

def download_image(url, save_dir="images"):
    """Downloads an image to the specified directory."""
    if not url:
        return None

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    try:
        filename = url.split('/')[-1].split('?')[0] # Basic filename extraction
        if not filename or len(filename) > 50:
             filename = "image_" + str(hash(url)) + ".jpg"

        filepath = os.path.join(save_dir, filename)

        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            return filepath
    except Exception as e:
        print(f"Failed to download image {url}: {e}")
        return None

def check_broken_links(html_content):
    """Finds and checks links within HTML content."""
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a', href=True)
    broken_links = []

    for a in links:
        url = a['href']
        if not url.startswith('http'):
            continue

        try:
            # Set timeout to avoid hanging
            r = requests.head(url, timeout=5, allow_redirects=True)
            if r.status_code >= 400:
                broken_links.append((url, r.status_code))
        except requests.RequestException:
             broken_links.append((url, "Connection Failed"))

    return broken_links

def analyze_rss_feed(feed_url, download_images=False, check_links=False):
    print(f"Fetching RSS feed from: {feed_url}")
    try:
        feed = feedparser.parse(feed_url)
    except Exception as e:
        print(f"Error parsing feed: {e}")
        return [], []

    if feed.bozo:
        print("Warning: There might be an issue with the feed format.")

    print(f"Feed Title: {feed.feed.get('title', 'N/A')}")
    num_entries = len(feed.entries)
    print(f"Number of entries: {num_entries}")
    print("-" * 30)

    promotional_data = []

    # Process top 5 posts
    for i, entry in enumerate(feed.entries[:5]):
        title = entry.get('title', '').strip()
        link = entry.get('link', '#')
        description = entry.get('description', '')

        # Try to find an image in media_content or description
        image_url = None
        if 'media_content' in entry:
            image_url = entry.media_content[0]['url']
        elif 'media_thumbnail' in entry:
            image_url = entry.media_thumbnail[0]['url']
        else:
             # Fallback: extract img from description
             soup = BeautifulSoup(description, 'html.parser')
             img = soup.find('img')
             if img:
                 image_url = img.get('src')

        local_image_path = None
        if download_images and image_url:
            print(f"Downloading image for post '{title}'...")
            local_image_path = download_image(image_url)

        broken = []
        if check_links:
            print(f"Checking links for post '{title}'...")
            broken = check_broken_links(description)

        if not title:
            title = "New Post"

        # Generate promotional copy
        hashtags = get_hashtags(title, description)
        tweet = f"Check out our latest post: {title} \n{link} \n{hashtags}"

        post_data = {
            'title': title,
            'link': link,
            'tweet': tweet,
            'image_url': image_url,
            'local_image': local_image_path,
            'broken_links': broken
        }
        promotional_data.append(post_data)

    return promotional_data

def analyze_homepage_seo(url):
    print(f"\nAnalyzing Homepage SEO for: {url}")
    report = []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        meta_desc = soup.find('meta', attrs={'name': 'description'})
        og_title = soup.find('meta', property='og:title')
        og_desc = soup.find('meta', property='og:description')
        og_image = soup.find('meta', property='og:image')

        if meta_desc:
            report.append(f"[OK] Meta Description: {meta_desc.get('content')}")
        else:
            report.append("[MISSING] Meta Description tag is missing!")

        if og_title:
            report.append(f"[OK] Open Graph Title: {og_title.get('content')}")
        else:
            report.append("[MISSING] Open Graph Title is missing.")

        if og_desc:
            report.append(f"[OK] Open Graph Description: {og_desc.get('content')}")
        else:
            report.append("[MISSING] Open Graph Description is missing.")

        if og_image:
            report.append(f"[OK] Open Graph Image: {og_image.get('content')}")
        else:
            report.append("[MISSING] Open Graph Image is missing.")

    except Exception as e:
        report.append(f"Error analyzing homepage: {e}")

    return report

def main():
    parser = argparse.ArgumentParser(description="Promote Site Tool - Auto-generate social media content from RSS.")
    parser.add_argument("--url", default="https://draagsterblocks.wordpress.com/", help="Base URL of the WordPress site.")
    parser.add_argument("--feed", help="RSS Feed URL (optional, defaults to url/feed/).")
    parser.add_argument("--output", help="File path to save the report (Markdown format).")
    parser.add_argument("--download-images", action="store_true", help="Download featured images to 'images/' folder.")
    parser.add_argument("--check-links", action="store_true", help="Check for broken links in post descriptions.")

    args = parser.parse_args()

    homepage_url = args.url
    rss_url = args.feed if args.feed else homepage_url.rstrip('/') + "/feed/"

    print("Starting promotion analysis...")

    posts = analyze_rss_feed(rss_url, download_images=args.download_images, check_links=args.check_links)
    seo_report = analyze_homepage_seo(homepage_url)

    # Output to Console
    print("\n" + "="*40)
    print("SOCIAL MEDIA DRAFTS")
    print("="*40)
    for p in posts:
        print(p['tweet'])
        if p['local_image']:
            print(f"[Image saved to]: {p['local_image']}")
        if p['broken_links']:
            print(f"[WARNING] Broken links found: {p['broken_links']}")
        print("-" * 20)

    print("\n" + "="*40)
    print("SEO HEALTH CHECK")
    print("="*40)
    for line in seo_report:
        print(line)

    # Output to File
    if args.output:
        with open(args.output, "w") as f:
            f.write(f"# Promotion Report for {homepage_url}\n\n")
            f.write("## Social Media Drafts\n\n")
            for p in posts:
                f.write(f"### {p['title']}\n")
                f.write(f"**Draft:**\n> {p['tweet']}\n\n")
                if p['image_url']:
                    f.write(f"**Image source:** {p['image_url']}\n")
                if p['local_image']:
                    f.write(f"**Local Image:** `{p['local_image']}`\n")

                if p['broken_links']:
                    f.write("\n**WARNING: Broken Links Detected**\n")
                    for link, status in p['broken_links']:
                        f.write(f"- {link} (Status: {status})\n")
                f.write("\n---\n\n")

            f.write("## SEO Health Check\n\n")
            for line in seo_report:
                f.write(f"- {line}\n")
        print(f"\nReport saved to {args.output}")

if __name__ == "__main__":
    main()
