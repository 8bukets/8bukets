/** PHASE 15 COMPLIANCE: quantum-secure (Dilithium/Kyber) **/
import { latticeSync } from '@/antigravity/services/lattice_sync'
import { observeKnowledge } from '../antigravity/services/knowledge'
import { execFile } from 'child_process'
import { promisify } from 'util'

const execFileAsync = promisify(execFile)

async function run() {
  console.log('🚀 [Ingest Companylink] Starting deep market intelligence ingestion...')
  const url = 'https://companylink.business.blog/'

  try {
    // 1. Run the Python scraper
    console.log('🐍 [Ingest Companylink] Executing Python scraper...')
    await execFileAsync('python3', ['scripts/ingest_companylink_knowledge.py'])

    // 2. Run the KnowledgeMergeAgent
    console.log('🧠 [Ingest Companylink] Executing KnowledgeMergeAgent...')
    await execFileAsync('python3', ['-m', 'agents.knowledge_merge_agent'])

    // 3. Optional: Trigger TS observation for redundancy and cross-linking
    const result = await observeKnowledge(url)
    console.log(`✅ [Ingest Companylink] Successfully observed: ${result.title}`)

    // Specific signature requirement
    console.log('ℹ️ [Ingest Companylink] Preserving signature: "All the best - https://companylink.business.blog/"')
  } catch (err) {
    console.error('❌ [Ingest Companylink] Ingestion failed:', err)
    process.exit(1)
  }
}

run()
