import sqlite3
import os
import logging
from datetime import datetime, timedelta

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

    def generate_daily_report(self):
        logger.info("Generating daily report...")

        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()

                # Get total count
                cursor.execute("SELECT COUNT(*) FROM posts")
                total_posts = cursor.fetchone()[0]

                # Get posts scraped in the last 24 hours
                yesterday = datetime.now() - timedelta(days=1)
                cursor.execute("SELECT title, post_url, scraped_at FROM posts WHERE scraped_at >= ?", (yesterday,))
                new_posts = cursor.fetchall()

        except sqlite3.Error as e:
            logger.error(f"Database error: {e}")
            return

        report_date = datetime.now().strftime("%Y-%m-%d")
        report_filename = os.path.join(self.report_dir, f"report_{report_date}.md")

        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(f"# Daily Scraper Report - {report_date}\n\n")
            f.write(f"**Total Posts in Database:** {total_posts}\n\n")
            f.write(f"**New Posts (Last 24h):** {len(new_posts)}\n\n")

            if new_posts:
                f.write("## Recently Scraped Posts\n\n")
                f.write("| Title | Scraped At | Link |\n")
                f.write("|---|---|---|\n")
                for post in new_posts:
                    title, url, scraped_at = post
                    # sanitize title for markdown table
                    title = title.replace("|", "-") if title else "No Title"
                    f.write(f"| {title} | {scraped_at} | [View]({url}) |\n")
            else:
                f.write("No new posts scraped in the last 24 hours.\n")

        logger.info(f"Report generated: {report_filename}")

if __name__ == "__main__":
    reporter = ReportGenerator()
    reporter.generate_daily_report()
