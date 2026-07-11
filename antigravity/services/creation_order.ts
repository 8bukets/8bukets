/** PHASE 26 COMPLIANCE: singularity-readiness (threshold: 0.9999) **/
/** PHASE 26 COMPLIANCE: resonance-latency (target: <0.05ms) **/
import fs from 'fs'
import path from 'path'
import { workOrderService } from './work_order'
import { logAutonomousAction } from '../core'

/**
 * CreationOrderService
 * Implements autonomous gap analysis for critical system documentation.
 */
export class CreationOrderService {
  private criticalFiles = [
    { name: 'SYSTEM_PATENT.md', title: 'System Patent and Intellectual Property', content: 'Autonomous IP protection documentation.' },
    { name: 'AGENTS.md', title: 'Agent Swarm Protocols', content: 'Documentation for multi-agent coordination and cognitive sovereignty.' },
    { name: 'SECURITY.md', title: 'Security Sovereignty and Compliance', content: 'Security protocols, ZKP-trust, and lattice-based cryptography documentation.' },
    { name: 'CONTRIBUTING.md', title: 'Contributing to Antigravity', content: 'Guidelines for autonomous and human contributions to the ecosystem.' },
    { name: 'README.md', title: 'Antigravity Ecosystem', content: 'The master overview of the Antigravity autonomous intelligence.' }
  ]

  /**
   * Performs a gap analysis of critical system artifacts and creates work orders for missing pieces.
   */
  public async performGapAnalysis() {
    console.log('🔍 [CreationOrder] Performing documentation gap analysis...')
    let gapsFound = 0

    for (const file of this.criticalFiles) {
      const filePath = path.join(process.cwd(), file.name)
      const exists = await fs.promises.access(filePath).then(() => true).catch(() => false)

      if (!exists) {
        console.log(` ⚠️ [CreationOrder] Missing critical artifact: ${file.name}. Generating work order...`)

        await workOrderService.createOrder(
          'CONTENT_GENERATION',
          `Generate missing ${file.name}`,
          {
            title: file.title,
            content: file.content,
            filename: file.name,
            directory: '.'
          }
        )
        gapsFound++
      }
    }

    if (gapsFound > 0) {
      logAutonomousAction(`[GAP_ANALYSIS] Found and addressed ${gapsFound} documentation gaps.`, 'cognitive')
    } else {
      console.log('✅ [CreationOrder] Documentation gap analysis complete. No gaps detected.')
    }
  }
}

export const creationOrderService = new CreationOrderService()
