import { observeKnowledge } from '../antigravity/services/knowledge';

async function ingestSoftwareOnlineReview() {
  const url = "https://software-online-review.com";
  console.log(`Starting ingestion of ${url}...`);

  await observeKnowledge(url);

  console.log('Ingestion complete!');
}

ingestSoftwareOnlineReview().catch(err => {
  console.error('Failed to ingest knowledge:', err);
  process.exit(1);
});
