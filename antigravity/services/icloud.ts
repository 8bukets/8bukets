import { execFileSync } from 'child_process'
import path from 'path'
import fs from 'fs'
import os from 'os'

/**
 * ANTIGRAVITY ICLOUD SYNCHRONIZATION SERVICE
 * Orchestrates the "Every Day" upload and sync to iCloud folder.
 */

export async function syncToICloud() {
  'use cache'
  console.log('☁️ [iCloud Sync] Initiating autonomous synchronization...')

  const sourcePath = process.cwd()

  // Use os.homedir() to make it more portable
  const homeDir = os.homedir()
  const defaultICloudPath = path.join(homeDir, 'Library/Mobile Documents/com~apple~CloudDocs/Antigravity_Sync')
  const targetPath = process.env.ICLOUD_SYNC_PATH || defaultICloudPath

  if (!targetPath) {
    console.warn('⚠️ [iCloud Sync] No target path configured. Skipping sync.')
    return { status: 'skipped', reason: 'no_path' }
  }

  // Ensure target directory exists and is reachable
  try {
    if (!fs.existsSync(targetPath)) {
      console.log(`☁️ [iCloud Sync] Creating target directory: ${targetPath}`)
      try {
        fs.mkdirSync(targetPath, { recursive: true })
      } catch (mkdirErr: any) {
        console.warn(`⚠️ [iCloud Sync] Could not create target directory: ${mkdirErr.message}. This is expected in restricted cloud environments.`)
        return { status: 'skipped', reason: 'target_unreachable' }
      }
    }

    // Explicitly verify write access
    const testFile = path.join(targetPath, '.sync_test')
    fs.writeFileSync(testFile, 'test')
    fs.unlinkSync(testFile)
  } catch (err: any) {
    console.warn(`⚠️ [iCloud Sync] Target path verification failed or restricted: ${targetPath}. Skipping iCloud sync.`)
    return { status: 'skipped', reason: 'read_only_or_missing' }
  }

  try {
    // Exclude list to keep the sync efficient and avoid syncing artifacts
    const excludes = [
      'node_modules',
      '.git',
      '.next',
      '.npm-cache',
      '.npm-cache-new',
      '.npm_cache_new',
      'venv',
      '__pycache__',
      'dist',
      'build',
      '*.log',
      '.DS_Store'
    ]

    const args = ['-av', ...excludes.map(e => `--exclude=${e}`), `${sourcePath}/`, `${targetPath}/`]

    console.log(`☁️ [iCloud Sync] Executing: rsync ${args.join(' ')}`)

    // Use execFileSync to prevent shell injection and handle arguments safely
    execFileSync('rsync', args)
    console.log('✅ [iCloud Sync] Synchronization completed successfully.')

    return {
        status: 'success',
        timestamp: new Date().toISOString(),
        target: targetPath
    }
  } catch (err: any) {
    console.error('❌ [iCloud Sync] Synchronization failed:', err.message)
    return {
        status: 'failed',
        error: err.message
    }
  }
}
