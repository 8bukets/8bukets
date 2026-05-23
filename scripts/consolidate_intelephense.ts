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

  // 3. Deduplicate sections by header, merging content if necessary
  const headerMap = new Map<string, { header: string; content: string }>()

  for (const section of allSections) {
    const existing = headerMap.get(section.header)
    if (!existing) {
      // Only keep sections with content, unless they are high-level structural headers
      if (section.content || ['Getting Started', 'Features', 'Installation'].includes(section.header)) {
        headerMap.set(section.header, { ...section })
      }
    } else {
      // If header exists, merge content if the new content is different and not empty
      if (section.content && section.content !== existing.content) {
        if (existing.content.includes(section.content)) {
          // New content is already a subset, ignore
        } else if (section.content.includes(existing.content)) {
          // New content is more complete, replace
          existing.content = section.content
        } else {
          // Both have unique info, append
          existing.content += '\n\n' + section.content
        }
      }
    }
  }

  const uniqueSections = Array.from(headerMap.values())

  // Ensure all headers from scratch are definitely here
  console.log(` 🧩 Total unique sections: ${uniqueSections.length}`)

  const consolidatedKnowledge: Knowledge = {
    title: 'Intelephense Documentation',
    sections: uniqueSections,
    metadata: {
      source: 'https://intelephense.com/docs',
      ingestedAt: new Date().toISOString()
    }
  }

  console.log(' 💾 Persisting consolidated knowledge...')
  const observer = new KnowledgeObserver()
  await observer.persistKnowledge(consolidatedKnowledge, 'Intelephense')

  console.log('✅ Consolidation complete.')
}

consolidate().catch(console.error)
