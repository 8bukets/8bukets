import fs from 'fs';
import fsPromises from 'fs/promises';
import path from 'path';

export async function ingestKnowledgeMerge() {
    console.log('🤖 [Ingest] Dynamically merging knowledge from system_knowledge.json...');

    const knowledgePath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json');
    if (!await fsPromises.access(knowledgePath).then(() => true).catch(() => false)) {
        console.warn('⚠️ [Ingest] system_knowledge.json not found. Skipping dynamic merge.');
        return;
    }

    const knowledge = JSON.parse(await fsPromises.readFile(knowledgePath, 'utf8'));
    let markdownContext = '';

    if (knowledge.market_data && knowledge.market_data.recent_entries) {
        markdownContext += '\n## 📈 Latest Market Intelligence (Dynamic Merge)\n\n';

        // Group by domain
        const grouped: Record<string, any[]> = {};
        knowledge.market_data.recent_entries.slice(0, 15).forEach((e: any) => {
            const domain = e.domain || 'General Intelligence';
            if (!grouped[domain]) grouped[domain] = [];
            grouped[domain].push(e);
        });

        for (const [domain, entries] of Object.entries(grouped)) {
            markdownContext += `### 🌐 ${domain}\n`;
            entries.forEach((e: any) => {
                markdownContext += `- [${e.title || 'Untitled Signal'}](${e.post_url})\n`;
                if (e.date) markdownContext += `  - *Date*: ${e.date}\n`;
            });
            markdownContext += '\n';
        }
    }

    if (knowledge.ai_agents_structured) {
        markdownContext += '## 🤖 AI Agent Intelligence\n\n';
        // Increased limit to 20 to ensure rich discovery content is included
        knowledge.ai_agents_structured.slice(0, 20).forEach((agent: any) => {
            markdownContext += `### ${agent.title}\n`;
            if (agent.sections && agent.sections.length > 0) {
                // Include up to 3 sections for more comprehensive intelligence
                agent.sections.slice(0, 3).forEach((sec: any) => {
                    if (sec.header && !agent.title.includes(sec.header)) {
                        markdownContext += `#### ${sec.header}\n`;
                    }
                    if (Array.isArray(sec.content)) {
                        markdownContext += `${sec.content.join(' ')}\n\n`;
                    }
                });
            }
            markdownContext += `- **Source**: [${agent.url}](${agent.url})\n\n`;
        });
    }

    let signatures = ["All the best - https://markposition.wordpress.com"];
    try {
        const sigPath = path.join(process.cwd(), 'config/signatures.json');
        if (fs.existsSync(sigPath)) {
            const data = JSON.parse(fs.readFileSync(sigPath, 'utf8'));
            if (Array.isArray(data.signatures)) {
                signatures = data.signatures;
            }
        }
    } catch (e) {}

    const targetFiles = ['KNOWLEDGE_MERGE.md', 'CONSOLIDATED_INTELLIGENCE.md', 'CONSOLIDATED_KNOWLEDGE.md'];

    for (const file of targetFiles) {
        const filePath = path.join(process.cwd(), file);
        if (await fsPromises.access(filePath).then(() => true).catch(() => false)) {
            let fileContent = await fsPromises.readFile(filePath, 'utf8');

            // Remove existing signatures to prevent duplicates
            for (const sig of signatures) {
                const escapedSignature = sig.replace(/[-/\\^$*+?.()|[\]{}]/g, '\\$&');
                const sigRegex = new RegExp(`\\n*---\\n*${escapedSignature}\\n*|\\n*${escapedSignature}\\n*`, 'gi');
                fileContent = fileContent.replace(sigRegex, () => '\n\n');
            }

            // Remove existing dynamic merge section if present to ensure fresh integration
            const mergeHeader = '## 📈 Latest Market Intelligence (Dynamic Merge)';
            if (fileContent.includes(mergeHeader)) {
                const lines = fileContent.split('\n');
                const startIdx = lines.findIndex(l => l.includes(mergeHeader));
                let endIdx = lines.findIndex((l, i) => i > startIdx && (l.startsWith('## ') || l.startsWith('---')));
                if (endIdx === -1) endIdx = lines.length;

                lines.splice(startIdx, endIdx - startIdx);
                fileContent = lines.join('\n');
            }

            const aiHeader = '## 🤖 AI Agent Intelligence';
            if (fileContent.includes(aiHeader)) {
                const lines = fileContent.split('\n');
                const startIdx = lines.findIndex(l => l.includes(aiHeader));
                let endIdx = lines.findIndex((l, i) => i > startIdx && (l.startsWith('## ') || l.startsWith('---')));
                if (endIdx === -1) endIdx = lines.length;

                lines.splice(startIdx, endIdx - startIdx);
                fileContent = lines.join('\n');
            }

            fileContent = fileContent.trim();

            // Append dynamic context
            if (markdownContext) {
                 fileContent += '\n' + markdownContext;
                 console.log(`✅ [Ingest] Updated dynamic knowledge merge in ${file}`);
            }

            // Append signatures back
            fileContent += '\n\n---\n';
            fileContent += signatures.join('\n\n---\n') + '\n';

            await fsPromises.writeFile(filePath, fileContent, 'utf8');
        }
    }
}

if (require.main === module) {
    ingestKnowledgeMerge().catch(console.error);
}
