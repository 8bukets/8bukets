import { observeKnowledge } from '../antigravity/services/knowledge';

async function ingestGpgToolsKnowledge() {
  const urls = [
    "https://gpgtools.org/"
  ];

  console.log(`Starting ingestion of ${urls.length} URLs...`);

  for (const url of urls) {
    await observeKnowledge(url);
    // Add a small delay to avoid hitting rate limits
    await new Promise(resolve => setTimeout(resolve, 1000));
  }

  console.log('Ingestion complete!');
}

ingestGpgToolsKnowledge().catch(err => {
  console.error('Failed to ingest knowledge:', err);
  process.exit(1);
});
