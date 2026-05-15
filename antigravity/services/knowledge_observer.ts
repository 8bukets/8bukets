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
                             (trimmed.toUpperCase() === trimmed || /^[A-Z][a-z0-9]*(\s[A-Z][a-z0-9]*)*$/.test(trimmed)) &&
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
    const mdStore = path.join(process.cwd(), 'KNOWLEDGE_INTEGRATION.md')

    // 1. JSON Persistence (Merge Logic)
    let store: { typescript_sections: Knowledge[] } = { typescript_sections: [] }
    if (fs.existsSync(jsonStore)) {
      try {
        const raw = fs.readFileSync(jsonStore, 'utf8')
        const parsed = JSON.parse(raw)
        if (parsed.typescript_sections && Array.isArray(parsed.typescript_sections)) {
          store = parsed
        } else if (Array.isArray(parsed)) {
          store.typescript_sections = parsed
        }
      } catch (e) {
        console.warn('⚠️ [KnowledgeObserver] Failed to parse existing JSON store. Starting fresh.')
      }
    }

    // Replace if same title exists, or append
    const index = store.typescript_sections.findIndex(k => k.title === knowledge.title)
    if (index !== -1) {
      store.typescript_sections[index] = knowledge
    } else {
      store.typescript_sections.push(knowledge)
    }

    fs.writeFileSync(jsonStore, JSON.stringify(store, null, 2))

    // 2. Markdown Persistence (Marker-Based Update)
    let mdContent = ''
    if (fs.existsSync(mdStore)) {
      mdContent = fs.readFileSync(mdStore, 'utf8')
    } else {
      mdContent = `# KNOWLEDGE INTEGRATION\n\n## What are AI Agents?\n\n<!-- AI_AGENTS_START -->\n<!-- AI_AGENTS_END -->\n\n## What does Compile mean?\n\n## IDE Integration\n\n## Gemma 4 Model Card\n`
    }

    const startMarker = '<!-- AI_AGENTS_START -->'
    const endMarker = '<!-- AI_AGENTS_END -->'

    let aiAgentsContent = '\n'
    for (const k of store.typescript_sections) {
      aiAgentsContent += `### DOCUMENT: ${k.title}\n`
      aiAgentsContent += `**Source:** ${k.metadata.source}  \n`
      aiAgentsContent += `**Ingested At:** ${k.metadata.ingestedAt}\n\n`

      for (const section of k.sections) {
        aiAgentsContent += `#### ${section.header}\n${section.content}\n\n`
      }
      aiAgentsContent += `---\n\n`
    }

    const startIdx = mdContent.indexOf(startMarker)
    const endIdx = mdContent.indexOf(endMarker)

    if (startIdx !== -1 && endIdx !== -1) {
      const before = mdContent.substring(0, startIdx + startMarker.length)
      const after = mdContent.substring(endIdx)
      mdContent = before + aiAgentsContent + after
    } else {
      // If markers are missing, append them to the first relevant section or at the end
      if (mdContent.includes('## What are AI Agents?')) {
          mdContent = mdContent.replace('## What are AI Agents?', `## What are AI Agents?\n\n${startMarker}${aiAgentsContent}${endMarker}`)
      } else {
          mdContent += `\n## What are AI Agents?\n\n${startMarker}${aiAgentsContent}${endMarker}\n`
      }
    }

    fs.writeFileSync(mdStore, mdContent)
    console.log(`✅ [KnowledgeObserver] Persisted "${knowledge.title}" to ${this.storageDir}`)
  }
}
