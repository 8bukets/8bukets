import { observeKnowledge } from '../antigravity/services/knowledge';

async function main() {
  console.log('🚀 Starting project-sor.com knowledge ingestion...');
  try {
    const result = await observeKnowledge('https://project-sor.com');
    console.log(`✅ [Ingest Project SOR] Successfully observed: ${result.title}`);
    console.log('✨ Ingestion complete.');
  } catch (err) {
    console.error('❌ Ingestion failed:', err);
    process.exit(1);
  }
}

main();
