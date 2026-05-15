import fs from 'fs'
import path from 'path'
import { getMissionMetadata, generateRelationshipMap } from './collaboration'
import { workOrderService } from './work_order'
import { jules } from '../jules'
import { healthCheck } from '../core'

/**
 * CONSOLIDATED INTELLIGENCE SERVICE
 * Generates system-wide intelligence reports.
 */

export async function generateConsolidatedReport(branchIntelligence?: any[]) {
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

  const relationshipMap = await generateRelationshipMap(branches, metadata.stakeholders, metadata.goals)

  report += `## 🗺️ Relationship Map\n`
  report += `### Goal Alignment\n`
  Object.entries(relationshipMap.goalAlignment).forEach(([goal, relevantBranches]: [string, any]) => {
    report += `- **Goal:** ${goal}\n`
    if (relevantBranches.length > 0) {
      report += `  - *Branches:* ${relevantBranches.join(', ')}\n`
    } else {
      report += `  - *No direct branch alignment detected.*\n`
    }
  })
  report += `\n`

  report += `### Stakeholder Engagement\n`
  Object.entries(relationshipMap.stakeholderEngagement).forEach(([role, data]: [string, any]) => {
    report += `- **${role}** (${data.email})\n`
    if (data.activeProjects.length > 0) {
      report += `  - *Active Projects:* ${data.activeProjects.join(', ')}\n`
    }
  })
  report += `\n`

  report += `## 📦 Resource Inventory\n`
  relationshipMap.resourceInventory.forEach((res: any) => {
    report += `- [${res.type}] **${res.name}** - Status: ${res.status}${res.source ? ` (*Source: ${res.source}*)` : ''}\n`
  })
  report += `\n`

  report += `## 🧠 Knowledge Matrix\n`
  const knowledgePath = path.join(process.cwd(), 'data/knowledge/ai_agents_knowledge.json')
  if (fs.existsSync(knowledgePath)) {
    try {
      const knowledge = JSON.parse(fs.readFileSync(knowledgePath, 'utf8'))
      knowledge.forEach((k: any) => {
        report += `### ${k.title}\n`
        report += `- **Source:** ${k.metadata.source}\n`
        report += `- **Sections:** ${k.sections.length}\n`
        if (k.sections.length > 0) {
          report += `  - *Key Topics:* ${k.sections.slice(0, 3).map((s: any) => s.header).join(', ')}\n`
        }
        report += `\n`
      })
    } catch (e) {
      report += `⚠️ Failed to parse Knowledge Matrix.\n\n`
    }
  } else {
    report += `*No autonomous knowledge ingested yet.*\n\n`
  }

  report += `## 🏆 Results Summary\n`
  const resultBranches = branches.filter(b => b.results && b.results !== 'N/A' && b.results !== b.lastMessage).slice(0, 5)
  if (resultBranches.length > 0) {
    resultBranches.forEach(b => {
      report += `- **${b.name}**: ${b.results}\n`
    })
  } else {
    report += `- No explicit results extracted from recent history.\n`
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
