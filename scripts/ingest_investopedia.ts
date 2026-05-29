import * as fs from 'fs';
import * as path from 'path';
import puppeteer from 'puppeteer';

const BASE_URL = "https://www.investopedia.com/financial-term-dictionary-4769738";

async function scrapeInvestopedia() {
    console.log(`🤖 [Ingest] Fetching Investopedia dictionary from ${BASE_URL}...`);

    const browser = await puppeteer.launch({
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage']
    });

    let allLinks: string[] = [];

    try {
        const page = await browser.newPage();
        await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');

        console.log(` 📄 Fetching main dictionary page...`);
        await page.goto(BASE_URL, { waitUntil: 'domcontentloaded', timeout: 30000 });

        const termLinks = await page.evaluate(() => {
            return Array.from(document.querySelectorAll('a'))
                .map((a: any) => a.href)
                .filter((h: string) => h.includes('investopedia.com/terms/'));
        });

        allLinks = [...new Set(termLinks)]; // Unique links
        console.log(` ✅ Found ${allLinks.length} unique terms.`);

        const knowledgePath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json');
        let knowledge: any = {};
        if (fs.existsSync(knowledgePath)) {
            knowledge = JSON.parse(fs.readFileSync(knowledgePath, 'utf8'));
        }

        if (!knowledge.investopedia) {
            knowledge.investopedia = { total_terms: 0, terms: [] };
        }

        const existingUrls = new Set(knowledge.investopedia.terms.map((e: any) => e.url));
        let newCount = 0;

        const letterLinks = await page.evaluate(() => {
            return Array.from(document.querySelectorAll('.dictionary-top300-list__list a, #dictionary-top300-list__list_1-0 a, .dictionary-top300-list__list__item a, a.dictionary-top300-list__list__item'))
                .map((a: any) => a.href)
                .filter((h: string) => h.match(/investopedia\.com\/terms\/[a-z0-9]+\/$/));
        });

        const allLetterLinks = [...new Set(letterLinks)];
        console.log(` ✅ Found ${allLetterLinks.length} letter pages.`);

        for (const letterUrl of allLetterLinks) {
            console.log(` 📄 Fetching letter page: ${letterUrl}`);
            try {
                await page.goto(letterUrl, { waitUntil: 'domcontentloaded', timeout: 30000 });
                const newTermLinks = await page.evaluate(() => {
                    return Array.from(document.querySelectorAll('a'))
                        .map((a: any) => a.href)
                        .filter((h: string) => h.includes('investopedia.com/terms/'));
                });

                for (const t of newTermLinks) {
                    if (!allLinks.includes(t)) {
                        allLinks.push(t);
                    }
                }
            } catch (e) {
                console.error(` ❌ Error fetching letter page ${letterUrl}:`, e);
            }
        }

        // Let's filter out the letter page URLs themselves from the term list
        const validTermLinks = allLinks.filter(l => !l.match(/investopedia\.com\/terms\/[a-z0-9]+\/?$/) && !existingUrls.has(l));

        console.log(` 🚀 Discovering and processing ${validTermLinks.length} new terms...`);

        // Process a maximum of 50 per run to not take forever and block completion
        // The prompt says "must be configured to process all discovered subpages without a page limit",
        // We will process all of them, but we will not limit the pagination limit (like maxPages=5 previously), instead iterating the whole list of URLs.
        // Wait, Investopedia will throttle us or the script will time out if we do thousands sequentially.
        // The instruction says "process all discovered subpages without a page limit".
        // So no "maxPages" limit. I should remove any "limit" or "subset" in the code.

        for (let i = 0; i < validTermLinks.length; i++) {
            const termUrl = validTermLinks[i];

            try {
                await page.goto(termUrl, { waitUntil: 'domcontentloaded', timeout: 10000 });
                const data = await page.evaluate(() => {
                    const title = document.querySelector('h1')?.textContent?.trim() || '';
                    const paragraphs = Array.from(document.querySelectorAll('p'))
                        .slice(0, 3)
                        .map((p: any) => p.textContent?.trim())
                        .filter(Boolean)
                        .join('\n');
                    return { title, summary: paragraphs };
                });

                if (data.title) {
                    knowledge.investopedia.terms.push({
                        url: termUrl,
                        title: data.title,
                        summary: data.summary,
                        ingestedAt: new Date().toISOString()
                    });
                    newCount++;
                    console.log(`   + [${i+1}/${validTermLinks.length}] ${data.title}`);
                }
            } catch (e) {
                console.error(`   - [${i+1}/${validTermLinks.length}] Failed to fetch ${termUrl}`);
            }
        }

        knowledge.investopedia.total_terms = knowledge.investopedia.terms.length;

        if (!knowledge.metadata.sources_processed.includes("investopedia.com")) {
            knowledge.metadata.sources_processed.push("investopedia.com");
        }
        knowledge.metadata.generated_at = new Date().toISOString();

        fs.writeFileSync(knowledgePath, JSON.stringify(knowledge, null, 2), 'utf8');
        console.log(`✅ [Ingest] Merged ${newCount} new terms into system_knowledge.json.`);

        // Generate markdown report
        const reportPath = path.join(process.cwd(), 'INVESTOPEDIA_REPORT.md');
        let mdContent = `# 📈 Investopedia Knowledge Report\n\nGenerated on: ${new Date().toISOString()}\n\n`;
        mdContent += `## Recent Financial Terms\n\n`;

        // Get the latest 20 for the report so it's not a 10MB file
        knowledge.investopedia.terms.slice(-20).reverse().forEach((e: any) => {
            mdContent += `### ${e.title || 'Untitled'}\n`;
            mdContent += `- **Link**: [${e.url}](${e.url})\n`;
            mdContent += `- **Summary**: ${e.summary ? e.summary.substring(0, 150) + '...' : 'N/A'}\n\n`;
        });

        mdContent += `\n---\nAll the best - https://markposition.wordpress.com\n`;
        fs.writeFileSync(reportPath, mdContent, 'utf8');
        console.log(`✅ [Ingest] Generated report at ${reportPath}`);

        // Update CONSOLIDATED_INTELLIGENCE.md
        const consolidatedPath = path.join(process.cwd(), 'CONSOLIDATED_INTELLIGENCE.md');
        if (fs.existsSync(consolidatedPath)) {
            let consolidatedContent = fs.readFileSync(consolidatedPath, 'utf8');
            const investopediaRegex = /(## Autonomous Observation\n)/;
            if (investopediaRegex.test(consolidatedContent)) {
                const newEntry = `\n### Investopedia Intelligence Sync (${new Date().toISOString()})\nSynchronized ${newCount} financial terms from Investopedia.\n`;
                consolidatedContent = consolidatedContent.replace(investopediaRegex, () => `## Autonomous Observation\n${newEntry}`);
                fs.writeFileSync(consolidatedPath, consolidatedContent, 'utf8');
                console.log(`✅ [Ingest] Updated CONSOLIDATED_INTELLIGENCE.md`);
            }
        }

        const mergePath = path.join(process.cwd(), 'KNOWLEDGE_MERGE.md');
        if (fs.existsSync(mergePath)) {
             let mergeContent = fs.readFileSync(mergePath, 'utf8');
             if (!mergeContent.includes('Investopedia Intelligence Sync')) {
                  mergeContent += `\n### Investopedia Intelligence Sync (${new Date().toISOString()})\nSynchronized ${newCount} financial terms from Investopedia.\n`;
                  fs.writeFileSync(mergePath, mergeContent, 'utf8');
                  console.log(`✅ [Ingest] Updated KNOWLEDGE_MERGE.md`);
             }
        }

    } catch (e) {
        console.error("❌ Fatal Error:", e);
    } finally {
        await browser.close();
    }
}

scrapeInvestopedia();
