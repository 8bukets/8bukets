import { resolve } from '@/antigravity/core'
import { logAutonomousAction } from '../core'
import fs from 'fs'
import path from 'path'
import * as cheerio from 'cheerio'
import puppeteer from 'puppeteer'
import { GoogleGenerativeAI } from '@google/generative-ai'

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
      await page.goto(url, { waitUntil: 'networkidle2' });
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

    const relationshipEntry = `
## Autonomous Observation
- **Date**: ${new Date().toISOString()}
- **Target**: ${url}
- **Title**: ${title}
- **Context**: Ingested and observed external market or technical intelligence from ${url}.
- **Summary**:
${summary}
`

    let exists = false;
    try {
        await fs.promises.access(knowledgePath, fs.constants.F_OK);
        exists = true;
    } catch (e) {
        exists = false;
    }

    if (exists) {
      let content = await fs.promises.readFile(knowledgePath, 'utf8')

      // Check if URL already exists
      if (!content.includes(`- **Target**: ${url}`)) {
        let newContent = content.trim();


        newContent += relationshipEntry;

        // Ensure signature is at the bottom
        const signature = 'All the best - https://markposition.wordpress.com';
        if (newContent.includes(signature)) {
            newContent = newContent.split(signature).join('').trim() + '\n\n' + signature + '\n';
        } else {
            newContent = newContent.trim() + '\n\n' + signature + '\n';
        }

        await fs.promises.writeFile(knowledgePath, newContent, 'utf8')
      }
    } else {
      await fs.promises.writeFile(knowledgePath, `# Market Intelligence Matrix\n${relationshipEntry}\n\nAll the best - https://markposition.wordpress.com\n`, 'utf8')
    }

    logAutonomousAction(`✅ [Knowledge Observer] Appended insights to KNOWLEDGE_MERGE.md.`, 'info')
    return { status: 'observed', url, title }
  } catch (error) {
    console.error(`⚠️ [Knowledge Observer] Failed to scan ${url}:`, error)
    return { status: 'failed', url, error: String(error) }
  }
}
