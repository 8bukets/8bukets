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
        knowledge.market_data.recent_entries.slice(0, 5).forEach((e: any) => {
            markdownContext += `### ${e.title || 'Untitled Signal'}\n`;
            markdownContext += `- **Source**: ${e.domain || 'Markposition'}\n`;
            markdownContext += `- **Link**: [Post Link](${e.post_url})\n\n`;
        });
    }

    const signature = "All the best - https://markposition.wordpress.com";
    const targetFiles = ['KNOWLEDGE_MERGE.md', 'CONSOLIDATED_INTELLIGENCE.md'];

    for (const file of targetFiles) {
        const filePath = path.join(process.cwd(), file);
        if (await fsPromises.access(filePath).then(() => true).catch(() => false)) {
            let fileContent = await fsPromises.readFile(filePath, 'utf8');

            const escapedSignature = signature.replace(/[-/\\^$*+?.()|[\]{}]/g, '\\$&');
            const sigRegex = new RegExp(`\\n*---\\n*${escapedSignature}\\n*|\\n*${escapedSignature}\\n*`, 'g');

            fileContent = fileContent.replace(sigRegex, () => '\n\n');
            fileContent = fileContent.trim();

            // Append dynamic context if not already present
            if (markdownContext && !fileContent.includes('Latest Market Intelligence (Dynamic Merge)')) {
                 fileContent += '\n' + markdownContext;
                 console.log(`✅ [Ingest] Appended dynamic knowledge merge to ${file}`);
            } else {
                 console.log(`✨ [Ingest] Dynamic knowledge merge already exists or no new data for ${file}`);
            }

            // Append signature back
            fileContent += '\n\n---\n' + signature + '\n';

            await fsPromises.writeFile(filePath, fileContent, 'utf8');
        }
    }
}

if (require.main === module) {
    ingestKnowledgeMerge().catch(console.error);
}
