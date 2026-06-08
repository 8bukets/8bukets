import unittest
from unittest.mock import patch, mock_open, MagicMock
import sys
import os

# Add parent directory to path so we can import main_orchestrator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main_orchestrator import save_daily_report

class TestOrchestratorUX(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.makedirs')
    def test_report_emoji_ux(self, mock_makedirs, mock_file):
        """Test that the generated report includes UX-enhancing emojis."""
        data = {
            'health': {'site_status': 'healthy', 'site_code': 200, 'robots_txt_accessible': True, 'googlebot_allowed': True},
            'research': {'posts_scraped': 5, 'google_results': 10},
            'intelligence': {'evolution_status': 'stable', 'recommended_focus': 'none', 'insights': []},
            'advertising': {'target_audience': 'tech', 'bid_strategy': []},
            'monetization': {'summary': 'good', 'details': []},
            'creativity': {'creative_ideas': []},
            'content_draft': {'draft_title': 'Test Draft', 'draft_content': 'Content'}
        }

        save_daily_report(data)

        # Get all arguments passed to write
        handle = mock_file()
        written_content = "".join(call.args[0] for call in handle.write.call_args_list)

        # Verify emojis are present in headers
        # These assertions will fail until we implement the changes
        self.assertIn("🏥", written_content, "Health section should have '🏥' emoji")
        self.assertIn("🔍", written_content, "Research section should have '🔍' emoji")
        self.assertIn("🧠", written_content, "Intelligence section should have '🧠' emoji")
        self.assertIn("📢", written_content, "Advertising section should have '📢' emoji")
        self.assertIn("💰", written_content, "Monetization section should have '💰' emoji")
        self.assertIn("🎨", written_content, "Creativity section should have '🎨' emoji")
        self.assertIn("✍️", written_content, "Content section should have '✍️' emoji")

if __name__ == '__main__':
    unittest.main()
