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

        if "AI" in findings:
            code_block = """
```python
# Python: Invoke Oracle Cloud Infrastructure (OCI) AI Services (Simulated)
import oci
import os

config = oci.config.from_file()
ai_client = oci.ai_language.AIServiceLanguageClient(config)

text_document = oci.ai_language.models.TextDocument(
    key="1",
    text="Oracle AI offers state-of-the-art generative AI and machine learning capabilities.",
    language_code="en"
)

# Detect sentiment using OCI AI Language service
detect_language_details = oci.ai_language.models.DetectLanguageSentimentsDetails(
    documents=[text_document]
)

try:
    response = ai_client.detect_language_sentiments(detect_language_details)
    for doc in response.data.documents:
        print(f"Sentiment for document {doc.key}: {doc.document_sentiment}")
except Exception as e:
    print(f"Error calling OCI AI Services: {e}")
```
"""
        elif "Google Cloud" in findings or "Google" in findings:
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
