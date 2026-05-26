import fs from 'fs'
import path from 'path'
import { KnowledgeObserver } from './knowledge_observer'
import { logAutonomousAction } from '../core'

/**
 * ICLOUD KNOWLEDGE OBSERVATION SERVICE
 * Autonomously scans a local iCloud-synchronized directory for new intelligence.
 */

export class ICloudObserver {
  private syncPath: string
  private observer: KnowledgeObserver

  constructor() {
    // Default to the known 8bukets iCloud path with a local fallback for simulation
    const homeDir = process.env.HOME || ''
    const standardICloudPath = path.join(homeDir, 'Library/Mobile Documents/com~apple~CloudDocs/8bukets')

    this.syncPath = process.env.ICLOUD_SYNC_PATH || ( fs.existsSync(standardICloudPath) ? standardICloudPath : path.join(process.cwd(), 'scratch/icloud_sim'))
    this.observer = new KnowledgeObserver()
  }

  /**
   * scan: Iterates through the sync directory and ingests new documents.
   */
  public async scan() {
    console.log(`☁️ [iCloud Observer] Scanning path: ${this.syncPath}`)

    try {
      await fs.promises.access(this.syncPath)
    } catch {
      console.log('ℹ️ [iCloud Observer] Sync path does not exist. Skipping scan.')
      return []
    }

    const files = await fs.promises.readdir(this.syncPath)
    const ingested: string[] = []

    for (const file of files) {
      const fullPath = path.join(this.syncPath, file)
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
          ingested.push(file)
          logAutonomousAction(`[ICLOUD] Ingested ${file}`, 'cognitive')
          console.log(` ✅ [iCloud Observer] Successfully ingested: ${file}`)
        } catch (err) {
          console.error(` ❌ [iCloud Observer] Failed to process ${file}:`, err)
        }
      }
    }

    return ingested
  }
}

export const icloudObserver = new ICloudObserver()
