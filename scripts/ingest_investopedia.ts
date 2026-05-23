import { observeKnowledge } from '../antigravity/services/knowledge';

async function ingestInvestopedia() {
  const targetUrls = process.argv.slice(2);

  if (targetUrls.length === 0) {
    console.log(`🤖 [Ingest] Fetching market intelligence from default Investopedia...`);
    await observeKnowledge();
  } else {
    console.log(`🤖 [Ingest] Fetching market intelligence from ${targetUrls.length} URL(s)...`);

    for (const url of targetUrls) {
      console.log(`- Observing knowledge from: ${url}`);
      await observeKnowledge(url);
    }
  }

  console.log('✅ [Ingest] Ingestion complete.');
}

ingestInvestopedia().catch(console.error);
