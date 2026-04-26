import os
import sys
import json
import asyncio
import pytest
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import scraper
import analytics
import run_system

def test_scraper_dry_run_no_files_created():
    """Test that the scraper with dry_run=True does not create any output files."""
    json_path = "test_links.json"
    csv_path = "test_links.csv"
    txt_path = "test_unique.txt"

    scr = scraper.MarkPositionScraperAsync(
        output_json=json_path,
        output_csv=csv_path,
        output_txt=txt_path,
        max_pages=1,
        concurrency=1,
        dry_run=True
    )

    async def mock_fetch_and_parse(session, page_num, sem):
        return [{"title": "Test", "external_link": "http://test.com"}]

    with patch.object(scr, 'fetch_and_parse', mock_fetch_and_parse):
        asyncio.run(scr.scrape())

    assert not os.path.exists(json_path)
    assert not os.path.exists(csv_path)
    assert not os.path.exists(txt_path)

def test_scraper_dry_run_updates_seen_links():
    """Test that dry run properly handles state without writing."""
    scr = scraper.MarkPositionScraperAsync(
        output_json="dummy.json",
        output_csv="dummy.csv",
        output_txt="dummy.txt",
        dry_run=True
    )

    seen_links = set()
    posts = [{"external_link": "http://test1.com"}, {"external_link": "http://test2.com"}]

    is_first = scr.save_batch(posts, None, None, None, seen_links, True)

    assert "http://test1.com" in seen_links
    assert "http://test2.com" in seen_links
    assert is_first == True

def test_analytics_dry_run_no_report(tmp_path, capsys):
    """Test that analytics with dry_run=True does not create a markdown report."""
    report_path = tmp_path / "test_REPORT.md"
    dummy_data = [{"domain": "test.com", "categories": ["Tech"], "author": "Jules"}]

    analytics.generate_report(dummy_data, str(report_path), dry_run=True)

    assert not os.path.exists(report_path)

    captured = capsys.readouterr()
    assert "Dry run enabled. Would have generated report at" in captured.out

@pytest.mark.asyncio
async def test_run_system_dry_run_no_destructive_writes(tmp_path):
    """Test that run_system properly passes dry_run flag."""

    with patch('run_system.load_data', return_value=[{"dummy": "data"}]):
        with patch('run_system.AgentOrchestrator') as mock_orch:
            with patch('run_system.run_scraper') as mock_scraper:
                with patch('run_system.generate_daily_report') as mock_report:
                    mock_orch.return_value.execute_cycle = MagicMock()
                    mock_orch.return_value.run_peer_review = MagicMock()

                    async def mock_execute_cycle(data):
                        pass
                    async def mock_run_peer_review():
                        pass

                    mock_orch.return_value.execute_cycle = mock_execute_cycle
                    mock_orch.return_value.run_peer_review = mock_run_peer_review

                    await run_system.run_cycle(auth_token="default_dev_token", skip_scraper=False, dry_run=True)

                    mock_scraper.assert_called_once_with(dry_run=True)
                    mock_report.assert_not_called()

                    agents_passed = mock_orch.call_args[0][0]
                    agent_classes = [type(a).__name__ for a in agents_passed]
                    assert "MongoDBAgent" not in agent_classes
                    assert "MySQLAgent" not in agent_classes
