import logging
import sys
import datetime
import os
from agents.researcher import ResearcherAgent
from agents.analyzer import AnalyzerAgent
from agents.intelligence import IntelligenceAgent
from agents.content_creator import ContentCreatorAgent
from agents.health_check import HealthCheckAgent
from agents.monetization import MonetizationAgent
from agents.creativity import CreativityAgent

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("Orchestrator")

def run_orchestration(save_report=True):
    logger.info(">>> STARTING AUTONOMOUS AGENT SWARM <<<")
    report_data = {}

    # 1. Health Check
    health_agent = HealthCheckAgent()
    health_status = health_agent.run()
    report_data['health'] = health_status

    if health_status.get("site_status") != "healthy":
        logger.error("Target site is unhealthy. Aborting operation.")
        # We proceed if robots.txt issues but site is up

    # 2. Research
    research_agent = ResearcherAgent()
    # Limit to 2 pages for daily updates
    raw_data = research_agent.run({"limit": 2})
    report_data['research'] = {
        'posts_scraped': len(raw_data.get('blog_posts', [])),
        'google_results': len(raw_data.get('google_listings', []))
    }

    if not raw_data.get('blog_posts'):
        logger.warning("No blog data scraped.")
        # Proceed with partial data if possible

    # 3. Analyze
    analyzer_agent = AnalyzerAgent()
    analysis_result = analyzer_agent.run(raw_data)
    report_data['analysis'] = analysis_result

    # 4. Intelligence
    intelligence_agent = IntelligenceAgent()
    intelligence_result = intelligence_agent.run(analysis_result)
    report_data['intelligence'] = intelligence_result

    # 5. Creativity
    creativity_agent = CreativityAgent()
    creative_result = creativity_agent.run(analysis_result)
    report_data['creativity'] = creative_result

    # 6. Monetization
    monetization_agent = MonetizationAgent()
    # Monetization checks blog posts mainly
    monetization_result = monetization_agent.run(raw_data.get('blog_posts', []))
    report_data['monetization'] = monetization_result

    # 7. Create Content
    content_agent = ContentCreatorAgent()
    content_draft = content_agent.run(intelligence_result)
    report_data['content_draft'] = content_draft

    logger.info(">>> SWARM OPERATION COMPLETE <<<")

    if save_report:
        save_daily_report(report_data)

    return report_data

def save_daily_report(data):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)
    report_file = os.path.join(report_dir, f"daily_report_{today}.md")

    with open(report_file, "w", encoding="utf-8") as f:
        f.write(f"# Daily Autonomous Report: {today}\n\n")

        # Health
        f.write("## 1. System Health\n")
        status = data.get('health', {})
        f.write(f"- **Site Status:** {status.get('site_status')} (Code: {status.get('site_code')})\n")
        f.write(f"- **Robots.txt Access:** {status.get('robots_txt_accessible')}\n")
        f.write(f"- **Googlebot Allowed:** {status.get('googlebot_allowed')}\n\n")

        # Research Stats
        research = data.get('research', {})
        f.write("## 2. Research Summary\n")
        f.write(f"- **New Posts Scraped:** {research.get('posts_scraped')}\n")
        f.write(f"- **Google Listings Found:** {research.get('google_results')}\n\n")

        # Intelligence
        intel = data.get('intelligence', {})
        f.write("## 3. Strategic Intelligence\n")
        f.write(f"- **Recommended Focus:** {intel.get('recommended_focus')}\n")
        for insight in intel.get('insights', []):
            f.write(f"- {insight}\n")
        f.write("\n")

        # Monetization
        money = data.get('monetization', {})
        f.write("## 4. Monetization Review\n")
        f.write(f"- **Summary:** {money.get('summary')}\n")
        for detail in money.get('details', []):
            f.write(f"- {detail}\n")
        f.write("\n")

        # Creativity
        creative = data.get('creativity', {})
        f.write("## 5. Creative Brainstorming\n")
        for idea in creative.get('creative_ideas', []):
            f.write(f"- {idea}\n")
        f.write("\n")

        # Content Draft
        draft = data.get('content_draft', {})
        f.write("## 6. Automated Content Draft\n")
        f.write(f"### {draft.get('draft_title', 'Untitled')}\n\n")
        f.write(draft.get('draft_content', ''))

    logger.info(f"Report saved to {report_file}")

if __name__ == "__main__":
    run_orchestration()
