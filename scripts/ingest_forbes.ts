import { observeKnowledge } from '../antigravity/services/knowledge'

async function run() {
  console.log('🚀 [Ingest Forbes] Starting deep market intelligence ingestion...')
  const url = 'https://forbes.com'

  try {
    const result = await observeKnowledge(url)
    console.log(`✅ [Ingest Forbes] Successfully observed: ${result.title}`)
  } catch (err) {
    console.error('❌ [Ingest Forbes] Ingestion failed:', err)
    process.exit(1)
  }
}

run()
