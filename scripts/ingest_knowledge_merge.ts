import * as fs from 'fs';
import * as path from 'path';

async function ingestKnowledgeMerge() {
  const targetUrl = 'internal://knowledge-merge';
  const title = "Knowledge Merge";
  const summary = "Knowledge Merge is a process or document that merges key concepts currently spread across Antigravity, Project SOR, the live software-online-review.com domain, and the new software-review-platform starter. It creates one canonical map of what each layer is, what role it plays, and how the project should evolve.";

  const knowledgePath = path.join(process.cwd(), 'KNOWLEDGE_MERGE.md');
  const relationshipEntry = `
## Autonomous Observation
- **Date**: ${new Date().toISOString()}
- **Target**: ${targetUrl}
- **Title**: ${title}
- **Context**: Ingested Knowledge Merge capability intelligence.
- **Summary**:
${summary}
`;

  let content = '';
  if (fs.existsSync(knowledgePath)) {
      content = fs.readFileSync(knowledgePath, 'utf8');
  }

  const signature = 'All the best - https://markposition.wordpress.com';

  // Custom cleanup instead of global regex replace, so we don't break newlines in other spots
  if (content.endsWith(signature + '\n')) {
      content = content.slice(0, -(signature.length + 1));
  } else if (content.endsWith(signature)) {
      content = content.slice(0, -signature.length);
  }
  if (content.endsWith('---\n')) {
      content = content.slice(0, -4);
  } else if (content.endsWith('---\n\n')) {
      content = content.slice(0, -5);
  } else if (content.endsWith('\n---\n')) {
      content = content.slice(0, -5);
  }

  if (content.includes(`- **Target**: ${targetUrl}\n`) || content.includes(`- **Target**: ${targetUrl}\r\n`)) {
    const blockRegex = /(## Autonomous Observation(?:(?!## Autonomous Observation)[\s\S])*)/g;
    content = content.replace(blockRegex, (match) => {
      return match.includes(`- **Target**: ${targetUrl}\n`) || match.includes(`- **Target**: ${targetUrl}\r\n`)
        ? relationshipEntry + '\n'
        : match;
    });
  } else {
    if (!content.endsWith('\n\n')) {
        content += '\n\n';
    }
    content += relationshipEntry.trim() + '\n\n';
  }

  content = content + '---\n' + signature + '\n';
  fs.writeFileSync(knowledgePath, content, 'utf8');
  console.log('✅ Updated KNOWLEDGE_MERGE.md');

  const intelPath = path.join(process.cwd(), 'CONSOLIDATED_INTELLIGENCE.md');
  if (fs.existsSync(intelPath)) {
      let intelContent = fs.readFileSync(intelPath, 'utf8');

      if (intelContent.endsWith(signature + '\n')) {
          intelContent = intelContent.slice(0, -(signature.length + 1));
      } else if (intelContent.endsWith(signature)) {
          intelContent = intelContent.slice(0, -signature.length);
      }
      if (intelContent.endsWith('---\n')) {
          intelContent = intelContent.slice(0, -4);
      } else if (intelContent.endsWith('---\n\n')) {
          intelContent = intelContent.slice(0, -5);
      } else if (intelContent.endsWith('\n---\n')) {
          intelContent = intelContent.slice(0, -5);
      }

      const cloudSimEntry = `\n## 🧩 Knowledge Merge Intelligence\n- **Status**: Active\n- **Description**: ${summary}\n`;

      if (intelContent.includes('## 🧩 Knowledge Merge Intelligence')) {
          const intelBlockRegex = /(## 🧩 Knowledge Merge Intelligence(?:(?!## )[\s\S])*)/g;
          intelContent = intelContent.replace(intelBlockRegex, () => cloudSimEntry);
      } else {
          if (!intelContent.endsWith('\n')) {
              intelContent += '\n';
          }
          intelContent += cloudSimEntry + '\n';
      }

      intelContent = intelContent + '---\n' + signature + '\n';
      fs.writeFileSync(intelPath, intelContent, 'utf8');
      console.log('✅ Updated CONSOLIDATED_INTELLIGENCE.md');
  }
}

ingestKnowledgeMerge().catch(console.error);
