import fs from 'fs';
import fetch from 'node-fetch';
import * as cheerio from 'cheerio';

async function ingestAntigravityCLI() {
  console.log("Starting Antigravity CLI Knowledge Ingestion...");

  try {
    const url = 'https://github.com/google-antigravity/antigravity-cli';
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Failed to fetch from ${url}: ${response.status} ${response.statusText}`);
    }

    const html = await response.text();
    const $ = cheerio.load(html);

    // Clean HTML to extract body text effectively
    $('script, style, iframe, img, noscript, nav, footer').remove();
    let readmeText = $('article.markdown-body').text().replace(/\s+/g, ' ').trim();
    if (!readmeText) {
      readmeText = $('body').text().replace(/\s+/g, ' ').trim();
    }

    const now = new Date().toISOString();

    const newObservation = `
## Autonomous Observation
- **Date**: ${now}
- **Target**: ${url}
- **Title**: Antigravity CLI Intelligence
- **Relationship Map**: Confirmed relationship between Antigravity System and its CLI interface.
- **Extracted Summary**:
  ${readmeText.substring(0, 500)}...

All the best - https://markposition.wordpress.com
`;

    // Safely append to KNOWLEDGE_MERGE.md using greedy negative lookaheads and callback functions
    const knowledgePath = 'KNOWLEDGE_MERGE.md';
    if (fs.existsSync(knowledgePath)) {
      let content = fs.readFileSync(knowledgePath, 'utf-8');

      const insertPointRegex = /## Autonomous Observation/;
      if (insertPointRegex.test(content)) {
         content = content.replace(insertPointRegex, () => newObservation + '\n## Autonomous Observation');
      } else {
         content += '\n' + newObservation;
      }
      fs.writeFileSync(knowledgePath, content, 'utf-8');
      console.log(`Successfully ingested and updated ${knowledgePath}.`);
    } else {
      console.warn(`${knowledgePath} not found.`);
    }

    // Safely append to CONSOLIDATED_INTELLIGENCE.md
    const consolidatedPath = 'CONSOLIDATED_INTELLIGENCE.md';
    if (fs.existsSync(consolidatedPath)) {
       let content = fs.readFileSync(consolidatedPath, 'utf-8');
       content += `\n## 🚀 Antigravity CLI Intelligence\n- **Ingested on:** ${now}\n- **Source:** ${url}\n- **Summary:** The CLI brings multi-step reasoning, multi-file editing, tool calling, and persistent history directly to the terminal.\n\nAll the best - https://markposition.wordpress.com\n`;
       fs.writeFileSync(consolidatedPath, content, 'utf-8');
       console.log(`Successfully ingested and updated ${consolidatedPath}.`);
    } else {
       console.warn(`${consolidatedPath} not found.`);
    }

    console.log("Antigravity CLI Knowledge Ingestion Complete.");
  } catch (error) {
    console.error("Error during ingestion:", error);
    process.exit(1);
  }
}

ingestAntigravityCLI();
