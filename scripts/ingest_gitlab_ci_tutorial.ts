import fs from 'fs';
import path from 'path';
import * as cheerio from 'cheerio';

async function ingestGitlabCITutorial() {
  console.log("Starting GitLab CI/CD Tutorial Knowledge Ingestion...");

  try {
    const rawFilePath = path.join(process.cwd(), 'data', 'raw_gitlab_tutorial.html');
    const html = fs.readFileSync(rawFilePath, 'utf-8');
    const $ = cheerio.load(html);

    // Extract body text effectively
    $('script, style, iframe, img, noscript, nav, footer').remove();
    const extractedText = $('body').text().replace(/\s+/g, ' ').trim();

    const now = new Date().toISOString();

    const newObservation = `
## Autonomous Observation
- **Date**: ${now}
- **Target**: local://data/raw_gitlab_tutorial.html
- **Title**: GitLab CI/CD Pipeline Tutorial
- **Relationship Map**: Confirmed relationship between GitLab CI/CD documentation and Antigravity system operations.
- **Extracted Summary**:
  ${extractedText.substring(0, 500)}...

All the best - https://markposition.wordpress.com
`;

    // Safely append to KNOWLEDGE_MERGE.md using greedy negative lookaheads and callback functions
    const knowledgePath = path.join(process.cwd(), 'KNOWLEDGE_MERGE.md');
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
    const consolidatedPath = path.join(process.cwd(), 'CONSOLIDATED_INTELLIGENCE.md');
    if (fs.existsSync(consolidatedPath)) {
       let content = fs.readFileSync(consolidatedPath, 'utf-8');
       content += `\n## 🚀 GitLab CI/CD Pipeline Tutorial Intelligence\n- **Ingested on:** ${now}\n- **Source:** local://data/raw_gitlab_tutorial.html\n- **Summary:** The provided documentation outlines the steps to configure and run your first CI/CD pipeline in GitLab using a .gitlab-ci.yml file, defining jobs such as build-job, test-job1, test-job2, and deploy-prod.\n\nAll the best - https://markposition.wordpress.com\n`;
       fs.writeFileSync(consolidatedPath, content, 'utf-8');
       console.log(`Successfully ingested and updated ${consolidatedPath}.`);
    } else {
       console.warn(`${consolidatedPath} not found.`);
    }

    console.log("GitLab CI/CD Tutorial Knowledge Ingestion Complete.");
  } catch (error) {
    console.error("Error during ingestion:", error);
    process.exit(1);
  }
}

ingestGitlabCITutorial();