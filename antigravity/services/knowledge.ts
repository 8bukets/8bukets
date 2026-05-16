import { logAutonomousAction } from '../core'
import fs from 'fs'
import path from 'path'
import * as cheerio from 'cheerio'
import { KnowledgeObserver } from './knowledge_observer'

/**
 * Scan and Observe Knowledge Service
 * Fetches basic metadata from a target URL and records relationship intelligence.
 */
export async function observeKnowledge(url: string) {
  console.log(`🧠 [Knowledge Observer] Scanning ${url} for market intelligence...`)

  try {
    const response = await fetch(url)
    const html = await response.text()
    const $ = cheerio.load(html)

    const title = $('title').text() || 'No Title Found'

    let mdContent = ''
    $('h1, h2, h3, h4, h5, h6, p, ul, ol, li, a').each((_, el) => {
      const tag = el.tagName.toLowerCase()
      const text = $(el).text().replace(/\s+/g, ' ').trim()

      if (text) {
        if (tag.startsWith('h')) {
          const level = parseInt(tag.replace('h', ''), 10)
          mdContent += `\n${'#'.repeat(level)} ${text}\n`
        } else if (tag === 'p') {
          mdContent += `${text}\n\n`
        } else if (tag === 'a') {
          const href = $(el).attr('href')
          if (href) {
            mdContent += `[${text}](${href})\n`
          }
        } else if (tag === 'li') {
            mdContent += `- ${text}\n`
        }
      }
    })

    logAutonomousAction(`[KNOWLEDGE] Scanned ${url}. Title: ${title}`, 'cognitive')

    // Parse and structure the extracted knowledge
    const knowledge = KnowledgeObserver.processContent(title, mdContent, url)
    const observer = new KnowledgeObserver()
    await observer.persistKnowledge(knowledge)

    // Append or create KNOWLEDGE_MERGE.md with formal relationships
    const knowledgePath = path.join(process.cwd(), 'KNOWLEDGE_MERGE.md')

    const relationshipEntry = `
## Autonomous Observation
- **Date**: ${new Date().toISOString()}
- **Target**: ${url}
- **Title**: ${title}
- **Relationship Map**: Confirmed relationship with ${url} (Title: ${title}) as an intelligence source.
`
    if (fs.existsSync(knowledgePath)) {
      fs.appendFileSync(knowledgePath, relationshipEntry, 'utf8')
    } else {
      fs.writeFileSync(knowledgePath, `# Market Intelligence Matrix\n${relationshipEntry}`, 'utf8')
    }

    console.log(`✅ [Knowledge Observer] Appended insights to KNOWLEDGE_MERGE.md.`)
    return { status: 'observed', url, title }
  } catch (error) {
    console.error(`⚠️ [Knowledge Observer] Failed to scan ${url}:`, error)
    return { status: 'failed', url, error: String(error) }
  }
}
