import { logAutonomousAction } from '../core'
import { exec } from 'child_process'
import { promisify } from 'util'

const execAsync = promisify(exec)

/**
 * ANTIGRAVITY GITHUB EVOLUTION TELEMETRY SERVICE
 */

export async function getGitHubMetrics() {
  const isCloud = !!(process.env.GITHUB_ACTIONS || process.env.AUTONOMOUS_MODE === 'cloud' || process.env.MACBOOK_CLOUD_SIMULATION === 'true')

  if (isCloud && process.env.MACBOOK_CLOUD_SIMULATION === 'true') {
    return {
      semanticCommitScore: 100,
      fullyOnline: true,
      prVelocity: 'high'
    }
  }

  try {
     // Basic metric: count commits in last 24h
     const { stdout } = await execAsync('git log --since="24 hours ago" --oneline | wc -l')
     const commitCount = parseInt(stdout.trim())
     return {
       semanticCommitScore: commitCount > 0 ? 90 : 50,
       recentCommits: commitCount
     }
  } catch (e) {
    return {
      semanticCommitScore: 0,
      error: true
    }
  }
}
