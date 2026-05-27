import fs from 'fs';
import path from 'path';

export interface KnowledgeInsights {
  source: string;
  title: string;
  description: string;
  topKeywords: string[];
  recentPosts: { title: string; link: string }[];
  analyzedAt: string;
  history?: { source: string; analyzedAt: string }[];
}

export function persistKnowledge(newInsights: KnowledgeInsights) {
  const jsonPath = path.join(process.cwd(), 'ai_agents_knowledge.json');
  const mdPath = path.join(process.cwd(), 'ai_agents_knowledge.md');

  let existingData: any = { topKeywords: [], recentPosts: [], history: [] };

  if (fs.existsSync(jsonPath)) {
    try {
      existingData = JSON.parse(fs.readFileSync(jsonPath, 'utf8'));
    } catch (e) {
      console.warn('⚠️ [Knowledge Observer] Could not parse existing knowledge JSON, starting fresh.');
    }
  }

  // Merging Logic
  const mergedKeywords = Array.from(new Set([...(existingData.topKeywords || []), ...newInsights.topKeywords])).slice(0, 30);

  // Filter out duplicates for recent posts based on link
  const existingLinks = new Set(existingData.recentPosts?.map((p: any) => p.link) || []);
  const newUniquePosts = newInsights.recentPosts.filter(p => !existingLinks.has(p.link));
  const mergedPosts = [...newUniquePosts, ...(existingData.recentPosts || [])].slice(0, 50);

  const history = existingData.history || [];
  history.push({ source: newInsights.source, analyzedAt: newInsights.analyzedAt });

  const finalInsights = {
    source: newInsights.source, // Keep the latest source as primary
    title: newInsights.title,
    description: newInsights.description,
    topKeywords: mergedKeywords,
    recentPosts: mergedPosts,
    history: history.slice(-10), // Keep last 10 sources
    analyzedAt: newInsights.analyzedAt
  };

  // Write JSON
  fs.writeFileSync(jsonPath, JSON.stringify(finalInsights, null, 2), 'utf8');

  // Write Markdown
  let mdContent = `# Knowledge Observation Insights (Unified)\n\n`;
  mdContent += `**Latest Source:** ${finalInsights.source}\n`;
  mdContent += `**Latest Analysis:** ${finalInsights.analyzedAt}\n\n`;

  mdContent += `## 🔑 Top Keywords (Merged)\n`;
  finalInsights.topKeywords.forEach((kw: string) => {
    mdContent += `- ${kw}\n`;
  });
  mdContent += `\n`;

  mdContent += `## 📰 Recent Intelligence & Posts\n`;
  finalInsights.recentPosts.forEach((post: { title: string; link: string }) => {
    mdContent += `- [${post.title}](${post.link})\n`;
  });
  mdContent += `\n`;

  mdContent += `## 📜 Observation History\n`;
  finalInsights.history.forEach((h: any) => {
    mdContent += `- ${h.source} (${h.analyzedAt})\n`;
  });

  fs.writeFileSync(mdPath, mdContent, 'utf8');
  console.log(`✅ [Knowledge Observer] Knowledge successfully merged into ${jsonPath} and ${mdPath}`);
  return finalInsights;
}

export function processContent(html: string, source: string): KnowledgeInsights {
  console.log(`🧠 [Knowledge Observer] Processing content from ${source}...`);

  // Very simple heuristic: look for <title>, some standard meta tags or just general size
  const titleMatch = html.match(/<title[^>]*>([^<]+)<\/title>/i);
  const title = titleMatch ? titleMatch[1].trim() : (source.startsWith('http') ? 'Unknown Title' : 'Direct Document');

  const metaDescriptionMatch = html.match(/<meta[^>]*name=["']description["'][^>]*content=["']([^"']*)["'][^>]*>/i);
  const description = metaDescriptionMatch ? metaDescriptionMatch[1].trim() : 'No description found';

  // Extract recent post titles and links
  const recentPosts: { title: string, link: string }[] = [];
  const linkRegex = /<h[1-3][^>]*>.*?<a[^>]*href=["']([^"']+)["'][^>]*>(.*?)<\/a>.*?<\/h[1-3]>/gi;
  let match;

  while ((match = linkRegex.exec(html)) !== null) {
    const link = match[1];
    const postTitle = match[2].replace(/<[^>]*>?/gm, '').replace(/&nbsp;/g, ' ').trim();

    // Filter out general links, attempt to capture actual articles (usually have dates or specific path structure)
    if (postTitle && link && !recentPosts.some(p => p.link === link) && postTitle.toLowerCase() !== 'software info by fk') {
        recentPosts.push({ title: postTitle, link });
    }
  }

  // Limit to top 15 recent posts
  const topRecentPosts = recentPosts.slice(0, 15);

  // Remove inline scripts and styles before keyword extraction
  const cleanHtml = html
    .replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, ' ')
    .replace(/<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>/gi, ' ');

  // Naive keyword extraction based on frequency (excluding common stop words)
  const words = cleanHtml
    .replace(/<[^>]*>?/gm, ' ') // remove HTML tags
    .replace(/[^a-zA-Z\s]/g, ' ') // remove non-alpha
    .toLowerCase()
    .split(/\s+/)
    .filter(w => w.length > 4); // filter short words

  const stopWords = new Set(['about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'aren', 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'cannot', 'could', 'couldn', 'did', 'didn', 'do', 'does', 'doesn', 'doing', 'don', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'hadn', 'has', 'hasn', 'have', 'haven', 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'however', 'i', 'if', 'in', 'into', 'is', 'isn', 'it', 'its', 'itself', 'let', 'me', 'more', 'most', 'mustn', 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', 'shan', 'she', 'should', 'shouldn', 'so', 'some', 'such', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'wasn', 'we', 'were', 'weren', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'with', 'won', 'would', 'wouldn', 'you', 'your', 'yours', 'yourself', 'yourselves', 'their', 'there', 'class', 'style', 'href', 'https', 'http', 'width', 'height', 'content', 'content', 'title', 'xmlns', 'svg', 'viewbox', 'path', 'fill', 'stroke', 'margin', 'padding', 'false', 'true', 'null', 'undefined', 'function', 'return', 'const', 'let', 'var', 'document', 'window', 'script', 'iframe', 'src', 'alt', 'data']);

  const wordCounts = new Map<string, number>();
  for (const w of words) {
    if (!stopWords.has(w)) {
      wordCounts.set(w, (wordCounts.get(w) || 0) + 1);
    }
  }

  const topKeywords = Array.from(wordCounts.entries())
    .sort((a, b) => b[1] - a[1])
    .slice(0, 15) // Slightly increased for more depth
    .map(entry => entry[0]);

  const insights = {
    source: source,
    title,
    description,
    topKeywords,
    recentPosts: topRecentPosts,
    analyzedAt: new Date().toISOString()
  };

  console.log(`✅ [Knowledge Observer] Extracted ${topKeywords.length} key concepts.`);
  return insights;
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

    return processContent(html, url);
  } catch (error: any) {
    if (error.name === 'AbortError') {
      console.error(`❌ [Knowledge Observer] Timeout observing ${url}`);
    } else {
      console.error(`❌ [Knowledge Observer] Error observing ${url}:`, error.message);
    }
    return null;
  }
}
