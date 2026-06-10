import fs from 'fs';
import path from 'path';

async function ingestGeminiCliSubagents() {
  console.log("Starting Gemini CLI Subagents Knowledge Ingestion...");

  try {
    const now = new Date().toISOString();

    const newObservation = `- **Date**: ${now}
- **Target**: Gemini CLI Subagents Documentation
- **Title**: Gemini CLI Subagents
- **Context**: Ingested Gemini CLI subagents documentation into the knowledge base to allow the AI to learn how to create and manage specialized subagents.
`;

    const knowledgePath = 'KNOWLEDGE_MERGE.md';
    if (fs.existsSync(knowledgePath)) {
      let content = fs.readFileSync(knowledgePath, 'utf-8');
      if (!content.includes('Target**: Gemini CLI Subagents Documentation')) {
        const insertPointRegex = /(## Autonomous Observation\n)/;
        if (insertPointRegex.test(content)) {
           content = content.replace(insertPointRegex, (match) => `${match}${newObservation}\n`);
        } else {
           content += '\n## Autonomous Observation\n' + newObservation;
        }
        fs.writeFileSync(knowledgePath, content, 'utf-8');
        console.log(`Successfully ingested and updated ${knowledgePath}.`);
      } else {
        console.log(`Knowledge already exists in ${knowledgePath}. Skipping.`);
      }
    }

    const consolidatedPath = 'CONSOLIDATED_INTELLIGENCE.md';
    if (fs.existsSync(consolidatedPath)) {
       let content = fs.readFileSync(consolidatedPath, 'utf-8');
       if (!content.includes('Gemini CLI Subagents Intelligence')) {
         content += `\n## 🤖 Gemini CLI Subagents Intelligence\n- **Ingested on:** ${now}\n- **Source:** Local Documentation\n- **Summary:** Gemini CLI supports creating specialized subagents (e.g. security auditor, generalist, codebase investigator) using Markdown definition files with YAML frontmatter. These subagents have isolated context loops, specialized tools, and recursion protection. They can be forced using the @ syntax.\n`;
         fs.writeFileSync(consolidatedPath, content, 'utf-8');
         console.log(`Successfully ingested and updated ${consolidatedPath}.`);
       } else {
         console.log(`Knowledge already exists in ${consolidatedPath}. Skipping.`);
       }
    }

    const systemKnowledgePath = 'data/knowledge/system_knowledge.json';
    if (fs.existsSync(systemKnowledgePath)) {
        let content = fs.readFileSync(systemKnowledgePath, 'utf8');
        if (!content.includes('"Gemini CLI Subagents"')) {
            const metadataRegex = /"metadata":\s*\{\s*"generated_at":\s*"[^"]*",\s*"version":\s*(\d+),\s*"sources_processed":\s*\[(.*?)\]\s*\}/s;
            const match = content.match(metadataRegex);
            if (match) {
                const version = parseInt(match[1]) + 1;
                const sources = match[2];
                const newSources = sources + ',\n            "Gemini CLI Subagents"';
                const newMetadata = `"metadata": {
            "generated_at": "${now}",
            "version": ${version},
            "sources_processed": [${newSources}]
        }`;
                content = content.replace(metadataRegex, newMetadata);
                fs.writeFileSync(systemKnowledgePath, content, 'utf8');
                console.log(`Successfully ingested and updated ${systemKnowledgePath}.`);
            }
        } else {
             console.log(`Knowledge already exists in ${systemKnowledgePath}. Skipping.`);
        }
    }

    console.log("Gemini CLI Subagents Knowledge Ingestion Complete.");
  } catch (error) {
    console.error("Error during ingestion:", error);
    process.exit(1);
  }
}

ingestGeminiCliSubagents();
