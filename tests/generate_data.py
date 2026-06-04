import json
import random
from datetime import datetime, timedelta

def generate_data(num_records=50000, filename="links.json"):
    data = []
    domains = ["example.com", "google.com", "wordpress.com", "github.com", "wikipedia.org",
               "medium.com", "nytimes.com", "techcrunch.com", "bbc.co.uk", "cnn.com"]
    categories = ["Tech", "News", "Science", "Programming", "Life", "Politics", "Sports", "Music", "Art", "Travel"]
    authors = ["Alice", "Bob", "Charlie", "Dave", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"]

    start_date = datetime(2020, 1, 1)

    print(f"Generating {num_records} records...")

    for i in range(num_records):
        domain = random.choice(domains)
        # 10% chance of missing domain to test fallback, though scraper provides it.
        # But for benchmarking the optimization "use domain if available", we should have it available most of the time.
        # Let's say 99% have it, to match scraper behavior (scraper always tries to extract it).
        has_domain = True

        external_link = f"https://{domain}/article/{i}"

        cats = random.sample(categories, k=random.randint(0, 3))
        author = random.choice(authors)

        # Random date
        days_offset = random.randint(0, 365 * 3)
        dt = start_date + timedelta(days=days_offset)
        dt_str = dt.isoformat()

        record = {
            "title": f"Article {i}",
            "date": dt.strftime("%B %d, %Y"),
            "datetime": dt_str,
            "author": author,
            "categories": cats,
            "external_link": external_link,
            "domain": domain if has_domain else None,
            "post_url": f"https://markposition.wordpress.com/post/{i}"
        }
        data.append(record)

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    print(f"Data saved to {filename}")

if __name__ == "__main__":
    generate_data()
