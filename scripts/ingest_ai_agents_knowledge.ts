import * as fs from 'fs';
import * as path from 'path';
import * as cheerio from 'cheerio';

const URL = "https://cloud.google.com/discover/what-are-ai-agents";

interface Section {
    title: string;
    content: string;
}

async function scrapeAiAgentsKnowledge() {
    console.log(`Fetching AI Agent knowledge from ${URL}...`);
    try {
        const response = await fetch(URL, { signal: AbortSignal.timeout(20000) });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const html = await response.text();
        const $ = cheerio.load(html);

        const data: Record<string, Section> = {};
        const orderedScrapedKeys: string[] = [];

        const stopMarkers = [
            "Additional resources", "Take the next step", "Continue browsing",
            "Why Google", "Products and pricing", "Solutions", "Resources", "Engage"
        ];

        const skipTitles = [
            "Stay informed", "Topics", "Page Contents",
            "arrow_forward", "Key benefits", "Reports and insights",
            "Industry Solutions", "Featured Products", "Business Intelligence",
            "Compute", "Containers", "Data Analytics", "Databases",
            "Developer Tools", "Distributed Cloud", "Hybrid and Multicloud",
            "Industry Specific", "Integration Services", "Management Tools",
            "Maps and Geospatial", "Media Services", "Migration",
            "Networking", "Operations", "Productivity and Collaboration",
            "Security and Identity", "Serverless", "Storage", "Web3",
            "Save money with our transparent approach to pricing",
            "Pricing overview and tools", "Product-specific Pricing",
            "Learn & build", "Connect", "Consulting and Partners",
            "Overview", "Products", "Pricing", "Docs", "Support", "Console",
            "Contact us", "Start free", "Sign in", "Language"
        ];

        const main = $('main, article, [role="main"]').first();
        const scope = main.length ? main : $('body');

        let currentSectionId = '';
        let currentSectionTitle = '';
        let currentContent: string[] = [];
        let stopScraping = false;

        const finalizeSection = () => {
            if (currentSectionId && currentContent.length > 0) {
                const filteredContent = currentContent.filter(line => {
                    const trimmed = line.trim();
                    if (!trimmed) return false;
                    if (skipTitles.some(skip => trimmed === skip || (trimmed.length < 50 && trimmed.includes(skip)))) return false;
                    if (stopMarkers.some(stop => trimmed === stop || trimmed.includes(stop))) return false;
                    return true;
                });

                if (filteredContent.length > 0) {
                    // Deduplicate within the section content (e.g. if table data is repeated as text)
                    const uniqueLines: string[] = [];
                    const seenLines = new Set<string>();
                    for (const line of filteredContent) {
                        const normalized = line.trim().toLowerCase();
                        if (!seenLines.has(normalized)) {
                            uniqueLines.push(line);
                            seenLines.add(normalized);
                        }
                    }

                    data[currentSectionId] = {
                        title: currentSectionTitle,
                        content: uniqueLines.join('\n\n')
                    };
                    if (!orderedScrapedKeys.includes(currentSectionId)) {
                        orderedScrapedKeys.push(currentSectionId);
                    }
                }
            }
        };

        scope.find('h1, h2, h3, h4, h5, h6, p, ul, ol, table, pre').each((_, el) => {
            if (stopScraping) return;

            const $el = $(el);
            const tagName = el.name.toLowerCase();

            if (['h1', 'h2', 'h3', 'h4', 'h5', 'h6'].includes(tagName)) {
                const title = $el.text().trim();
                if (!title) return;

                if (stopMarkers.some(stop => title === stop || title.includes(stop))) {
                    finalizeSection();
                    stopScraping = true;
                    return;
                }

                finalizeSection();

                if (skipTitles.some(skip => title === skip || title.includes(skip))) {
                    currentSectionId = '';
                    currentSectionTitle = '';
                    currentContent = [];
                    return;
                }

                currentSectionTitle = title;
                currentSectionId = $el.attr('id') || title.toLowerCase().replace(/\s+/g, '-').replace(/[?,]/g, '');
                currentContent = [];
            } else if (currentSectionId) {
                if (tagName === 'p') {
                    const text = $el.text().replace(/\s+/g, ' ').trim();
                    if (text && text.length > 1) currentContent.push(text);
                } else if (tagName === 'ul' || tagName === 'ol') {
                    const items: string[] = [];
                    $el.find('> li').each((_, li) => {
                        const $li = $(li);
                        // Ensure spaces between elements within the li to prevent word concatenation
                        let liText = $li.contents().map((_, node) => {
                            const $node = $(node);
                            return node.type === 'text' ? $node.text() : ` ${$node.text()} `;
                        }).get().join('').replace(/\s+/g, ' ').trim();

                        if (liText) {
                            // Specifically fix known concatenations if they still occur or for better formatting
                            liText = liText.replace(/([a-z])([A-Z])/g, '$1 $2'); // Basic camelCase split for likely joined words
                            items.push(`- ${liText}`);
                        }
                    });
                    if (items.length > 0) currentContent.push(items.join('\n'));
                } else if (tagName === 'table') {
                    const rows: string[] = [];
                    let headerCount = 0;
                    $el.find('tr').each((_, tr) => {
                        const cells: string[] = [];
                        $(tr).find('th, td').each((_, cell) => {
                            cells.push($(cell).text().replace(/\s+/g, ' ').trim());
                        });
                        if (cells.length > 0) {
                            rows.push(cells.join(' | '));
                            if (headerCount === 0) headerCount = cells.length;
                        }
                    });
                    if (rows.length > 0) {
                        if (headerCount > 1) {
                            const separator = Array(headerCount).fill('---').join(' | ');
                            rows.splice(1, 0, separator);
                        }
                        currentContent.push(rows.join('\n'));
                    }
                } else if (tagName === 'pre') {
                    const text = $el.text().trim();
                    if (text) currentContent.push(`\`\`\`\n${text}\n\`\`\``);
                }
            }
        });

        finalizeSection();

        const targetDir = "data/knowledge";
        if (!fs.existsSync(targetDir)) {
            fs.mkdirSync(targetDir, { recursive: true });
        }
        const jsonPath = path.join(targetDir, "ai_agents_knowledge.json");
        fs.writeFileSync(jsonPath, JSON.stringify(data, null, 2), 'utf8');

        const mdPath = "ai_agents_knowledge.md";
        let mdContent = `# What are AI Agents?\n\nScraped from [${URL}](${URL})\n\n`;

        for (const key of orderedScrapedKeys) {
            if (data[key]) {
                mdContent += `## ${data[key].title}\n\n${data[key].content}\n\n`;
            }
        }

        fs.writeFileSync(mdPath, mdContent, 'utf8');
        console.log(`Updated knowledge files successfully.`);

        return true;
    } catch (error) {
        console.error("Failed to scrape AI Agent knowledge:", error);
        return false;
    }
}

scrapeAiAgentsKnowledge();
