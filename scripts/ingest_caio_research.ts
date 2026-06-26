import fs from 'fs';
import path from 'path';
import { KnowledgeObserver } from '../antigravity/services/knowledge_observer';

async function ingestCAIOResearch() {
  console.log('🧪 [Ingest] Starting CAIO Executive Intelligence Ingestion...');

  const researchPath = path.join(process.cwd(), 'data/knowledge/caio_executive_intelligence_2026.md');

  if (!fs.existsSync(researchPath)) {
    console.error(`❌ [Ingest] Master Intelligence file not found at ${researchPath}`);
    process.exit(1);
  }

  const rawContent = fs.readFileSync(researchPath, 'utf8');
  const source = `local://${path.basename(researchPath)}`;
  const title = 'Chief AI Officer (CAIO) Executive Intelligence 2026';

  const observer = new KnowledgeObserver();
  const insights = KnowledgeObserver.processContent(title, rawContent, source);

  // Custom metadata for this research
  insights.metadata = {
    type: 'executive_intelligence',
    adoption_rate: '76%',
    target_year: 2026,
    roi_target: '95%',
    licensure: 'verified_not_required'
  };

  await observer.persistKnowledge(insights);

  console.log('✅ [Ingest] CAIO Executive Intelligence successfully integrated into system knowledge.');
}

ingestCAIOResearch().catch(err => {
  console.error('💥 [Ingest] Critical failure during intelligence ingestion:', err);
  process.exit(1);
});
