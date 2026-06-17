import os
import json
import pytest
import shutil
from scripts.ingest_markposition_knowledge import scrape_markposition_knowledge

def test_ingest_markposition_logic(tmp_path):
    # Setup mock data environment
    knowledge_dir = tmp_path / "data" / "knowledge"
    knowledge_dir.mkdir(parents=True)
    knowledge_file = knowledge_dir / "system_knowledge.json"

    initial_knowledge = {
        "metadata": {"sources_processed": [], "generated_at": ""},
        "market_data": {"total_entries": 0, "recent_entries": [], "all_entries": []}
    }
    with open(knowledge_file, "w") as f:
        json.dump(initial_knowledge, f)

    # Change working directory to tmp_path for the test
    old_cwd = os.getcwd()
    os.chdir(tmp_path)

    try:
        # We can't easily mock the internet without more complex setup,
        # but we can check if it at least attempts to run and handles the file system correctly.
        # For a true unit test, we should mock 'requests.get'.

        # Mocking requests.get
        import requests
        class MockResponse:
            def __init__(self, text, status_code):
                self.text = text
                self.status_code = status_code
            def raise_for_status(self):
                if self.status_code >= 400:
                    raise Exception("Error")

        def mock_get(url, timeout=20):
            return MockResponse('<html><article class="post category-test"><h1 class="entry-title"><a href="https://test.com/post">Test Post</a></h1><time class="entry-date">Jan 1, 2024</time><div class="entry-content"><a href="https://external.com">Link</a></div></article></html>', 200)

        import scripts.ingest_markposition_knowledge
        scripts.ingest_markposition_knowledge.requests.get = mock_get

        scrape_markposition_knowledge(max_pages=1)

        # Verify results
        with open(knowledge_file, "r") as f:
            updated_knowledge = json.load(f)

        assert updated_knowledge["market_data"]["total_entries"] > 0
        assert updated_knowledge["market_data"]["all_entries"][0]["title"] == "Test Post"
        assert updated_knowledge["metadata"]["sources_processed"] == ["markposition.wordpress.com"]

        assert os.path.exists("MARKPOSITION_REPORT.md")

    finally:
        os.chdir(old_cwd)

def test_knowledge_merge_agent_dynamic(tmp_path):
    from agents.knowledge_merge_agent import KnowledgeMergeAgent
    from agents.base_agent import Blackboard

    # Setup mock files
    target_file = tmp_path / "KNOWLEDGE_MERGE.md"
    target_file.write_text("# Knowledge Merge\n")

    knowledge_dir = tmp_path / "data" / "knowledge"
    knowledge_dir.mkdir(parents=True)
    system_knowledge_file = knowledge_dir / "system_knowledge.json"

    knowledge_data = {
        "market_data": {
            "recent_entries": [
                {"title": "Dynamic Post", "domain": "test.com", "post_url": "https://test.com/1"}
            ]
        },
        "metadata": {"generated_at": "now", "version": 1.0}
    }
    with open(system_knowledge_file, "w") as f:
        json.dump(knowledge_data, f)

    old_cwd = os.getcwd()
    os.chdir(tmp_path)

    try:
        agent = KnowledgeMergeAgent()
        blackboard = Blackboard()

        import asyncio
        asyncio.run(agent._dynamic_knowledge_merge(knowledge_data))

        content = target_file.read_text()
        assert "Latest Market Intelligence (Dynamic Merge)" in content
        assert "Dynamic Post" in content
        assert "All the best - https://markposition.wordpress.com" in content

    finally:
        os.chdir(old_cwd)
