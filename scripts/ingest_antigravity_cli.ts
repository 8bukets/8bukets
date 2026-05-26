import { observeKnowledge } from '../antigravity/services/knowledge'

async function run() {
  console.log('🚀 [Ingest Antigravity CLI] Starting intelligence ingestion...')
  const url = 'https://antigravity.google/product/antigravity-cli'

  try {
    const result = await observeKnowledge(url)
    console.log(`✅ [Ingest Antigravity CLI] Successfully observed: ${result.title}`)
  } catch (err) {
    console.error('❌ [Ingest Antigravity CLI] Ingestion failed:', err)
    process.exit(1)
  }
}

run()
