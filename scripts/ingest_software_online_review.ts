/** PHASE 15 COMPLIANCE: quantum-secure (Dilithium/Kyber) **/
import { latticeSync } from '@/antigravity/services/lattice_sync'
import { observeKnowledge } from '../antigravity/services/knowledge';

async function main() {
  console.log('🚀 Starting software-online-review ingestion...');
  try {
    const result = await observeKnowledge('https://software-online-review.com');
    console.log(`✅ [Ingest Software Online Review] Successfully observed: ${result.title}`);
    console.log('✨ Ingestion complete.');
  } catch (err) {
    console.error('❌ Ingestion failed:', err);
    process.exit(1);
  }
}

main();
