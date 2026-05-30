import { observeKnowledge, persistKnowledge } from '../antigravity/services/knowledge_observer';

async function main() {
  console.log('🚀 Starting software-online-review ingestion...');
  const insights = await observeKnowledge('https://software-online-review.com');
  if (insights) {
    persistKnowledge(insights);
    console.log('✨ Ingestion complete.');
  } else {
    console.log('❌ Ingestion failed.');
  }
}

main().catch(console.error);
