import sqlite3
import os
import logging
from datetime import datetime, timedelta
from collections import Counter
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ReportGenerator:
    def __init__(self, db_name="wishlist_data.db", report_dir="reports"):
        self.db_name = db_name
        self.report_dir = report_dir
        if not os.path.exists(self.report_dir):
            os.makedirs(self.report_dir)

    def create_ascii_bar(self, count, max_count, width=10):
        if max_count == 0:
            return ""
        bar_len = int((count / max_count) * width)
        return "█" * bar_len + "░" * (width - bar_len)

    def generate_daily_report(self):
        logger.info("Generating daily report...")

        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()

                # Get total count
                cursor.execute("SELECT COUNT(*) FROM posts")
                total_posts = cursor.fetchone()[0]

                yesterday = datetime.now() - timedelta(days=1)

                # New posts
                cursor.execute("SELECT title, post_url, scraped_at FROM posts WHERE scraped_at >= ? AND id NOT IN (SELECT post_id FROM changes)", (yesterday,))
                new_posts = cursor.fetchall()

                # Updated posts
                cursor.execute("""
                    SELECT p.title, p.post_url, c.field, c.old_value, c.new_value, c.changed_at
                    FROM changes c
                    JOIN posts p ON c.post_id = p.id
                    WHERE c.changed_at >= ?
                """, (yesterday,))
                updated_posts = cursor.fetchall()

                # Latest SEO rankings
                cursor.execute("SELECT query, rank, title, url, checked_at FROM rankings WHERE checked_at >= ? ORDER BY checked_at DESC", (yesterday,))
                rankings = cursor.fetchall()

                # Previous SEO rankings (older than 24h)
                cursor.execute("SELECT query, rank, checked_at FROM rankings WHERE checked_at < ? ORDER BY checked_at DESC", (yesterday,))
                past_rankings = cursor.fetchall()

        except sqlite3.Error as e:
            logger.error(f"Database error: {e}")
            return

        report_date = datetime.now().strftime("%Y-%m-%d")
        report_filename = os.path.join(self.report_dir, f"report_{report_date}.md")

        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(f"# Daily Scraper Report - {report_date}\n\n")
            f.write(f"**Total Posts:** {total_posts}\n")
            f.write(f"**New Posts:** {len(new_posts)}\n")
            f.write(f"**Updated Posts:** {len(updated_posts)}\n\n")

            # Recommendations Section
            f.write("## 💡 Recommendations\n\n")
            recommendations = self.generate_recommendations(new_posts, updated_posts, rankings, past_rankings)
            for rec in recommendations:
                f.write(f"- {rec}\n")
            if not recommendations:
                f.write("Everything looks stable. No specific actions recommended.\n")
            f.write("\n")

            # Keyword Analysis
            all_recent_titles = [p[0] for p in new_posts] + [p[0] for p in updated_posts]
            if all_recent_titles:
                f.write("## 🧠 Keyword Trends\n\n")
                f.write("Most frequent words in recent activity:\n\n")
                keywords = self.analyze_keywords(all_recent_titles)

                max_freq = keywords[0][1] if keywords else 0

                f.write("| Keyword | Frequency | Distribution |\n")
                f.write("|---|---|---|\n")
                for word, count in keywords:
                    bar = self.create_ascii_bar(count, max_freq)
                    f.write(f"| {word} | {count} | `{bar}` |\n")
                f.write("\n")

            # SEO Rankings Trend
            f.write("## 📈 SEO Trend Analysis\n\n")
            if rankings:
                f.write("| Query | Rank | Change | Checked At |\n")
                f.write("|---|---|---|---|---|\n")
                trends = self.analyze_seo_trends(rankings, past_rankings)
                for item in trends:
                    f.write(f"| {item['query']} | {item['rank']} | {item['change']} | {item['date']} |\n")
            else:
                f.write("No SEO ranking data for today.\n\n")

            # Content Updates Section
            if updated_posts:
                f.write("## 🔄 Content Updates\n\n")
                f.write("| Post | Field | Old | New | Time |\n")
                f.write("|---|---|---|---|---|\n")
                for u in updated_posts:
                    title, url, field, old, new, time = u
                    title = title.replace("|", "-")
                    f.write(f"| [{title}]({url}) | {field} | {old} | {new} | {time} |\n")
                f.write("\n")

            # New Posts Section
            if new_posts:
                f.write("## 🆕 Recently Scraped Posts\n\n")
                f.write("| Title | Scraped At | Link |\n")
                f.write("|---|---|---|\n")
                for post in new_posts:
                    title, url, scraped_at = post
                    title = title.replace("|", "-") if title else "No Title"
                    f.write(f"| {title} | {scraped_at} | [View]({url}) |\n")
            else:
                f.write("No new posts scraped in the last 24 hours.\n")

        logger.info(f"Report generated: {report_filename}")

    def analyze_keywords(self, titles):
        text = " ".join(titles).lower()
        text = re.sub(r'[^\w\s]', '', text)
        words = text.split()
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'this', 'that', 'it', 'as', 'from', 'de', 'la'}
        filtered_words = [w for w in words if w not in stop_words and len(w) > 2]
        return Counter(filtered_words).most_common(10)

    def analyze_seo_trends(self, current, past):
        analysis = []
        past_dict = {r[0]: r[1] for r in past} # Query -> Rank mapping

        seen_queries = set()
        for r in current:
            query, rank, title, url, checked_at = r
            if query in seen_queries: continue # Just take latest per query
            seen_queries.add(query)

            change_str = "New"
            if query in past_dict:
                diff = past_dict[query] - rank
                if diff > 0:
                    change_str = f"⬆️ +{diff}"
                elif diff < 0:
                    change_str = f"⬇️ {diff}"
                else:
                    change_str = "➖ 0"

            analysis.append({
                "query": query,
                "rank": rank,
                "change": change_str,
                "date": checked_at
            })
        return analysis

    def generate_recommendations(self, new_posts, updated_posts, rankings, past_rankings):
        recs = []

        # Frequency advice
        if not new_posts:
            recs.append("⚠️ **Low Activity**: No new posts detected today. Consider creating new content.")
        elif len(new_posts) > 5:
            recs.append("✅ **High Activity**: Great job! More than 5 posts today.")

        # Update advice
        if updated_posts:
            recs.append(f"ℹ️ **Maintenance**: {len(updated_posts)} posts were updated. Review changes to ensure accuracy.")

        # SEO advice
        if not rankings:
            recs.append("⚠️ **SEO Alert**: Ranking check failed or data missing. Check internet connection or Google blocks.")
        else:
            trends = self.analyze_seo_trends(rankings, past_rankings)
            for t in trends:
                if "⬇️" in t['change']:
                    recs.append(f"📉 **SEO Drop**: Rank dropped for '{t['query']}'. Review page content and keywords.")
                if t['rank'] > 10:
                    recs.append(f"🔍 **SEO Visibility**: '{t['query']}' is on Page {int(t['rank']/10)+1}. Aim for top 10.")

        return recs

if __name__ == "__main__":
    reporter = ReportGenerator()
    reporter.generate_daily_report()
