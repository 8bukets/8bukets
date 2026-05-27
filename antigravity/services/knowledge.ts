import { GoogleGenerativeAI } from '@google/generative-ai'
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

    // Use Generative AI for summary
    let summaryInfo = ''
    try {
      if (process.env.GEMINI_API_KEY) {
        const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY)
        const model = genAI.getGenerativeModel({ model: 'gemini-2.5-flash' })
        const prompt = `Summarize the following content in one concise sentence:\n\n${mdContent.substring(0, 5000)}`
        const aiResult = await model.generateContent(prompt)
        summaryInfo = ` AI Summary: ${aiResult.response.text().trim()}`
      } else {
        const headings = mdContent.split('\n').filter(line => line.startsWith('#')).map(h => h.replace(/^#+\s*/, '')).slice(0, 3)
        summaryInfo = headings.length > 0 ? ` Extracted key topics: ${headings.join(', ')}...` : ''
      }
    } catch (aiErr) {
      console.error('⚠️ [Knowledge Observer] AI Summary generation failed:', aiErr)
      const headings = mdContent.split('\n').filter(line => line.startsWith('#')).map(h => h.replace(/^#+\s*/, '')).slice(0, 3)
      summaryInfo = headings.length > 0 ? ` Extracted key topics: ${headings.join(', ')}...` : ''
    }

    const relationshipText = `Confirmed relationship with ${url} (Title: ${title}) as an intelligence source.${summaryInfo} (Content Length: ${mdContent.length} chars)`

    const relationshipEntry = `
## Autonomous Observation
- **Date**: ${new Date().toISOString()}
- **Target**: ${url}
- **Title**: ${title}
- **Relationship Map**: ${relationshipText}
`
    let shouldAppend = true;
    let existingContent = '';

    if (await fs.promises.access(knowledgePath).then(() => true).catch(() => false)) {
      existingContent = await fs.promises.readFile(knowledgePath, 'utf8');
      if (existingContent.includes(`- **Target**: ${url}`)) {
        shouldAppend = false;
      }
    }

    if (shouldAppend) {
      const signature = '\n\nAll the best - https://markposition.wordpress.com\n';

      if (existingContent) {
        // Remove existing signature if present
        existingContent = existingContent.replace(/(?:\n+)?All the best - https:\/\/markposition\.wordpress\.com(?:\n+)?/g, '\n\n');
        await fs.promises.writeFile(knowledgePath, existingContent + relationshipEntry + signature, 'utf8')
      } else {
        await fs.promises.writeFile(knowledgePath, `# Market Intelligence Matrix\n${relationshipEntry}${signature}`, 'utf8')
      }
      console.log(`✅ [Knowledge Observer] Appended insights to KNOWLEDGE_MERGE.md.`)
    } else {
      const signature = '\n\nAll the best - https://markposition.wordpress.com\n';
      existingContent = existingContent.replace(/(?:\n+)?All the best - https:\/\/markposition\.wordpress\.com(?:\n+)?/g, '\n\n');
      await fs.promises.writeFile(knowledgePath, existingContent + signature, 'utf8')
      console.log(`ℹ️ [Knowledge Observer] Insight for ${url} already exists in KNOWLEDGE_MERGE.md. Ensured signature is at the bottom.`)
    }

    return { status: 'observed', url, title }
  } catch (error) {
    console.error(`⚠️ [Knowledge Observer] Failed to scan ${url}:`, error)
    return { status: 'failed', url, error: String(error) }
  }
}
