import { KnowledgeObserver, persistKnowledge } from '@/antigravity/services/knowledge_observer';
import puppeteer from 'puppeteer-extra';
import StealthPlugin from 'puppeteer-extra-plugin-stealth';
import * as cheerio from 'cheerio';

puppeteer.use(StealthPlugin());

async function getDBCodeLinks(baseUrl: string): Promise<string[]> {
  console.log(`🔍 [DBCode Crawler] Extracting subpages from ${baseUrl}...`);
  try {
    const browser = await puppeteer.launch({
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36');
    await page.goto(baseUrl, { waitUntil: 'domcontentloaded' });
    const html = await page.content();
    await browser.close();

    const $ = cheerio.load(html);
    const links = new Set<string>();

    $('a').each((_, element) => {
      const href = $(element).attr('href');
      // Look for documentation links specifically
      if (href && (href.startsWith('https://dbcode.io/docs') || href.startsWith('/docs')) && !href.includes('#')) {
        const fullUrl = href.startsWith('/') ? `https://dbcode.io${href}` : href;
        links.add(fullUrl);
      }
    });

    return Array.from(links);
  } catch (err) {
    console.error(`⚠️ [DBCode Crawler] Failed to extract subpages from ${baseUrl}:`, err);
    return [];
  }
}

async function scrapeAndObserve(url: string) {
    try {
        const browser = await puppeteer.launch({
            headless: true,
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        });
        const page = await browser.newPage();
        await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36');
        await page.goto(url, { waitUntil: 'domcontentloaded' });
        const html = await page.content();
        await browser.close();

        const title = url === 'https://dbcode.io/docs' ? 'DBCode Documentation Index' : 'DBCode Technical Insight';
        const knowledge = KnowledgeObserver.processContent(title, html, url);
        await persistKnowledge(knowledge);
    } catch (err) {
        console.error(`❌ [Ingest] Failed to observe ${url}:`, err);
    }
}

async function ingestDBCode() {
  const targetUrls = process.argv.slice(2);

  if (targetUrls.length === 0) {
    console.log(`🤖 [Ingest] Fetching market intelligence from DBCode Docs...`);
    const defaultUrl = 'https://dbcode.io/docs';
    await scrapeAndObserve(defaultUrl);

    const subpages = await getDBCodeLinks(defaultUrl);
    // Limit to top 15 to cover major features
    const limit = 15;
    console.log(`🤖 [Ingest] Found ${subpages.length} subpages. Observing top ${limit}...`);

    for (let i = 0; i < Math.min(subpages.length, limit); i++) {
        const url = subpages[i];
        if (url !== defaultUrl) {
            console.log(`- Observing knowledge from subpage: ${url}`);
            await scrapeAndObserve(url);
        }
    }
  } else {
    console.log(`🤖 [Ingest] Fetching market intelligence from ${targetUrls.length} URL(s)...`);

    for (const url of targetUrls) {
      console.log(`- Observing knowledge from: ${url}`);
      await scrapeAndObserve(url);
    }
  }

  console.log('✅ [Ingest] Ingestion complete.');
}

ingestDBCode().catch(console.error);
