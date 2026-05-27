import * as fs from 'fs';
import * as path from 'path';
import puppeteer from 'puppeteer';

const URLS = [
    "https://support.google.com/google-ads/answer/2459326?hl=en&ref_topic=10289453&sjid=5167206403107665975-EU",
    "https://business.google.com/uk/ad-tools/bidding/",
    "https://business.google.com/uk/resources/",
    "https://developers.google.com/ad-manager",
    "https://developers.google.com/ad-manager/dynamic-ad-insertion",
    "https://developers.google.com/ad-manager/dynamic-ad-insertion/full-service",
    "https://developers.google.com/ad-manager/dynamic-ad-insertion/pod-serving",
    "https://developers.google.com/ad-manager/api/start",
    "https://admanager.google.com/home/resources/",
    "https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/overview"
];

interface Section {
    heading: string;
    content: string[];
}

interface PageData {
    title: string;
    url: string;
    key_links: string[];
    sections: Section[];
}

async function scrapeGoogleAdsDocs() {
    const data: Record<string, PageData> = {};
    let mdContent = "# Google Ads & Ad Manager Documentation\n\n";

    const browser = await puppeteer.launch({ headless: true, args: ['--no-sandbox'] });

    for (const url of URLS) {
        const parsedUrl = new URL(url);
        parsedUrl.searchParams.set('hl', 'en');
        const fetchUrl = parsedUrl.toString();

        console.log(`Fetching Google Ads docs from ${fetchUrl}...`);
        try {
            const page = await browser.newPage();
            // Network idle is better for SPAs/JS-heavy pages
            await page.goto(fetchUrl, { waitUntil: 'networkidle2', timeout: 30000 });

            // Extract the data using evaluation within the page context
            const result = await page.evaluate(() => {
                // Find main content area (heuristics)
                let main = document.querySelector('article') ||
                           document.querySelector('main') ||
                           document.querySelector('.devsite-article-body') ||
                           document.querySelector('body');

                if (!main) return null;

                const titleEl = document.querySelector('h1');
                const title = titleEl ? titleEl.innerText.trim() : document.title;

                const extractedSections: {heading: string, content: string[]}[] = [];

                // Get all links globally within main
                const links: string[] = Array.from(main.querySelectorAll('a'))
                    .map(el => (el as HTMLAnchorElement).href)
                    .filter(href => href && href.startsWith('http'));

                // Deduplicate links
                const uniqueLinks = [...new Set(links)];

                let currentSection = { heading: title, content: [] as string[] };

                // Get all relevant elements for text content
                const elements = main.querySelectorAll('h1, h2, h3, h4, p, li');

                elements.forEach(el => {
                    const tag = el.tagName.toLowerCase();
                    const text = (el as HTMLElement).innerText?.replace(/\s+/g, ' ').trim();

                    if (!text) return;

                    if (tag.match(/^h[1-4]$/)) {
                        if (currentSection.content.length > 0 || currentSection.heading !== title) {
                            extractedSections.push({...currentSection});
                        }
                        currentSection = { heading: text, content: [] };
                    } else if (tag === 'p' || tag === 'li') {
                        currentSection.content.push(tag === 'li' ? `- ${text}` : text);
                    }
                });

                if (currentSection.content.length > 0 || currentSection.heading !== title) {
                    extractedSections.push(currentSection);
                }

                return {
                    title,
                    sections: extractedSections,
                    links: uniqueLinks
                };
            });

            await page.close();

            if (!result) {
                console.warn(`Could not extract content for ${url}`);
                continue;
            }

            const pageData: PageData = {
                title: result.title,
                url: url,
                key_links: result.links,
                sections: result.sections
            };

            mdContent += `## ${result.title}\n\n`;
            mdContent += `Source: [${url}](${url})\n\n`;

            result.sections.forEach((section: any) => {
                if (section.heading !== result.title) {
                    mdContent += `### ${section.heading}\n\n`;
                }
                section.content.forEach((text: string) => {
                    mdContent += `${text}\n\n`;
                });
            });

            data[url] = pageData;
            mdContent += "\n---\n\n";

        } catch (error) {
             console.error(`Error fetching ${fetchUrl}:`, error);
        }
    }

    await browser.close();

    const jsonPath = "data/knowledge/google_ads_docs.json";
    fs.writeFileSync(jsonPath, JSON.stringify(data, null, 4), 'utf-8');
    console.log(`Saved Google Ads docs JSON to ${jsonPath}`);

    const mdPath = "data/knowledge/google_ads_docs.md";
    fs.writeFileSync(mdPath, mdContent, 'utf-8');
    console.log(`Saved Google Ads docs Markdown to ${mdPath}`);

    // Update system_knowledge.json
    const knowledgePath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json');
    if (fs.existsSync(knowledgePath)) {
        const knowledge = JSON.parse(fs.readFileSync(knowledgePath, 'utf8'));

        // Flattening check during ingest
        if (knowledge.sections && knowledge.sections.google_ads) {
            console.log("📦 [Ingest] Migrating nested google_ads to flat structure...");
            knowledge.google_ads = knowledge.sections.google_ads;
            delete knowledge.sections.google_ads;
            if (Object.keys(knowledge.sections).length === 0) delete knowledge.sections;
        }

        knowledge.google_ads = data;

        if (!knowledge.metadata.sources_processed.includes("google_ads_docs.json")) {
            knowledge.metadata.sources_processed.push("google_ads_docs.json");
        }
        knowledge.metadata.generated_at = new Date().toISOString();

        fs.writeFileSync(knowledgePath, JSON.stringify(knowledge, null, 4), 'utf8');
        console.log(`✅ [Ingest] Merged Google Ads docs into system_knowledge.json.`);
    }
}

scrapeGoogleAdsDocs().catch(console.error);
