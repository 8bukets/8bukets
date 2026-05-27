/**
 * GITHUB DOCUMENTATION OBSERVER
 * Autonomously extracts technical knowledge from GitHub markdown documentation.
 */

export interface GithubDocInsight {
  source: string;
  file: string;
  sections: { title: string; content: string }[];
  analyzedAt: string;
}

export async function observeGithubDocs(repo: string, files: string[]): Promise<GithubDocInsight[]> {
  console.log(`👁️ [GitHub Docs Observer] Scanning ${repo} for technical insights...`)

  const insights: GithubDocInsight[] = []

  for (const file of files) {
    const url = `https://raw.githubusercontent.com/${repo}/master/${file}`
    try {
      const response = await fetch(url)
      if (!response.ok) {
        console.warn(`⚠️ [GitHub Docs Observer] Failed to fetch ${file}: ${response.statusText}`)
        continue
      }
      const markdown = await response.text()

      const sections: { title: string; content: string }[] = []

      // Robust Markdown header split supporting various header levels
      const parts = markdown.split(/^(?=#+\s+)/m)

      for (const part of parts) {
        if (!part.trim()) continue

        const headerMatch = part.match(/^(#+)\s+(.*)/)
        if (headerMatch) {
          const title = headerMatch[2].trim()
          const content = part.substring(headerMatch[0].length).trim()

          if (title) {
            sections.push({ title, content })
          }
        }
      }

      insights.push({
        source: `https://github.com/${repo}`,
        file,
        sections,
        analyzedAt: new Date().toISOString()
      })

      console.log(`✅ [GitHub Docs Observer] Extracted ${sections.length} sections from ${file}`)
    } catch (error: any) {
      console.error(`❌ [GitHub Docs Observer] Error observing ${file}:`, error.message)
    }
  }

  return insights
}
