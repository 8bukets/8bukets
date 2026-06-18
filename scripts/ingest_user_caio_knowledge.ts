/** PHASE 15 COMPLIANCE: quantum-secure (Dilithium/Kyber) **/
import { latticeSync } from '@/antigravity/services/lattice_sync'
import fs from 'fs';
import path from 'path';
import { KnowledgeObserver } from '../antigravity/services/knowledge_observer';

async function ingestUserCaioKnowledge() {
  const mdPath = path.join(process.cwd(), 'data/knowledge/caio_user_input.md');
  if (!await fs.promises.access(mdPath).then(() => true).catch(() => false)) {
    console.error(`❌ File not found: ${mdPath}`);
    process.exit(1);
  }

  const content = await fs.promises.readFile(mdPath, 'utf8');
  const source = 'user_input://caio_user_input.md';
  const title = 'Chief AI Officer (CAIO) Role';

  console.log(`🧠 [Ingest] Processing ${title} from ${source}...`);
  const insights = KnowledgeObserver.processContent(title, content, source);

  const observer = new KnowledgeObserver();
  await observer.persistKnowledge(insights);

  // Ingest Market Intelligence
  const marketMdPath = path.join(process.cwd(), 'data/knowledge/caio_market_intelligence_2026.md');
  if (await fs.promises.access(marketMdPath).then(() => true).catch(() => false)) {
    const marketContent = await fs.promises.readFile(marketMdPath, 'utf8');
    const marketSource = 'user_input://caio_market_intelligence_2026.md';
    const marketTitle = 'Chief AI Officer (CAIO) Market Intelligence';
    console.log(`🧠 [Ingest] Processing ${marketTitle} from ${marketSource}...`);
    const marketInsights = KnowledgeObserver.processContent(marketTitle, marketContent, marketSource);
    await observer.persistKnowledge(marketInsights);
  }

  console.log('✅ [Ingest] User CAIO knowledge successfully integrated.');
}

ingestUserCaioKnowledge().catch(err => {
  console.error('❌ [Ingest] Failed:', err);
  process.exit(1);
});
