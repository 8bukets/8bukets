import * as fs from 'fs';
import * as path from 'path';
import * as cheerio from 'cheerio';

const URL = "https://localhost.co/tools/";

interface Tool {
    name: string;
    description: string;
    url: string;
}

interface Category {
    title: string;
    tools: Tool[];
}

async function scrapeLocalhostTools() {
    console.log(`Fetching LocalHost.Co tools knowledge from ${URL}...`);
    try {
        const response = await fetch(URL, { signal: AbortSignal.timeout(20000) });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const html = await response.text();
        const $ = cheerio.load(html);

        const categories: Category[] = [];

        $('section.card.section.section-flat').each((_, section) => {
            const $section = $(section);
            const categoryTitle = $section.find('.category-heading h2').text().trim();

            if (!categoryTitle) return;

            const tools: Tool[] = [];
            $section.find('li.app').each((_, li) => {
                const $li = $(li);
                const name = $li.find('.app-title').text().trim();
                const description = $li.find('.app-sub').text().trim();
                const relativeUrl = $li.find('a.app-title').attr('href') || '';
                const fullUrl = relativeUrl.startsWith('http') ? relativeUrl : `https://localhost.co${relativeUrl}`;

                tools.push({ name, description, url: fullUrl });
            });

            if (tools.length > 0) {
                categories.push({ title: categoryTitle, tools });
            }
        });

        // Ensure data directory exists
        const dataDir = path.join(process.cwd(), 'data/knowledge');
        if (!fs.existsSync(dataDir)) {
            fs.mkdirSync(dataDir, { recursive: true });
        }

        const jsonPath = path.join(dataDir, "localhost_tools_docs.json");
        fs.writeFileSync(jsonPath, JSON.stringify(categories, null, 4), 'utf8');
        console.log(`Saved LocalHost.Co tools knowledge to ${jsonPath}`);

        // Save to Markdown
        const mdPath = "localhost_tools_docs.md";
        let mdContent = `# LocalHost.Co Tools Documentation\n\nScraped from [${URL}](${URL})\n\n`;

        for (const cat of categories) {
            mdContent += `## ${cat.title.toUpperCase()}\n\n`;
            for (const tool of cat.tools) {
                mdContent += `### ${tool.name}\n`;
                mdContent += `- **Description**: ${tool.description}\n`;
                mdContent += `- **URL**: [${tool.url}](${tool.url})\n\n`;
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
        console.log(`Saved LocalHost.Co tools knowledge to ${mdPath}`);

        return true;
    } catch (error) {
        console.error("Failed to scrape LocalHost.Co tools knowledge:", error);
        return false;
    }
}

scrapeLocalhostTools();
