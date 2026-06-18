import { observeKnowledge } from '@/antigravity/services/knowledge'
import { execFile } from 'child_process'
import { promisify } from 'util'

const execFileAsync = promisify(execFile)

export async function runInfogadgettechWorkflow() {
  console.log('🚀 [Workflow] Starting Infogadgettech market intelligence cycle...')

  try {
    // 1. Run the Python scraper
    console.log('🐍 [Workflow] Executing Python scraper...')
    await execFileAsync('python3', ['scripts/ingest_infogadgettech.py'])

    // 2. Run the KnowledgeMergeAgent
    console.log('🧠 [Workflow] Executing KnowledgeMergeAgent...')
    await execFileAsync('python3', ['-m', 'agents.knowledge_merge_agent'])

    // 3. System-wide observation
    await observeKnowledge('https://infogadgettech.wordpress.com/')

    console.log('✅ [Workflow] Infogadgettech intelligence integrated successfully.')
  } catch (err) {
    console.error('❌ [Workflow] Infogadgettech cycle failed:', err)
    throw err
  }
}

if (require.main === module) {
  runInfogadgettechWorkflow()
}
