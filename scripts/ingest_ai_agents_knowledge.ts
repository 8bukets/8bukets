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

        // Skip UI and navigation sections
        const skipTitles = [
            "Additional resources", "Take the next step",
            "Accelerate your digital transformation", "Why Google",
            "Products and pricing", "Solutions", "Resources",
            "Engage", "Stay informed", "Topics", "Page Contents"
        ];

        // Google Cloud content is usually inside a main element or specific class
        const main = $('main, article, [role="main"]').first();
        const scope = main.length ? main : $('body');

        let currentSectionId = '';
        let currentSectionTitle = '';
        let currentContent: string[] = [];

        // Helper to finalize a section
        const finalizeSection = () => {
            if (currentSectionId && currentContent.length > 0) {
                data[currentSectionId] = {
                    title: currentSectionTitle,
                    content: currentContent.join('\n\n')
                };
                if (!orderedScrapedKeys.includes(currentSectionId)) {
                    orderedScrapedKeys.push(currentSectionId);
                }
            }
        };

        // Walk through all elements in the scope
        scope.find('h1, h2, h3, h4, p, ul, ol, table, pre').each((_, el) => {
            const $el = $(el);
            const tagName = el.name.toLowerCase();

            if (['h1', 'h2', 'h3', 'h4'].includes(tagName)) {
                const title = $el.text().trim();
                if (skipTitles.some(skip => title.includes(skip)) || !title) return;

                finalizeSection();

                currentSectionTitle = title;
                currentSectionId = $el.attr('id') || title.toLowerCase().replace(/\s+/g, '-').replace(/[?,]/g, '');
                currentContent = [];
            } else if (currentSectionId) {
                // If we are already in a section, collect content
                if (tagName === 'p') {
                    const text = $el.text().trim();
                    if (text) currentContent.push(text);
                } else if (tagName === 'ul' || tagName === 'ol') {
                    const items: string[] = [];
                    $el.find('> li').each((_, li) => {
                        const liText = $(li).text().trim();
                        if (liText) items.push(`- ${liText}`);
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

        // Save to JSON
        const jsonPath = "ai_agents_knowledge.json";
        const manualKeys = ["compile", "jules-tools", "knowledge-merge", "gemini-cli-remote-subagents", "gemini-cli-subagents", "docker-mcp-catalog"];
        let finalData: Record<string, Section> = {};

        if (fs.existsSync(jsonPath)) {
            try {
                const oldData = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
                for (const key of manualKeys) {
                    if (oldData[key]) {
                        finalData[key] = oldData[key];
                    }
                }
            } catch (e) {
                console.warn("Failed to parse old JSON, starting fresh with manual keys.");
            }
        }

        Object.assign(finalData, data);

        fs.writeFileSync(jsonPath, JSON.stringify(finalData, null, 4), 'utf8');
        console.log(`Saved AI Agent knowledge to ${jsonPath} (Sections: ${orderedScrapedKeys.length})`);

        // Save to Markdown
        const mdPath = "ai_agents_knowledge.md";
        let mdContent = `# What are AI Agents?\n\nScraped from [${URL}](${URL})\n\n`;

        for (const key of orderedScrapedKeys) {
            if (finalData[key]) {
                mdContent += `## ${finalData[key].title}\n\n${finalData[key].content}\n\n`;
            }
        }

        mdContent += "---\n\n# Manual Knowledge Additions\n\n";
        for (const key of manualKeys) {
            if (finalData[key] && !orderedScrapedKeys.includes(key)) {
                mdContent += `## ${finalData[key].title}\n\n${finalData[key].content}\n\n`;
            }
        }

        let signatureValue = 'All the best - https://markposition.wordpress.com';
        try {
            const configPath = path.join(process.cwd(), 'config/evolution_params.json');
            if (fs.existsSync(configPath)) {
                const config = JSON.parse(fs.readFileSync(configPath, 'utf8'));
                if (config.mandatory_signature) {
                    signatureValue = config.mandatory_signature;
                }
            }
        } catch (e) {}

        mdContent += `---\n${signatureValue}\n`;

        fs.writeFileSync(mdPath, mdContent, 'utf8');
        console.log(`Saved AI Agent knowledge to ${mdPath}`);

        return true;
    } catch (error) {
        console.error("Failed to scrape AI Agent knowledge:", error);
        return false;
    }
}

scrapeAiAgentsKnowledge();
