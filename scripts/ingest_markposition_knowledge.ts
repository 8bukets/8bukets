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

async function scrapeMarkpositionKnowledge() {
    console.log(`🤖 [Ingest] Fetching market intelligence from ${BASE_URL}...`);
    try {
        const response = await fetch(BASE_URL, { signal: AbortSignal.timeout(20000) });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const html = await response.text();
        const $ = cheerio.load(html);

        const entries: MarketEntry[] = [];

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

            entries.push({
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

        console.log(`✅ [Ingest] Parsed ${entries.length} entries.`);

        // Update system_knowledge.json
        const knowledgePath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json');
        if (fs.existsSync(knowledgePath)) {
            const knowledge = JSON.parse(fs.readFileSync(knowledgePath, 'utf8'));

            if (!knowledge.market_data) {
                knowledge.market_data = { total_entries: 0, recent_entries: [], all_entries: [] };
            }

            // Merge logic: avoid duplicates based on post_url
            const existingUrls = new Set(knowledge.market_data.all_entries.map((e: any) => e.post_url));
            const newEntries = entries.filter(e => !existingUrls.has(e.post_url));

            if (newEntries.length > 0) {
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

        entries.slice(0, 10).forEach(e => {
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
