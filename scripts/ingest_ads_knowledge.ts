import * as fs from 'fs';
import * as path from 'path';
import * as cheerio from 'cheerio';

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

    for (const url of URLS) {
        const parsedUrl = new URL(url);
        parsedUrl.searchParams.set('hl', 'en');
        const fetchUrl = parsedUrl.toString();

        console.log(`Fetching Google Ads docs from ${fetchUrl}...`);
        try {
            const response = await fetch(fetchUrl, { signal: AbortSignal.timeout(10000) });
            if (!response.ok) {
                console.error(`Error fetching ${fetchUrl}: HTTP ${response.status}`);
                continue;
            }

            const html = await response.text();
            const $ = cheerio.load(html);

            const mainContent = $('article').length ? $('article') :
                                $('main').length ? $('main') :
                                $('body');

            if (!mainContent.length) {
                console.warn(`Could not find main content for ${url}`);
                continue;
            }

            const h1 = mainContent.find('h1').first();
            const pageTitle = h1.length ? h1.text().trim() : url;

            const pageData: PageData = {
                title: pageTitle,
                url: url,
                key_links: [],
                sections: []
            };

            mdContent += `## ${pageTitle}\n\n`;
            mdContent += `Source: [${url}](${url})\n\n`;

            let currentSection: Section = {
                heading: pageTitle,
                content: []
            };

            const elements = mainContent.find('h1, h2, h3, p, li, a');

            elements.each((_, elem) => {
                const $elem = $(elem);
                const tagName = elem.name.toLowerCase();

                if (tagName === 'a') {
                    const href = $elem.attr('href');
                    if (href && href.startsWith('http') && !pageData.key_links.includes(href)) {
                        pageData.key_links.push(href);
                    }
                    return;
                }

                const text = $elem.text().replace(/\s+/g, ' ').trim();
                if (!text) {
                    return;
                }

                if (['h1', 'h2', 'h3'].includes(tagName)) {
                    if (currentSection.content.length > 0 || currentSection.heading !== pageTitle) {
                        pageData.sections.push(currentSection);
                    }

                    currentSection = {
                        heading: text,
                        content: []
                    };
                    const mdPrefix = '#'.repeat(parseInt(tagName[1]));
                    mdContent += `${mdPrefix} ${text}\n\n`;
                } else if (tagName === 'p') {
                    mdContent += `${text}\n\n`;
                    currentSection.content.push(text);
                } else if (tagName === 'li') {
                    mdContent += `- ${text}\n`;
                    currentSection.content.push(`- ${text}`);
                }
            });

            if (currentSection.content.length > 0 || currentSection.heading !== pageTitle) {
                pageData.sections.push(currentSection);
            }

            data[url] = pageData;
            mdContent += "\n---\n\n";

        } catch (error) {
             console.error(`Error fetching ${fetchUrl}:`, error);
        }
    }

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

        if (!knowledge.sections) {
            knowledge.sections = {};
        }

        knowledge.sections.google_ads = data;

        if (!knowledge.metadata.sources_processed.includes("google_ads_docs.json")) {
            knowledge.metadata.sources_processed.push("google_ads_docs.json");
        }
        knowledge.metadata.generated_at = new Date().toISOString();

        fs.writeFileSync(knowledgePath, JSON.stringify(knowledge, null, 2), 'utf8');
        console.log(`✅ [Ingest] Merged Google Ads docs into system_knowledge.json.`);
    }
}

scrapeGoogleAdsDocs().catch(console.error);
