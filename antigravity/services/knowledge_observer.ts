import fs from 'fs';
import path from 'path';

export interface KnowledgeSection {
  header: string;
  content: string;
}

export interface Knowledge {
  title: string;
  sections: KnowledgeSection[];
  metadata?: {
    source: string;
    ingestedAt: string;
  };
}

export interface KnowledgeInsights {
  source: string;
  title: string;
  description: string;
  topKeywords: string[];
  recentPosts: { title: string; link: string }[];
  analyzedAt: string;
  history?: { source: string; analyzedAt: string }[];
}

export class KnowledgeObserver {
  /**
   * processContent: Splits raw content into sections (Title, Content, Source).
   * Restored for compatibility with intelephense_service and consolidate_intelephense.
   */
  public static processContent(title: string, content: string, source: string): Knowledge {
    console.log(`🧠 [Knowledge Observer] Processing content for: ${title}`);

    const sections: KnowledgeSection[] = [];
    // Split by markdown headers
    const parts = content.split(/^(?=#+\s+)/m);

    for (const part of parts) {
      if (!part.trim()) continue;

      const headerMatch = part.match(/^(#+)\s+(.*)/);
      if (headerMatch) {
        const header = headerMatch[2].trim();
        const sectionContent = part.substring(headerMatch[0].length).trim();
        sections.push({ header, content: sectionContent });
      } else {
        // No header found, use title as header if sections is empty
        if (sections.length === 0) {
          sections.push({ header: title, content: part.trim() });
        } else {
          // Append to last section
          sections[sections.length - 1].content += '\n\n' + part.trim();
        }
      }
    }

    return {
      title,
      sections,
      metadata: {
        source,
        ingestedAt: new Date().toISOString()
      }
    };
  }

  /**
   * persistKnowledge: Saves consolidated knowledge to JSON and Markdown.
   * Handles both new Knowledge format and legacy KnowledgeInsights format.
   */
  public async persistKnowledge(knowledge: Knowledge | KnowledgeInsights, domain: string = 'General'): Promise<void> {
    const storageDir = path.join(process.cwd(), 'data/knowledge');
    if (!fs.existsSync(storageDir)) {
      fs.mkdirSync(storageDir, { recursive: true });
    }

    const filename = (knowledge.title || 'unknown').toLowerCase().replace(/\s+/g, '_').replace(/[^\w]/g, '') + '.json';
    const jsonPath = path.join(storageDir, filename);

    console.log(`✅ [Knowledge Observer] Persisted "${knowledge.title}" to ${storageDir}`);

    if ('sections' in knowledge) {
      // New format handling
      fs.writeFileSync(jsonPath, JSON.stringify(knowledge, null, 2), 'utf8');

      // Update system_knowledge.json if applicable
      const systemStore = path.join(storageDir, 'system_knowledge.json');
      let systemData: any = { typescript_sections: [] };
      if (fs.existsSync(systemStore)) {
        try {
          systemData = JSON.parse(fs.readFileSync(systemStore, 'utf8'));
        } catch (e) {}
      }

      if (!systemData.typescript_sections) systemData.typescript_sections = [];

      // Add or update entries
      const existingIdx = systemData.typescript_sections.findIndex((s: any) => s.title === knowledge.title);
      if (existingIdx !== -1) {
        systemData.typescript_sections[existingIdx] = knowledge;
      } else {
        systemData.typescript_sections.push(knowledge);
      }

      fs.writeFileSync(systemStore, JSON.stringify(systemData, null, 2), 'utf8');
    } else {
      // Legacy format handling (ai_agents_knowledge logic)
      const legacyJsonPath = path.join(process.cwd(), 'ai_agents_knowledge.json');
      const legacyMdPath = path.join(process.cwd(), 'ai_agents_knowledge.md');

      let existingData: any = { topKeywords: [], recentPosts: [], history: [] };
      if (fs.existsSync(legacyJsonPath)) {
        try {
          existingData = JSON.parse(fs.readFileSync(legacyJsonPath, 'utf8'));
        } catch (e) {}
      }

      const mergedKeywords = Array.from(new Set([...(existingData.topKeywords || []), ...knowledge.topKeywords])).slice(0, 30);
      const existingLinks = new Set(existingData.recentPosts?.map((p: any) => p.link) || []);
      const newUniquePosts = knowledge.recentPosts.filter(p => !existingLinks.has(p.link));
      const mergedPosts = [...newUniquePosts, ...(existingData.recentPosts || [])].slice(0, 50);
      const history = existingData.history || [];
      history.push({ source: knowledge.source, analyzedAt: knowledge.analyzedAt });

      const finalInsights = {
        ...knowledge,
        topKeywords: mergedKeywords,
        recentPosts: mergedPosts,
        history: history.slice(-10)
      };

      fs.writeFileSync(legacyJsonPath, JSON.stringify(finalInsights, null, 2), 'utf8');

      let mdContent = `# Knowledge Observation Insights (Unified)\n\n`;
      mdContent += `**Latest Source:** ${finalInsights.source}\n`;
      mdContent += `**Latest Analysis:** ${finalInsights.analyzedAt}\n\n`;
      mdContent += `## 🔑 Top Keywords (Merged)\n`;
      finalInsights.topKeywords.forEach((kw: string) => { mdContent += `- ${kw}\n`; });
      mdContent += `\n## 📰 Recent Intelligence & Posts\n`;
      finalInsights.recentPosts.forEach((post: { title: string; link: string }) => { mdContent += `- [${post.title}](${post.link})\n`; });
      mdContent += `\n## 📜 Observation History\n`;
      finalInsights.history.forEach((h: any) => { mdContent += `- ${h.source} (${h.analyzedAt})\n`; });

      fs.writeFileSync(legacyMdPath, mdContent, 'utf8');
    }
  }
}

/**
 * processLegacyContent: Original processContent logic renamed but compatible with KnowledgeInsights.
 */
export function processContent(html: string, source: string): KnowledgeInsights {
  console.log(`🧠 [Knowledge Observer] Processing content from ${source}...`);

  const titleMatch = html.match(/<title[^>]*>([^<]+)<\/title>/i);
  const title = titleMatch ? titleMatch[1].trim() : (source.startsWith('http') ? 'Unknown Title' : 'Direct Document');

  const metaDescriptionMatch = html.match(/<meta[^>]*name=["']description["'][^>]*content=["']([^"']*)["'][^>]*>/i);
  const description = metaDescriptionMatch ? metaDescriptionMatch[1].trim() : 'No description found';

  const recentPosts: { title: string, link: string }[] = [];
  const linkRegex = /<h[1-3][^>]*>.*?<a[^>]*href=["']([^"']+)["'][^>]*>(.*?)<\/a>.*?<\/h[1-3]>/gi;
  let match;

  while ((match = linkRegex.exec(html)) !== null) {
    const link = match[1];
    const postTitle = match[2].replace(/<[^>]*>?/gm, '').replace(/&nbsp;/g, ' ').trim();
    if (postTitle && link && !recentPosts.some(p => p.link === link) && postTitle.toLowerCase() !== 'software info by fk') {
        recentPosts.push({ title: postTitle, link });
    }
  }

  const cleanHtml = html
    .replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, ' ')
    .replace(/<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>/gi, ' ');

  const words = cleanHtml
    .replace(/<[^>]*>?/gm, ' ')
    .replace(/[^a-zA-Z\s]/g, ' ')
    .toLowerCase()
    .split(/\s+/)
    .filter(w => w.length > 4);

  const stopWords = new Set(['about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'aren', 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'cannot', 'could', 'couldn', 'did', 'didn', 'do', 'does', 'doesn', 'doing', 'don', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'hadn', 'has', 'hasn', 'have', 'haven', 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'however', 'i', 'if', 'in', 'into', 'is', 'isn', 'it', 'its', 'itself', 'let', 'me', 'more', 'most', 'mustn', 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', 'shan', 'she', 'should', 'shouldn', 'so', 'some', 'such', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'wasn', 'we', 'were', 'weren', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'with', 'won', 'would', 'wouldn', 'you', 'your', 'yours', 'yourself', 'yourselves', 'their', 'there', 'class', 'style', 'href', 'https', 'http', 'width', 'height', 'content', 'title', 'xmlns', 'svg', 'viewbox', 'path', 'fill', 'stroke', 'margin', 'padding', 'false', 'true', 'null', 'undefined', 'function', 'return', 'const', 'let', 'var', 'document', 'window', 'script', 'iframe', 'src', 'alt', 'data']);

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
    source: source,
    title,
    description,
    topKeywords,
    recentPosts: recentPosts.slice(0, 15),
    analyzedAt: new Date().toISOString()
  };
}

export function persistKnowledge(newInsights: KnowledgeInsights) {
  const observer = new KnowledgeObserver();
  return observer.persistKnowledge(newInsights);
}

export async function observeKnowledge(url: string) {
  console.log(`👁️ [Knowledge Observer] Scanning ${url} for autonomous insights...`);
  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 10000);

    const response = await fetch(url, { signal: controller.signal });
    clearTimeout(timeoutId);

    if (!response.ok) throw new Error(`Failed to fetch ${url}: ${response.statusText}`);
    const html = await response.text();
    if (!html || html.length < 100) throw new Error(`Received insufficient content from ${url}`);

    return processContent(html, url);
  } catch (error: any) {
    console.error(`❌ [Knowledge Observer] Error observing ${url}:`, error.message);
    return null;
  }
}
