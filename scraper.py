import requests
from bs4 import BeautifulSoup
import json
import csv
import time

def scrape():
    base_url = 'https://malubeach.wordpress.com'
    current_url = base_url
    all_data = []
    unique_links = set()

    while current_url:
        print(f"Scraping {current_url}...")
        try:
            response = requests.get(current_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            articles = soup.find_all('article')
            for article in articles:
                # Extract Title
                title_tag = article.find('h2', class_='entry-title')
                title = title_tag.get_text(strip=True) if title_tag else "No Title"

                # Extract Date
                date_tag = article.find('time', class_='entry-date published')
                date = date_tag.get_text(strip=True) if date_tag else "No Date"

                # Extract External Link
                content_div = article.find('div', class_='entry-content')
                external_link = None
                if content_div:
                    link_tag = content_div.find('a')
                    if link_tag:
                        external_link = link_tag.get('href')

                if external_link:
                    all_data.append({
                        'title': title,
                        'date': date,
                        'link': external_link
                    })
                    unique_links.add(external_link)

            # Find next page
            nav_previous = soup.find('div', class_='nav-previous')
            if nav_previous and nav_previous.find('a'):
                current_url = nav_previous.find('a')['href']
            else:
                current_url = None

            # Be nice to the server
            time.sleep(1)

        except Exception as e:
            print(f"Error scraping {current_url}: {e}")
            break

    # Save to JSON
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(all_data, f, indent=4, ensure_ascii=False)
    print(f"Saved {len(all_data)} items to links.json")

    # Save to CSV
    with open('links.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Date', 'Link'])
        for item in all_data:
            writer.writerow([item['title'], item['date'], item['link']])
    print("Saved to links.csv")

    # Save Unique Links
    with open('unique_links.txt', 'w', encoding='utf-8') as f:
        for link in sorted(unique_links):
            f.write(link + '\n')
    print(f"Saved {len(unique_links)} unique links to unique_links.txt")

if __name__ == "__main__":
    scrape()
