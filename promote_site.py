import feedparser
import requests
from bs4 import BeautifulSoup
import warnings
from bs4 import MarkupResemblesLocatorWarning

# Filter spurious BS4 warnings
warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

def get_hashtags(title):
    """Generate relevant hashtags based on keywords in the title."""
    title_lower = title.lower()
    tags = ["#web"]

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

    # Default tags if none specific found
    if len(tags) == 1:
         tags.extend(["#blog", "#news"])

    return " ".join(tags)

def analyze_rss_feed(feed_url):
    print(f"Fetching RSS feed from: {feed_url}")
    try:
        feed = feedparser.parse(feed_url)
    except Exception as e:
        print(f"Error parsing feed: {e}")
        return []

    if feed.bozo:
        print("Warning: There might be an issue with the feed format.")

    print(f"Feed Title: {feed.feed.get('title', 'N/A')}")
    print(f"Feed Description: {feed.feed.get('description', 'N/A')}")
    print(f"Number of entries: {len(feed.entries)}")
    print("-" * 30)

    promotional_posts = []

    for i, entry in enumerate(feed.entries[:5]): # Check top 5 posts
        title = entry.get('title', '').strip()
        link = entry.get('link', '#')

        if not title:
            print(f"Skipping Post {i+1} due to missing title.")
            continue

        print(f"Post {i+1}: {title}")
        print(f"Link: {link}")

        # Generate promotional copy
        hashtags = get_hashtags(title)
        tweet = f"Check out our latest post: {title} \n{link} \n{hashtags}"
        promotional_posts.append(tweet)
        print("-" * 30)

    return promotional_posts

def analyze_homepage_seo(url):
    print(f"\nAnalyzing Homepage SEO for: {url}")
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        meta_desc = soup.find('meta', attrs={'name': 'description'})
        og_title = soup.find('meta', property='og:title')
        og_desc = soup.find('meta', property='og:description')
        og_image = soup.find('meta', property='og:image')

        print("SEO Report:")
        if meta_desc:
            print(f"[OK] Meta Description found: {meta_desc.get('content')}")
        else:
            print("[MISSING] Meta Description tag is missing! Consider adding one to improve search rankings.")

        if og_title:
            print(f"[OK] Open Graph Title found: {og_title.get('content')}")
        else:
            print("[MISSING] Open Graph Title is missing.")

        if og_desc:
            print(f"[OK] Open Graph Description found: {og_desc.get('content')}")
        else:
            print("[MISSING] Open Graph Description is missing.")

        if og_image:
            print(f"[OK] Open Graph Image found: {og_image.get('content')}")
        else:
            print("[MISSING] Open Graph Image is missing. Social shares won't have a preview image.")

    except Exception as e:
        print(f"Error analyzing homepage: {e}")

if __name__ == "__main__":
    rss_url = "https://draagsterblocks.wordpress.com/feed/"
    homepage_url = "https://draagsterblocks.wordpress.com/"

    social_posts = analyze_rss_feed(rss_url)

    print("\nGenerated Social Media Drafts:")
    if social_posts:
        for post in social_posts:
            print(post)
            print("---")
    else:
        print("No valid posts found to promote.")

    analyze_homepage_seo(homepage_url)
