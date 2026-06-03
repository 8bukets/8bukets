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

async function scrapeGoogleBlog(url: string): Promise<Article[]> {
    console.log(`🤖 [Ingest] Fetching ${url}...`);
    try {
        const response = await fetch(url, { signal: AbortSignal.timeout(20000) });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const html = await response.text();
        const $ = cheerio.load(html);

        const articleMap = new Map<string, Article>();

        $('a').each((_, el) => {
            const href = $(el).attr('href');
            if (!href) return;

            const fullUrl = href.startsWith('http') ? href : `https://blog.google${href}`;

            // Validation: Must be an article-like URL
            const isArticleUrl = fullUrl.includes('/innovation-and-ai/') &&
                                !fullUrl.endsWith('/innovation-and-ai/') &&
                                !fullUrl.endsWith('/models-and-research/') &&
                                !fullUrl.endsWith('/google-deepmind/') &&
                                !fullUrl.endsWith('/google-research/') &&
                                !fullUrl.endsWith('/google-labs/') &&
                                !fullUrl.endsWith('/gemini-models/') &&
                                !fullUrl.endsWith('/quantum-computing/') &&
                                !fullUrl.endsWith('/developers-tools/') &&
                                !fullUrl.endsWith('/global-network/') &&
                                !fullUrl.endsWith('/google-cloud/') &&
                                !fullUrl.endsWith('/safety-security/') &&
                                !fullUrl.endsWith('/products/') &&
                                !fullUrl.endsWith('/technology/') &&
                                !fullUrl.endsWith('/health/') &&
                                !fullUrl.endsWith('/infrastructure-and-cloud/') &&
                                !fullUrl.includes('/authors/') &&
                                !fullUrl.includes('shareArticle');

            if (!isArticleUrl) return;

            // Target GA4 analytics data which contains reliable titles
            const gaDataAttr = $(el).attr('data-ga4-analytics-lead-click');
            let gaTitle = "";
            if (gaDataAttr) {
                try {
                    const gaData = JSON.parse(gaDataAttr);
                    if (gaData.article_name) {
                        gaTitle = gaData.article_name;
                    }
                } catch (e) {}
            }

            // Target specific title classes
            const heroTitle = $(el).find('.featured-article-cat-subcat-hero__title').text().trim();
            const nupTitle = $(el).find('.uni-nup__header').text().trim();
            const directTitle = $(el).text().trim();

            const title = gaTitle || heroTitle || nupTitle || directTitle;
            const isNotNav = !['Home', 'Innovation & AI', 'Products & platforms', 'Company news', 'Feed', 'Subscribe', 'See all'].includes(title);

            if (title && title.length > 10 && isNotNav) {
                let snippet = "";

                // Try finding snippet inside the link (Hero case)
                const heroSummary = $(el).find('.featured-article-cat-subcat-hero__summary').text().trim();
                const generalSnippet = $(el).find('[class*="summary"], [class*="snippet"], [class*="description"], [class*="deck"]').text().trim();

                snippet = heroSummary || generalSnippet;

                // Try finding snippet in parent or siblings
                if (!snippet) {
                    const parent = $(el).closest('div, section, li, article');
                    const summaryTag = parent.find('[class*="summary"], [class*="snippet"], [class*="description"], [class*="deck"]').first();
                    if (summaryTag.length) {
                        snippet = summaryTag.text().trim();
                    }
                }

                if (!snippet) {
                    const siblingP = $(el).nextAll('p').first();
                    if (siblingP.length && siblingP.text().trim().length > 30) {
                        snippet = siblingP.text().trim();
                    }
                }

                const existing = articleMap.get(fullUrl);
                if (!existing || (!existing.snippet && snippet) || (existing.title.length < title.length)) {
                    articleMap.set(fullUrl, {
                        title: title || (existing ? existing.title : ""),
                        url: fullUrl,
                        snippet: snippet || (existing ? existing.snippet : "")
                    });
                }
            }
        });
        return Array.from(articleMap.values());
    } catch (error) {
        console.error(`❌ [Ingest] Error fetching URL ${url}:`, error);
        return [];
    }
}

async function main() {
    const researchArticles = await scrapeGoogleBlog(MODELS_RESEARCH_URL);
    const innovationArticles = await scrapeGoogleBlog(INNOVATION_URL);

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
        const existing = uniqueMap.get(art.url);
        if (!existing || (!existing.snippet && art.snippet)) {
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
