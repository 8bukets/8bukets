import fs from 'fs'
import path from 'path'
import { getMissionMetadata } from './collaboration'
import { workOrderService } from './work_order'
import { jules } from '../jules'
import { healthCheck } from '../core'

/**
 * CONSOLIDATED INTELLIGENCE SERVICE
 * Generates system-wide intelligence reports.
 */

export async function generateConsolidatedReport(branchIntelligence?: any[]) {
  'use cache'
  console.log('📊 [Intelligence] Generating consolidated system report...')

  const metadata = await getMissionMetadata()
  const branches = branchIntelligence || await jules.scanAllBranches()
  const health = await healthCheck()
  const workOrders = workOrderService.getPendingOrders()

  const reportPath = path.join(process.cwd(), 'CONSOLIDATED_INTELLIGENCE.md')

  let report = `# CONSOLIDATED INTELLIGENCE REPORT\n\n`
  report += `*Generated: ${new Date().toISOString()}*\n\n`

  report += `## 🎯 Mission Statement\n> ${metadata.missionStatement}\n\n`

  report += `## 🏥 System Sovereignty\n`
  report += `- **MongoDB:** ${health.mongodb}\n`
  report += `- **Supabase:** ${health.supabase}\n`
  report += `- **Total Branches:** ${branches.length}\n\n`

  report += `## 🌿 Branch Intelligence (Recent Activity)\n`
  const recentBranches = branches
    .sort((a, b) => new Date(b.lastSeen).getTime() - new Date(a.lastSeen).getTime())
    .slice(0, 10)

  recentBranches.forEach(b => {
    report += `- **${b.name}**: ${b.lastMessage} (*${b.lastSeen}*)\n`
  })
  report += `\n`

  report += `## 🛠️ Cognitive State\n`
  report += `- **Pending Work Orders:** ${workOrders.length}\n`
  if (workOrders.length > 0) {
    workOrders.forEach(wo => {
      report += `  - [${wo.type}] ${wo.goal}\n`
    })
  } else {
    report += `  - No pending orders. System is optimal.\n`
  }
  report += `\n`

  report += `## 👥 Stakeholders\n`
  metadata.stakeholders.forEach(s => {
    report += `- **${s.role}**: ${s.email}\n`
  })

  fs.writeFileSync(reportPath, report)
  console.log(`✅ [Intelligence] Report saved to ${reportPath}`)

  return { reportPath, branchCount: branches.length }
}
