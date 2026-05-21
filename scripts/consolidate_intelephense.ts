import fs from 'fs'
import path from 'path'
import { githubDocsObserver } from '../antigravity/services/github_docs_observer'
import { KnowledgeObserver, Knowledge } from '../antigravity/services/knowledge_observer'

async function consolidate() {
  console.log('🧠 Starting Intelephense Documentation consolidation...')

  const owner = 'bmewburn'
  const repo = 'intelephense-docs'
  const files = ['README.md', 'installation.md', 'gettingStarted.md', 'features.md', 'support.md']

  let allSections: { header: string; content: string }[] = []

  // 1. Ingest from local scratch (most complete usually)
  const localPath = path.join(process.cwd(), 'scratch/intelephense_docs.md')
  if (fs.existsSync(localPath)) {
    console.log(' 📄 Ingesting local scratch docs...')
    const localContent = fs.readFileSync(localPath, 'utf8')
    const localKnowledge = KnowledgeObserver.processContent('Intelephense Documentation', localContent, 'local://intelephense_docs.md')
    allSections.push(...localKnowledge.sections)
  }

  // 2. Fetch and merge from GitHub
  for (const file of files) {
    try {
      console.log(` 📡 Fetching ${file} from GitHub...`)
      const result = await githubDocsObserver.fetchDoc(owner, repo, file)
      const rawContent = result.sections.map((s: any) => `# ${s.title}\n${s.content}`).join('\n\n')
      const knowledge = KnowledgeObserver.processContent(`Intelephense: ${file.replace('.md', '')}`, rawContent, result.rawUrl)

      // Add these sections to our consolidated list
      allSections.push(...knowledge.sections)
    } catch (err) {
      console.error(` ❌ Failed to fetch ${file}:`, err)
    }
  }

  // 3. Deduplicate sections by header, prioritizing content length (quality)
  const headerMap = new Map<string, { header: string; content: string }>()

  for (const section of allSections) {
    const existing = headerMap.get(section.header)
    // Heuristic: Prefer the section with the most content (likely more detailed)
    // Also ensure we keep structural headers even if empty
    const isStructural = ['Getting Started', 'Features', 'Installation', 'Type System'].includes(section.header)

    if (!existing || (section.content.length >= existing.content.length)) {
      if (section.content.trim().length > 0 || isStructural) {
        headerMap.set(section.header, section)
      }
    }
  }

  const uniqueSections = Array.from(headerMap.values())

  const consolidatedKnowledge: Knowledge = {
    title: 'Intelephense Documentation',
    sections: uniqueSections,
    metadata: {
      source: 'https://intelephense.com/docs',
      ingestedAt: new Date().toISOString()
    }
  }

  // 4. Purge redundant entries from the store before persisting
  const storageDir = path.join(process.cwd(), 'data/knowledge')
  const jsonStore = path.join(storageDir, 'system_knowledge.json')

  if (fs.existsSync(jsonStore)) {
    console.log(' 🧹 Purging redundant Intelephense entries...')
    const systemKnowledge = JSON.parse(fs.readFileSync(jsonStore, 'utf8'))
    if (systemKnowledge.typescript_sections) {
      systemKnowledge.typescript_sections = systemKnowledge.typescript_sections.filter((k: any) => {
        // Purge any "Intelephense: ..." variants, only keeping the main consolidated one if it exists (it will be updated)
        return !k.title.startsWith('Intelephense:')
      })
      fs.writeFileSync(jsonStore, JSON.stringify(systemKnowledge, null, 2))
    }
  }

  console.log(' 💾 Persisting consolidated knowledge...')
  const observer = new KnowledgeObserver()
  await observer.persistKnowledge(consolidatedKnowledge)

  console.log('✅ Consolidation complete.')
}

consolidate().catch(console.error)
