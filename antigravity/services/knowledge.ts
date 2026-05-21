import { resolve } from '@/antigravity/core'
import { logAutonomousAction } from '../core'
import fs from 'fs'
import path from 'path'
import * as cheerio from 'cheerio'
import puppeteer from 'puppeteer'

/**
 * Scan and Observe Knowledge Service
 * Fetches basic metadata from a target URL and records relationship intelligence.
 */
export async function observeKnowledge(url: string) {
  logAutonomousAction(`🧠 [Knowledge Observer] Scanning ${url} for market intelligence...`, 'info')

  try {
    let html = '';

    // Axiom: always pull knowledge from investopedia thrue chrome active browser
    if (url.includes('investopedia.com')) {
      logAutonomousAction(`[Knowledge Observer] Using Chrome active browser (Puppeteer) for Investopedia...`, 'info')
      const browser = await puppeteer.launch({ headless: true, args: ['--no-sandbox'] });
      try {
        const page = await browser.newPage();
        await page.goto(url, { waitUntil: 'networkidle2' });
        html = await page.content();
      } finally {
        await browser.close();
      }
    } else {
      const response = await fetch(url)
      html = await response.text()
    }

    const $ = cheerio.load(html)

    const title = $('title').text() || 'No Title Found'

    logAutonomousAction(`[KNOWLEDGE] Scanned ${url}. Title: ${title}`, 'cognitive')

    // Append or create KNOWLEDGE_MERGE.md with formal relationships
    const knowledgePath = path.join(process.cwd(), 'KNOWLEDGE_MERGE.md')

    const relationshipEntry = `
## Autonomous Observation
- **Date**: ${new Date().toISOString()}
- **Target**: ${url}
- **Title**: ${title}
- **Context**: Ingested and observed external market or technical intelligence from ${url}.
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
        await fs.promises.writeFile(knowledgePath, newContent, 'utf8')
      }
    } else {
      await fs.promises.writeFile(knowledgePath, `# Market Intelligence Matrix\n${relationshipEntry}`, 'utf8')
    }

    logAutonomousAction(`✅ [Knowledge Observer] Appended insights to KNOWLEDGE_MERGE.md.`, 'info')
    return { status: 'observed', url, title }
  } catch (error) {
    console.error(`⚠️ [Knowledge Observer] Failed to scan ${url}:`, error)
    return { status: 'failed', url, error: String(error) }
  }
}
