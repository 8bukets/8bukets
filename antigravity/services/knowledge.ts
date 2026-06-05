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
  'use cache'
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

      if (text && text.toLowerCase() !== 'skip to content') {
        if (tag.startsWith('h')) {
          const level = parseInt(tag.replace('h', ''), 10)
          mdContent += `\n${'#'.repeat(level)} ${text}\n`
        } else if (tag === 'p') {
          mdContent += `${text}\n\n`
        } else if (tag === 'a') {
          const href = $(el).attr('href')
          // Do not extract bare, uninformative links, or duplication
          if (href && !href.startsWith('#') && text.length > 2) {
            mdContent += `- [${text}](${href})\n`
          }
        } else if (tag === 'li') {
          // If the list item has an anchor inside, avoid duplication by skipping raw li text if it matches a
          const hasAnchor = $(el).find('a').length > 0;
          if (!hasAnchor) {
            mdContent += `- ${text}\n`
          }
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

    // Extract some summaries for the merge file
    const headings = mdContent.split('\n').filter(line => line.startsWith('#')).map(h => h.replace(/^#+\s*/, '')).slice(0, 3)
    const summaryInfo = headings.length > 0 ? ` Extracted key topics: ${headings.join(', ')}...` : ''

    const relationshipText = `Confirmed relationship with ${url} (Title: ${title}) as an intelligence source.${summaryInfo} (Content Length: ${mdContent.length} chars)`

    const relationshipEntry = `
## Autonomous Observation
- **Date**: ${new Date().toISOString()}
- **Target**: ${url}
- **Title**: ${title}
- **Relationship Map**: ${relationshipText}
`
    let existingContent = ''
    try {
      existingContent = await fs.promises.readFile(knowledgePath, 'utf8')
    } catch (e) {
      existingContent = '# Market Intelligence Matrix\n'
    }

    let cleanContent = existingContent.trimEnd()

    // Check if the target is already observed
    const targetIndicator = `- **Target**: ${url}`;
    const targetPos = cleanContent.indexOf(targetIndicator);
    let newContent = cleanContent;
    let updated = false;

    if (targetPos !== -1) {
        // Find the beginning of this observation block
        const blockStartPos = cleanContent.lastIndexOf('## Autonomous Observation', targetPos);

        // Find the end of this block (start of the next header, or end of string)
        const nextHeaderPos = cleanContent.indexOf('\n## ', targetPos + targetIndicator.length);
        const blockEndPos = nextHeaderPos !== -1 ? nextHeaderPos : cleanContent.length;

        // Replace the old block with the new one
        newContent = cleanContent.slice(0, blockStartPos) + relationshipEntry.trimStart() + '\n' + cleanContent.slice(blockEndPos);
        updated = true;
    } else {
        // Append observation block right before the first Ecosystem Knowledge Consolidation, or at the end
        const ecosystemStart = cleanContent.indexOf('\n## Ecosystem Knowledge Consolidation');
        if (ecosystemStart !== -1) {
             newContent = cleanContent.slice(0, ecosystemStart) + '\n\n' + relationshipEntry.trimStart() + '\n\n' + cleanContent.slice(ecosystemStart);
        } else {
             newContent = cleanContent + '\n\n' + relationshipEntry.trimStart() + '\n\n';
        }
    }

    newContent = newContent.trimEnd() + '\n'
    await fs.promises.writeFile(knowledgePath, newContent, 'utf8')
    console.log(`✅ [Knowledge Observer] ${updated ? 'Updated' : 'Appended'} insights in KNOWLEDGE_MERGE.md.`)

    return { status: 'observed', url, title }
  } catch (error) {
    console.error(`⚠️ [Knowledge Observer] Failed to scan ${url}:`, error)
    return { status: 'failed', url, error: String(error) }
  }
}
