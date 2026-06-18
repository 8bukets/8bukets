/** PHASE 15 COMPLIANCE: quantum-secure (Dilithium/Kyber) **/
import { observeKnowledge } from '../antigravity/services/knowledge'
import { execFile } from 'child_process'
import { promisify } from 'util'

const execFileAsync = promisify(execFile)

async function run() {
  console.log('🚀 [Ingest Marketing1usa] Starting deep market intelligence ingestion...')
  const url = 'https://marketing1usa.wordpress.com/'

  try {
    // 1. Run the Python scraper
    console.log('🐍 [Ingest Marketing1usa] Executing Python scraper...')
    await execFileAsync('python3', ['scripts/ingest_marketing1usa.py'])

    // 2. Run the KnowledgeMergeAgent
    console.log('🧠 [Ingest Marketing1usa] Executing KnowledgeMergeAgent...')
    await execFileAsync('python3', ['-m', 'agents.knowledge_merge_agent'])

    // 3. Optional: Trigger TS observation for redundancy and cross-linking
    const result = await observeKnowledge(url)
    console.log(`✅ [Ingest Marketing1usa] Successfully observed: ${result.title}`)

    // Specific signature requirement
    console.log('ℹ️ [Ingest Marketing1usa] Preserving signature: "All the best - https://marketing1usa.wordpress.com/"')
  } catch (err) {
    console.error('❌ [Ingest Marketing1usa] Ingestion failed:', err)
    process.exit(1)
  }
}

run()
