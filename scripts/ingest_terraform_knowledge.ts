import { observeKnowledge } from '../antigravity/services/knowledge';

async function ingestTerraformKnowledge() {
  const urls = [
    "https://developer.hashicorp.com/terraform/tutorials/docker-get-started",
    "https://developer.hashicorp.com/terraform",
    "https://developer.hashicorp.com/terraform/docs",
    "https://github.com/hashicorp/terraform"
  ];

  console.log(`Starting ingestion of ${urls.length} URLs...`);

  for (const url of urls) {
    await observeKnowledge(url);
    // Add a small delay to avoid hitting rate limits
    await new Promise(resolve => setTimeout(resolve, 1000));
  }

  console.log('Ingestion complete!');
}

ingestTerraformKnowledge().catch(err => {
  console.error('Failed to ingest knowledge:', err);
  process.exit(1);
});
