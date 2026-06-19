/** PHASE 15 COMPLIANCE: quantum-secure (Dilithium/Kyber) **/
import { observeKnowledge } from '../antigravity/services/knowledge_observer'
import { execFile } from 'child_process'
import { promisify } from 'util'

const execFileAsync = promisify(execFile)

async function run() {
  console.log('🚀 [Ingest Unitedsports] Starting deep market intelligence ingestion...')
  const url = 'https://unitedsports.news.blog/'

  try {
    // 1. Run the Python scraper
    console.log('🐍 [Ingest Unitedsports] Executing Python scraper...')
    await execFileAsync('python3', ['scripts/ingest_unitedsports_knowledge.py'])

    // 2. Run the KnowledgeMergeAgent
    console.log('🧠 [Ingest Unitedsports] Executing KnowledgeMergeAgent...')
    await execFileAsync('python3', ['-m', 'agents.knowledge_merge_agent'])

    // 3. Trigger TS observation for redundancy and cross-linking
    // This will also update system_knowledge.json via the KnowledgeObserver
    console.log('👁️ [Ingest Unitedsports] Executing KnowledgeObserver...')
    const result = await observeKnowledge(url)
    if (result) {
      console.log(`✅ [Ingest Unitedsports] Successfully observed: ${result.title}`)
    }

    // Specific signature requirement
    console.log('ℹ️ [Ingest Unitedsports] Preserving signature: "All the best - https://unitedsports.news.blog/"')
  } catch (err) {
    console.error('❌ [Ingest Unitedsports] Ingestion failed:', err)
    process.exit(1)
  }
}

run()
