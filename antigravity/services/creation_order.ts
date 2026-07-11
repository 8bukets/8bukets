import fs from 'fs'
import path from 'path'
import { workOrderService } from './work_order'
import { logAutonomousAction } from '../core'

/**
 * ANTIGRAVITY CREATION ORDER SERVICE
 * Performs gap analysis for critical system documentation and assets.
 * Triggered during the autonomous work cycle.
 */
export class CreationOrderService {
  private criticalFiles = [
    { name: 'SYSTEM_PATENT.md', description: 'System Patent and Intellectual Property Documentation' },
    { name: 'AGENTS.md', description: 'Autonomous Agent Architectural Guidelines' },
    { name: 'SECURITY.md', description: 'Security Policy and Cognitive Security Protocols' },
    { name: 'CONTRIBUTING.md', description: 'Guidelines for Contributing to Antigravity' },
    { name: 'README.md', description: 'Main Project Documentation' }
  ]

  public async performGapAnalysis() {
    logAutonomousAction('🔍 [CreationOrder] Performing gap analysis for critical documentation...', 'info')

    let gapsFound = 0
    for (const file of this.criticalFiles) {
      const filePath = path.join(process.cwd(), file.name)
      if (!fs.existsSync(filePath)) {
        logAutonomousAction(`⚠️ [CreationOrder] Missing critical file: ${file.name}. Creating generation order.`, 'warning')

        await workOrderService.createOrder(
          'CONTENT_GENERATION',
          `Generate missing ${file.name}`,
          {
            title: file.name.replace('.md', '').replace('_', ' '),
            content: `This document provides the ${file.description}. It was autonomously generated to fill a system gap.`,
            filename: file.name,
            directory: '.'
          }
        )
        gapsFound++
      }
    }

    if (gapsFound === 0) {
      logAutonomousAction('✨ [CreationOrder] All critical documentation is present.', 'info')
    } else {
      logAutonomousAction(`✅ [CreationOrder] Gap analysis complete. Created ${gapsFound} work orders.`, 'info')
    }
  }
}

export const creationOrderService = new CreationOrderService()
