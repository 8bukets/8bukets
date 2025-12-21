import json
import logging
from collections import Counter
from textblob import TextBlob
import sys
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"File not found: {filepath}")
        return []
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON in {filepath}")
        return []

def analyze_sentiment(text):
    if not text:
        return 0.0, 0.0
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity

def generate_report(data, report_file="daily_report.md"):
    logging.info("Starting analysis...")

    total_posts = len(data)
    if total_posts == 0:
        logging.warning("No data to analyze.")
        return

    categories_counter = Counter()
    dates_counter = Counter()
    all_content = ""

    sentiments = []

    for post in data:
        # Category count
        for cat in post.get('categories', []):
            categories_counter[cat] += 1

        # Date count (simple string count)
        if post.get('date_text'):
            dates_counter[post['date_text']] += 1

        # Sentiment Analysis
        content = post.get('content', '')
        if content:
            # We treat markdown as text for simple sentiment analysis
            polarity, subjectivity = analyze_sentiment(content)
            sentiments.append(polarity)
            all_content += " " + content

    avg_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0

    # Keyword extraction (Nouns)
    blob = TextBlob(all_content)
    # Get top 20 noun phrases - limited to avoid huge processing if content is massive
    # Using word counts as proxy for speed if needed, but noun_phrases is better
    # For speed on large text, simple word frequency with stop words removal is better
    # Let's use simple word frequency of words > 4 chars to filter noise

    words = [w.lower() for w in blob.words if len(w) > 4 and w.isalpha()]
    word_freq = Counter(words).most_common(20)

    # Generate Markdown Report
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(f"# Daily Content Analysis Report\n\n")
        f.write(f"**Total Posts Analyzed:** {total_posts}\n\n")

        f.write(f"## Intelligent Insights\n")
        f.write(f"- **Average Sentiment Polarity:** {avg_sentiment:.4f} (-1.0 to 1.0)\n")
        sentiment_desc = "Neutral"
        if avg_sentiment > 0.1: sentiment_desc = "Generally Positive"
        elif avg_sentiment < -0.1: sentiment_desc = "Generally Negative"
        f.write(f"- **Tone:** {sentiment_desc}\n\n")

        f.write(f"## Top Categories\n")
        for cat, count in categories_counter.most_common(10):
            f.write(f"- {cat}: {count}\n")
        f.write("\n")

        f.write(f"## Top Keywords (Frequency)\n")
        for word, count in word_freq:
            f.write(f"- {word}: {count}\n")
        f.write("\n")

        f.write(f"## Recent Activity\n")
        for date, count in dates_counter.most_common(5):
            f.write(f"- {date}: {count} posts\n")

    logging.info(f"Report generated: {report_file}")

if __name__ == "__main__":
    data_file = "data.json"
    if len(sys.argv) > 1:
        data_file = sys.argv[1]

    data = load_data(data_file)
    generate_report(data)
