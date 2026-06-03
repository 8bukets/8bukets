import fs from 'fs';
import path from 'path';
import { KnowledgeObserver } from '../antigravity/services/knowledge_observer';

async function ingestUserCaioKnowledge() {
  const mdPath = path.join(process.cwd(), 'data/knowledge/caio_user_input.md');
  if (!fs.existsSync(mdPath)) {
    console.error(`❌ File not found: ${mdPath}`);
    process.exit(1);
  }

  const content = fs.readFileSync(mdPath, 'utf8');
  const source = 'user_input://caio_user_input.md';
  const title = 'Chief AI Officer (CAIO) Role';

  console.log(`🧠 [Ingest] Processing ${title} from ${source}...`);
  const insights = KnowledgeObserver.processContent(title, content, source);

  const observer = new KnowledgeObserver();
  await observer.persistKnowledge(insights);

  console.log('✅ [Ingest] User CAIO knowledge successfully integrated.');
}

ingestUserCaioKnowledge().catch(err => {
  console.error('❌ [Ingest] Failed:', err);
  process.exit(1);
});
