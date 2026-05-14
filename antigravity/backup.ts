import fs from 'fs'
import path from 'path'
import { jules } from './jules'

/**
 * ANTIGRAVITY AUTONOMOUS BACKUP AGENT
 * Ensures safe, timestamped persistence of core state files.
 */
export async function runBackup() {
  'use cache'
  console.log('🛡️ [Backup Agent] Initiating autonomous system backup...')

  const rootDir = process.cwd()
  const backupDir = path.join(rootDir, 'backups')

  // Ensure backups directory exists
  if (!fs.existsSync(backupDir)) {
    fs.mkdirSync(backupDir, { recursive: true })
    console.log(`🛡️ [Backup Agent] Created backup directory at: ${backupDir}`)
  }

  const timestamp = new Date().toISOString().replace(/[:.]/g, '-')
  let backupCount = 0

  // 1. Backup Jules Memory
  const memoryPath = path.join(rootDir, 'antigravity/.jules_memory.json')
  if (fs.existsSync(memoryPath)) {
    try {
      // Verify Integrity
      const memoryContent = fs.readFileSync(memoryPath, 'utf8')
      const parsed = JSON.parse(memoryContent)

      if (parsed && typeof parsed === 'object') {
        const backupMemoryPath = path.join(backupDir, `jules_memory_${timestamp}.json`)
        fs.writeFileSync(backupMemoryPath, memoryContent)
        console.log(`✅ [Backup Agent] Archived Jules Memory to ${backupMemoryPath}`)
        backupCount++
      }
    } catch (e) {
      console.error(`⚠️ [Backup Agent] Integrity check failed for Jules Memory. Skipping backup. Error:`, e)
    }
  } else {
      console.warn(`⚠️ [Backup Agent] Could not find Jules Memory at ${memoryPath}`)
  }

  // 2. Backup Core Autonomous State if it exists
  const statePath = path.join(rootDir, 'autonomous_state.json')
  if (fs.existsSync(statePath)) {
    try {
      const stateContent = fs.readFileSync(statePath, 'utf8')
      const parsed = JSON.parse(stateContent)

      if (parsed && typeof parsed === 'object') {
        const backupStatePath = path.join(backupDir, `autonomous_state_${timestamp}.json`)
        fs.writeFileSync(backupStatePath, stateContent)
        console.log(`✅ [Backup Agent] Archived Autonomous State to ${backupStatePath}`)
        backupCount++
      }
    } catch (e) {
      console.error(`⚠️ [Backup Agent] Integrity check failed for Autonomous State. Skipping backup. Error:`, e)
    }
  }

  // Record task in cognitive memory
  if (backupCount > 0) {
     jules.recordTask(`Autonomous backup completed successfully. Archived ${backupCount} core state files.`)
     console.log(`🛡️ [Backup Agent] Backup complete. Logged to Jules Memory.`)
  } else {
     console.warn(`🛡️ [Backup Agent] Backup cycle completed, but no files were archived.`)
  }

  return { timestamp, filesBackedUp: backupCount }
}

// Allow running directly if needed
if (require.main === module) {
  runBackup().catch(console.error)
}
