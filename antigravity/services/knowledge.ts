import { logAutonomousAction } from '../core'
import fs from 'fs'
import path from 'path'
import * as cheerio from 'cheerio'
import puppeteer from 'puppeteer-extra'
import StealthPlugin from 'puppeteer-extra-plugin-stealth'
import { GoogleGenerativeAI } from '@google/generative-ai'

puppeteer.use(StealthPlugin())

/**
 * Scan and Observe Knowledge Service
 * Fetches basic metadata from a target URL and records relationship intelligence.
 */
export async function observeKnowledge(url: string = 'https://www.investopedia.com/') {
  logAutonomousAction(`🧠 [Knowledge Observer] Scanning ${url} for market intelligence...`, 'info')

  try {
    let html = '';
    if (url.includes('investopedia.com')) {
      const browser = await puppeteer.launch({
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
      });
      const page = await browser.newPage();
      await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36');
      await page.goto(url, { waitUntil: 'domcontentloaded' });
      html = await page.content();
      await browser.close();
    } else {
      const response = await fetch(url)
      html = await response.text()
    }

    const $ = cheerio.load(html)

    // Remove non-informative elements
    $('header').remove()
    $('footer').remove()
    $('nav').remove()
    $('.skip-to-content').remove()
    $('a[href^="#"]').remove()
    $('script').remove()
    $('style').remove()

    const title = $('title').text() || 'No Title Found'
    const bodyText = $('body').text().replace(/\s+/g, ' ').trim()

    let summary = 'Basic extraction performed.';
    if (bodyText) {
        summary = bodyText.substring(0, 500) + '...'; // Fallback summary
        const geminiKey = process.env.GEMINI_API_KEY;
        if (geminiKey) {
            try {
                const genAI = new GoogleGenerativeAI(geminiKey);
                const model = genAI.getGenerativeModel({ model: "gemini-2.0-flash" });
                const prompt = `Summarize the following text, focusing on key topics and market intelligence. Provide a concise bulleted summary:\n\n${bodyText.substring(0, 10000)}`;
                const result = await model.generateContent(prompt);
                summary = result.response.text();
            } catch (err) {
                console.warn('⚠️ [Knowledge Observer] Failed to generate AI summary, using fallback.', err);
            }
        }
    }

    logAutonomousAction(`[KNOWLEDGE] Scanned ${url}. Title: ${title}`, 'cognitive')

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
- **Context**: Ingested and observed external market or technical intelligence from ${url}.
- **Summary**:
${summary}
`
    let existingContent = ''
    try {
      existingContent = await fs.promises.readFile(knowledgePath, 'utf8')
    } catch (e) {
      existingContent = '# Market Intelligence Matrix\n'
    }

    const signatures = [
      'All the best - https://markposition.wordpress.com',
      'All the best - https://software-online-review.com/',
      'All the best - https://dbcode.io/'
    ]

    // Instead of regex, split on signature and trim
    let cleanContent = existingContent
    for (const signature of signatures) {
      if (cleanContent.includes(signature)) {
        cleanContent = cleanContent.split(signature)[0]
      }
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

    newContent = newContent.trimEnd() + '\n\n---\n'
    newContent += signatures.join('\n\n---\n') + '\n'
    await fs.promises.writeFile(knowledgePath, newContent, 'utf8')
    console.log(`✅ [Knowledge Observer] ${updated ? 'Updated' : 'Appended'} insights in KNOWLEDGE_MERGE.md.`)

    logAutonomousAction(`✅ [Knowledge Observer] Appended insights to KNOWLEDGE_MERGE.md.`, 'info')
    return { status: 'observed', url, title }
  } catch (error) {
    console.error(`⚠️ [Knowledge Observer] Failed to scan ${url}:`, error)
    return { status: 'failed', url, error: String(error) }
  }
}
