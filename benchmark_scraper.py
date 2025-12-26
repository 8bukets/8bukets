import time
from bs4 import BeautifulSoup, Comment
import re

def parse_with_bs4(html):
    soup = BeautifulSoup(html, 'html.parser')
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
    news_html = None
    for c in comments:
        if 'rc92v0' in c and '<section' in c:
            news_html = c
            break
    return news_html

def parse_with_regex(html):
    # Regex to find comments.
    # HTML comments start with <!-- and end with -->
    # We use non-greedy match .*? and DOTALL to match newlines
    pattern = re.compile(r'<!--(.*?)-->', re.DOTALL)

    # We can iterate over matches
    for match in pattern.finditer(html):
        content = match.group(1)
        if 'rc92v0' in content and '<section' in content:
             return content
    return None

def main():
    with open('temp_oracle.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Verify correctness
    bs4_result = parse_with_bs4(html)
    regex_result = parse_with_regex(html)

    if bs4_result:
        print(f"BS4 found content length: {len(bs4_result)}")
    else:
        print("BS4 found nothing")

    if regex_result:
        print(f"Regex found content length: {len(regex_result)}")
    else:
        print("Regex found nothing")

    if bs4_result and regex_result and bs4_result.strip() == regex_result.strip():
        print("Results match!")
    else:
        print("Results DO NOT match or one failed.")

    # Benchmark BS4
    start_time = time.time()
    for _ in range(50):
        parse_with_bs4(html)
    bs4_duration = time.time() - start_time
    print(f"BS4 duration (50 runs): {bs4_duration:.4f}s")

    # Benchmark Regex
    start_time = time.time()
    for _ in range(50):
        parse_with_regex(html)
    regex_duration = time.time() - start_time
    print(f"Regex duration (50 runs): {regex_duration:.4f}s")

    if regex_duration < bs4_duration:
        print(f"Speedup: {bs4_duration / regex_duration:.2f}x")

if __name__ == "__main__":
    main()
