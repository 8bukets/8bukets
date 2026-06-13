import fs from 'fs/promises'
import path from 'path'
import { KnowledgeObserver } from './knowledge_observer'
import { logAutonomousAction } from '../core'

/**
 * ICLOUD KNOWLEDGE OBSERVATION SERVICE
 * Autonomously scans a local iCloud-synchronized directory for new intelligence.
 */

export class ICloudObserver {
  private scanPaths: string[]
  private observer: KnowledgeObserver

  constructor() {
    const homeDir = process.env.HOME || ''
    const cloudDocs = path.join(homeDir, 'Library/Mobile Documents/com~apple~CloudDocs')
    
    this.scanPaths = [
      path.join(cloudDocs, 'Antigravity_Sync'),
      path.join(cloudDocs, 'CodeBackups/Antigravity'),
      path.join(cloudDocs, 'MapAntigravity')
    ]

    if (process.env.ICLOUD_SYNC_PATH) {
      this.scanPaths.push(process.env.ICLOUD_SYNC_PATH)
    }

    this.observer = new KnowledgeObserver()
  }

  /**
   * scan: Iterates through all scan paths and ingests new documents.
   */
  public async scan() {
    const ingested: string[] = []

    for (const scanPath of this.scanPaths) {
      try {
        await fs.access(scanPath)
      } catch {
        continue
      }

      console.log(`☁️ [iCloud Observer] Scanning path: ${scanPath}`)
      let files: string[] = []
      try {
        files = await fs.readdir(scanPath, { recursive: true }) as string[]
      } catch (e) {
        continue
      }

      for (const file of files) {
        if (file.includes('node_modules')) continue

        const fullPath = path.join(scanPath, file)
        try {
          const stats = await fs.stat(fullPath)

          if (stats.isFile() && (file.endsWith('.md') || file.endsWith('.json'))) {
            try {
              const content = await fs.readFile(fullPath, 'utf8')
              let knowledge;

              if (file.endsWith('.json')) {
                try {
                  const data = JSON.parse(content)
                  knowledge = {
                    source: `icloud://${file}`,
                    title: data.title || `iCloud: ${file}`,
                    description: data.description || 'Extracted system knowledge from iCloud JSON',
                    topKeywords: [],
                    recentPosts: [],
                    analyzedAt: new Date().toISOString(),
                    sections: data.sections || [{ header: 'Content', content: JSON.stringify(data, null, 2) }]
                  }
                } catch (e) { continue }
              } else {
                knowledge = KnowledgeObserver.processContent(`iCloud: ${file}`, content, `icloud://${file}`)
              }

              if (knowledge) {
                await this.observer.persistKnowledge(knowledge)
                ingested.push(file)
                logAutonomousAction(`[ICLOUD] Ingested ${file}`, 'cognitive')
                console.log(` ✅ [iCloud Observer] Successfully ingested: ${file}`)
              }
            } catch (err) {
              console.error(` ❌ [iCloud Observer] Failed to process ${file}:`, err)
            }
          }
        } catch (statErr) {
          // Ignore files that disappeared during scan
        }
      }
    }

    return ingested
  }
}

export const icloudObserver = new ICloudObserver()
