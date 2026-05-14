import fs from 'fs'
import path from 'path'
import { z } from 'zod'

/**
 * KNOWLEDGE OBSERVER SERVICE
 * Autonomously parses and persists technical documentation and insights.
 */

export const KnowledgeSchema = z.object({
  title: z.string(),
  sections: z.array(z.object({
    header: z.string(),
    content: z.string()
  })),
  metadata: z.object({
    source: z.string(),
    ingestedAt: z.string()
  })
})

export type Knowledge = z.infer<typeof KnowledgeSchema>

const DEFAULT_STORAGE_DIR = path.join(process.cwd(), 'data/knowledge')

export class KnowledgeObserver {
  private storageDir: string

  constructor(storageDir: string = DEFAULT_STORAGE_DIR) {
    this.storageDir = storageDir
  }

  /**
   * processContent: Parses raw text into structured knowledge with code-block awareness.
   */
  public static processContent(title: string, rawContent: string, source: string): Knowledge {
    const sections: { header: string; content: string }[] = []
    const lines = rawContent.split('\n')
    let currentHeader = 'Introduction'
    let currentLines: string[] = []
    let inCodeBlock = false

    for (const line of lines) {
      const trimmed = line.trim();

      // Toggle code block state
      if (trimmed.startsWith('```') || trimmed.startsWith('<?php')) {
        inCodeBlock = !inCodeBlock
      }

      // Detect headers ONLY if not in a code block
      const hasLetters = /[a-zA-Z]/.test(trimmed)
      const isMarkdownHeader = !inCodeBlock && trimmed.startsWith('#')
      const isStrongHeader = !inCodeBlock && trimmed && hasLetters &&
                             trimmed.length < 60 && trimmed.length > 2 &&
                             !trimmed.endsWith('.') &&
                             !trimmed.endsWith(':') &&
                             !trimmed.endsWith(',') &&
                             (trimmed.toUpperCase() === trimmed || /^[A-Z][a-z]+(\s[A-Z][a-z]+)*$/.test(trimmed)) &&
                             !trimmed.startsWith('This ') &&
                             !trimmed.startsWith('Some ') &&
                             !/^[{}/*<>?]+$/.test(trimmed) && // Exclude common code symbols
                             !trimmed.includes('(') && !trimmed.includes(')') && // Exclude function calls
                             !trimmed.includes(' = ') && // Exclude assignments
                             !trimmed.includes(' => ') // Exclude arrow funcs/mappings

      // Heuristic: If it's a markdown header, always count it.
      // If it's a strong header, it must not be immediately followed by a lot of text on the same line (already trimmed)
      // and it should ideally be on its own line (which it is here since we iterate lines).
      if (isMarkdownHeader || isStrongHeader) {
        if (currentLines.length > 0) {
          sections.push({ header: currentHeader, content: currentLines.join('\n').trim() })
        }
        currentHeader = trimmed.replace(/^#+\s*/, '').trim()
        currentLines = []
      } else {
        currentLines.push(line)
      }

      // If we just ended a code block, make sure we stay out of it for the next lines
      // unless another one starts. The simple toggle works if we have distinct start/end markers.
      if (trimmed.endsWith('?>') && inCodeBlock) {
        inCodeBlock = false
      }
    }

    if (currentLines.length > 0) {
      sections.push({ header: currentHeader, content: currentLines.join('\n').trim() })
    }

    return {
      title,
      sections,
      metadata: {
        source,
        ingestedAt: new Date().toISOString()
      }
    }
  }

  /**
   * persistKnowledge: Merges and saves knowledge to persistent stores.
   */
  public async persistKnowledge(knowledge: Knowledge) {
    if (!fs.existsSync(this.storageDir)) {
      fs.mkdirSync(this.storageDir, { recursive: true })
    }

    const jsonStore = path.join(this.storageDir, 'ai_agents_knowledge.json')
    const mdStore = path.join(this.storageDir, 'ai_agents_knowledge.md')

    // 1. JSON Persistence (Merge Logic)
    let existingData: Knowledge[] = []
    if (fs.existsSync(jsonStore)) {
      try {
        existingData = JSON.parse(fs.readFileSync(jsonStore, 'utf8'))
      } catch (e) {
        console.warn('⚠️ [KnowledgeObserver] Failed to parse existing JSON store. Starting fresh.')
      }
    }

    // Replace if same title exists, or append
    const index = existingData.findIndex(k => k.title === knowledge.title)
    if (index !== -1) {
      existingData[index] = knowledge
    } else {
      existingData.push(knowledge)
    }

    fs.writeFileSync(jsonStore, JSON.stringify(existingData, null, 2))

    // 2. Markdown Persistence (Rebuild)
    let mdContent = `# ANTIGRAVITY AI AGENTS KNOWLEDGE BASE\n\n*Last Updated: ${new Date().toISOString()}*\n\n`

    for (const k of existingData) {
      mdContent += `## DOCUMENT: ${k.title}\n`
      mdContent += `**Source:** ${k.metadata.source}  \n`
      mdContent += `**Ingested At:** ${k.metadata.ingestedAt}\n\n`

      for (const section of k.sections) {
        mdContent += `### ${section.header}\n${section.content}\n\n`
      }
      mdContent += `---\n\n`
    }

    fs.writeFileSync(mdStore, mdContent)
    console.log(`✅ [KnowledgeObserver] Persisted "${knowledge.title}" to ${this.storageDir}`)
  }
}
