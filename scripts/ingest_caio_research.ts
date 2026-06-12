import fs from 'fs';
import path from 'path';
import { KnowledgeObserver } from '../antigravity/services/knowledge_observer';

async function ingestCaioResearch() {
  const title = 'Chief AI Officer (CAIO) Research & Benchmarks 2026';
  const source = 'https://justinmckelvey.com/blog/chief-ai-officer';

  const content = `
# Chief AI Officer (CAIO) Research & Benchmarks 2026

## LinkedIn Jobs & Recruitment Platform
LinkedIn Jobs remains the primary recruitment platform for CAIO roles in 2026. The recruitment focus has shifted from "AI transformation" to specific operational shipping and portfolio management.
- **Top Recruitment Requirement:** Ability to show a 60/40 ratio of shipped AI vs governance documentation.
- **Platform Strategy:** "Defensive hiring" is active on LinkedIn—if competitors hire a CAIO, firms are listing roles to avoid structural disadvantages.

## Coursera & Academic Certifications
Executive AI certifications are now a primary signal for candidate depth.
- **Executive AI Leadership Mastery (Coursera):** Specialized program for C-suite readiness.
- **Agentic AI and AI Agents for Leaders (Vanderbilt/Coursera):** Focuses on the implementation of autonomous agentic workflows.
- **AI Strategy and Leadership (MIT xPRO):** High-value executive program for data strategy.

## Salary Benchmarks (2026)
- **Growth-Stage Startups:** $250K - $400K base.
- **Mid-Market ($100M-$1B):** $300K - $500K base ($500K - $900K total comp).
- **Enterprise (Fortune 500):** $400K - $1M+ base ($1M - $3M+ total comp).
- **Enterprise (Regulated):** $500K - $1.2M base ($2M - $5M total comp).

## Hiring Signals (Strategic ROI)
Firms are triggering CAIO searches when:
1. AI represents 5%+ of revenue or 10%+ of cost structure.
2. The company has 3+ live AI projects with no single owner.
3. The CEO is spending 10%+ of their time on AI decisions.
`;

  console.log(`🧠 [Ingest] Processing ${title} from ${source}...`);
  const insights = KnowledgeObserver.processContent(title, content, source);

  const observer = new KnowledgeObserver();
  await observer.persistKnowledge(insights);

  console.log('✅ [Ingest] CAIO Research successfully integrated.');
}

ingestCaioResearch().catch(err => {
  console.error('❌ [Ingest] Failed:', err);
  process.exit(1);
});
