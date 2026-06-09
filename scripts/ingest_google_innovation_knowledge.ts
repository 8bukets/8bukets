import * as fs from 'fs';
import * as path from 'path';
import * as cheerio from 'cheerio';

const INNOVATION_URL = "https://blog.google/innovation-and-ai/";
const MODELS_RESEARCH_URL = "https://blog.google/innovation-and-ai/models-and-research/";

interface Article {
    title: string;
    url: string;
    snippet: string;
    content?: string;
}

async function scrapeArticleContent(url: string): Promise<string> {
    console.log(`   📄 [Content] Fetching article content from ${url}...`);
    try {
        const response = await fetch(url, { signal: AbortSignal.timeout(15000) });
        if (!response.ok) return "";
        const html = await response.text();
        const $ = cheerio.load(html);

        // Try to find the main content
        const articleBody = $('.article-post__content, .uni-article__body, .rich-text').text().trim();
        if (articleBody) {
            // Get first 500 characters as a meaningful summary
            return articleBody.substring(0, 1000).replace(/\s+/g, ' ') + "...";
        }
        return "";
    } catch (e) {
        return "";
    }
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

        const links = $('a').toArray();
        for (const el of links) {
            const href = $(el).attr('href');
            if (!href) continue;

            const fullUrl = href.startsWith('http') ? href : `https://blog.google${href}`;

            // Validation: Must be an article-like URL
            const isArticleUrl = fullUrl.includes('/innovation-and-ai/') &&
                                !fullUrl.endsWith('/innovation-and-ai/') &&
                                !fullUrl.endsWith('/models-and-research/') &&
                                !fullUrl.includes('/authors/') &&
                                !fullUrl.includes('shareArticle');

            if (!isArticleUrl) continue;

            // Target specific title classes
            const heroTitle = $(el).find('.featured-article-cat-subcat-hero__title').text().trim();
            const nupTitle = $(el).find('.uni-nup__header').text().trim();
            const directTitle = $(el).text().trim();

            const title = heroTitle || nupTitle || directTitle;
            const isNotNav = !['Home', 'Innovation & AI', 'Products & platforms', 'Company news', 'Feed', 'Subscribe', 'See all'].includes(title);

            if (title && title.length > 10 && isNotNav && !articleMap.has(fullUrl)) {
                articleMap.set(fullUrl, {
                    title,
                    url: fullUrl,
                    snippet: ""
                });
            }
        }

        const articles = Array.from(articleMap.values()).slice(0, 20); // Expanded limit for deeper ingestion
        for (const art of articles) {
            art.content = await scrapeArticleContent(art.url);
        }

        return articles;
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
        } catch (e) {}
    }

    const uniqueMap = new Map<string, Article>();
    [...allArticles, ...existingArticles].forEach(art => {
        const existing = uniqueMap.get(art.url);
        if (!existing || (!existing.content && art.content)) {
            uniqueMap.set(art.url, art);
        }
    });
    const finalArticles = Array.from(uniqueMap.values());

    // Save to JSON
    fs.writeFileSync(jsonPath, JSON.stringify(finalArticles, null, 4), 'utf8');
    console.log(`✅ [Ingest] Saved JSON data to ${jsonPath}`);

    // Save to Markdown
    const mdPath = path.join(process.cwd(), 'google_innovation_ai_report.md');
    let mdContent = `# Google Innovation & AI Blog Updates\n\n`;
    mdContent += `Scraped from [${INNOVATION_URL}](${INNOVATION_URL}) and [${MODELS_RESEARCH_URL}](${MODELS_RESEARCH_URL})\n\n`;

    finalArticles.forEach(article => {
        mdContent += `### ${article.title}\n`;
        mdContent += `- URL: ${article.url}\n`;
        if (article.content) {
            mdContent += `- Insight: ${article.content}\n`;
        }
        mdContent += `\n`;
    });

    mdContent += `\nAll the best - https://markposition.wordpress.com\n`;
    fs.writeFileSync(mdPath, mdContent, 'utf8');
    console.log(`✅ [Ingest] Saved Markdown report to ${mdPath}`);
}

main().catch(console.error);
