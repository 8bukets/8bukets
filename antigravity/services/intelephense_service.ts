import fs from 'fs'
import path from 'path'
import { githubDocsObserver } from './github_docs_observer'
import { KnowledgeObserver, Knowledge } from './knowledge_observer'

/**
 * INTELEPHENSE SERVICE
 * Orchestrates the consolidation of Intelephense documentation from local and remote sources.
 */
export class IntelephenseService {
  private readonly owner = 'bmewburn'
  private readonly repo = 'intelephense-docs'
  private readonly files = ['README.md', 'installation.md', 'gettingStarted.md', 'features.md', 'support.md']

  /**
   * consolidate: Fetches, merges, and persists Intelephense knowledge.
   */
  public async consolidate(): Promise<void> {
    console.log('🧠 Starting Intelephense Documentation consolidation...')

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
    for (const file of this.files) {
      try {
        console.log(` 📡 Fetching ${file} from GitHub...`)
        const result = await githubDocsObserver.fetchDoc(this.owner, this.repo, file)
        const title = `Intelephense: ${file.replace('.md', '')}`
        const rawContent = result.sections.map((s: any) => `# ${s.title}\n${s.content}`).join('\n\n')
        const knowledge = KnowledgeObserver.processContent(title, rawContent, result.rawUrl)

        // Add these sections to our consolidated list
        allSections.push(...knowledge.sections)
      } catch (err) {
        console.error(` ❌ Failed to fetch ${file}:`, err)
      }
    }

    if (allSections.length === 0) {
      console.warn(' ⚠️ No Intelephense sections found to consolidate.')
      return
    }

    // 3. Deduplicate sections by header, merging content if necessary
    const headerMap = new Map<string, { header: string; content: string }>()

    for (const section of allSections) {
      const existing = headerMap.get(section.header)
      const isStructural = ['Getting Started', 'Features', 'Installation', 'Type System'].includes(section.header)

      if (!existing) {
        // Only keep sections with content, unless they are high-level structural headers
        if (section.content || isStructural) {
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
    console.log(` 🧩 Total unique sections: ${uniqueSections.length}`)

    const consolidatedKnowledge: Knowledge = {
      title: 'Intelephense Documentation',
      sections: uniqueSections,
      metadata: {
        source: 'https://intelephense.com/docs',
        ingestedAt: new Date().toISOString()
      }
    }

    // 4. Persist consolidated knowledge
    const observer = new KnowledgeObserver()
    await observer.persistKnowledge(consolidatedKnowledge, 'Intelephense')

    console.log('✅ Intelephense consolidation complete.')
  }
}

export const intelephenseService = new IntelephenseService()
