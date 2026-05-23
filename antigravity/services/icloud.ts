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

  // Ensure target directory exists
  try {
    if (!fs.existsSync(targetPath)) {
      console.log(`☁️ [iCloud Sync] Creating target directory: ${targetPath}`)
      fs.mkdirSync(targetPath, { recursive: true })
    }
  } catch (err) {
    console.warn(`⚠️ [iCloud Sync] Could not verify or create target path: ${targetPath}. It might be a restricted iCloud location or missing permissions.`)
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
