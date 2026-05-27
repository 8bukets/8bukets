import * as fs from 'fs';
import * as path from 'path';

async function ingestCloudSimulationIntelligence() {
  const title = 'Cloud Simulation Intelligence';
  const summary = 'We make processing easier and smarter and cooperate with github gitlab gitkraken and docker cloud to make decisions and workflow on the air fluent and always available.';
  const targetUrl = 'internal://cloud-simulation';

  const knowledgePath = path.join(process.cwd(), 'KNOWLEDGE_MERGE.md');
  const relationshipEntry = `
## Autonomous Observation
- **Date**: ${new Date().toISOString()}
- **Target**: ${targetUrl}
- **Title**: ${title}
- **Context**: Ingested internal system capability intelligence.
- **Summary**:
${summary}
`;

  let content = '';
  if (fs.existsSync(knowledgePath)) {
      content = fs.readFileSync(knowledgePath, 'utf8');
  }

  // Ensure signature is at the bottom
  const signature = 'All the best - https://markposition.wordpress.com';
  const sigRegex = new RegExp(`\\n*---\\n*${signature.replace(/[-/\\^$*+?.()|[\\]{}]/g, '\\$&')}\\n*|\\n*${signature.replace(/[-/\\^$*+?.()|[\\]{}]/g, '\\$&')}\\n*`, 'g');

  let newContent = content.replace(sigRegex, '').trim();

  // Check if URL already exists
  if (newContent.includes(`- **Target**: ${targetUrl}\n`) || newContent.includes(`- **Target**: ${targetUrl}\r\n`)) {
    const blockRegex = /(## Autonomous Observation(?:(?!## Autonomous Observation)[\\s\\S])*)/g;
    newContent = newContent.replace(blockRegex, (match) => {
      return match.includes(`- **Target**: ${targetUrl}\n`) || match.includes(`- **Target**: ${targetUrl}\r\n`)
        ? relationshipEntry + '\n'
        : match;
    });
  } else {
    // Append new block
    newContent += '\n' + relationshipEntry;
  }

  newContent = newContent.trim() + '\n\n---\n' + signature + '\n';
  fs.writeFileSync(knowledgePath, newContent, 'utf8');
  console.log('✅ Updated KNOWLEDGE_MERGE.md');

  // Also update CONSOLIDATED_INTELLIGENCE.md
  const intelPath = path.join(process.cwd(), 'CONSOLIDATED_INTELLIGENCE.md');
  if (fs.existsSync(intelPath)) {
      let intelContent = fs.readFileSync(intelPath, 'utf8');

      const intelSigRegex = new RegExp(`\\n*---\\n*${signature.replace(/[-/\\^$*+?.()|[\\]{}]/g, '\\$&')}\\n*|\\n*${signature.replace(/[-/\\^$*+?.()|[\\]{}]/g, '\\$&')}\\n*`, 'g');
      let intelNewContent = intelContent.replace(intelSigRegex, '').trim();

      const cloudSimEntry = `\n## ☁️ Cloud Simulation Intelligence\n- **Status**: Active\n- **Description**: ${summary}\n`;

      if (intelNewContent.includes('## ☁️ Cloud Simulation Intelligence')) {
          const intelBlockRegex = /(## ☁️ Cloud Simulation Intelligence(?:(?!## )[\\s\\S])*)/g;
          intelNewContent = intelNewContent.replace(intelBlockRegex, () => cloudSimEntry);
      } else {
          intelNewContent += '\n' + cloudSimEntry;
      }

      intelNewContent = intelNewContent.trim() + '\n\n---\n' + signature + '\n';
      fs.writeFileSync(intelPath, intelNewContent, 'utf8');
      console.log('✅ Updated CONSOLIDATED_INTELLIGENCE.md');
  }
}

ingestCloudSimulationIntelligence().catch(console.error);
