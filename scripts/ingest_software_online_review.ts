import { observeKnowledge } from '../antigravity/services/knowledge';

async function ingestSoftwareOnlineReview() {
  console.log('🤖 [Ingest] Fetching market intelligence from Software Online Review...');

  const targetUrls = [
    'https://software-online-review.com/',
  ];

  for (const url of targetUrls) {
    await observeKnowledge(url);
  }

  console.log('✅ [Ingest] Software Online Review ingestion complete.');
}

ingestSoftwareOnlineReview().catch(console.error);
