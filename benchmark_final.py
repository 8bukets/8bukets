
import timeit
from bs4 import BeautifulSoup, SoupStrainer
import re

with open('sample.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

def parse_full():
    soup = BeautifulSoup(html_content, 'html.parser')
    articles = soup.find_all('article', class_='post')
    return len(articles)

def parse_strained_tag():
    # Parsing only <article> tags is safer and provides good enough optimization
    strainer = SoupStrainer('article')
    soup = BeautifulSoup(html_content, 'html.parser', parse_only=strainer)
    articles = soup.find_all('article', class_='post')
    return len(articles)

print(f"Full parse count: {parse_full()}")
print(f"Strained tag parse count: {parse_strained_tag()}")

# Run benchmark
time_full = timeit.timeit(parse_full, number=100)
time_strained = timeit.timeit(parse_strained_tag, number=100)

print(f"Full parse time (100 runs): {time_full:.4f}s")
print(f"Strained parse time (100 runs): {time_strained:.4f}s")
print(f"Improvement: {(time_full - time_strained) / time_full * 100:.2f}%")
