import { observeKnowledge } from '../antigravity/services/knowledge';

async function ingestSoftwareOnlineReview() {
  const targetUrls = process.argv.slice(2);

  if (targetUrls.length === 0) {
    console.error('❌ [Ingest] No target URLs provided. Please provide URLs as command-line arguments.');
    process.exit(1);
  }

  console.log(`🤖 [Ingest] Fetching market intelligence from ${targetUrls.length} URL(s)...`);

  for (const url of targetUrls) {
    console.log(`- Observing knowledge from: ${url}`);
    await observeKnowledge(url);
  }

  console.log('✅ [Ingest] Ingestion complete.');
}

ingestSoftwareOnlineReview().catch(console.error);
