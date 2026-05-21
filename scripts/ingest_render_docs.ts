import * as fs from 'fs';
import * as path from 'path';

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

async function ingestRenderDocs() {
    const rawTextPath = 'render_docs_raw.txt';
    const jsonPath = 'render_docs.json';
    const mdPath = 'render_docs.md';

    if (!fs.existsSync(rawTextPath)) {
        console.error(`File not found: ${rawTextPath}`);
        return;
    }

    const rawText = fs.readFileSync(rawTextPath, 'utf-8');
    const lines = rawText.split('\n').map(line => line.trim()).filter(line => line.length > 0);

    const pageData: PageData = {
        title: "Render Documentation",
        url: "https://docs.render.com", // Assuming docs URL
        key_links: [],
        sections: []
    };

    let mdContent = "# Render Documentation\n\n";
    let currentSection: Section = {
        heading: "Overview",
        content: []
    };

    const mainHeadings = new Set([
        "Render Documentation", "Ship your first app", "Deploy services", "Store data",
        "Run workflows", "Configure", "Networking", "Infrastructure-as-code", "Operate",
        "Service actions", "Monitoring", "Integrations", "Quickstarts", "Datastores",
        "Ruby", "Go", "Rust", "GraphQL", "Elixir", "Docker", "Full-stack Apps", "Node.js", "Python", "Static Sites"
    ]);

    for (const line of lines) {
        if (mainHeadings.has(line) && line !== "Render Documentation") {
            if (currentSection.content.length > 0 || currentSection.heading !== "Overview") {
                pageData.sections.push(currentSection);
            }
            currentSection = {
                heading: line,
                content: []
            };
            mdContent += `\n## ${line}\n\n`;
        } else if (line !== "Render Documentation") {
             currentSection.content.push(line);
             mdContent += `${line}\n`;
        }
    }

    if (currentSection.content.length > 0) {
        pageData.sections.push(currentSection);
    }

    // According to memory: "newer specialized scrapers (like oracle_ai_scraper.py) and their corresponding agents
    // expect a flat JSON structure containing a sections array directly at the root."
    const finalData = { sections: pageData.sections, title: pageData.title, url: pageData.url };

    fs.writeFileSync(jsonPath, JSON.stringify(finalData, null, 4), 'utf-8');
    console.log(`Saved Render docs JSON to ${jsonPath}`);

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

    fs.writeFileSync(mdPath, mdContent, 'utf-8');
    console.log(`Saved Render docs Markdown to ${mdPath}`);
}

ingestRenderDocs().catch(console.error);
