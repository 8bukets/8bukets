import fs from 'fs'
import path from 'path'
import os from 'os'

/**
 * ANTIGRAVITY LOCAL ICLOUD SYNC SERVICE
 * Synchronizes Docker configurations to the local macOS iCloud Drive path.
 */
export async function syncDockerLocalICloud() {
  console.log('🔄 [iCloud-Local] Initiating local Docker sync to iCloud Drive...')

  const homeDir = os.homedir()
  const icloudPath = path.join(homeDir, 'Library/Mobile Documents/com~apple~CloudDocs/antigravity-sync')

  const dockerFiles = [
    'Dockerfile',
    'docker-compose.yml',
    'docker-compose.cloud.yml',
    '.dockerignore',
    'autonomous_state.json'
  ]

  // Check if we are on macOS and the iCloud path exists
  if (os.platform() !== 'darwin' || !fs.existsSync(path.dirname(icloudPath))) {
    console.log('⏩ [iCloud-Local] Local iCloud Drive path not detected or not on macOS. Skipping.')
    return false
  }

  try {
    if (!fs.existsSync(icloudPath)) {
      fs.mkdirSync(icloudPath, { recursive: true })
      console.log(`📂 [iCloud-Local] Created directory: ${icloudPath}`)
    }

    let syncCount = 0
    for (const file of dockerFiles) {
      const src = path.join(process.cwd(), file)
      const dest = path.join(icloudPath, file)

      if (fs.existsSync(src)) {
        fs.copyFileSync(src, dest)
        console.log(`📤 [iCloud-Local] Synced ${file}`)
        syncCount++
      }
    }

    console.log(`✅ [iCloud-Local] Local sync complete. ${syncCount} files synced.`)
    return true
  } catch (err) {
    console.error('❌ [iCloud-Local] Sync failed:', err)
    return false
  }
}
