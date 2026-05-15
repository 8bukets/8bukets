import fs from 'fs'
import path from 'path'
import { getMissionMetadata } from './collaboration'
import { workOrderService } from './work_order'
import { jules } from '../jules'
import { healthCheck } from '../core'
import { checkJenkinsHealth } from './jenkins'

/**
 * CONSOLIDATED INTELLIGENCE SERVICE
 * Generates system-wide intelligence reports.
 */

export async function generateConsolidatedReport(branchIntelligence?: any[]) {
  console.log('📊 [Intelligence] Generating consolidated system report...')

  const metadata = await getMissionMetadata()
  const branches = branchIntelligence || await jules.scanAllBranches()
  const health = await healthCheck()
  const workOrders = await workOrderService.getPendingOrders()

  const reportPath = path.join(process.cwd(), 'CONSOLIDATED_INTELLIGENCE.md')

  let report = `# CONSOLIDATED INTELLIGENCE REPORT\n\n`
  report += `*Generated: ${new Date().toISOString()}*\n\n`

  report += `## 🎯 Mission Statement\n> ${metadata.missionStatement}\n\n`

  report += `## 🏥 System Sovereignty\n`
  report += `- **Execution Environment:** ${process.env.GITHUB_ACTIONS ? 'Cloud (GitHub Actions)' : 'Local'}\n`
  report += `- **MongoDB:** ${health.mongodb}\n`
  report += `- **Supabase:** ${health.supabase}\n`
  const jenkinsHealth = await checkJenkinsHealth()
  report += `- **Jenkins Pipeline:** ${jenkinsHealth.metrics.pipeline_efficiency}\n`
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

  report += `## 🤖 Python Ecosystem Intelligence\n`
  try {
    const linksPath = path.join(process.cwd(), 'links.json')
    if (fs.existsSync(linksPath)) {
      const links = JSON.parse(fs.readFileSync(linksPath, 'utf8'))
      report += `- **Market Data:** ${links.length} entries analyzed.\n`
    } else {
      report += `- **Market Data:** Scraper results pending.\n`
    }

    const resultsDir = path.join(process.cwd(), 'results')
    if (fs.existsSync(resultsDir)) {
      const files = fs.readdirSync(resultsDir)
      report += `- **Autonomous Reports:** ${files.length} generated.\n`

      const latestReport = files.filter(f => f.startsWith('DAILY_REPORT')).sort().reverse()[0]
      if (latestReport) {
        report += `- **Latest Report:** ${latestReport}\n`
      }
    }
  } catch (e) {
    report += `- **Ecosystem Status:** Limited observability into Python layer.\n`
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
