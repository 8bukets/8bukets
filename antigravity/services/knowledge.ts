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

    const signature = 'All the best - https://markposition.wordpress.com'

    // Instead of regex, split on signature and trim
    let cleanContent = existingContent
    if (existingContent.includes(signature)) {
       cleanContent = existingContent.split(signature)[0]
    }
    cleanContent = cleanContent.trimEnd()

    let updated = false
    // Use string parsing to avoid regex bugs
    const blockRegex = /## Autonomous Observation(?:(?!## Autonomous Observation)[\s\S])*/g

    let blocks = [];
    let match;
    while ((match = blockRegex.exec(cleanContent)) !== null) {
        blocks.push(match[0]);
    }

    let newBlocks = blocks.map(block => {
        if (block.includes(`- **Target**: ${url}\n`) || block.includes(`- **Target**: ${url}\r`)) {
            updated = true;
            return relationshipEntry.trimStart();
        }
        return block;
    });

    if (!updated) {
        newBlocks.push(relationshipEntry.trimStart());
    }

    // Replace the part of string where the blocks are
    let newContent = cleanContent.split(/## Autonomous Observation/)[0].trimEnd()
    if (newBlocks.length > 0) {
        newContent += '\n\n' + newBlocks.join('\n\n')
    }

    newContent = newContent.trimEnd() + '\n\n' + signature + '\n'
    await fs.promises.writeFile(knowledgePath, newContent, 'utf8')
    console.log(`✅ [Knowledge Observer] ${updated ? 'Updated' : 'Appended'} insights in KNOWLEDGE_MERGE.md.`)

    return { status: 'observed', url, title }
  } catch (error) {
    console.error(`⚠️ [Knowledge Observer] Failed to scan ${url}:`, error)
    return { status: 'failed', url, error: String(error) }
  }
}
