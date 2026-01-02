from playwright.sync_api import sync_playwright, expect
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the index.html file
        filepath = os.path.abspath("index.html")
        page.goto(f"file://{filepath}")

        # Verify search input exists
        search_input = page.locator("#search-input")
        expect(search_input).to_be_visible()

        # Verify article list exists
        article_list = page.locator("#article-list")
        expect(article_list).to_be_visible()

        # Get all articles
        articles = article_list.locator("article").all()
        print(f"Found {len(articles)} articles initially.")

        # Type "Football" into the search box
        search_input.fill("Football")

        # Wait for debounce (300ms) + execution time
        page.wait_for_timeout(500)

        # Count visible articles
        visible_articles = 0
        for article in articles:
            # We need to check style.display because playwright is_visible handles standard visibility,
            # but we are toggling style.display='none'.
            # However, is_visible() should return false for display:none.
            if article.is_visible():
                visible_articles += 1

        print(f"Found {visible_articles} visible articles after search.")

        if visible_articles < len(articles):
             print("SUCCESS: Filtering occurred.")
        else:
             print("WARNING: No filtering occurred (or all matched).")

        # Take a screenshot
        page.screenshot(path="verification/search_result.png")
        print("Screenshot saved to verification/search_result.png")

        browser.close()

if __name__ == "__main__":
    run()
