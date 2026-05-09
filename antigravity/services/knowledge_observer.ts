export async function observeKnowledge(url: string) {
  console.log(`👁️ [Knowledge Observer] Scanning ${url} for autonomous insights...`)
  try {
    const response = await fetch(url)
    if (!response.ok) {
      throw new Error(`Failed to fetch ${url}: ${response.statusText}`)
    }
    const html = await response.text()

    // Very simple heuristic: look for <title>, some standard meta tags or just general size
    const titleMatch = html.match(/<title[^>]*>([^<]+)<\/title>/i)
    const title = titleMatch ? titleMatch[1].trim() : 'Unknown Title'

    const metaDescriptionMatch = html.match(/<meta[^>]*name=["']description["'][^>]*content=["']([^"']*)["'][^>]*>/i)
    const description = metaDescriptionMatch ? metaDescriptionMatch[1].trim() : 'No description found'

    // Extract recent post titles and links
    const recentPosts: { title: string, link: string }[] = []
    const linkRegex = /<h[1-3][^>]*>.*?<a[^>]*href=["']([^"']+)["'][^>]*>(.*?)<\/a>.*?<\/h[1-3]>/gi
    let match

    while ((match = linkRegex.exec(html)) !== null) {
      const link = match[1]
      const postTitle = match[2].replace(/<[^>]*>?/gm, '').replace(/&nbsp;/g, ' ').trim()

      // Filter out general links, attempt to capture actual articles (usually have dates or specific path structure)
      if (postTitle && link && !recentPosts.some(p => p.link === link) && postTitle.toLowerCase() !== 'software info by fk') {
          recentPosts.push({ title: postTitle, link })
      }
    }

    // Limit to top 15 recent posts
    const topRecentPosts = recentPosts.slice(0, 15)

    // Remove inline scripts and styles before keyword extraction
    const cleanHtml = html
      .replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, ' ')
      .replace(/<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>/gi, ' ')

    // Naive keyword extraction based on frequency (excluding common stop words)
    const words = cleanHtml
      .replace(/<[^>]*>?/gm, ' ') // remove HTML tags
      .replace(/[^a-zA-Z\s]/g, ' ') // remove non-alpha
      .toLowerCase()
      .split(/\s+/)
      .filter(w => w.length > 4) // filter short words

    const stopWords = new Set(['about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'aren', 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'can', 'cannot', 'could', 'couldn', 'did', 'didn', 'do', 'does', 'doesn', 'doing', 'don', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'hadn', 'has', 'hasn', 'have', 'haven', 'having', 'he', 'her', 'here', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'however', 'i', 'if', 'in', 'into', 'is', 'isn', 'it', 'its', 'itself', 'let', 'me', 'more', 'most', 'mustn', 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', 'shan', 'she', 'should', 'shouldn', 'so', 'some', 'such', 'than', 'that', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'these', 'they', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'wasn', 'we', 'were', 'weren', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'with', 'won', 'would', 'wouldn', 'you', 'your', 'yours', 'yourself', 'yourselves', 'their', 'there', 'class', 'style', 'href', 'https', 'http', 'width', 'height', 'content', 'content', 'title', 'xmlns', 'svg', 'viewbox', 'path', 'fill', 'stroke', 'margin', 'padding', 'false', 'true', 'null', 'undefined', 'function', 'return', 'const', 'let', 'var', 'document', 'window', 'script', 'iframe', 'src', 'alt', 'data'])

    const wordCounts = new Map<string, number>()
    for (const w of words) {
      if (!stopWords.has(w)) {
        wordCounts.set(w, (wordCounts.get(w) || 0) + 1)
      }
    }

    const topKeywords = Array.from(wordCounts.entries())
      .sort((a, b) => b[1] - a[1])
      .slice(0, 10)
      .map(entry => entry[0])

    const insights = {
      source: url,
      title,
      description,
      topKeywords,
      recentPosts: topRecentPosts,
      analyzedAt: new Date().toISOString()
    }

    console.log(`✅ [Knowledge Observer] Extracted ${topKeywords.length} key concepts and ${topRecentPosts.length} recent posts.`)
    return insights
  } catch (error: any) {
    console.error(`❌ [Knowledge Observer] Error observing ${url}:`, error.message)
    return null
  }
}
