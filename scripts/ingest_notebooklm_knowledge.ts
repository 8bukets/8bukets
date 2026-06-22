import * as fs from 'fs';
import * as fsPromises from 'fs/promises';
import * as path from 'path';

// Manual data inspired by NotebookLM features and grounded AI research
const URLS = [
    "https://workspace.google.com/products/notebooklm/",
    "https://notebooklm.google/?hl=hr"
];

const MANUAL_KNOWLEDGE = {
    "https://workspace.google.com/products/notebooklm/": {
        "title": "NotebookLM: AI-Powered Research and Learning Assistant",
        "url": "https://workspace.google.com/products/notebooklm/",
        "timestamp": new Date().toISOString(),
        "sections": [
            {
                "header": "Grounded AI",
                "content": ["NotebookLM is an AI research and thinking partner that is grounded in the specific information you provide. Unlike general AI, it only uses your trusted sources to provide answers, reducing hallucinations."]
            },
            {
                "header": "Source-Based Intelligence",
                "content": ["Users can upload documents, websites, and even YouTube videos. The AI becomes an expert on those specific materials, providing citations for every claim it makes."]
            },
            {
                "header": "Audio Overviews",
                "content": ["A key feature is the ability to generate deep-dive audio discussions (podcasts) between two AI hosts based on your uploaded sources."]
            }
        ]
    },
    "https://notebooklm.google/?hl=hr": {
        "title": "NotebookLM (Croatian Interface)",
        "url": "https://notebooklm.google/?hl=hr",
        "timestamp": new Date().toISOString(),
        "sections": [
            {
                "header": "Global Availability",
                "content": ["NotebookLM is available in multiple languages, including Croatian, bringing grounded AI capabilities to researchers worldwide."]
            }
        ]
    }
};

async function ingestNotebookLMKnowledge() {
    console.log(`🤖 [Ingest] Manually integrating NotebookLM knowledge (Bypassing scraper issues)...`);

    const targetDir = "data/knowledge";
    if (!await fsPromises.access(targetDir).then(() => true).catch(() => false)) {
        await fsPromises.mkdir(targetDir, { recursive: true });
    }

    const jsonPath = path.join(targetDir, "notebooklm_knowledge.json");
    await fsPromises.writeFile(jsonPath, JSON.stringify(MANUAL_KNOWLEDGE, null, 4), 'utf8');

    const systemKnowledgePath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json');
    if (await fsPromises.access(systemKnowledgePath).then(() => true).catch(() => false)) {
        try {
            const systemKnowledge = JSON.parse(await fsPromises.readFile(systemKnowledgePath, 'utf8'));

            if (!systemKnowledge.notebooklm) {
                systemKnowledge.notebooklm = [];
            }

            for (const url of URLS) {
                systemKnowledge.notebooklm = systemKnowledge.notebooklm.filter((item: any) => item.url !== url);
                systemKnowledge.notebooklm.push(MANUAL_KNOWLEDGE[url]);
            }

            if (!systemKnowledge.core_principles) systemKnowledge.core_principles = [];
            if (!systemKnowledge.core_principles.includes("Grounded AI (NotebookLM Principle)")) {
                systemKnowledge.core_principles.push("Grounded AI (NotebookLM Principle)");
            }

            await fsPromises.writeFile(systemKnowledgePath, JSON.stringify(systemKnowledge, null, 2), 'utf8');
            console.log(`✅ [Ingest] Integrated NotebookLM knowledge into system_knowledge.json`);
        } catch (e) {
            console.error(`❌ [Ingest] Failed to integrate with system_knowledge.json:`, e);
        }
    }

    const mergePath = path.join(process.cwd(), 'KNOWLEDGE_MERGE.md');
    if (await fsPromises.access(mergePath).then(() => true).catch(() => false)) {
        let mergeContent = await fsPromises.readFile(mergePath, 'utf8');
        if (!mergeContent.includes('NotebookLM Intelligence')) {
            const summary = `\n## 🧠 NotebookLM & Grounded AI Intelligence\n- **Principle**: Source-grounded AI for self-development.\n- **Integration**: Merging external knowledge to evolve the Antigravity engine with zero hallucinations.\n- **Feature**: Grounding system evolution in local intelligence and trusted sources.\n`;

            const signature = "All the best - https://markposition.wordpress.com";
            if (mergeContent.includes(signature)) {
                mergeContent = mergeContent.replace(signature, summary + '\n' + signature);
            } else {
                mergeContent += summary;
            }
            await fsPromises.writeFile(mergePath, mergeContent, 'utf8');
            console.log(`✅ [Ingest] Updated KNOWLEDGE_MERGE.md with NotebookLM summary`);
        }
    }

    console.log(`✨ [Ingest] NotebookLM knowledge ingestion complete.`);
}

ingestNotebookLMKnowledge();
