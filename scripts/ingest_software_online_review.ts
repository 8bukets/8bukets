import { observeKnowledge } from '../antigravity/services/knowledge'

async function run() {
  console.log('🚀 [Ingest SOR] Starting deep market intelligence ingestion...')
  const url = 'https://software-online-review.com'

  try {
    const result = await observeKnowledge(url)
    console.log(`✅ [Ingest SOR] Successfully observed: ${result.title}`)
  } catch (err) {
    console.error('❌ [Ingest SOR] Ingestion failed:', err)
    process.exit(1)
  }
}

run()
