import { observeKnowledge } from '../antigravity/services/knowledge'

async function run() {
  console.log('🚀 [Ingest Boundary] Starting HashiCorp Boundary intelligence ingestion...')
  const url = 'https://e15e881b-2d8b-49da-9306-e8aaf84eef37.boundary.hashicorp.cloud'

  try {
    const result = await observeKnowledge(url)
    if (result.status === 'failed') {
      console.warn(`⚠️ [Ingest Boundary] Observation failed, likely due to 404 (expected). Status: ${result.status}`)
    } else {
      console.log(`✅ [Ingest Boundary] Successfully observed: ${result.title}`)
    }
  } catch (err) {
    console.error('❌ [Ingest Boundary] Ingestion failed:', err)
  }
}

run()
