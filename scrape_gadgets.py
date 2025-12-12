import requests
from bs4 import BeautifulSoup
import json
import time

BASE_URL = "https://infogadgettech.wordpress.com"
OUTPUT_FILE = "gadgets.json"
MAX_PAGES = 5

def scrape_posts():
    all_posts = []
    url = BASE_URL
    page_count = 0

    while url and page_count < MAX_PAGES:
        print(f"Scraping {url}...")
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            break

        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('article', class_='post')

        for article in articles:
            post_data = {}

            # Extract Title
            title_tag = article.find('h2', class_='entry-title')
            if title_tag and title_tag.find('a'):
                post_data['title'] = title_tag.find('a').get_text(strip=True)
            else:
                post_data['title'] = "No Title"

            # Extract Date
            date_tag = article.find('time', class_='entry-date')
            if date_tag:
                post_data['date'] = date_tag.get_text(strip=True)
            else:
                post_data['date'] = "No Date"

            # Extract External Link
            # The structure seems to be that the content contains a paragraph with a link
            content_div = article.find('div', class_='entry-content')
            external_link = None
            if content_div:
                link_tag = content_div.find('a')
                if link_tag:
                    external_link = link_tag.get('href')

            post_data['external_link'] = external_link

            # Only add if we found a link, as the site seems to be a link aggregator
            if external_link:
                all_posts.append(post_data)

        # Pagination
        nav_previous = soup.find('div', class_='nav-previous')
        if nav_previous and nav_previous.find('a'):
            url = nav_previous.find('a')['href']
            page_count += 1
            time.sleep(1) # Be polite
        else:
            url = None

    return all_posts

def main():
    data = scrape_posts()
    with open(OUTPUT_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Scraped {len(data)} posts. Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
