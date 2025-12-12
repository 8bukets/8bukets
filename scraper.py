import requests
from bs4 import BeautifulSoup
import json
import time

def scrape_wishlist():
    base_url = "https://wishlist.design.blog"
    url = base_url
    print(f"Starting scrape at {url}...")

    all_data = []

    while url:
        print(f"Fetching {url}...")
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching URL: {e}")
            break

        soup = BeautifulSoup(response.content, "html.parser")
        articles = soup.find_all("article")
        print(f"Found {len(articles)} articles on this page.")

        for article in articles:
            item = {}

            # Title
            title_tag = article.select_one("header.entry-header h2.entry-title a")
            if title_tag:
                item['title'] = title_tag.get_text(strip=True)
            else:
                item['title'] = None

            # Link (External)
            content_div = article.select_one("div.entry-content")
            external_link = None
            if content_div:
                link_tag = content_div.find("a")
                if link_tag:
                    external_link = link_tag.get('href')
                    if not external_link and link_tag.get_text(strip=True).startswith('http'):
                         external_link = link_tag.get_text(strip=True)

                if not external_link:
                     text_content = content_div.get_text(strip=True)
                     if text_content.startswith('http'):
                         external_link = text_content

            item['external_link'] = external_link

            # Date
            time_tag = article.select_one(".entry-meta .posted-on time")
            if time_tag:
                item['date'] = time_tag.get_text(strip=True)
                item['datetime'] = time_tag.get('datetime')
            else:
                item['date'] = None
                item['datetime'] = None

            # Author
            author_tag = article.select_one(".entry-meta .byline .author a")
            if author_tag:
                item['author'] = author_tag.get_text(strip=True)
            else:
                item['author'] = None

            # Category
            cat_links = article.select("header.entry-header .cat-links a")
            if cat_links:
                item['categories'] = [cat.get_text(strip=True) for cat in cat_links]
            else:
                item['categories'] = []

            all_data.append(item)

        # Pagination: Look for "Older posts" link
        # Based on typical WP themes and my earlier debug, it might not be obvious if it's infinite scroll.
        # But if it is paginated, it usually has "nav-previous" or "Older posts".
        # However, previous debug showed no "nav-previous".
        # But requests.get returned 222 articles which seemed to be ALL articles.
        # If there IS pagination, we should check for it.
        # I'll check for any link containing "Older posts" case insensitive.

        next_page_link = None
        # Standard WP pagination
        nav_previous = soup.find("div", class_="nav-previous")
        if nav_previous:
            a_tag = nav_previous.find("a")
            if a_tag:
                next_page_link = a_tag.get('href')

        # If standard class not found, search text
        if not next_page_link:
            for a in soup.find_all("a", href=True):
                if "older posts" in a.get_text(strip=True).lower():
                    next_page_link = a['href']
                    break

        if next_page_link:
            print(f"Found next page: {next_page_link}")
            url = next_page_link
            time.sleep(1) # Be polite
        else:
            print("No more pages found.")
            url = None

    # Save to JSON
    output_file = "wishlist_data.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)

    print(f"Scraped {len(all_data)} articles in total.")
    print(f"Scraped data saved to {output_file}")

if __name__ == "__main__":
    scrape_wishlist()
