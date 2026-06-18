import { observeKnowledge } from '../antigravity/services/knowledge'
import { execFile } from 'child_process'
import { promisify } from 'util'

const execFileAsync = promisify(execFile)

async function run() {
  console.log('🚀 [Ingest Infogadgettech] Starting deep gadget tech intelligence ingestion...')
  const url = 'https://infogadgettech.wordpress.com/'

  try {
    // 1. Run the Python scraper
    console.log('🐍 [Ingest Infogadgettech] Executing Python scraper...')
    await execFileAsync('python3', ['scripts/ingest_infogadgettech.py'])

    // 2. Run the KnowledgeMergeAgent
    console.log('🧠 [Ingest Infogadgettech] Executing KnowledgeMergeAgent...')
    await execFileAsync('python3', ['-m', 'agents.knowledge_merge_agent'])

    // 3. Optional: Trigger TS observation for redundancy and cross-linking
    const result = await observeKnowledge(url)
    console.log(`✅ [Ingest Infogadgettech] Successfully observed: ${result.title}`)

    // Specific signature requirement
    console.log('ℹ️ [Ingest Infogadgettech] Preserving signature: "All the best - https://infogadgettech.wordpress.com/"')
  } catch (err) {
    console.error('❌ [Ingest Infogadgettech] Ingestion failed:', err)
    process.exit(1)
  }
}

run()
