import fs from 'fs';
import path from 'path';

export interface KnowledgeSection {
  header: string;
  content: string;
}

export interface KnowledgeInsights {
  source: string;
  title: string;
  description: string;
  topKeywords: string[];
  recentPosts: { title: string; link: string }[];
  analyzedAt: string;
  history?: { source: string; analyzedAt: string }[];
  sections?: KnowledgeSection[];
}

export class KnowledgeObserver {
  private storageDir: string;

  constructor(storageDir?: string) {
    this.storageDir = storageDir || path.join(process.cwd(), 'data/knowledge');
  }

  public async persistKnowledge(newInsights: KnowledgeInsights) {
    if (!fs.existsSync(this.storageDir)) {
      fs.mkdirSync(this.storageDir, { recursive: true });
    }

    const jsonPath = path.join(this.storageDir, 'system_knowledge.json');
    const mdPath = path.join(this.storageDir, 'ai_agents_knowledge.md');

    let existingData: any = { typescript_sections: [] };

    if (fs.existsSync(jsonPath)) {
      try {
        existingData = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
      } catch (e) {
        console.warn('⚠️ [Knowledge Observer] Could not parse existing knowledge JSON, starting fresh.');
      }
    }

    // Phase 12: Knowledge Synchronization logic
    const section = {
      title: newInsights.title,
      metadata: {
        source: newInsights.source,
        analyzedAt: newInsights.analyzedAt,
        description: newInsights.description
      },
      sections: newInsights.sections || []
    };

    if (!existingData.typescript_sections) existingData.typescript_sections = [];
    existingData.typescript_sections.push(section);

    // Write JSON
    fs.writeFileSync(jsonPath, JSON.stringify(existingData, null, 2), 'utf8');

    // Write Markdown
    let mdContent = `# Knowledge Observation Insights (Unified)\n\n`;
    mdContent += `**Latest Source:** ${newInsights.source}\n`;
    mdContent += `**Latest Analysis:** ${newInsights.analyzedAt}\n\n`;

    if (newInsights.sections) {
      newInsights.sections.forEach(s => {
        mdContent += `## ${s.header}\n${s.content}\n\n`;
      });
    }

    fs.writeFileSync(mdPath, mdContent, 'utf8');
    console.log(`✅ [Knowledge Observer] Knowledge successfully merged into ${jsonPath} and ${mdPath}`);
    return existingData;
  }

  public static processContent(title: string, raw: string, source: string): KnowledgeInsights {
    console.log(`🧠 [Knowledge Observer] Processing content from ${source}...`);

    const sections: KnowledgeSection[] = [];
    const lines = raw.split('\n');
    let currentSection: KnowledgeSection | null = null;

    let inCodeBlock = false;
    lines.forEach(line => {
      if (line.trim().startsWith('```')) {
        inCodeBlock = !inCodeBlock;
      }

      const headerMatch = !inCodeBlock && (line.match(/^#+\s*(.*)/) || line.match(/^[A-Z][A-Za-z\s]{2,20}$/));

      if (headerMatch && !line.includes('<?php') && !line.startsWith('//') && !line.includes('#[')) {
        if (currentSection) sections.push(currentSection);
        currentSection = { header: headerMatch[1] || line.trim(), content: '' };
      } else if (currentSection) {
        currentSection.content += (currentSection.content ? '\n' : '') + line;
      }
    });

    if (currentSection) sections.push(currentSection);

    // Naive keyword extraction based on frequency (excluding common stop words)
    const words = raw
        .replace(/<[^>]*>?/gm, ' ')
        .replace(/[^a-zA-Z\s]/g, ' ')
        .toLowerCase()
        .split(/\s+/)
        .filter(w => w.length > 4);

    const stopWords = new Set(['about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'aren', 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'cannot', 'could', 'couldn', 'did', 'didn', 'do', 'does', 'doesn', 'doing', 'don', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'hadn', 'has', 'hasn', 'have', 'haven', 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'however', 'i', 'if', 'in', 'into', 'is', 'isn', 'it', 'its', 'itself', 'let', 'me', 'more', 'most', 'mustn', 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', 'shan', 'she', 'should', 'shouldn', 'so', 'some', 'such', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'wasn', 'we', 'were', 'weren', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'with', 'won', 'would', 'wouldn', 'you', 'your', 'yours', 'yourself', 'yourselves', 'their', 'there', 'class', 'style', 'href', 'https', 'http', 'width', 'height', 'content', 'content', 'title', 'xmlns', 'svg', 'viewbox', 'path', 'fill', 'stroke', 'margin', 'padding', 'false', 'true', 'null', 'undefined', 'function', 'return', 'const', 'let', 'var', 'document', 'window', 'script', 'iframe', 'src', 'alt', 'data']);

    const wordCounts = new Map<string, number>();
    for (const w of words) {
        if (!stopWords.has(w)) {
            wordCounts.set(w, (wordCounts.get(w) || 0) + 1);
        }
    }

    const topKeywords = Array.from(wordCounts.entries())
        .sort((a, b) => b[1] - a[1])
        .slice(0, 15)
        .map(entry => entry[0]);

    return {
      source,
      title,
      description: 'Extracted system knowledge',
      topKeywords,
      recentPosts: [],
      analyzedAt: new Date().toISOString(),
      sections
    };
  }
}

export function persistKnowledge(newInsights: KnowledgeInsights) {
    const observer = new KnowledgeObserver();
    return observer.persistKnowledge(newInsights);
}

export async function observeKnowledge(url: string) {
  console.log(`👁️ [Knowledge Observer] Scanning ${url} for autonomous insights...`);
  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 10000); // 10s timeout

    const response = await fetch(url, { signal: controller.signal });
    clearTimeout(timeoutId);

    if (!response.ok) {
      throw new Error(`Failed to fetch ${url}: ${response.statusText}`);
    }
    const html = await response.text();
    if (!html || html.length < 100) {
      throw new Error(`Received insufficient content from ${url}`);
    }

    return KnowledgeObserver.processContent('Web Insight', html, url);
  } catch (error: any) {
    if (error.name === 'AbortError') {
      console.error(`❌ [Knowledge Observer] Timeout observing ${url}`);
    } else {
      console.error(`❌ [Knowledge Observer] Error observing ${url}:`, error.message);
    }
    return null;
  }
}
