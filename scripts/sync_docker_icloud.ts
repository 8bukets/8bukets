import { runICloudDockerSync } from '../antigravity/icloud_backup'

/**
 * SYNC DOCKER ICLOUD SCRIPT
 * Standalone entry point for manual or scheduled iCloud synchronization.
 */
async function main() {
  console.log('🚀 [Antigravity] Launching iCloud Docker Sync Cycle...')

  try {
    await runICloudDockerSync()
    console.log('✅ [Antigravity] Sync cycle finished.')
  } catch (err) {
    console.error('💥 [Antigravity] Sync cycle failed:', err)
    process.exit(1)
  }
}

main()
