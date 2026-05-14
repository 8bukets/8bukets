import fs from 'fs'
import path from 'path'
import { KnowledgeObserver } from '../antigravity/services/knowledge_observer'

async function ingest() {
  const docsPath = path.join(process.cwd(), 'scratch/intelephense_docs.md')
  if (!fs.existsSync(docsPath)) {
    console.error('❌ Intelephense docs not found at', docsPath)
    process.exit(1)
  }

  const rawContent = fs.readFileSync(docsPath, 'utf8')
  const title = 'Intelephense Documentation'
  const source = 'https://intelephense.com/docs'

  console.log(`🧠 Processing ${title} with improved parser...`)
  const knowledge = KnowledgeObserver.processContent(title, rawContent, source)

  console.log(`💾 Persisting knowledge...`)
  const observer = new KnowledgeObserver()
  await observer.persistKnowledge(knowledge)

  console.log('✅ Ingestion complete.')
}

ingest().catch(console.error)
