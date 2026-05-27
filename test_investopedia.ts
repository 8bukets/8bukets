import puppeteer from 'puppeteer-extra';
import StealthPlugin from 'puppeteer-extra-plugin-stealth';
import * as cheerio from 'cheerio';

puppeteer.use(StealthPlugin());

async function test() {
    const browser = await puppeteer.launch({
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    const page = await browser.newPage();
    await page.goto('https://www.investopedia.com/', { waitUntil: 'domcontentloaded' });
    const html = await page.content();
    await browser.close();

    const $ = cheerio.load(html);
    const links: string[] = [];
    $('a').each((i, el) => {
        const href = $(el).attr('href');
        if (href && href.startsWith('https://www.investopedia.com/')) {
            links.push(href);
        }
    });
    console.log("Found links:", Array.from(new Set(links)).slice(0, 10));
}
test().catch(console.error);
