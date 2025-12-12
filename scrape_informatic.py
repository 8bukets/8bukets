import requests
from bs4 import BeautifulSoup
import json
import time

BASE_URL = "https://informaticmagazine.data.blog"

def scrape():
    all_posts = []
    page = 1
    current_url = BASE_URL

    while current_url:
        print(f"Scraping {current_url}...")
        try:
            response = requests.get(current_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {current_url}: {e}")
            break

        soup = BeautifulSoup(response.content, 'html.parser')

        posts = soup.find_all('article')
        print(f"Found {len(posts)} posts on page {page}.")

        for post in posts:
            item = {}

            # Title
            title_tag = post.find('h2', class_='entry-title')
            if title_tag and title_tag.find('a'):
                item['title'] = title_tag.find('a').get_text(strip=True)
                item['post_url'] = title_tag.find('a')['href']
            else:
                item['title'] = None
                item['post_url'] = None

            # Date
            date_tag = post.find('time', class_='entry-date')
            if date_tag:
                item['date'] = date_tag.get('datetime')
                item['date_text'] = date_tag.get_text(strip=True)
            else:
                item['date'] = None
                item['date_text'] = None

            # Category
            cat_links = post.find('span', class_='cat-links')
            if cat_links:
                cats = [a.get_text(strip=True) for a in cat_links.find_all('a')]
                item['categories'] = cats
            else:
                item['categories'] = []

            # External Links in Content
            content_div = post.find('div', class_='entry-content')
            external_links = []
            if content_div:
                for link in content_div.find_all('a'):
                    href = link.get('href')
                    if href:
                        external_links.append(href)
            item['external_links'] = external_links

            # Image
            img = post.find('div', class_='featured-image')
            if img and img.find('img'):
                 item['image_url'] = img.find('img').get('src')
            else:
                item['image_url'] = None

            all_posts.append(item)

        # Pagination
        # Look for "Older posts" link in .nav-links .nav-previous a
        nav_previous = soup.find('div', class_='nav-previous')
        if nav_previous and nav_previous.find('a'):
            current_url = nav_previous.find('a')['href']
            page += 1
            # Be nice to the server
            time.sleep(1)
        else:
            current_url = None

    print(f"Total posts scraped: {len(all_posts)}")

    with open('data.json', 'w') as f:
        json.dump(all_posts, f, indent=4)
    print("Saved to data.json")

if __name__ == "__main__":
    scrape()
