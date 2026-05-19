import { logAutonomousAction } from '../core'
import fs from 'fs'
import path from 'path'
import * as cheerio from 'cheerio'

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

    logAutonomousAction(`[KNOWLEDGE] Scanned ${url}. Title: ${title}`, 'cognitive')

    // Append or create KNOWLEDGE_MERGE.md with formal relationships
    const knowledgePath = path.join(process.cwd(), '../KNOWLEDGE_MERGE.md')

    const relationshipText = `Confirmed relationship with ${url} (Title: ${title}) as an intelligence source.`

    const relationshipEntry = `
## Autonomous Observation
- **Date**: ${new Date().toISOString()}
- **Target**: ${url}
- **Title**: ${title}
- **Relationship Map**: ${relationshipText}
`
    let shouldAppend = true;
    let existingContent = '';

    if (fs.existsSync(knowledgePath)) {
      existingContent = fs.readFileSync(knowledgePath, 'utf8');
      if (existingContent.includes(`- **Target**: ${url}`)) {
        shouldAppend = false;
      }
    }

    if (shouldAppend) {
      if (existingContent) {
        fs.writeFileSync(knowledgePath, existingContent + relationshipEntry, 'utf8')
      } else {
        fs.writeFileSync(knowledgePath, `# Market Intelligence Matrix\n${relationshipEntry}`, 'utf8')
      }
      console.log(`✅ [Knowledge Observer] Appended insights to KNOWLEDGE_MERGE.md.`)
    } else {
      console.log(`ℹ️ [Knowledge Observer] Insight for ${url} already exists in KNOWLEDGE_MERGE.md.`)
    }
    return { status: 'observed', url, title }
  } catch (error) {
    console.error(`⚠️ [Knowledge Observer] Failed to scan ${url}:`, error)
    return { status: 'failed', url, error: String(error) }
  }
}
