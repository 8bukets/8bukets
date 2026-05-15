import { execSync } from 'child_process'

/**
 * ANTIGRAVITY GIT PROVIDER SERVICE
 * Abstracted interface for GitHub and GitLab operations.
 */

export interface CommitOptions {
  message: string
  files: string[]
  push?: boolean
  provider?: 'github' | 'gitlab'
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
      execSync(`git add ${filesToStage}`)

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
        await this.push(options.provider)
      }

      return { status: 'success' }
    } catch (err: any) {
      console.error('❌ [GitProvider] Git operation failed:', err.message)
      throw err
    }
  }

  private async push(provider?: 'github' | 'gitlab') {
    const token = process.env.GITHUB_TOKEN || process.env.GITLAB_TOKEN
    if (!token) {
      console.warn('⚠️ [GitProvider] No authentication token found. Push skipped.')
      return
    }

    try {
      console.log('🔄 [GitProvider] Synchronizing with remote...')
      execSync('git pull --rebase origin main')
      execSync('git push origin main')
      console.log('🚀 [GitProvider] Changes pushed to origin.')
    } catch (err: any) {
      console.error('❌ [GitProvider] Push failed:', err.message)
      // Cleanup rebase if failed
      try { execSync('git rebase --abort') } catch (e) {}
    }
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
