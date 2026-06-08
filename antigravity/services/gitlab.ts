import { logAutonomousAction } from '../core'
import { exec } from 'child_process'
import { promisify } from 'util'

const execAsync = promisify(exec)

/**
 * ANTIGRAVITY GITLAB TELEMETRY SERVICE
 */

export async function getGitLabMetrics() {
  const isCloud = !!(process.env.GITLAB_CI || process.env.AUTONOMOUS_MODE === 'cloud' || process.env.MACBOOK_CLOUD_SIMULATION === 'true')

  if (isCloud && process.env.MACBOOK_CLOUD_SIMULATION === 'true') {
     return {
       pipelineStages: ['build', 'test', 'deploy'],
       hasPipeline: true,
       fullyOnline: true,
       status: 'optimal'
     }
  }

  try {
    // Attempt to use glab CLI if available
    const { stdout } = await execAsync('glab pipeline status --format json')
    const pipeline = JSON.parse(stdout)
    return {
      pipelineStages: pipeline.stages || [],
      hasPipeline: !!pipeline,
      status: pipeline.status || 'unknown'
    }
  } catch (e) {
    return {
      pipelineStages: [],
      hasPipeline: false,
      status: 'unavailable'
    }
  }
}
