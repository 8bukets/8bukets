/**
 * GITHUB DOCUMENTATION OBSERVER
 * Autonomously extracts technical knowledge from GitHub markdown documentation.
 */

export interface GithubDocInsight {
  source: string;
  file: string;
  sections: { title: string; content: string }[];
  analyzedAt: string;
  rawUrl: string;
}

export class GithubDocsObserver {
  /**
   * fetchDoc: Single file version expected by IntelephenseService and consolidate_intelephense script.
   */
  public async fetchDoc(owner: string, repo: string, file: string): Promise<GithubDocInsight> {
    const rawUrl = `https://raw.githubusercontent.com/${owner}/${repo}/master/${file}`
    const response = await fetch(rawUrl)
    if (!response.ok) {
      throw new Error(`Failed to fetch ${file}: ${response.statusText}`)
    }
    const markdown = await response.text()
    const sections: { title: string; content: string }[] = []

    // Split by markdown headers
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

    return {
      source: `https://github.com/${owner}/${repo}`,
      file,
      sections,
      analyzedAt: new Date().toISOString(),
      rawUrl
    }
  }

  /**
   * observeGithubDocs: Batch version.
   */
  public async observeGithubDocs(repo: string, files: string[]): Promise<GithubDocInsight[]> {
    console.log(`👁️ [GitHub Docs Observer] Scanning ${repo} for technical insights...`)
    const insights: GithubDocInsight[] = []
    const [owner, name] = repo.split('/')

    for (const file of files) {
      try {
        const insight = await this.fetchDoc(owner, name, file)
        insights.push(insight)
        console.log(`✅ [GitHub Docs Observer] Extracted ${insight.sections.length} sections from ${file}`)
      } catch (error: any) {
        console.error(`❌ [GitHub Docs Observer] Error observing ${file}:`, error.message)
      }
    }
    return insights
  }
}

export const githubDocsObserver = new GithubDocsObserver()

/**
 * Legacy standalone function export.
 */
export async function observeGithubDocs(repo: string, files: string[]): Promise<GithubDocInsight[]> {
  return githubDocsObserver.observeGithubDocs(repo, files)
}
