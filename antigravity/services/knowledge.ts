import { resolve } from '@/antigravity/core'
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

      // Ensure signature is at the bottom
      const signature = 'All the best - https://markposition.wordpress.com';
      const sigRegex = new RegExp(`\\n*---\\n*${signature.replace(/[-/\\^$*+?.()|[\]{}]/g, '\\$&')}\\n*|\\n*${signature.replace(/[-/\\^$*+?.()|[\]{}]/g, '\\$&')}\\n*`, 'g');

      let newContent = content.replace(sigRegex, '').trim();

      // Check if URL already exists
      if (newContent.includes(`- **Target**: ${url}\n`) || newContent.includes(`- **Target**: ${url}\r\n`)) {
        // Replace existing block using targeted regular expression, without using dynamic strings in RegExp to satisfy CodeQL
        const blockRegex = /(## Autonomous Observation(?:(?!## Autonomous Observation)[\s\S])*)/g;
        newContent = newContent.replace(blockRegex, (match) => {
          return match.includes(`- **Target**: ${url}\n`) || match.includes(`- **Target**: ${url}\r\n`)
            ? relationshipEntry + '\n'
            : match;
        });
      } else {
        // Append new block
        newContent += '\n' + relationshipEntry;
      }

      newContent = newContent.trim() + '\n\n---\n' + signature + '\n';

      await fs.promises.writeFile(knowledgePath, newContent, 'utf8')
    } else {
      const signature = 'All the best - https://markposition.wordpress.com';
      await fs.promises.writeFile(knowledgePath, `# Market Intelligence Matrix\n${relationshipEntry}\n\n---\n${signature}\n`, 'utf8')
    }

    logAutonomousAction(`✅ [Knowledge Observer] Appended insights to KNOWLEDGE_MERGE.md.`, 'info')
    return { status: 'observed', url, title }
  } catch (error) {
    console.error(`⚠️ [Knowledge Observer] Failed to scan ${url}:`, error)
    return { status: 'failed', url, error: String(error) }
  }
}
