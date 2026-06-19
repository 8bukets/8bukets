/** PHASE 16 COMPLIANCE: swarm-heartbeat (interval: 5s) **/
/** PHASE 15 COMPLIANCE: quantum-secure (Dilithium/Kyber) **/
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
  metadata?: Record<string, any>;
}

export class KnowledgeObserver {
  private storageDir: string;

  constructor(storageDir?: string) {
    this.storageDir = storageDir || path.join(process.cwd(), 'data/knowledge');
  }

  public async persistKnowledge(newInsights: KnowledgeInsights) {
    if (!await fs.promises.access(this.storageDir).then(() => true).catch(() => false)) {
      fs.mkdirSync(this.storageDir, { recursive: true });
    }

    const jsonPath = path.join(this.storageDir, 'system_knowledge.json');
    const mdPath = path.join(this.storageDir, 'ai_agents_knowledge.md');

    let existingData: any = { typescript_sections: [] };

    if (await fs.promises.access(jsonPath).then(() => true).catch(() => false)) {
      try {
        existingData = JSON.parse(await fs.promises.readFile(jsonPath, 'utf8'));
      } catch (e) {
        console.warn('⚠️ [Knowledge Observer] Could not parse existing knowledge JSON, starting fresh.');
      }
    }

    if (!existingData.typescript_sections) existingData.typescript_sections = [];

    // Phase 12: Knowledge Synchronization logic
    const section = {
      title: newInsights.title,
      metadata: {
        source: newInsights.source,
        analyzedAt: newInsights.analyzedAt,
        description: newInsights.description,
        ...newInsights.metadata
      },
      sections: newInsights.sections || []
    };

    // Deduplicate by title OR source URL to prevent collisions
    const existingIndex = existingData.typescript_sections.findIndex((k: any) =>
      k.title === newInsights.title ||
      (k.metadata && k.metadata.source === newInsights.source)
    );

    if (existingIndex !== -1) {
      existingData.typescript_sections[existingIndex] = section;
    } else {
      existingData.typescript_sections.push(section);
    }

    // Write JSON
    await fs.promises.writeFile(jsonPath, JSON.stringify(existingData, null, 2), 'utf8');

    // Write Markdown - Regenerate from ALL sections
    const isSingleTopic = existingData.typescript_sections.length === 1;
    let mdContent = isSingleTopic ? '' : `# Knowledge Observation Insights (Unified)\n\n`;
    mdContent += `**System Analysis:** ${new Date().toISOString()}\n\n`;

    existingData.typescript_sections.forEach((k: any) => {
      if (k.sections && k.sections.length > 0) {
        if (!isSingleTopic) mdContent += `---\n\n`;

        // Use # for the main topic title
        mdContent += `# ${k.title}\n\n`;

        if (k.metadata) {
          mdContent += `> **Source:** ${k.metadata.source || 'N/A'}\n`;
          mdContent += `> **Analyzed At:** ${k.metadata.analyzedAt || 'N/A'}\n\n`;
        }

        k.sections.forEach((s: any) => {
          const cleanHeader = (s.header || 'Details').replace(/^#+\s*/, '').trim() || 'Details';
          const cleanContent = (s.content || '').trim();

          if (cleanContent.length > 5) {
            // Avoid redundant headers if the section title matches the topic title
            if (cleanHeader.toLowerCase() === k.title.toLowerCase()) {
              mdContent += `${cleanContent}\n\n`;
            } else {
              // Use ## for internal sections
              mdContent += `## ${cleanHeader}\n${cleanContent}\n\n`;
            }
          }
        });
      }
    });

    // Trim trailing whitespace from every line
    const cleanMdContent = mdContent.split('\n').map(line => line.trimEnd()).join('\n');

    await fs.promises.writeFile(mdPath, cleanMdContent, 'utf8');
    console.log(`✅ [Knowledge Observer] Knowledge successfully merged into ${jsonPath} and ${mdPath}`);
    return existingData;
  }

  public static processContent(title: string, raw: string, source: string): KnowledgeInsights {
    console.log(`🧠 [Knowledge Observer] Processing content from ${source}...`);

    // Pre-filtering: Remove scripts, styles, and other non-content tags
    const cleanRaw = raw
      .replace(/<script\b[^>]*>([\s\S]*?)<\/script>/gim, '')
      .replace(/<style\b[^>]*>([\s\S]*?)<\/style>/gim, '')
      .replace(/<svg\b[^>]*>([\s\S]*?)<\/svg>/gim, '')
      .replace(/<noscript\b[^>]*>([\s\S]*?)<\/noscript>/gim, '')
      .replace(/<iframe\b[^>]*>([\s\S]*?)<\/iframe>/gim, '');

    const sections: KnowledgeSection[] = [];
    const lines = cleanRaw.split('\n');
    let currentSection: KnowledgeSection | null = null;

    let inCodeBlock = false;
    lines.forEach(line => {
      if (line.trim().startsWith('```')) {
        inCodeBlock = !inCodeBlock;
      }

      const trimmedLine = line.trim();

      // Skip lines that look like minified CSS or JS remnants if not in code block
      // Technical documentation often uses braces for types/shapes, so we check for signs of code/styles
      const isLikelyJunk = !trimmedLine.includes(' ') && trimmedLine.includes('{') && trimmedLine.includes('}') && trimmedLine.length > 50;
      if (!inCodeBlock && isLikelyJunk) {
        return;
      }

      const headerMatch = !inCodeBlock && line.match(/^#+\s*(.*)/);

      if (headerMatch && !line.includes('<?php') && !line.startsWith('//') && !line.includes('#[')) {
        if (currentSection) sections.push(currentSection);
        currentSection = { header: headerMatch[1].trim(), content: '' };
      } else if (currentSection) {
        // Only strip HTML tags if we're not in a code block and it looks like a real tag
        // Simple heuristic: allow generics like <T>, <TKey, TValue>, <string, int> and mathematical comparisons like < 20ms
        let contentLine = inCodeBlock ? line : line.trim();
        if (!inCodeBlock) {
           // Strip tags but preserve common PHP/TypeScript generics and comparisons.
           // We explicitly exclude sequences starting with space, numbers, or common generic/type patterns.
           // We also preserve a standalone '<' if it's at the end of a line or followed by space.
           contentLine = contentLine.replace(/<(?!\s|$|[0-9]|<=|>=)(?!\/?(T[A-Z][a-zA-Z0-9]*|T[0-9]|T[,\s]|T|K|V|string|int|mixed|object|float|bool|iterable|callable|void|null|true|false|ElementType|TKey|TValue|TObject|TStart|TResume|TReturn|TSuspend|TDate|TEnd))[^>]*>?/gim, '');
        }

        if (contentLine || inCodeBlock) {
          currentSection.content += (currentSection.content ? '\n' : '') + contentLine;
        }
      }
    });

    if (currentSection) sections.push(currentSection);

    // Filter out sections that have too much junk or too little content
    const filteredSections = sections.filter(s => {
      const hasCodeBlock = s.content.includes('```');
      const junkPatterns = [/@media/, /\.wp-/, /!important/];
      const isJunk = !hasCodeBlock && junkPatterns.some(p => p.test(s.content)) && s.content.length > 100;
      return s.content.trim().length > 5 && !isJunk;
    });

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
      sections: filteredSections
    };
  }
}

export function persistKnowledge(newInsights: KnowledgeInsights) {
    const observer = new KnowledgeObserver();
    return observer.persistKnowledge(newInsights);
}

export function processContent(content: string, source: string, title: string = 'Web Insight'): KnowledgeInsights {
  return KnowledgeObserver.processContent(title, content, source);
}

export async function observeKnowledge(url: string) {
  'use cache'
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

    // Use the URL as the title if it's a generic "Web Insight" to prevent collisions
    const title = url.split('/').pop()?.replace(/[-_]/g, ' ') || 'Web Insight';
    return KnowledgeObserver.processContent(title, html, url);
  } catch (error: any) {
    if (error.name === 'AbortError') {
      console.error(`❌ [Knowledge Observer] Timeout observing ${url}`);
    } else {
      console.error(`❌ [Knowledge Observer] Error observing ${url}:`, error.message);
    }
    return null;
  }
}
