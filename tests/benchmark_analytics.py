import time
import json
import random
import sys
import os
from datetime import datetime, timedelta

# Add parent directory to path to import analytics
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analytics import generate_report

def generate_dummy_data(n=100000):
    data = []
    domains = ['example.com', 'google.com', 'test.org', 'blog.net']
    authors = ['Alice', 'Bob', 'Charlie', 'Dave']
    categories = ['Tech', 'Life', 'Code', 'News', 'Random']

    start_date = datetime(2020, 1, 1)

    for i in range(n):
        dt = start_date + timedelta(days=random.randint(0, 1000))
        item = {
            'title': f'Post {i}',
            'date': dt.strftime('%B %d, %Y'),
            'datetime': dt.isoformat(),
            'author': random.choice(authors),
            'categories': random.sample(categories, k=random.randint(1, 3)),
            'external_link': f'https://{random.choice(domains)}/post/{i}',
            'domain': random.choice(domains),
            'post_url': f'https://markposition.wordpress.com/post/{i}'
        }
        data.append(item)
    return data

if __name__ == "__main__":
    print("Generating dummy data...")
    # Use fewer records for quick verification during development if needed,
    # but 200k is good for benchmark.
    data = generate_dummy_data(200000)
    print(f"Generated {len(data)} records.")

    start_time = time.time()
    generate_report(data, 'benchmark_report.md')
    end_time = time.time()

    print(f"Execution time: {end_time - start_time:.4f} seconds")

    # Clean up
    if os.path.exists('benchmark_report.md'):
        os.remove('benchmark_report.md')
