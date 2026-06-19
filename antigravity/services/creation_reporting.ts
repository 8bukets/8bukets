import fs from 'fs'
import path from 'path'
import { WorkOrder } from './work_order'

/**
 * CREATION REPORTING SERVICE
 * Generates persistent Markdown records of autonomous creation cycles.
 */
export class CreationReportingService {
  private reportPath = path.join(process.cwd(), 'data/latest_creation_order.md')

  public async generateReport(pulseId: string, orders: WorkOrder[]) {
    const now = new Date().toISOString()
    let md = `# Autonomous Creation Cycle Report\n\n`
    md += `**Pulse ID:** ${pulseId}\n`
    md += `**Timestamp:** ${now}\n`
    md += `**Status:** ${orders.every(o => o.status === 'completed' || o.status === 'pending') ? '✅ ACTIVE' : '⚠️ DEGRADED'}\n\n`

    md += `## ⚡ Work Order Outcomes\n\n`
    md += `| ID | Type | Goal | Status | Completed At |\n`
    md += `|---|---|---|---|---|\n`

    for (const o of orders) {
      const statusIcon = o.status === 'completed' ? '✅' : (o.status === 'failed' ? '❌' : '⏳')
      md += `| ${o.id} | ${o.type} | ${o.goal || o.description || 'N/A'} | ${statusIcon} ${o.status} | ${o.completed_at || 'N/A'} |\n`
    }

    md += `\n## 🔍 Pulse Details\n`
    md += `- Total Orders: ${orders.length}\n`
    md += `- Completed: ${orders.filter(o => o.status === 'completed').length}\n`
    md += `- Failed: ${orders.filter(o => o.status === 'failed').length}\n`
    md += `- Pending/Executing: ${orders.filter(o => o.status === 'pending' || o.status === 'executing' || o.status === 'in_progress').length}\n`

    const dataDir = path.dirname(this.reportPath)
    if (!fs.existsSync(dataDir)) {
      fs.mkdirSync(dataDir, { recursive: true })
    }

    fs.writeFileSync(this.reportPath, md)
    console.log(`✅ [CreationReporting] Report generated at ${this.reportPath}`)
  }
}

export const creationReportingService = new CreationReportingService()
