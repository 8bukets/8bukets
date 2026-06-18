import { observeKnowledge } from '../antigravity/services/knowledge'
import { execFile } from 'child_process'
import { promisify } from 'util'

const execFileAsync = promisify(execFile)

async function run() {
  console.log('🚀 [Ingest Webshop] Starting deep market intelligence ingestion...')
  const url = 'https://webshop.business.blog/'

  try {
    // 1. Run the Python scraper
    console.log('🐍 [Ingest Webshop] Executing Python scraper...')
    await execFileAsync('python3', ['scripts/ingest_webshop_knowledge.py'])

    // 2. Run the KnowledgeMergeAgent
    console.log('🧠 [Ingest Webshop] Executing KnowledgeMergeAgent...')
    await execFileAsync('python3', ['-m', 'agents.knowledge_merge_agent'])

    // 3. Optional: Trigger TS observation for redundancy and cross-linking
    const result = await observeKnowledge(url)
    if (result) {
        console.log(`✅ [Ingest Webshop] Successfully observed: ${result.title}`)
    }

    // Specific signature requirement
    console.log('ℹ️ [Ingest Webshop] Preserving signature: "All the best - https://webshop.business.blog/"')
  } catch (err) {
    console.error('❌ [Ingest Webshop] Ingestion failed:', err)
    process.exit(1)
  }
}

run()
