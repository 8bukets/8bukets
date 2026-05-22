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
    let inMarkdownCodeBlock = false
    let inPhpCodeBlock = false

    for (const line of lines) {
      const trimmed = line.trim();

      // Manage code block states
      if (trimmed.startsWith('```')) {
        inMarkdownCodeBlock = !inMarkdownCodeBlock
      } else if (trimmed.startsWith('<?php')) {
        inPhpCodeBlock = true
      }

      const inCodeBlock = inMarkdownCodeBlock || inPhpCodeBlock

      // Detect header candidates
      const hasLetters = /[a-zA-Z]/.test(trimmed)
      const isMarkdownHeader = trimmed.startsWith('#')
      const isStrongHeaderCandidate = trimmed && hasLetters &&
                             trimmed.length < 60 && trimmed.length > 2 &&
                             !trimmed.endsWith('.') &&
                             !trimmed.endsWith(':') &&
                             !trimmed.endsWith(',') &&
                             !trimmed.includes('\t') &&
                             !trimmed.includes('|') && !trimmed.includes('&') &&
                             !trimmed.includes('[') && !trimmed.includes(']') &&
                             !trimmed.includes('\\') &&
                             (trimmed.toUpperCase() === trimmed || /^[A-Z][a-zA-Z0-9.-]*(\s[A-Z][a-zA-Z0-9.-]*)*$/.test(trimmed)) &&
                             !trimmed.startsWith('This ') &&
                             !trimmed.startsWith('Some ') &&
                             !/^[{}/*<>?]+$/.test(trimmed) &&
                             !trimmed.includes('(') && !trimmed.includes(')') &&
                             !trimmed.includes(' = ') &&
                             !trimmed.includes(' => ')

      // Heuristic: If we hit a markdown header or a strong header candidate,
      // we assume any unclosed PHP block has ended.
      let effectiveHeader = false
      if (isMarkdownHeader) {
        effectiveHeader = true
        inPhpCodeBlock = false // Markdown headers break PHP blocks
      } else if (!inCodeBlock && isStrongHeaderCandidate) {
        effectiveHeader = true
      } else if (inPhpCodeBlock && isStrongHeaderCandidate) {
        // Strong headers also break PHP blocks (which often lack closing tags in docs)
        effectiveHeader = true
        inPhpCodeBlock = false
      }

      if (effectiveHeader) {
        if (currentLines.length > 0) {
          sections.push({ header: currentHeader, content: currentLines.join('\n').trim() })
        }
        currentHeader = trimmed.replace(/^#+\s*/, '').trim()
        currentLines = []
      } else {
        currentLines.push(line)
      }

      // Close PHP code block if we see the closing tag
      if (trimmed.includes('?>') && inPhpCodeBlock) {
        inPhpCodeBlock = false
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

    const jsonStore = path.join(this.storageDir, 'system_knowledge.json')
    const mdStore = path.join(this.storageDir, 'ai_agents_knowledge.md')

    // 1. JSON Persistence (Merge Logic - Unified Store)
    let systemKnowledge: any = { typescript_sections: [] }
    if (fs.existsSync(jsonStore)) {
      try {
        systemKnowledge = JSON.parse(fs.readFileSync(jsonStore, 'utf8'))
        if (!systemKnowledge.typescript_sections) {
          systemKnowledge.typescript_sections = []
        }
      } catch (e) {
        console.warn('⚠️ [KnowledgeObserver] Failed to parse existing JSON store. Starting fresh.')
      }
    }

    // Replace if same title exists, or append
    const existingData = systemKnowledge.typescript_sections
    const index = existingData.findIndex((k: Knowledge) => k.title === knowledge.title)
    if (index !== -1) {
      existingData[index] = knowledge
    } else {
      existingData.push(knowledge)
    }

    fs.writeFileSync(jsonStore, JSON.stringify(systemKnowledge, null, 2))

    // 2. Markdown Persistence (Rebuild)
    let mdContent = `# ANTIGRAVITY AI AGENTS KNOWLEDGE BASE\n\n*Last Updated: ${new Date().toISOString()}*\n\n`

    for (const k of existingData as Knowledge[]) {
      mdContent += `## DOCUMENT: ${k.title}\n`
      mdContent += `**Source:** ${k.metadata.source.trim()}\n`
      mdContent += `**Ingested At:** ${k.metadata.ingestedAt.trim()}\n\n`

      for (const section of k.sections) {
        mdContent += `### ${section.header.trim()}\n${section.content.trim()}\n\n`
      }
      mdContent += `---\n\n`
    }

    fs.writeFileSync(mdStore, mdContent)
    console.log(`✅ [KnowledgeObserver] Persisted "${knowledge.title}" to ${this.storageDir}`)
  }
}
