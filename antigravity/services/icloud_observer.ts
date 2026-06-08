import fs from 'fs/promises'
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
    // Default to the known 8bukets iCloud path
    const homeDir = process.env.HOME || ''
    const standardICloudPath = path.join(homeDir, 'Library/Mobile Documents/com~apple~CloudDocs/8bukets')

    this.syncPath = process.env.ICLOUD_SYNC_PATH || standardICloudPath
    this.observer = new KnowledgeObserver()
  }

  /**
   * scan: Iterates through the sync directory and ingests new documents.
   */
  public async scan() {
    let effectivePath = this.syncPath

    try {
      await fs.access(effectivePath)
    } catch {
      // Fallback to local scratch for simulation if iCloud path is missing
      effectivePath = path.join(process.cwd(), 'scratch/icloud_sim')
      try {
        await fs.access(effectivePath)
      } catch {
        console.log('ℹ️ [iCloud Observer] Sync path does not exist. Skipping scan.')
        return []
      }
    }

    console.log(`☁️ [iCloud Observer] Scanning path: ${effectivePath}`)

    const files = await fs.readdir(effectivePath)
    const ingested: string[] = []

    for (const file of files) {
      const fullPath = path.join(effectivePath, file)
      const stats = await fs.stat(fullPath)

      if (stats.isFile() && (file.endsWith('.md') || file.endsWith('.json'))) {
        try {
          const content = await fs.readFile(fullPath, 'utf8')
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
