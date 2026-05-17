import { execSync } from 'child_process'
import { syncDockerLocalICloud } from './services/icloud_local_sync'
import { jules } from './jules'

/**
 * ANTIGRAVITY UNIFIED ICLOUD BACKUP TASK
 * Orchestrates both local and remote iCloud synchronization for Docker configurations.
 */
export async function runICloudDockerSync() {
  console.log('🛡️ [iCloud-Backup] Starting autonomous Docker-iCloud synchronization...')

  // 1. Attempt Local Sync (macOS native)
  const localSuccess = await syncDockerLocalICloud()

  // 2. Attempt Remote Sync (via pyicloud)
  let remoteSuccess = false
  try {
    console.log('🔄 [iCloud-Backup] Invoking remote sync agent...')
    execSync('python3 antigravity/icloud_remote_sync.py', { stdio: 'inherit' })
    remoteSuccess = true
  } catch (err: any) {
    if (err.status === 2) {
        console.log('⏩ [iCloud-Backup] Remote sync agent skipped (no credentials).')
    } else {
        console.log('❌ [iCloud-Backup] Remote sync agent failed.')
    }
  }

  const overallStatus = localSuccess || remoteSuccess ? 'Success' : 'Skipped/Failed'

  // Log to cognitive memory
  jules.recordTask(`iCloud Docker Synchronization: ${overallStatus} (Local: ${localSuccess}, Remote: ${remoteSuccess})`)

  console.log(`🛡️ [iCloud-Backup] Task complete. Status: ${overallStatus}`)
  return { localSuccess, remoteSuccess }
}
