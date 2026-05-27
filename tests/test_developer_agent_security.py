import unittest
import sys
import os

# Ensure we can import from the agents directory
sys.path.append(os.getcwd())

from agents.developer_agent import DeveloperAgent

class TestDeveloperAgentSecurity(unittest.TestCase):
    def setUp(self):
        self.agent = DeveloperAgent()

    def test_oracle_connection_snippet_is_secure(self):
        """
        Verify that the generated Python snippet for Oracle connection
        uses environment variables for credentials and not hardcoded strings.
        """
        # Trigger the "else" branch by not mentioning "Google Cloud"
        result = self.agent.process({})

        # Check for presence of secure patterns
        self.assertIn('import os', result, "Generated code should import os")
        self.assertIn('os.environ.get("DB_USER"', result, "Should use DB_USER env var")
        self.assertIn('os.environ.get("DB_PASSWORD")', result, "Should use DB_PASSWORD env var")

        # Check for absence of insecure patterns
        self.assertNotIn('password="welcome"', result, "Should not contain hardcoded password 'welcome'")

    def test_terraform_snippet(self):
        """
        Verify that Terraform snippet is generated when appropriate.
        """
        result = self.agent.process({"findings": "Google Cloud"})
        self.assertIn('resource "google_compute_instance"', result)

if __name__ == '__main__':
    unittest.main()
