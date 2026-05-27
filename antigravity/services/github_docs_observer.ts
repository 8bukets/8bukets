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
 * observeGithubDocs: Standalone function to fetch multiple docs from a repo.
 */
export async function observeGithubDocs(repoPath: string, files: string[]): Promise<GithubDocs[]> {
  'use cache'
  const [owner, repo] = repoPath.split('/')
  const results: GithubDocs[] = []

  for (const file of files) {
    try {
      const doc = await githubDocsObserver.fetchDoc(owner, repo, file)
      results.push(doc)
    } catch (err) {
      console.error(` ❌ [GithubDocsObserver] Failed to fetch ${file}:`, err)
    }
  }

  return results
}

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
   * Improved to handle empty sections, nested headers, and link-only titles.
   * Ensures headers are captured even if content is empty.
   */
  private parseMarkdown(markdown: string): { title: string; content: string }[] {
    const sections: { title: string; content: string }[] = []

    const lines = markdown.split('\n')
    let currentTitle = 'Overview'
    let currentContent: string[] = []

    for (const line of lines) {
      const headerMatch = line.match(/^#+\s+(.*)$/)
      if (headerMatch) {
        // Save previous section. We capture it even if content is empty to ensure headers are preserved.
        const content = currentContent.join('\n').trim()

        // We always push the section if it has a title, unless it's the initial empty Overview
        if (currentTitle !== 'Overview' || content !== '') {
          sections.push({
            title: currentTitle,
            content: content
          })
        }

        // Clean up title: Extract text from link-only headers like "### [Features](features.md)"
        let nextTitle = headerMatch[1].trim()
        const linkMatch = nextTitle.match(/^\[(.*)\]\(.*\)$/)
        if (linkMatch) {
          nextTitle = linkMatch[1]
        }

        currentTitle = nextTitle
        currentContent = []
      } else {
        currentContent.push(line)
      }
    }

    // Push final section
    const finalContent = currentContent.join('\n').trim()
    if (currentTitle !== 'Overview' || finalContent !== '') {
      sections.push({
        title: currentTitle,
        content: finalContent
      })
    }

    // Filter: Remove sections that are strictly empty Overview placeholders.
    // We keep empty sections with meaningful titles (like "Features" in features.md).
    return sections.filter(s => {
      const isPlaceholder = s.content === '' && (s.title === 'Overview' || s.title.toLowerCase().includes('placeholder'))
      return !isPlaceholder && s.title !== ''
    })
  }
}

export const githubDocsObserver = new GithubDocsObserver()
