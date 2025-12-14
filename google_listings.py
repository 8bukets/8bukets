import requests
from bs4 import BeautifulSoup
import time

def get_google_listings(query, num_results=10):
    print(f"Searching Google for: '{query}'")

    # Headers to mimic a browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    # Construct the search URL
    url = f"https://www.google.com/search?q={query}&num={num_results}"

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 429:
            print("Google blocked the request (429 Too Many Requests). This is common for automated scripts.")
            return

        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Google search results are typically in div.g
        results = soup.find_all('div', class_='g')

        if not results:
            # Fallback for different HTML structures (Google changes frequently)
            results = soup.find_all('div', class_='tF2Cxc')

        if not results:
             print("No results found in the HTML response. The layout might have changed or we were served a captcha page.")
             # Debug: print a snippet
             # print(soup.prettify()[:500])
             return

        print(f"\nFound {len(results)} results (showing top {num_results}):\n")

        count = 0
        for result in results:
            title_tag = result.find('h3')
            link_tag = result.find('a')

            if title_tag and link_tag:
                count += 1
                title = title_tag.get_text()
                link = link_tag['href']
                print(f"{count}. {title}")
                print(f"   {link}")
                print("-" * 40)

            if count >= num_results:
                break

        if count == 0:
            print("Could not parse results from the page.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Searching for listings for the webpage
    target_site = "site:malubeach.wordpress.com"
    get_google_listings(target_site)
