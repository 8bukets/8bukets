import { observeKnowledge } from '../antigravity/services/knowledge';

async function ingestHcpKnowledge() {
  const urls = [
    "https://github.com/hashicorp/web-unified-docs/blob/main/content/hcp-docs/content/docs/hcp/index.mdx"
  ];

  console.log(`Starting ingestion of ${urls.length} URLs...`);

  for (const url of urls) {
    await observeKnowledge(url);
    // Add a small delay to avoid hitting rate limits
    await new Promise(resolve => setTimeout(resolve, 1000));
  }

  console.log('Ingestion complete!');
}

ingestHcpKnowledge().catch(err => {
  console.error('Failed to ingest knowledge:', err);
  process.exit(1);
});
