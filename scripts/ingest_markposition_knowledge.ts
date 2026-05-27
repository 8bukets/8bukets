import * as fs from 'fs';
import * as path from 'path';
import * as cheerio from 'cheerio';

const BASE_URL = "https://markposition.wordpress.com/";

interface MarketEntry {
    title: string;
    date: string;
    datetime: string;
    author: string;
    categories: string[];
    external_link: string | null;
    domain: string | null;
    post_url: string;
}

async function scrapeMarkpositionKnowledge(maxPages: number = 3) {
    console.log(`🤖 [Ingest] Fetching market intelligence from ${BASE_URL} (max ${maxPages} pages)...`);
    try {
        const allEntries: MarketEntry[] = [];

        for (let page = 1; page <= maxPages; page++) {
            const url = page === 1 ? BASE_URL : `${BASE_URL}page/${page}/`;
            console.log(` - Scraping page ${page}: ${url}`);

            const response = await fetch(url, { signal: AbortSignal.timeout(20000) });
            if (!response.ok) {
                if (response.status === 404) {
                    console.log(` ✨ [Ingest] Page ${page} not found. Ending pagination.`);
                    break;
                }
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const html = await response.text();
            const $ = cheerio.load(html);

            const pageEntries: MarketEntry[] = [];

            $('article.post').each((_, el) => {
            const $el = $(el);
            const titleHeader = $el.find('h1.entry-title');
            const titleTag = titleHeader.find('a');
            const title = titleTag.text().trim();
            const post_url = titleTag.attr('href') || '';

            const dateTag = $el.find('time.entry-date');
            const date = dateTag.text().trim();
            const datetime = dateTag.attr('datetime') || '';

            const authorTag = $el.find('.author .fn');
            const author = authorTag.text().trim() || 'Filip Keser';

            const categories: string[] = [];
            const classAttr = $el.attr('class') || '';
            classAttr.split(' ').forEach(cls => {
                if (cls.startsWith('category-')) {
                    categories.push(cls.replace('category-', '').replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase()));
                }
            });

            let external_link: string | null = null;
            const contentDiv = $el.find('.entry-content');
            const linkTag = contentDiv.find('a');
            if (linkTag.length) {
                external_link = linkTag.attr('href') || null;
            }

            if (!external_link) {
                const iframeTag = contentDiv.find('iframe');
                if (iframeTag.length) {
                    external_link = iframeTag.attr('src') || null;
                }
            }

            let domain: string | null = null;
            if (external_link) {
                try {
                    domain = new URL(external_link).hostname.replace('www.', '');
                } catch (e) {}
            }

                pageEntries.push({
                    title,
                    date,
                    datetime,
                    author,
                    categories,
                    external_link,
                    domain,
                    post_url
                });
            });

            if (pageEntries.length === 0) {
                console.log(` ✨ [Ingest] No entries found on page ${page}. Ending pagination.`);
                break;
            }

            allEntries.push(...pageEntries);
            console.log(` ✅ [Ingest] Parsed ${pageEntries.length} entries from page ${page}.`);

            // Avoid rate limiting
            if (page < maxPages) await new Promise(resolve => setTimeout(resolve, 500));
        }

        console.log(`✅ [Ingest] Total entries parsed: ${allEntries.length}`);

        // Update system_knowledge.json
        const knowledgePath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json');
        if (fs.existsSync(knowledgePath)) {
            const knowledge = JSON.parse(fs.readFileSync(knowledgePath, 'utf8'));

            if (!knowledge.market_data) {
                knowledge.market_data = { total_entries: 0, recent_entries: [], all_entries: [] };
            }

            // Merge logic: avoid duplicates based on post_url
            const existingUrls = new Set(knowledge.market_data.all_entries.map((e: any) => e.post_url));
            const newEntries = allEntries.filter(e => !existingUrls.has(e.post_url));

            if (newEntries.length > 0) {
                // Flattening check during ingest
                if (knowledge.sections && knowledge.sections.market_data) {
                    console.log("📦 [Ingest] Migrating nested market_data to flat structure...");
                    knowledge.market_data = knowledge.sections.market_data;
                    delete knowledge.sections.market_data;
                    if (Object.keys(knowledge.sections).length === 0) delete knowledge.sections;
                }

                knowledge.market_data.all_entries = [...newEntries, ...knowledge.market_data.all_entries];
                knowledge.market_data.recent_entries = knowledge.market_data.all_entries.slice(0, 20);
                knowledge.market_data.total_entries = knowledge.market_data.all_entries.length;

                if (!knowledge.metadata.sources_processed.includes("markposition.wordpress.com")) {
                    knowledge.metadata.sources_processed.push("markposition.wordpress.com");
                }
                knowledge.metadata.generated_at = new Date().toISOString();

                fs.writeFileSync(knowledgePath, JSON.stringify(knowledge, null, 4), 'utf8');
                console.log(`✅ [Ingest] Merged ${newEntries.length} new entries into system_knowledge.json.`);
            } else {
                console.log(`✨ [Ingest] No new entries found.`);
            }
        }

        // Generate a quick Markdown report
        const reportPath = path.join(process.cwd(), 'MARKPOSITION_REPORT.md');
        let mdContent = `# 📈 Markposition Intelligence Report\n\nGenerated on: ${new Date().toISOString()}\n\n`;
        mdContent += `## Recent Market Intelligence\n\n`;

        allEntries.slice(0, 20).forEach(e => {
            mdContent += `### ${e.title}\n`;
            mdContent += `- **Date**: ${e.date}\n`;
            mdContent += `- **Domain**: ${e.domain || 'N/A'}\n`;
            mdContent += `- **Link**: [${e.external_link || 'Post Link'}](${e.external_link || e.post_url})\n\n`;
        });

        mdContent += `\n---\nAll the best - https://markposition.wordpress.com\n`;
        fs.writeFileSync(reportPath, mdContent, 'utf8');
        console.log(`✅ [Ingest] Generated report at ${reportPath}`);

    } catch (error) {
        console.error(`❌ [Ingest] Failed to ingest Markposition knowledge:`, error);
    }
}

scrapeMarkpositionKnowledge();
