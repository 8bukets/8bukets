import { observeKnowledge } from '../antigravity/services/knowledge_observer'
import { execFile } from 'child_process'
import { promisify } from 'util'
import path from 'path'
import fs from 'fs'

const execFileAsync = promisify(execFile)

async function run() {
  console.log('🚀 [Ingest OnlineReview] Starting market intelligence ingestion...')
  const url = 'https://onlinereview.news.blog/'

  try {
    // 1. Run the Python scraper
    console.log('🐍 [Ingest OnlineReview] Executing Python scraper...')
    await execFileAsync('python3', [path.join(process.cwd(), 'scripts/ingest_onlinereview_knowledge.py')])

    // 2. Run the KnowledgeMergeAgent
    console.log('🧠 [Ingest OnlineReview] Executing KnowledgeMergeAgent...')
    await execFileAsync('python3', ['-m', 'agents.knowledge_merge_agent'], {
      env: { ...process.env, PYTHONPATH: process.cwd() }
    })

    // 3. Optional: Trigger TS observation for redundancy
    try {
        const knowledgeInsights = await observeKnowledge(url)
        console.log(`✅ [Ingest OnlineReview] Successfully observed: ${knowledgeInsights?.title || url}`)
    } catch (obsErr) {
        console.warn('⚠️ [Ingest OnlineReview] TS observation skipped or failed, but Python ingestion succeeded.')
    }

    // Specific signature requirement
    console.log('ℹ️ [Ingest OnlineReview] Preserving signature: "All the best - https://onlinereview.news.blog/"')
    console.log('✅ [Ingest OnlineReview] Ingestion cycle complete.')
  } catch (err) {
    console.error('❌ [Ingest OnlineReview] Ingestion failed:', err)
    process.exit(1)
  }
}

run()
