import { z } from 'zod'
import { autonomousFetch } from '@/antigravity/core'

export const GithubDocSectionSchema = z.object({
  title: z.string(),
  content: z.string()
})

export const GithubDocsSchema = z.object({
  repo: z.string(),
  file: z.string(),
  sections: z.array(GithubDocSectionSchema),
  rawUrl: z.string(),
  lastUpdated: z.string()
})

export type GithubDocs = z.infer<typeof GithubDocsSchema>

/**
 * GITHUB DOCS OBSERVER
 * Autonomously extracts technical sections from raw GitHub markdown files.
 */
export class GithubDocsObserver {
  private baseUrl = 'https://raw.githubusercontent.com'

  /**
   * fetchDoc: Retrieves and parses a markdown file from GitHub.
   */
  public async fetchDoc(owner: string, repo: string, path: string, branch: string = 'master'): Promise<GithubDocs> {
    const rawUrl = `${this.baseUrl}/${owner}/${repo}/${branch}/${path}`

    return autonomousFetch(GithubDocsSchema, async () => {
      console.log(`📡 [GithubDocsObserver] Fetching: ${owner}/${repo}/${path}...`)
      const response = await fetch(rawUrl)

      if (!response.ok) {
        throw new Error(`Failed to fetch doc from GitHub: ${response.statusText}`)
      }

      const markdown = await response.text()
      const sections = this.parseMarkdown(markdown)

      return {
        repo: `${owner}/${repo}`,
        file: path,
        sections,
        rawUrl,
        lastUpdated: new Date().toISOString()
      }
    }, { life: 'catalog', tags: [`github-docs-${repo}-${path.replace(/\//g, '-')}`] })
  }

  /**
   * parseMarkdown: Extracts sections based on markdown headers.
   * Improved to handle empty sections and nested headers.
   */
  private parseMarkdown(markdown: string): { title: string; content: string }[] {
    const sections: { title: string; content: string }[] = []

    const lines = markdown.split('\n')
    let currentTitle = 'Overview'
    let currentContent: string[] = []

    for (const line of lines) {
      const headerMatch = line.match(/^#+\s+(.*)$/)
      if (headerMatch) {
        // Save previous section if it has content or isn't the default Overview
        if (currentContent.length > 0 || currentTitle !== 'Overview') {
          sections.push({
            title: currentTitle,
            content: currentContent.join('\n').trim()
          })
        }
        currentTitle = headerMatch[1]
        currentContent = []
      } else {
        currentContent.push(line)
      }
    }

    // Push final section
    sections.push({
      title: currentTitle,
      content: currentContent.join('\n').trim()
    })

    return sections.filter(s => s.title !== 'Overview' || s.content !== '')
  }
}

export const githubDocsObserver = new GithubDocsObserver()
