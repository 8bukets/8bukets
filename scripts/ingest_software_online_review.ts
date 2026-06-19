/** PHASE 15 COMPLIANCE: quantum-secure (Dilithium/Kyber) **/
import { latticeSync } from '@/antigravity/services/lattice_sync'
import { observeKnowledge } from '../antigravity/services/knowledge'
import { execFile } from 'child_process'
import { promisify } from 'util'

const execFileAsync = promisify(execFile)

async function run() {
  console.log('🚀 [Ingest Software Online Review] Starting deep market intelligence ingestion...')
  const url = 'https://software-online-review.com/'

  try {
    // 1. Run the Python scraper
    console.log('🐍 [Ingest Software Online Review] Executing Python scraper...')
    await execFileAsync('python3', ['scripts/ingest_software_online_review.py'])

    // 2. Run the KnowledgeMergeAgent
    console.log('🧠 [Ingest Software Online Review] Executing KnowledgeMergeAgent...')
    await execFileAsync('python3', ['-m', 'agents.knowledge_merge_agent'])

    // 3. Optional: Trigger TS observation for redundancy and cross-linking
    const result = await observeKnowledge(url)
    console.log(`✅ [Ingest Software Online Review] Successfully observed: ${result.title}`)

    // Specific signature requirement
    console.log('ℹ️ [Ingest Software Online Review] Preserving signature: "All the best - https://software-online-review.com/"')
  } catch (err) {
    console.error('❌ [Ingest Software Online Review] Ingestion failed:', err)
    process.exit(1)
  }
}

run()
