import { execSync } from 'child_process'
import * as github from '@actions/github'

/**
 * ANTIGRAVITY GIT PROVIDER SERVICE
 * Abstracted interface for GitHub and GitLab operations.
 */

export interface CommitOptions {
  message: string
  files: string[]
  push?: boolean
  provider?: 'github' | 'gitlab'
  branch?: string
}

export interface PRInfo {
  id: number | string
  title: string
  author: string
  branch: string
  status: 'open' | 'closed' | 'merged'
  provider: 'github' | 'gitlab'
}

export class GitProviderService {
  /**
   * Performs an autonomous commit with GitKraken-optimized formatting.
   */
  public async commit(options: CommitOptions) {
    console.log(`🌿 [GitProvider] Commencing autonomous commit for ${options.provider || 'default'}...`)

    try {
      // 1. Stage files
      const filesToStage = options.files.join(' ')
      execSync(`git add -f ${filesToStage}`)

      // 2. Verify changes
      const status = execSync('git status --porcelain').toString().trim()
      if (!status) {
        console.log('✨ [GitProvider] No changes detected. Skipping commit.')
        return { status: 'skipped', reason: 'no_changes' }
      }

      // 3. Commit
      execSync(`git commit -m "${options.message}"`)
      console.log('✅ [GitProvider] Changes committed locally.')

      // 4. Push if requested
      if (options.push) {
        await this.push(options.provider, options.branch)
      }

      return { status: 'success' }
    } catch (err: any) {
      console.error('❌ [GitProvider] Git operation failed:', err.message)
      throw err
    }
  }

  private async push(provider?: 'github' | 'gitlab', branch: string = 'main') {
    const token = process.env.GITHUB_TOKEN || process.env.GITLAB_TOKEN
    if (!token) {
      console.warn('⚠️ [GitProvider] No authentication token found. Push skipped.')
      return
    }

    try {
      console.log(`🔄 [GitProvider] Synchronizing with remote (${branch})...`)
      if (branch === 'main') {
        execSync('git pull --rebase origin main')
        execSync('git push origin main')
      } else {
        execSync(`git push origin ${branch}`)
      }
      console.log(`🚀 [GitProvider] Changes pushed to origin/${branch}.`)
    } catch (err: any) {
      console.error('❌ [GitProvider] Push failed:', err.message)
      if (branch === 'main') {
        try { execSync('git rebase --abort') } catch (e) {}
      }
    }
  }

  /**
   * Autonomously creates a Pull Request or Merge Request.
   */
  public async createPullRequest(title: string, body: string, head: string, base: string = 'main') {
    console.log(`PR [GitProvider] Creating autonomous PR/MR: ${title}...`)

    // 1. GitHub
    if (process.env.GITHUB_TOKEN) {
      try {
        const octokit = github.getOctokit(process.env.GITHUB_TOKEN)
        const context = github.context
        const { data: pr } = await octokit.rest.pulls.create({
          ...context.repo,
          title,
          body,
          head,
          base
        })
        console.log(`✅ [GitProvider] GitHub PR created: ${pr.html_url}`)
        return pr.number
      } catch (err: any) {
        console.error('❌ [GitProvider] GitHub PR creation failed:', err.message)
      }
    }

    // 2. GitLab (via glab CLI if token present)
    if (process.env.GITLAB_TOKEN) {
      try {
        execSync(`glab mr create --title "${title}" --description "${body}" --head "${head}" --base "${base}" --yes`)
        console.log('✅ [GitProvider] GitLab MR created.')
        return 'gitlab-mr'
      } catch (err: any) {
        console.error('❌ [GitProvider] GitLab MR creation failed:', err.message)
      }
    }

    return null
  }

  /**
   * Lists open Pull Requests for the current repository.
   */
  public async listPullRequests(): Promise<PRInfo[]> {
    const prs: PRInfo[] = []

    // GitHub
    if (process.env.GITHUB_TOKEN) {
      try {
        const octokit = github.getOctokit(process.env.GITHUB_TOKEN)
        const context = github.context
        const { data: pulls } = await octokit.rest.pulls.list({
          ...context.repo,
          state: 'open'
        })
        prs.push(...pulls.map(p => ({
          id: p.number,
          title: p.title,
          author: p.user?.login || 'unknown',
          branch: p.head.ref,
          status: 'open' as const,
          provider: 'github' as const
        })))
      } catch (err) {}
    }

    // GitLab
    if (process.env.GITLAB_TOKEN) {
      try {
        const output = execSync('glab mr list --status open --format json').toString()
        const mrs = JSON.parse(output)
        prs.push(...mrs.map((m: any) => ({
          id: m.iid,
          title: m.title,
          author: m.author.username,
          branch: m.source_branch,
          status: 'open' as const,
          provider: 'gitlab' as const
        })))
      } catch (err) {}
    }

    return prs
  }

  /**
   * Merges a Pull Request if criteria are met.
   */
  public async mergePullRequest(prId: number | string, provider: 'github' | 'gitlab' = 'github') {
    if (provider === 'github' && process.env.GITHUB_TOKEN) {
      try {
        const octokit = github.getOctokit(process.env.GITHUB_TOKEN)
        const context = github.context
        await octokit.rest.pulls.merge({
          ...context.repo,
          pull_number: Number(prId),
          merge_method: 'squash'
        })
        console.log(`✅ [GitProvider] GitHub PR #${prId} merged.`)
        return true
      } catch (err: any) {
        console.error(`❌ [GitProvider] GitHub Merge failed for PR #${prId}:`, err.message)
      }
    } else if (provider === 'gitlab' && process.env.GITLAB_TOKEN) {
      try {
        execSync(`glab mr merge ${prId} --squash --remove-source-branch`)
        console.log(`✅ [GitProvider] GitLab MR !${prId} merged.`)
        return true
      } catch (err: any) {
        console.error(`❌ [GitProvider] GitLab Merge failed for MR !${prId}:`, err.message)
      }
    }

    return false
  }

  /**
   * Formats a commit message with GitKraken roadmap tags.
   */
  public static formatGitKrakenMessage(title: string, phase: string, progress: number, details: string[] = []) {
    const progressBar = this.generateProgressBar(progress)
    let msg = `[ROADMAP:${phase}] ${title}\n\n`
    msg += `Progress: ${progressBar} (${progress}%)\n\n`
    if (details.length > 0) {
      msg += `Details:\n${details.map(d => `- ${d}`).join('\n')}\n\n`
    }
    msg += `Automated by Antigravity Autonomous Engine.`
    return msg
  }

  private static generateProgressBar(percent: number, length: number = 20) {
    const filledLength = Math.round((length * percent) / 100)
    const filled = '█'.repeat(filledLength)
    const empty = '░'.repeat(length - filledLength)
    return filled + empty
  }
}

export const gitProvider = new GitProviderService()
