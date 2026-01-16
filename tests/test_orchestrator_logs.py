from unittest.mock import patch, MagicMock
import logging
import unittest
from main_orchestrator import run_orchestration

class TestOrchestratorLogs(unittest.TestCase):
    @patch('main_orchestrator.HealthCheckAgent')
    @patch('main_orchestrator.ResearcherAgent')
    @patch('main_orchestrator.AnalyzerAgent')
    @patch('main_orchestrator.AdvertisingAgent')
    @patch('main_orchestrator.IntelligenceAgent')
    @patch('main_orchestrator.CreativityAgent')
    @patch('main_orchestrator.MonetizationAgent')
    @patch('main_orchestrator.ContentCreatorAgent')
    @patch('main_orchestrator.save_daily_report')
    def test_logs_contain_emojis(self, mock_save, mock_content, mock_money, mock_creative, mock_intel, mock_ad, mock_analyze, mock_research, mock_health):
        # Setup mocks to return valid-ish data so the script doesn't crash
        mock_health.return_value.run.return_value = {"site_status": "healthy"}
        mock_research.return_value.run.return_value = {"blog_posts": [], "google_listings": []}

        # Capture logs
        with self.assertLogs('Orchestrator', level='INFO') as cm:
            run_orchestration(save_report=False)

        # Check for emojis
        logs = cm.output
        self.assertTrue(any("🚀" in log for log in logs), "Missing rocket emoji")
        self.assertTrue(any("🏥" in log for log in logs), "Missing health emoji")
        self.assertTrue(any("🔍" in log for log in logs), "Missing research emoji")
        self.assertTrue(any("📊" in log for log in logs), "Missing analysis emoji")
        self.assertTrue(any("📢" in log for log in logs), "Missing advertising emoji")
        self.assertTrue(any("🧠" in log for log in logs), "Missing intelligence emoji")
        self.assertTrue(any("🎨" in log for log in logs), "Missing creativity emoji")
        self.assertTrue(any("💰" in log for log in logs), "Missing monetization emoji")
        self.assertTrue(any("📝" in log for log in logs), "Missing content emoji")
        self.assertTrue(any("✅" in log for log in logs), "Missing completion emoji")

if __name__ == '__main__':
    unittest.main()
