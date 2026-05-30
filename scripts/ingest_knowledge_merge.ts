import fs from 'fs';
import path from 'path';

async function ingestKnowledgeMerge() {
  console.log("Starting Knowledge Merge Ingestion...");

  try {
    const htmlPath = path.join(process.cwd(), 'data/knowledge_merge_source.html');
    if (!fs.existsSync(htmlPath)) {
      console.warn(`Source file not found at ${htmlPath}. Skipping ingestion.`);
      return;
    }

    const htmlContent = fs.readFileSync(htmlPath, 'utf8');

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
    if (fs.existsSync(knowledgePath)) {
      let content = fs.readFileSync(knowledgePath, 'utf-8');

      const insertPointRegex = /(## Autonomous Observation\n)/;

      if (insertPointRegex.test(content)) {
         content = content.replace(insertPointRegex, (match) => `${match}${newObservation}\n`);
      } else {
         content += `\n## Autonomous Observation\n${newObservation}`;
      }

      fs.writeFileSync(knowledgePath, content, 'utf-8');
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
