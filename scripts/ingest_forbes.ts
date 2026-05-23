import { observeKnowledge } from '../antigravity/services/knowledge';

async function ingestForbes() {
  console.log('🤖 [Ingest] Fetching market intelligence from Forbes...');

  const targetUrls = [
    'https://www.forbes.com/business/',
    'https://www.forbes.com/innovation/', // Covers IT, tech, and informatics
    'https://www.forbes.com/money/'       // Covers economy and finance
  ];

  for (const url of targetUrls) {
    await observeKnowledge(url);
  }

  console.log('✅ [Ingest] Forbes ingestion complete.');
}

ingestForbes().catch(console.error);
