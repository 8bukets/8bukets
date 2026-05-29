import { logAutonomousAction } from '../core'
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
   * persistKnowledge: Merges and saves knowledge to the unified system store.
   */
  public async persistKnowledge(knowledge: Knowledge) {
    if (!fs.existsSync(this.storageDir)) {
      fs.mkdirSync(this.storageDir, { recursive: true })
    }

    const jsonStore = path.join(this.storageDir, 'system_knowledge.json')

    // 1. JSON Persistence (Cross-Ecosystem Merge Logic)
    let systemKnowledge: any = {
      metadata: {
        generated_at: new Date().toISOString(),
        version: 1.0,
        sources_processed: []
      },
      sections: {},
      typescript_sections: {}
    }

    if (fs.existsSync(jsonStore)) {
      try {
        systemKnowledge = JSON.parse(fs.readFileSync(jsonStore, 'utf8'))
      } catch (e) {
        console.warn('⚠️ [KnowledgeObserver] Failed to parse unified store. Initializing new structure.')
      }
    }

    // Explicit Flat Key Whitelist to ensure ecosystem compatibility
    const FLAT_KEYS = [
      'ai_agents',
      'market_data',
      'legal_ecosystem',
      'gemma_model',
      'intelephense',
      'litert',
      'stitch',
      'vscode_intelephense',
      'google_ads'
    ]
    const isFlatKey = FLAT_KEYS.includes(knowledge.title)

    if (isFlatKey) {
      systemKnowledge[knowledge.title] = {
        sections: knowledge.sections,
        metadata: knowledge.metadata
      }
    } else {
      // For descriptive titles, we still use the typescript_sections namespace
      // to avoid polluting the top-level flat key space.
      if (!systemKnowledge.typescript_sections) {
        systemKnowledge.typescript_sections = {}
      }

      systemKnowledge.typescript_sections[knowledge.title] = {
        sections: knowledge.sections,
        metadata: knowledge.metadata
      }
    }

    // Update global metadata
    systemKnowledge.metadata.generated_at = new Date().toISOString()
    if (!systemKnowledge.metadata.sources_processed.includes(knowledge.metadata.source)) {
      systemKnowledge.metadata.sources_processed.push(knowledge.metadata.source)
    }

    fs.writeFileSync(jsonStore, JSON.stringify(systemKnowledge, null, 2))
    logAutonomousAction(`✅ [KnowledgeObserver] Persisted "${knowledge.title}" to unified store at ${jsonStore}`, 'info')
  }
}
