import { icloudObserver } from '../antigravity/services/icloud_observer'

async function main() {
  console.log('🚀 [Ingest] Starting iCloud knowledge ingestion...')
  try {
    const ingested = await icloudObserver.scan()
    console.log(`✅ [Ingest] Successfully ingested ${ingested.length} files: ${ingested.join(', ')}`)
  } catch (error) {
    console.error('❌ [Ingest] Critical failure during ingestion:', error)
    process.exit(1)
  }
}

main()
