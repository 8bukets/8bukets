import * as fs from 'fs';
import * as fsPromises from 'fs/promises';
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

                    // Special case for portfolio items to ensure they are joined by newline but listed nicely
                    const contentStr = currentSectionTitle.includes("portfolio") || currentSectionTitle.includes("Google Cloud and AI agents")
                        ? uniqueLines.join('\n')
                        : uniqueLines.join('\n\n');

                    data[currentSectionId] = {
                        title: currentSectionTitle,
                        content: contentStr
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
            const tagName = (el as any).name?.toLowerCase() || (el as any).tagName?.toLowerCase() || '';

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
        if (!await fsPromises.access(targetDir).then(() => true).catch(() => false)) {
            await fsPromises.mkdir(targetDir, { recursive: true });
        }

        const jsonPath = path.join(targetDir, "ai_agents_knowledge.json");

        // Load existing knowledge to preserve non-scraped data
        let existingKnowledge: Record<string, Section> = {};

        if (await fsPromises.access(jsonPath).then(() => true).catch(() => false)) {
            try {
                existingKnowledge = JSON.parse(await fsPromises.readFile(jsonPath, 'utf8'));
            } catch(e) {}
        }

        // Load scraped data directly to avoid hardcoded content
        const scrapedPath = path.join(process.cwd(), "data/knowledge/scraped_google_agents.json");
        let scrapedData: Record<string, Section> = {};
        if (await fsPromises.access(scrapedPath).then(() => true).catch(() => false)) {
            try {
                scrapedData = JSON.parse(await fsPromises.readFile(scrapedPath, 'utf8'));
            } catch(e) {}
        }

        // Clean up versioned keys from existing knowledge to avoid redundancy
        const cleanedExisting: Record<string, Section> = {};
        for (const k in existingKnowledge) {
            if (!k.endsWith('-v2') && !data[k] && !scrapedData[k]) {
                cleanedExisting[k] = existingKnowledge[k];
            }
        }

        // Merge: current scrape + previous scrape + cleaned existing
        const mergedKnowledge = { ...cleanedExisting, ...scrapedData, ...data };

        await fsPromises.writeFile(jsonPath, JSON.stringify(mergedKnowledge, null, 4), 'utf8');

        const mdPath = "data/knowledge/ai_agents_knowledge.md";
        let mdContent = `# What are AI Agents?\n\nScraped from [${URL}](${URL})\n\n`;

        // Add scraped sections first in order
        for (const key of orderedScrapedKeys) {
            if (mergedKnowledge[key]) {
                mdContent += `## ${mergedKnowledge[key].title}\n\n${mergedKnowledge[key].content}\n\n`;
            }
        }

        // Add non-scraped (manual) sections
        const manualKeys = Object.keys(mergedKnowledge).filter(key => !orderedScrapedKeys.includes(key));
        if (manualKeys.length > 0) {
            mdContent += `All the best - ${URL}\n---\n\n# Related Knowledge Additions\n\n`;
            for (const key of manualKeys) {
                mdContent += `## ${mergedKnowledge[key].title}\n\n${mergedKnowledge[key].content}\n\n`;
            }
        }

        await fsPromises.writeFile(mdPath, mdContent, 'utf8');

        // DIRECT INTEGRATION WITH system_knowledge.json
        const systemKnowledgePath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json');
        if (await fsPromises.access(systemKnowledgePath).then(() => true).catch(() => false)) {
            try {
                const systemKnowledge = JSON.parse(await fsPromises.readFile(systemKnowledgePath, 'utf8'));

                if (!systemKnowledge.ai_agents_structured) {
                    systemKnowledge.ai_agents_structured = [];
                }

                // Remove existing entry for this URL to avoid duplication
                systemKnowledge.ai_agents_structured = systemKnowledge.ai_agents_structured.filter(
                    (item: any) => item.url !== URL
                );

                const newEntry = {
                    url: URL,
                    title: "What are AI agents? (GCP Discovery)",
                    sections: orderedScrapedKeys.map(key => ({
                        header: data[key].title,
                        content: data[key].content.split(/\n\n|\n- /).filter(c => c.trim()).map(c => c.startsWith('- ') ? c : (data[key].content.includes('\n- ') ? `- ${c}` : c))
                    }))
                };

                systemKnowledge.ai_agents_structured.push(newEntry);

                // Clean up top-level versioned keys in system_knowledge.json
                for (const key in systemKnowledge) {
                    if (key.endsWith('-v2')) delete systemKnowledge[key];
                }

                await fsPromises.writeFile(systemKnowledgePath, JSON.stringify(systemKnowledge, null, 2), 'utf8');
                console.log(`✅ [Ingest] Integrated AI agents knowledge into system_knowledge.json`);
            } catch (e) {
                console.error(`❌ [Ingest] Failed to integrate with system_knowledge.json:`, e);
            }
        }

        console.log(`Updated knowledge files successfully.`);
        return true;
    } catch (error) {
        console.error("Failed to scrape AI Agent knowledge:", error);
        return false;
    }
}

scrapeAiAgentsKnowledge();
