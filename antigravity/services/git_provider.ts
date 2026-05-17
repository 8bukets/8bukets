import { logAutonomousAction } from '../core'
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
    logAutonomousAction(`🌿 [GitProvider] Commencing autonomous commit for ${options.provider || 'default'}...`, 'info')

    try {
      // 1. Stage files
      const filesToStage = options.files.join(' ')
      execSync(`git add -f ${filesToStage}`)

      // 2. Verify changes
      const status = execSync('git status --porcelain').toString().trim()
      if (!status) {
        logAutonomousAction('✨ [GitProvider] No changes detected. Skipping commit.', 'info')
        return { status: 'skipped', reason: 'no_changes' }
      }

      // 3. Commit
      execSync(`git commit -m "${options.message}"`)
      logAutonomousAction('✅ [GitProvider] Changes committed locally.', 'info')

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
      logAutonomousAction(`🔄 [GitProvider] Synchronizing with remote (${branch}, 'info')...`)
      if (branch === 'main') {
        execSync('git pull --rebase origin main')
        execSync('git push origin main')
      } else {
        execSync(`git push origin ${branch}`)
      }
      logAutonomousAction(`🚀 [GitProvider] Changes pushed to origin/${branch}.`, 'info')
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
    logAutonomousAction(`PR [GitProvider] Creating autonomous PR/MR: ${title}...`, 'info')

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
        logAutonomousAction(`✅ [GitProvider] GitHub PR created: ${pr.html_url}`, 'info')
        return pr.number
      } catch (err: any) {
        console.error('❌ [GitProvider] GitHub PR creation failed:', err.message)
      }
    }

    // GitLab (via glab CLI or REST API fallback)
    if (process.env.GITLAB_TOKEN) {
      try {
        execSync(`glab mr create --title "${title}" --description "${body}" --source-branch "${head}" --target-branch "${base}" --yes`)
        logAutonomousAction('✅ [GitProvider] GitLab MR created via glab.', 'info')
        return 'gitlab-mr'
      } catch (err: any) {
        console.warn('⚠️ [GitProvider] GitLab MR creation via glab failed. Attempting REST API fallback...')
        const projectId = process.env.CI_PROJECT_ID
        if (projectId) {
          try {
            const response = await fetch(`https://gitlab.com/api/v4/projects/${projectId}/merge_requests`, {
              method: 'POST',
              headers: {
                'PRIVATE-TOKEN': process.env.GITLAB_TOKEN,
                'Content-Type': 'application/json'
              },
              body: JSON.stringify({
                source_branch: head,
                target_branch: base,
                title,
                description: body
              })
            })
            const data = await response.json()
            if (response.ok) {
              logAutonomousAction(`✅ [GitProvider] GitLab MR created via API: ${data.web_url}`, 'info')
              return data.iid
            } else {
              console.error('❌ [GitProvider] GitLab API MR creation failed:', data.message)
            }
          } catch (apiErr: any) {
            console.error('❌ [GitProvider] GitLab API fallback failed:', apiErr.message)
          }
        }
      }
    }

    return null
  }

  /**
   * Verifies CI checks for a specific branch.
   */
  public async verifyCIStatus(branch: string, provider: 'github' | 'gitlab' = 'github'): Promise<boolean> {
    if (provider === 'github' && process.env.GITHUB_TOKEN) {
      try {
        const octokit = github.getOctokit(process.env.GITHUB_TOKEN)
        const context = github.context
        const { data } = await octokit.rest.checks.listForRef({
          ...context.repo,
          ref: branch
        })

        if (data.check_runs.length === 0) return true; // No checks is treated as passed

        return data.check_runs.every(check => check.status === 'completed' && check.conclusion === 'success')
      } catch (err: any) {
        console.error(`❌ [GitProvider] GitHub verifyCIStatus failed for ${branch}:`, err.message)
        return false;
      }
    }
    // GitLab could be implemented similarly using glab or raw curl
    return false; // default to false if provider not supported or missing token to prevent unsafe merges
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
      } catch (err) {
        const projectId = process.env.CI_PROJECT_ID
        if (projectId) {
          try {
            const response = await fetch(`https://gitlab.com/api/v4/projects/${projectId}/merge_requests?state=opened`, {
              headers: { 'PRIVATE-TOKEN': process.env.GITLAB_TOKEN }
            })
            if (response.ok) {
              const mrs = await response.json()
              prs.push(...mrs.map((m: any) => ({
                id: m.iid,
                title: m.title,
                author: m.author.username,
                branch: m.source_branch,
                status: 'open' as const,
                provider: 'gitlab' as const
              })))
            }
          } catch (e) {}
        }
      }
    }

    return prs
  }

  /**
   * Merges a Pull Request if criteria are met.
   */
  public async mergePullRequest(prId: number | string, provider: 'github' | 'gitlab' = 'github') {
    // Protocol Audit: Ensure we are not merging in a restricted environment without a token
    const token = process.env.GITHUB_TOKEN || process.env.GITLAB_TOKEN
    if (!token) {
      console.warn(`⚠️ [GitProvider] Cannot merge ${provider} PR/MR #${prId} without authentication token.`)
      return false
    }

    if (provider === 'github' && process.env.GITHUB_TOKEN) {
      try {
        const octokit = github.getOctokit(process.env.GITHUB_TOKEN)
        const context = github.context
        await octokit.rest.pulls.merge({
          ...context.repo,
          pull_number: Number(prId),
          merge_method: 'squash'
        })
        logAutonomousAction(`✅ [GitProvider] GitHub PR #${prId} merged.`, 'info')
        return true
      } catch (err: any) {
        console.error(`❌ [GitProvider] GitHub Merge failed for PR #${prId}:`, err.message)
      }
    } else if (provider === 'gitlab' && process.env.GITLAB_TOKEN) {
      try {
        execSync(`glab mr merge ${prId} --squash --remove-source-branch`)
        logAutonomousAction(`✅ [GitProvider] GitLab MR !${prId} merged via glab.`, 'info')
        return true
      } catch (err: any) {
        console.warn(`⚠️ [GitProvider] GitLab Merge via glab failed for MR !${prId}. Attempting API fallback...`)
        const projectId = process.env.CI_PROJECT_ID
        if (projectId) {
          try {
            const response = await fetch(`https://gitlab.com/api/v4/projects/${projectId}/merge_requests/${prId}/merge`, {
              method: 'PUT',
              headers: { 'PRIVATE-TOKEN': process.env.GITLAB_TOKEN },
              body: JSON.stringify({ squash: true, should_remove_source_branch: true })
            })
            if (response.ok) {
              logAutonomousAction(`✅ [GitProvider] GitLab MR !${prId} merged via API.`, 'info')
              return true
            } else {
              const data = await response.json()
              console.error(`❌ [GitProvider] GitLab API Merge failed:`, data.message)
            }
          } catch (apiErr: any) {
            console.error(`❌ [GitProvider] GitLab API fallback failed:`, apiErr.message)
          }
        }
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
