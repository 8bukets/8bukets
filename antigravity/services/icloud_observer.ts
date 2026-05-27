import fs from 'fs'
import path from 'path'
import os from 'os'
import { KnowledgeObserver } from './knowledge_observer'
import { logAutonomousAction } from '../core'

/**
 * ICLOUD KNOWLEDGE OBSERVATION SERVICE
 * Autonomously scans a local iCloud-synchronized directory for new intelligence.
 */

export class ICloudObserver {
  private syncPaths: string[]
  private observer: KnowledgeObserver

  constructor() {
    const homeDir = os.homedir()

    // Support multiple possible iCloud sync paths
    const candidates = [
      path.join(homeDir, 'Library/Mobile Documents/com~apple~CloudDocs/8bukets'),
      path.join(homeDir, 'Library/Mobile Documents/com~apple~CloudDocs/Antigravity_Sync')
    ]

    if (process.env.ICLOUD_SYNC_PATH) {
      candidates.unshift(process.env.ICLOUD_SYNC_PATH)
    }

    // Filter to existing paths or fallback to simulation
    this.syncPaths = candidates.filter(p => fs.existsSync(p))

    if (this.syncPaths.length === 0) {
      const simPath = path.join(process.cwd(), 'scratch/icloud_sim')
      if (fs.existsSync(simPath)) {
        this.syncPaths.push(simPath)
      }
    }

    this.observer = new KnowledgeObserver()
  }

  /**
   * scan: Iterates through the sync directories and ingests new documents.
   */
  public async scan() {
    const ingested: string[] = []

    if (this.syncPaths.length === 0) {
       console.log('ℹ️ [iCloud Observer] No sync paths found. Skipping scan.')
       return ingested
    }

    for (const syncPath of this.syncPaths) {
      console.log(`☁️ [iCloud Observer] Scanning path: ${syncPath}`)

      try {
        const files = await fs.promises.readdir(syncPath)

        for (const file of files) {
          const fullPath = path.join(syncPath, file)
      const stats = await fs.promises.stat(fullPath)

      if (stats.isFile() && (file.endsWith('.md') || file.endsWith('.json'))) {
        try {
          const content = await fs.promises.readFile(fullPath, 'utf8')
          let knowledge;

          if (file.endsWith('.json')) {
             const data = JSON.parse(content)
             // Handle both structured and raw JSON
             knowledge = {
               title: data.title || `iCloud: ${file}`,
               sections: data.sections || [{ header: 'Content', content: JSON.stringify(data, null, 2) }],
               metadata: {
                 source: `icloud://${file}`,
                 ingestedAt: new Date().toISOString()
               }
             }
          } else {
             knowledge = KnowledgeObserver.processContent(`iCloud: ${file}`, content, `icloud://${file}`)
          }

          await this.observer.persistKnowledge(knowledge)
          if (!ingested.includes(file)) ingested.push(file)
          logAutonomousAction(`[ICLOUD] Ingested ${file}`, 'cognitive')
          console.log(` ✅ [iCloud Observer] Successfully ingested: ${file}`)
        } catch (err) {
          console.error(` ❌ [iCloud Observer] Failed to process ${file}:`, err)
        }
      }
    }
  } catch (err) {
    console.error(` ❌ [iCloud Observer] Failed to scan path ${syncPath}:`, err)
  }
}

    return ingested
  }
}

export const icloudObserver = new ICloudObserver()
