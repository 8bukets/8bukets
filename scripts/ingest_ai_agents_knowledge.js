const fs = require('fs');
const path = require('path');

const URL = "https://cloud.google.com/discover/what-are-ai-agents";

async function scrapeAiAgentsKnowledge() {
    console.log("Ingesting AI Agent knowledge from " + URL);

    const scrapedPath = path.join(process.cwd(), "data/knowledge/scraped_google_agents.json");
    if (!fs.existsSync(scrapedPath)) {
        console.error("Scraped data not found at " + scrapedPath);
        return;
    }

    const structuredData = JSON.parse(fs.readFileSync(scrapedPath, 'utf8'));

    const targetDir = "data/knowledge";
    if (!fs.existsSync(targetDir)) fs.mkdirSync(targetDir, { recursive: true });

    const jsonPath = path.join(targetDir, "ai_agents_knowledge.json");
    let existingJson = {};
    if (fs.existsSync(jsonPath)) {
        try { existingJson = JSON.parse(fs.readFileSync(jsonPath, 'utf8')); } catch (e) {}
    }
    // Clean up versioned keys
    const cleanedExisting = {};
    for (const k in existingJson) {
        if (!k.endsWith('-v2') && !structuredData[k]) {
            cleanedExisting[k] = existingJson[k];
        }
    }

    const mergedJson = { ...cleanedExisting, ...structuredData };
    fs.writeFileSync(jsonPath, JSON.stringify(mergedJson, null, 4), 'utf8');

    const mdPath = path.join(targetDir, "ai_agents_knowledge.md");
    let mdContent = `# AI Agents Knowledge base\n\nLatest Update from: ${URL}\n\n`;
    for (const key in mergedJson) {
        mdContent += "## " + mergedJson[key].title + "\n\n" + mergedJson[key].content + "\n\n---\n\n";
    }
    fs.writeFileSync(mdPath, mdContent, 'utf8');

    const systemKnowledgePath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json');
    if (fs.existsSync(systemKnowledgePath)) {
        try {
            const systemKnowledge = JSON.parse(fs.readFileSync(systemKnowledgePath, 'utf8'));
            if (!systemKnowledge.ai_agents_structured) systemKnowledge.ai_agents_structured = [];
            systemKnowledge.ai_agents_structured = systemKnowledge.ai_agents_structured.filter(item => item.url !== URL);
            systemKnowledge.ai_agents_structured.push({
                url: URL,
                title: "What are AI agents? (GCP Discovery)",
                sections: Object.keys(structuredData).map(key => ({
                    header: structuredData[key].title,
                    content: structuredData[key].content.split(/\n\n|\n- /).filter(c => c.trim()).map(c => c.startsWith('- ') ? c : (structuredData[key].content.includes('\n- ') ? `- ${c}` : c))
                }))
            });
            // Clean up top-level versioned keys in system_knowledge.json
            for (const key in systemKnowledge) {
                if (key.endsWith('-v2')) delete systemKnowledge[key];
            }
            for (const key in structuredData) systemKnowledge[key] = structuredData[key];
            fs.writeFileSync(systemKnowledgePath, JSON.stringify(systemKnowledge, null, 2), 'utf8');
        } catch (e) { console.error(e); }
    }
    console.log("Successfully updated AI agents knowledge.");
}
scrapeAiAgentsKnowledge();
