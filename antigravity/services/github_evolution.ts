import { execFileSync } from 'child_process'

export async function getGitHubMetrics() {
  console.log('🐙 [GitHubEvolutionAgent] Evaluating GitHub semantic commit patterns...')
  let semanticCommitScore = 0

  try {
    const logs = /* [Evolution] TODO: Refactor to async */ /* [Evolution] TODO: Refactor to async */ execFileSync('git', ['log', '--format=%s', '-n', '50']).toString().trim().split('\n')
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
