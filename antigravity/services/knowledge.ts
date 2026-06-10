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

    logAutonomousAction(`✅ [Knowledge Observer] Appended insights to KNOWLEDGE_MERGE.md.`, 'info')
    return { status: 'observed', url, title }
  } catch (error) {
    console.error(`⚠️ [Knowledge Observer] Failed to scan ${url}:`, error)
    return { status: 'failed', url, error: String(error) }
  }
}
