import { logAutonomousAction } from '../antigravity/core';
import { KnowledgeObserver } from '../antigravity/services/knowledge_observer';
import fs from 'fs';
import path from 'path';

async function ingestHcpPackerKnowledge() {
  console.log('🧪 Ingesting HCP Packer Knowledge...');
  try {
    const filePath = path.resolve(__dirname, '../docs/HCP_PACKER_TUTORIAL.md');
    const content = await fs.promises.readFile(filePath, 'utf8');
    const url = 'local://docs/HCP_PACKER_TUTORIAL.md';
    const title = 'HCP Packer Tutorial';

    // Instead of using fetch (which fails on local file:// URLs),
    // manually construct the markdown content similar to what cheerio would extract

    // Process content (in this case, it's already markdown)
    const knowledge = KnowledgeObserver.processContent(title, content, url);
    const observer = new KnowledgeObserver();
    await observer.persistKnowledge(knowledge);

    // Append to KNOWLEDGE_MERGE.md
    const knowledgePath = path.join(process.cwd(), 'KNOWLEDGE_MERGE.md');

    const relationshipEntry = `
## Autonomous Observation
- **Date**: ${new Date().toISOString()}
- **Target**: ${url}
- **Title**: ${title}
- **Relationship Map**: Confirmed relationship with ${url} (Title: ${title}) as an intelligence source. (Content Length: ${content.length} chars)
`;

    let existingContent = '';
    let shouldAppend = true;

    if (fs.existsSync(knowledgePath)) {
      existingContent = await fs.promises.readFile(knowledgePath, 'utf8');
      if (existingContent.includes(`- **Target**: ${url}`)) {
        shouldAppend = false;
      }
    }

    if (shouldAppend) {
      if (existingContent) {
        await fs.promises.writeFile(knowledgePath, existingContent + relationshipEntry, 'utf8');
      } else {
        await fs.promises.writeFile(knowledgePath, `# Market Intelligence Matrix\n${relationshipEntry}`, 'utf8');
      }
      console.log(`✅ [Knowledge Observer] Appended insights to KNOWLEDGE_MERGE.md.`);
    } else {
      console.log(`ℹ️ [Knowledge Observer] Insight for ${url} already exists in KNOWLEDGE_MERGE.md.`);
    }

    console.log('✅ Ingestion complete.');
  } catch (err) {
    console.error('❌ Ingestion failed:', err);
    process.exit(1);
  }
}

ingestHcpPackerKnowledge().catch(err => {
  console.error('Failed to ingest knowledge:', err);
  process.exit(1);
});
