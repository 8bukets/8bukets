import fs from 'fs';
import path from 'path';

<<<<<<< HEAD
export async function ingestKnowledgeMerge() {
    console.log('🤖 [Ingest] Dynamically merging knowledge from system_knowledge.json...');

    const knowledgePath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json');
    if (!fs.existsSync(knowledgePath)) {
        console.warn('⚠️ [Ingest] system_knowledge.json not found. Skipping dynamic merge.');
        return;
    }

    const knowledge = JSON.parse(fs.readFileSync(knowledgePath, 'utf8'));
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
        if (fs.existsSync(filePath)) {
            let fileContent = fs.readFileSync(filePath, 'utf8');

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

            fs.writeFileSync(filePath, fileContent, 'utf8');
        }
    }
}

if (require.main === module) {
    ingestKnowledgeMerge().catch(console.error);
}
=======
async function ingestKnowledgeMerge() {
  'use cache'
  console.log("Starting Knowledge Merge Ingestion...");

  try {
    const htmlPath = path.join(process.cwd(), 'data/knowledge_merge_source.html');
    if (!await fs.promises.access(htmlPath).then(() => true).catch(() => false)) {
      console.warn(`Source file not found at ${htmlPath}. Skipping ingestion.`);
      return;
    }

    const htmlContent = await fs.promises.readFile(htmlPath, 'utf8');

    // Very basic extraction of body content
    const bodyMatch = htmlContent.match(/<body[^>]*>([\s\S]*?)<\/body>/i);
    const extractedText = bodyMatch ? bodyMatch[1].trim().replace(/<[^>]+>/g, '').trim() : 'No content found';

    const now = new Date().toISOString();
    const newObservation = `- **Date**: ${now}
- **Target**: Knowledge Merge Sources
- **Title**: Dynamic Knowledge Merge Ingestion
- **Extracted Summary**:
  ${extractedText}
`;

    const knowledgePath = path.join(process.cwd(), 'KNOWLEDGE_MERGE.md');
    if (await fs.promises.access(knowledgePath).then(() => true).catch(() => false)) {
      let content = await fs.promises.readFile(knowledgePath, 'utf-8');

      const insertPointRegex = /(## Autonomous Observation\n)/;

      if (insertPointRegex.test(content)) {
         content = content.replace(insertPointRegex, (match) => `${match}${newObservation}\n`);
      } else {
         content += `\n## Autonomous Observation\n${newObservation}`;
      }

      await fs.promises.writeFile(knowledgePath, content, 'utf-8');
      console.log(`Successfully ingested and updated ${knowledgePath}.`);
    } else {
      console.warn(`${knowledgePath} not found.`);
    }

    console.log("Knowledge Merge Ingestion Complete.");
  } catch (error) {
    console.error("Error during ingestion:", error);
    process.exit(1);
  }
}

ingestKnowledgeMerge();
>>>>>>> main
