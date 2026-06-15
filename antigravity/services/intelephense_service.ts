import fs from 'fs'
import path from 'path'
import { githubDocsObserver } from './github_docs_observer'
import { KnowledgeObserver, Knowledge } from './knowledge_observer'

/**
 * INTELEPHENSE SERVICE
 * Orchestrates the consolidation of Intelephense documentation from local and remote sources.
 * Phase 13: Integrated with Jules work cycle for autonomous knowledge maintenance.
 */
export class IntelephenseService {
  private readonly owner = 'bmewburn'
  private readonly repo = 'intelephense-docs'
  private readonly files = ['README.md', 'installation.md', 'gettingStarted.md', 'features.md', 'support.md', 'LICENSE.txt']

  /**
   * consolidate: Fetches, merges, and persists Intelephense knowledge.
   */
  public async consolidate(): Promise<void> {
    console.log('🧠 Starting Intelephense Documentation consolidation...')

    let allSections: { header: string; content: string }[] = []

    // 1. Fetch from GitHub first (source of truth for latest)
    for (const file of this.files) {
      try {
        console.log(` 📡 Fetching ${file} from GitHub...`)
        const result = await githubDocsObserver.fetchDoc(this.owner, this.repo, file)
        const title = `Intelephense: ${file.replace('.md', '')}`
        const rawContent = result.sections.map((s: any) => `# ${s.title}\n${s.content}`).join('\n\n')
        const knowledge = KnowledgeObserver.processContent(title, rawContent, result.rawUrl)

        // Add these sections to our consolidated list
        allSections.push(...knowledge.sections)
      } catch (err: any) {
        console.error(` ❌ Failed to fetch ${file} from GitHub (bmewburn/intelephense-docs):`, err.message || err)
      }
    }

    // 2. Ingest from local scratch (supplementary or manual overrides)
    const localPath = path.join(process.cwd(), 'scratch/intelephense_docs.md')
    try {
      const localContent = await fs.promises.readFile(localPath, 'utf8')
      console.log(' 📄 Ingesting local scratch docs...')
      const localKnowledge = KnowledgeObserver.processContent('Intelephense Documentation', localContent, 'local://intelephense_docs.md')
      allSections.push(...localKnowledge.sections)
    } catch (err) {
      // Local scratch may not exist in all environments, skip silently
    }

    if (allSections.length === 0) {
      console.warn(' ⚠️ No Intelephense sections found to consolidate.')
      return
    }

    // 3. Deduplicate sections by header, merging content if necessary
    const headerMap = new Map<string, { header: string; content: string }>()

    for (const section of allSections) {
      const trimmedHeader = section.header.trim()
      const existing = headerMap.get(trimmedHeader)
      const isStructural = ['Getting Started', 'Features', 'Installation', 'Type System', 'Visual Studio Code', 'Other Editors'].includes(trimmedHeader)

      if (!existing) {
        // Only keep sections with content, unless they are high-level structural headers
        if (section.content || isStructural) {
          headerMap.set(trimmedHeader, { header: trimmedHeader, content: section.content })
        }
      } else {
        // Deduplication Logic: Prioritize local overrides if they contain images or more detail.
        const cleanExisting = (existing.content || '').replace(/\s+/g, ' ').trim()
        const cleanNew = (section.content || '').replace(/\s+/g, ' ').trim()

        // Heuristic: If new content has an image tag and existing doesn't, or if new is significantly longer
        const hasImage = (text: string) => /!\[.*\]\(.*\)/.test(text)

        if (cleanExisting === cleanNew) {
          continue;
        }

        if (hasImage(section.content) && !hasImage(existing.content)) {
          existing.content = section.content
        } else if (cleanExisting.includes(cleanNew)) {
          // New content is already a subset, skip
        } else if (cleanNew.includes(cleanExisting)) {
          // New content is more complete, replace
          existing.content = section.content
        } else if (section.content && section.content.length > existing.content.length * 1.5) {
          // Significantly longer content usually means more detail
          existing.content = section.content
        } else if (section.content) {
          // Both have unique info, append unique parts if not already similar
          existing.content += '\n\n' + section.content
        }
      }
    }

    const uniqueSections = Array.from(headerMap.values())
    console.log(` 🧩 Total unique sections: ${uniqueSections.length}`)

    const consolidatedKnowledge: any = {
      title: 'Intelephense Documentation',
      sections: uniqueSections,
      source: 'https://intelephense.com/docs',
      description: 'Consolidated Intelephense documentation from local and remote sources.',
      topKeywords: ['intelephense', 'php', 'lsp', 'types', 'completion'],
      recentPosts: [],
      analyzedAt: new Date().toISOString()
    }

    // 4. Persist consolidated knowledge
    const observer = new KnowledgeObserver()
    await observer.persistKnowledge(consolidatedKnowledge)

    // 5. Purge redundant legacy entries (Post-persist to avoid data loss if write fails)
    const storageDir = path.join(process.cwd(), 'data/knowledge')
    const jsonStore = path.join(storageDir, 'system_knowledge.json')

    try {
      const data = await fs.promises.readFile(jsonStore, 'utf8')
      const systemKnowledge = JSON.parse(data)

      if (systemKnowledge.typescript_sections) {
        const originalCount = systemKnowledge.typescript_sections.length
        const filtered = systemKnowledge.typescript_sections.filter((k: any) => {
          // Purge legacy "Intelephense: file" titles but KEEP the new "Intelephense Documentation"
          const isLegacyIntelephense = k.title.startsWith('Intelephense') && k.title !== 'Intelephense Documentation'
          const isLocalFilename = k.title === 'intelephense_docs.md'
          return !isLegacyIntelephense && !isLocalFilename
        })

        if (filtered.length !== originalCount) {
          console.log(` 🧹 Purged ${originalCount - filtered.length} redundant Intelephense entries.`)
          await fs.promises.writeFile(jsonStore, JSON.stringify({ ...systemKnowledge, typescript_sections: filtered }, null, 2))
        }
      }
    } catch (err) {
      // Silently handle if file is missing or unparseable
    }

    console.log('✅ Intelephense consolidation complete.')
  }
}

export const intelephenseService = new IntelephenseService()
