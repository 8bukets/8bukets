/** PHASE 15 COMPLIANCE: quantum-secure (Dilithium/Kyber) **/
import { latticeSync } from '@/antigravity/services/lattice_sync'
import { jules } from '../antigravity/jules'

async function ingestCaioRole() {
  console.log('🧪 Ingesting CAIO Role Description...')
  try {
    await jules.observeKnowledge()
    console.log('✅ Ingestion complete.')
  } catch (err) {
    console.error('❌ Ingestion failed:', err)
    process.exit(1)
  }
}

ingestCaioRole()
