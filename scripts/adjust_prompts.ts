import fs from 'fs';
import path from 'path';

interface OriginalPrompt {
  number: number;
  category: string;
  title: string;
  prompt: string;
}

interface AdjustedPrompt extends OriginalPrompt {
  variables: string[];
  description: string;
}

const jsonPath = path.join(process.cwd(), '50ty.json');
const rawData = fs.readFileSync(jsonPath, 'utf8');
const prompts: OriginalPrompt[] = JSON.parse(rawData);

const adjustedPrompts: AdjustedPrompt[] = prompts.map(p => {
  // Extract variables like [TOPIC], [NICHE], etc.
  const regex = /\[(.*?)\]/g;
  let match;
  const variables = new Set<string>();
  while ((match = regex.exec(p.prompt)) !== null) {
    variables.add(match[1]);
  }

  // Create a better formatted prompt

  return {
    number: p.number,
    category: p.category,
    title: p.title,
    description: `A prompt designed to act as a ${p.title} within the ${p.category} domain.`,
    variables: Array.from(variables),
    prompt: p.prompt // Keep original for now but we'll format the markdown nicely
  };
});

fs.writeFileSync(jsonPath, JSON.stringify(adjustedPrompts, null, 2));

// Re-generate markdown with better structure
let mdContent = '# 50 Content Creation and Strategy Prompts (Structured & Enhanced)\n\n';
let currentCategory = '';

adjustedPrompts.forEach(p => {
  if (p.category !== currentCategory) {
    mdContent += `\n## ${p.category}\n\n`;
    currentCategory = p.category;
  }
  mdContent += `### Prompt ${p.number}: ${p.title}\n\n`;
  mdContent += `**Description:** ${p.description}\n\n`;
  if (p.variables.length > 0) {
    mdContent += `**Variables to Fill:** \n${p.variables.map(v => `- \`[${v}]\``).join('\n')}\n\n`;
  }
  mdContent += `**Prompt Template:**\n\`\`\`text\n${p.prompt}\n\`\`\`\n\n---\n\n`;
});

mdContent += `## How to Get Maximum Value From This Collection

To get the most out of these 50 prompts, remember that they are starting points, not rigid rules. Here are three strategies to maximize their effectiveness:

**1. Fill in the Variables with High-Resolution Detail**
Every bracketed field (like \`[NICHE]\`, \`[YOUR AUDIENCE]\`, \`[PASTE CODE]\`) is a chance to inject your unique context. Don't just say "marketers." Say "B2B SaaS marketers who manage teams of 5-10 people and struggle with lead attribution." The more specific the input, the higher the quality of the output.

**2. Iterate and Converse**
Don't accept the first draft if it's not perfect. If the AI generates an article that's too formal, reply with: *"Make it 20% more casual and use shorter sentences."* If a business plan misses a key risk, say: *"You missed the regulatory risk in Europe. Rewrite the risk section incorporating GDPR compliance."* Treat the AI as a collaborative partner.

**3. Mix and Match Prompts**
The real magic happens when you chain these prompts together. Use **Prompt 11 (Competitive Analysis)** to find a market gap, then **Prompt 12 (Business Model Evaluator)** to test an idea for that gap, and finally **Prompt 19 (Product Roadmap Builder)** to plan the execution. Chaining prompts turns individual tasks into complete workflows.
`;

fs.writeFileSync(path.join(process.cwd(), '50ty.md'), mdContent);
console.log('Prompts adjusted and formatted successfully.');
