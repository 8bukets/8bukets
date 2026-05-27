import { execSync } from 'child_process'

/**
 * GIT PROVIDER SERVICE
 * Abstract layer for interacting with GitHub and GitLab.
 */

export interface PullRequest {
  id: string
  title: string
  url: string
  provider: 'github' | 'gitlab'
}

export class GitProviderService {
  private githubToken: string | undefined
  private gitlabToken: string | undefined
  private _execSync: typeof execSync

  constructor(customExec?: typeof execSync) {
    this.githubToken = process.env.GITHUB_TOKEN
    this.gitlabToken = process.env.GITLAB_TOKEN
    this._execSync = customExec || execSync
  }

  /**
   * Detects the remote provider for the current repository.
   */
  public async getActiveProvider(): Promise<'github' | 'gitlab' | 'unknown'> {
    try {
      const remotes = this._execSync('git remote -v').toString()
      if (remotes.includes('github.com')) return 'github'
      if (remotes.includes('gitlab.com')) return 'gitlab'
      return 'unknown'
    } catch (e) {
      return 'unknown'
    }
  }

  /**
   * Creates a Pull Request or Merge Request.
   */
  public async createPR(title: string, body: string, head: string, base: string = 'main'): Promise<PullRequest | null> {
    const provider = await this.getActiveProvider()

    if (provider === 'github') {
      return this.createGitHubPR(title, body, head, base)
    } else if (provider === 'gitlab') {
      return this.createGitLabMR(title, body, head, base)
    }

    console.warn('⚠️ [GitProvider] No supported provider found for PR creation.')
    return null
  }

  private async createGitHubPR(title: string, body: string, head: string, base: string): Promise<PullRequest | null> {
    console.log(`🚀 [GitProvider] Creating GitHub PR: ${title}`)
    try {
      // Use GitHub CLI if available, otherwise fallback to API
      const cmd = `gh pr create --title "${title}" --body "${body}" --head "${head}" --base "${base}"`
      const result = this._execSync(cmd).toString().trim()
      return { id: result, title, url: result, provider: 'github' }
    } catch (e) {
      console.error('❌ [GitProvider] GitHub PR creation failed:', e)
      return null
    }
  }

  private async createGitLabMR(title: string, body: string, head: string, base: string): Promise<PullRequest | null> {
    console.log(`🚀 [GitProvider] Creating GitLab MR: ${title}`)
    try {
      // Use glab CLI if available
      const cmd = `glab mr create --title "${title}" --description "${body}" --head "${head}" --base "${base}" -y`
      const result = this._execSync(cmd).toString().trim()
      return { id: result, title, url: result, provider: 'gitlab' }
    } catch (e) {
      console.error('❌ [GitProvider] GitLab MR creation failed:', e)
      return null
    }
  }

  /**
   * Comments on a PR/MR.
   */
  public async addComment(id: string, comment: string): Promise<boolean> {
    const provider = await this.getActiveProvider()
    try {
      if (provider === 'github') {
        this._execSync(`gh pr comment ${id} --body "${comment}"`)
      } else if (provider === 'gitlab') {
        this._execSync(`glab mr note ${id} --message "${comment}"`)
      }
      return true
    } catch (e) {
      return false
    }
  }

  /**
   * Merges a PR/MR if checks pass.
   */
  public async autonomousMerge(id: string): Promise<boolean> {
    const provider = await this.getActiveProvider()
    console.log(`🔄 [GitProvider] Attempting autonomous merge for ${id} on ${provider}...`)
    try {
      if (provider === 'github') {
        this._execSync(`gh pr merge ${id} --auto --merge`)
      } else if (provider === 'gitlab') {
        this._execSync(`glab mr merge ${id} --when-pipeline-succeeds`)
      }
      return true
    } catch (e) {
      return false
    }
  }
}

export const gitProviderService = new GitProviderService()
