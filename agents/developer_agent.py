from .base_agent import BaseAgent
from typing import Dict, List

class DeveloperAgent(BaseAgent):
    def __init__(self):
        super().__init__("Developer Agent")

    def process(self, research_results: Dict) -> str:
        self.log("Generating code snippets...")

        # Heuristic: if Google Cloud is mentioned, generate Terraform for GCP
        findings = str(research_results)
        code_block = ""

        if "Google Cloud" in findings or "Google" in findings:
            code_block = """
```hcl
# Terraform: Deploy Oracle Database on Google Cloud (Simulated)
resource "google_compute_instance" "oracle_db" {
  name         = "oracle-db-node"
  machine_type = "n2-standard-8"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "oracle-linux-8"
    }
  }

  network_interface {
    network = "default"
  }
}
```
"""
        else:
            code_block = """
```python
# Python: Connect to Oracle Database
import cx_Oracle
import os

dsn = cx_Oracle.makedsn("dbhost", 1521, service_name="orcl")

# Use environment variables for credentials
user = os.environ.get("DB_USER", "hr")
password = os.environ.get("DB_PASSWORD")

if not password:
    raise ValueError("DB_PASSWORD environment variable not set")

connection = cx_Oracle.connect(user=user, password=password, dsn=dsn)
print("Successfully connected to Oracle Database")
```
"""
        return f"# Developer Corner\n\nHere is a starter snippet for your deployment:\n{code_block}"
