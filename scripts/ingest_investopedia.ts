import { observeKnowledge } from '../antigravity/services/knowledge';
import puppeteer from 'puppeteer-extra';
import StealthPlugin from 'puppeteer-extra-plugin-stealth';
import * as cheerio from 'cheerio';

puppeteer.use(StealthPlugin());

async function getInvestopediaLinks(baseUrl: string): Promise<string[]> {
  console.log(`🔍 [Investopedia Crawler] Extracting subpages from ${baseUrl}...`);
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
      if (href && href.startsWith('https://www.investopedia.com/') && !href.includes('#')) {
        links.add(href);
      } else if (href && href.startsWith('/') && !href.includes('#')) {
        links.add(`https://www.investopedia.com${href}`);
      }
    });

    return Array.from(links);
  } catch (err) {
    console.error(`⚠️ [Investopedia Crawler] Failed to extract subpages from ${baseUrl}:`, err);
    return [];
  }
}

async function ingestInvestopedia() {
  const targetUrls = process.argv.slice(2);

  if (targetUrls.length === 0) {
    console.log(`🤖 [Ingest] Fetching market intelligence from default Investopedia...`);
    const defaultUrl = 'https://www.investopedia.com/';
    await observeKnowledge(defaultUrl);

    const subpages = await getInvestopediaLinks(defaultUrl);
    console.log(`🤖 [Ingest] Found ${subpages.length} subpages. Observing all subpages...`);

    for (let i = 0; i < subpages.length; i++) {
        const url = subpages[i];
        if (url !== defaultUrl) {
            console.log(`- Observing knowledge from subpage: ${url}`);
            await observeKnowledge(url);
        }
    }
  } else {
    console.log(`🤖 [Ingest] Fetching market intelligence from ${targetUrls.length} URL(s)...`);

    for (const url of targetUrls) {
      console.log(`- Observing knowledge from: ${url}`);
      await observeKnowledge(url);
    }
  }

  console.log('✅ [Ingest] Ingestion complete.');
}

ingestInvestopedia().catch(console.error);
