import { execFile } from 'child_process'
import { promisify } from 'util'

const execFileAsync = promisify(execFile)

export async function getGitHubMetrics() {
  console.log('🐙 [GitHubEvolutionAgent] Evaluating GitHub semantic commit patterns...')
  let semanticCommitScore = 0

  try {
    const { stdout: logsRaw } = await execFileAsync('git', ['log', '--format=%s', '-n', '50'])
    const logs = logsRaw.trim().split('\n')
    let semanticCount = 0

    for (const log of logs) {
      if (/^(feat|fix|chore|docs|refactor|agent|🤖)(\(.*\))?:/.test(log)) {
        semanticCount++
      }
    }

    semanticCommitScore = logs.length > 0 ? Math.round((semanticCount / logs.length) * 100) : 0
  } catch (err) {
    console.warn('⚠️ [GitHubEvolutionAgent] Failed to fetch git logs', err)
  }

  return {
    semanticCommitScore
  }
}
