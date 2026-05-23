import { jules } from '@/antigravity/jules'

async function testIngestion() {
  console.log('🧪 Testing GitHub Docs Ingestion...')
  try {
    await jules.observeGithubDocs()
    console.log('✅ Ingestion test complete.')
  } catch (err) {
    console.error('❌ Ingestion test failed:', err)
    process.exit(1)
  }
}

testIngestion()
