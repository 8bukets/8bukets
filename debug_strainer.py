
import re
from bs4 import BeautifulSoup, SoupStrainer

with open('test_page.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Try with regex for class
strainer = SoupStrainer('article', class_=re.compile(r'\bpost\b'))
soup = BeautifulSoup(html, 'html.parser', parse_only=strainer)
articles = soup.find_all('article', class_='post')

print(f"Count with regex: {len(articles)}")
