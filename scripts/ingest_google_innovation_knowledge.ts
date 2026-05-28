import * as fs from 'fs';
import * as path from 'path';
import * as cheerio from 'cheerio';

const INNOVATION_URL = "https://blog.google/innovation-and-ai/";
const MODELS_RESEARCH_URL = "https://blog.google/innovation-and-ai/models-and-research/";

interface Article {
    title: string;
    url: string;
    snippet: string;
}

async function scrapeGoogleBlog(url: string, categoryPath: string): Promise<Article[]> {
    console.log(`🤖 [Ingest] Fetching ${url}...`);
    try {
        const response = await fetch(url, { signal: AbortSignal.timeout(20000) });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const html = await response.text();
        const $ = cheerio.load(html);

        const articles: Article[] = [];
        const seenUrls = new Set<string>();

        $('a').each((_, el) => {
            const href = $(el).attr('href');
            if (href && href.includes(categoryPath) && href !== url && !href.endsWith(categoryPath)) {
                const fullUrl = href.startsWith('http') ? href : `https://blog.google${href}`;
                if (!seenUrls.has(fullUrl)) {
                    const title = $(el).text().trim();
                    if (title && title.length > 5 && !title.startsWith('http')) {
                        let snippet = "";
                        const parent = $(el).closest('div, section, li, article');
                        if (parent.length) {
                            const summaryTag = parent.find('p, span, div').filter((_, tag) => {
                                const cls = $(tag).attr('class');
                                return !!(cls && (cls.toLowerCase().includes('summary') ||
                                          cls.toLowerCase().includes('description') ||
                                          cls.toLowerCase().includes('snippet') ||
                                          cls.toLowerCase().includes('deck')));
                            });
                            if (summaryTag.length) {
                                snippet = summaryTag.text().trim();
                            }
                        }

                        articles.push({
                            title,
                            url: fullUrl,
                            snippet
                        });
                        seenUrls.add(fullUrl);
                    }
                }
            }
        });
        return articles;
    } catch (error) {
        console.error(`❌ [Ingest] Error fetching URL ${url}:`, error);
        return [];
    }
}

async function main() {
    const researchArticles = await scrapeGoogleBlog(MODELS_RESEARCH_URL, "/innovation-and-ai/models-and-research/");
    const innovationArticles = await scrapeGoogleBlog(INNOVATION_URL, "/innovation-and-ai/");

    const allArticles = [...researchArticles, ...innovationArticles];

    // Deduplicate and merge with existing
    const jsonPath = path.join(process.cwd(), 'data/google_innovation_ai.json');
    let existingArticles: Article[] = [];
    if (fs.existsSync(jsonPath)) {
        try {
            existingArticles = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
        } catch (e) {
            console.warn('⚠️ [Ingest] Failed to read existing JSON.');
        }
    }

    const combined = [...allArticles, ...existingArticles];
    const uniqueMap = new Map<string, Article>();
    combined.forEach(art => {
        if (!uniqueMap.has(art.url)) {
            uniqueMap.set(art.url, art);
        }
    });
    const finalArticles = Array.from(uniqueMap.values());

    // Save to JSON
    const dataDir = path.dirname(jsonPath);
    if (!fs.existsSync(dataDir)) fs.mkdirSync(dataDir, { recursive: true });
    fs.writeFileSync(jsonPath, JSON.stringify(finalArticles, null, 4), 'utf8');
    console.log(`✅ [Ingest] Saved JSON data to ${jsonPath}`);

    // Save to Markdown
    const mdPath = path.join(process.cwd(), 'google_innovation_ai_report.md');
    let mdContent = `# Google Innovation & AI Blog Updates\n\n`;
    mdContent += `Scraped from [${INNOVATION_URL}](${INNOVATION_URL}) and [${MODELS_RESEARCH_URL}](${MODELS_RESEARCH_URL})\n\n`;

    if (finalArticles.length === 0) {
        mdContent += "No recent articles found.\n";
    } else {
        finalArticles.forEach(article => {
            mdContent += `### ${article.title}\n`;
            mdContent += `- URL: ${article.url}\n`;
            if (article.snippet) {
                mdContent += `- Summary: ${article.snippet}\n`;
            }
            mdContent += `\n`;
        });
    }

    mdContent += `\nAll the best - https://markposition.wordpress.com\n`;
    fs.writeFileSync(mdPath, mdContent, 'utf8');
    console.log(`✅ [Ingest] Saved Markdown report to ${mdPath}`);
}

main().catch(console.error);
