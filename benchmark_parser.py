import timeit
from bs4 import BeautifulSoup

# Sample HTML payload mimicking a list of articles
html_content = """
<html>
<body>
  <div class="container">
    <article class="post">
      <h2 class="title"><a href="/post/1">Post 1</a></h2>
      <div class="content">Content 1</div>
    </article>
    <article class="post">
      <h2 class="title"><a href="/post/2">Post 2</a></h2>
      <div class="content">Content 2</div>
    </article>
    <article class="post">
      <h2 class="title"><a href="/post/3">Post 3</a></h2>
      <div class="content">Content 3</div>
    </article>
    <article class="post">
      <h2 class="title"><a href="/post/4">Post 4</a></h2>
      <div class="content">Content 4</div>
    </article>
    <article class="post">
      <h2 class="title"><a href="/post/5">Post 5</a></h2>
      <div class="content">Content 5</div>
    </article>
  </div>
</body>
</html>
""" * 100 # Multiply to make the payload larger

def parse_with_html_parser():
    soup = BeautifulSoup(html_content, 'html.parser')
    articles = soup.find_all('article', class_='post')
    return len(articles)

def parse_with_lxml():
    soup = BeautifulSoup(html_content, 'lxml')
    articles = soup.find_all('article', class_='post')
    return len(articles)

if __name__ == "__main__":
    iterations = 100

    print("Benchmarking html.parser...")
    html_parser_time = timeit.timeit(parse_with_html_parser, number=iterations)
    print(f"html.parser time for {iterations} iterations: {html_parser_time:.4f} seconds")

    print("Benchmarking lxml...")
    lxml_time = timeit.timeit(parse_with_lxml, number=iterations)
    print(f"lxml time for {iterations} iterations: {lxml_time:.4f} seconds")

    if lxml_time < html_parser_time:
        improvement = ((html_parser_time - lxml_time) / html_parser_time) * 100
        speedup = html_parser_time / lxml_time
        print(f"lxml is {improvement:.2f}% faster than html.parser ({speedup:.2f}x speedup)")
    else:
        print("lxml was not faster.")
