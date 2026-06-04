/**
 * Edge-to-Cloud Bridge
 * Facilitates state synchronization between local artifacts and cloud persistence.
 * Rationale: Ensures continuity when the MacBook is offline and a cloud node takes over.
 */
import { z } from 'zod'
import { autonomousFetch, getMongoClient, logAutonomousAction } from '../core'
import fs from 'fs'
import path from 'path'
import os from 'os'

export const EdgetoCloudBridgeSchema = z.object({
  status: z.string(),
  lastRun: z.string(),
  syncedFiles: z.array(z.string()).optional()
})

export type EdgetoCloudBridgeData = z.infer<typeof EdgetoCloudBridgeSchema>

export class EdgeToCloudBridge {
  private filesToSync = [
    'data/work_orders.json',
    'data/knowledge/system_knowledge.json',
    'autonomous_state.json'
  ]

  /**
   * Synchronizes critical local state files to MongoDB.
   */
  public async syncLocalToCloud() {
    logAutonomousAction('🌉 [EdgeToCloudBridge] Synchronizing local state to cloud...', 'info')

    const synced = []
    try {
      const client = await getMongoClient()
      const db = client.db()
      const collection = db.collection('cloud_bridge_state')

      for (const relativePath of this.filesToSync) {
        const fullPath = path.join(process.cwd(), relativePath)
        if (fs.existsSync(fullPath)) {
          try {
            const content = fs.readFileSync(fullPath, 'utf8')
            const data = JSON.parse(content)

            await collection.updateOne(
              { file: relativePath },
              { $set: {
                file: relativePath,
                data,
                updatedAt: new Date().toISOString(),
                node: os.hostname()
              }},
              { upsert: true }
            )
            synced.push(relativePath)
          } catch (err: any) {
            logAutonomousAction(`⚠️ [EdgeToCloudBridge] Failed to sync ${relativePath}: ${err.message}`, 'warning')
          }
        }
      }

      logAutonomousAction(`✅ [EdgeToCloudBridge] Successfully synced ${synced.length} files to cloud.`, 'info')
    } catch (e: any) {
      logAutonomousAction(`❌ [EdgeToCloudBridge] Cloud sync failed: ${e.message}`, 'error')
    }
    return synced
  }

  /**
   * Recovers state from cloud to local.
   * Includes path validation to prevent traversal vulnerabilities.
   */
  public async recoverCloudToLocal() {
    logAutonomousAction('🌉 [EdgeToCloudBridge] Recovering state from cloud...', 'info')

    const recovered = []
    try {
      const client = await getMongoClient()
      const db = client.db()
      const collection = db.collection('cloud_bridge_state')

      const cloudStates = await collection.find({}).toArray()

      for (const state of cloudStates) {
        // Path Traversal Mitigation: Ensure the file is within the whitelist
        if (!this.filesToSync.includes(state.file)) {
          logAutonomousAction(`⚠️ [EdgeToCloudBridge] Skipping unauthorized file recovery: ${state.file}`, 'warning')
          continue
        }

        const targetPath = path.join(process.cwd(), state.file)

        // Final sanity check: targetPath must be within process.cwd()
        if (!targetPath.startsWith(process.cwd())) {
           logAutonomousAction(`⚠️ [EdgeToCloudBridge] Potential path traversal detected for: ${state.file}`, 'error')
           continue
        }

        const targetDir = path.dirname(targetPath)

        if (!fs.existsSync(targetDir)) {
          fs.mkdirSync(targetDir, { recursive: true })
        }

        fs.writeFileSync(targetPath, JSON.stringify(state.data, null, 2))
        recovered.push(state.file)
      }

      logAutonomousAction(`✅ [EdgeToCloudBridge] Successfully recovered ${recovered.length} files from cloud.`, 'info')
    } catch (e: any) {
      logAutonomousAction(`❌ [EdgeToCloudBridge] Cloud recovery failed: ${e.message}`, 'error')
    }
    return recovered
  }
}

export const edgeToCloudBridge = new EdgeToCloudBridge()

export async function getEdgetoCloudBridgeData(): Promise<EdgetoCloudBridgeData> {
  return {
    status: 'active',
    lastRun: new Date().toISOString()
  }
}
