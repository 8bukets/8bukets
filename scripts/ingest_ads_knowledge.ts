import * as fs from 'fs';
import * as path from 'path';
import * as cheerio from 'cheerio';
import puppeteer from 'puppeteer';

const URLS = [
    "https://support.google.com/google-ads/answer/2459326?hl=en&ref_topic=10289453&sjid=5167206403107665975-EU",
    "https://business.google.com/uk/ad-tools/bidding/?hl=en",
    "https://business.google.com/uk/resources/?hl=en",
    "https://developers.google.com/ad-manager?hl=en",
    "https://developers.google.com/ad-manager/dynamic-ad-insertion?hl=en",
    "https://developers.google.com/ad-manager/dynamic-ad-insertion/full-service?hl=en",
    "https://developers.google.com/ad-manager/dynamic-ad-insertion/pod-serving?hl=en",
    "https://developers.google.com/ad-manager/api/start?hl=en",
    "https://admanager.google.com/home/resources/?hl=en",
    "https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/overview?hl=en"
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
        console.log(`Fetching Google Ads docs from ${url}...`);
        try {
            const page = await browser.newPage();
            await page.goto(url, { waitUntil: 'networkidle2', timeout: 30000 });
            const html = await page.content();
            await page.close();

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
             console.error(`Error fetching ${url}:`, error);
        }
    }

    await browser.close();

    const jsonPath = "data/knowledge/google_ads_docs.json";
    fs.writeFileSync(jsonPath, JSON.stringify(data, null, 4), 'utf-8');
    console.log(`Saved Google Ads docs JSON to ${jsonPath}`);

    const mdPath = "data/knowledge/google_ads_docs.md";
    fs.writeFileSync(mdPath, mdContent, 'utf-8');
    console.log(`Saved Google Ads docs Markdown to ${mdPath}`);

    const systemKnowledgePath = "data/knowledge/system_knowledge.json";
    if (fs.existsSync(systemKnowledgePath)) {
        try {
            const systemKnowledgeContent = fs.readFileSync(systemKnowledgePath, 'utf-8');
            const systemKnowledge = JSON.parse(systemKnowledgeContent);

            const newEntry = {
                sections: [],
                metadata: {
                    source: "local://google_ads_docs.md",
                    ingestedAt: new Date().toISOString()
                }
            };

            // Populate sections from our parsed data
            for (const key of Object.keys(data)) {
                const pageData = data[key];
                for (const section of pageData.sections) {
                    newEntry.sections.push({
                        header: section.heading,
                        content: section.content.join('\n')
                    });
                }
            }

            systemKnowledge["Google Ads Strategic Documentation"] = newEntry;

            fs.writeFileSync(systemKnowledgePath, JSON.stringify(systemKnowledge, null, 2), 'utf-8');
            console.log(`Updated system knowledge in ${systemKnowledgePath}`);
        } catch (error) {
            console.error(`Error updating system knowledge:`, error);
        }
    }
}

scrapeGoogleAdsDocs().catch(console.error);
