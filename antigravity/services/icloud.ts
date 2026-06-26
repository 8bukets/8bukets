import { logAutonomousAction } from '../core'
import { exec } from 'child_process'
import { promisify } from 'util'

const execAsync = promisify(exec)

/**
 * ANTIGRAVITY ICLOUD SYNC SERVICE
 * Orchestrates synchronization with iCloud Drive.
 */
export async function syncToICloud() {
  const isCloud = !!(process.env.GITHUB_ACTIONS || process.env.GITLAB_CI || process.env.AUTONOMOUS_MODE === 'cloud' || process.env.MACBOOK_CLOUD_SIMULATION === 'true')

  if (isCloud) {
    logAutonomousAction('☁️ [iCloud] Skipping native sync in Cloud Mode (Simulation active).', 'info')
    return { status: 'skipped', reason: 'cloud_environment' }
  }

  logAutonomousAction('☁️ [iCloud] Synchronizing system state to iCloud...', 'info')
  try {
    const { stdout } = await execAsync('python3 sync_icloud.py --upload')
    logAutonomousAction('✅ [iCloud] Synchronization complete.', 'info')
    return { status: 'success', output: stdout }
  } catch (err: any) {
    // If it requires 2FA, it will fail in headless mode, which is expected.
    logAutonomousAction(`⚠️ [iCloud] Synchronization failed: ${err.message}`, 'warning')
    return { status: 'failed', error: err.message }
  }
}
