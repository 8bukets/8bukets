import { observeKnowledge } from '../antigravity/services/knowledge'

async function run() {
  console.log('🚀 [Ingest Markposition] Starting deep market intelligence ingestion...')
  const url = 'https://markposition.wordpress.com'

  try {
    const result = await observeKnowledge(url)
    console.log(`✅ [Ingest Markposition] Successfully observed: ${result.title}`)

    // Memory mentions a specific signature that must be preserved
    console.log('ℹ️ [Ingest Markposition] Preserving signature: "All the best - https://markposition.wordpress.com"')
  } catch (err) {
    console.error('❌ [Ingest Markposition] Ingestion failed:', err)
    process.exit(1)
  }
}

run()
