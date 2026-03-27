import unittest
from unittest.mock import MagicMock, patch
import os
import shutil
import tempfile
from report_generator import ReportGenerator
from agent_orchestrator import AgentOrchestrator

class TestReportUX(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.reporter = ReportGenerator(db_name="test.db", report_dir=self.test_dir)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    @patch('sqlite3.connect')
    def test_report_structure(self, mock_connect):
        # Mock DB results
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        # Configure mock return values for fetchone/fetchall
        mock_cursor.fetchone.return_value = (100,)

        mock_cursor.fetchall.side_effect = [
            [('New Post 1', 'http://url1', '2025-01-01')], # new_posts
            [('Old Post', 'http://url2', 'title', 'Old', 'New', '2025-01-01')], # updated_posts
            [('keyword', 1, 'Title', 'http://url', '2025-01-01')], # rankings
            [] # past_rankings
        ]

        self.reporter.generate_daily_report()

        # Find the generated file
        files = [f for f in os.listdir(self.test_dir) if f.startswith("report_")]
        self.assertTrue(len(files) > 0, "No report file generated")
        with open(os.path.join(self.test_dir, files[0]), 'r', encoding='utf-8') as f:
            content = f.read()

        # UX Checks - Table of Contents
        self.assertIn("## Table of Contents", content, "Missing Table of Contents header")

        # Check links
        self.assertIn("[💡 Recommendations](#recommendations)", content)
        self.assertIn("[🧠 Keyword Trends](#keyword-trends)", content)
        self.assertIn("[📈 SEO Trend Analysis](#seo-trend-analysis)", content)
        self.assertIn("[🔄 Content Updates](#content-updates)", content)
        self.assertIn("[🆕 Recently Scraped Posts](#recently-scraped-posts)", content)

        # Check Anchors
        self.assertIn('## <a id="recommendations"></a>💡 Recommendations', content)
        self.assertIn('## <a id="keyword-trends"></a>🧠 Keyword Trends', content)
        self.assertIn('## <a id="seo-trend-analysis"></a>📈 SEO Trend Analysis', content)
        self.assertIn('## <a id="content-updates"></a>🔄 Content Updates', content)
        self.assertIn('## <a id="recently-scraped-posts"></a>🆕 Recently Scraped Posts', content)

    def test_agent_report_structure(self):
        orchestrator = AgentOrchestrator(report_dir=self.test_dir)

        outputs = {
            'HealthAgent': {'db_status': 'OK'},
            'IntelligenceAgent': {'strategy': 'Test', 'trend_alert': 'None'},
            'CuriosityAgent': {'exploration_query': 'Test', 'findings': []},
            'CreativeAgent': {'system_improvement_ideas': []},
            'AdManagerAgent': {'campaigns': []},
            'MonetizationAgent': {'top_opportunities': []},
            'CreatorAgent': {'draft_title': 'Test Title', 'draft_content': 'Test Content'}
        }

        orchestrator.generate_report(outputs)

        # Find the file
        files = [f for f in os.listdir(self.test_dir) if f.startswith("agent_report_")]
        self.assertEqual(len(files), 1)
        with open(os.path.join(self.test_dir, files[0]), 'r', encoding='utf-8') as f:
            content = f.read()

        # UX Checks
        self.assertIn("## Table of Contents", content)
        self.assertIn("[🏥 System Health](#system-health)", content)
        self.assertIn('## <a id="system-health"></a>🏥 System Health', content)
        self.assertIn('## <a id="intelligence"></a>🧠 Intelligence', content)
        self.assertIn('## <a id="curiosity-innovation"></a>🌌 Curiosity & Innovation', content)
        self.assertIn('## <a id="ad-manager"></a>📢 Ad Manager', content)
        self.assertIn('## <a id="monetization"></a>💰 Monetization', content)
        self.assertIn('## <a id="content-draft"></a>✍️ Content Draft', content)

if __name__ == '__main__':
    unittest.main()
