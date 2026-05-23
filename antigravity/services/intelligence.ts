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
  'use cache'
  console.log('📊 [Intelligence] Generating consolidated system report...')

  const metadata = await getMissionMetadata()
  const branches = branchIntelligence || await jules.scanAllBranches()
  const health = await healthCheck()
  const workOrders = workOrderService.getPendingOrders()

  const reportPath = path.join(process.cwd(), 'CONSOLIDATED_INTELLIGENCE.md')

  let report = `# CONSOLIDATED INTELLIGENCE REPORT\n\n`
  report += `*Generated: ${new Date().toISOString()}*\n\n`

  report += `## 📋 Executive Summary\n`
  report += `- **System Posture:** ${health.mongodb === 'connected' && health.supabase === 'connected' ? '✅ OPTIMAL' : '⚠️ DEGRADED'}\n`
  report += `- **Active Synergy:** ${branches.length} branches analyzed across multiple domains.\n`
  report += `- **Mission Alignment:** ${metadata.goals.length} strategic goals tracked.\n\n`

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

  // Phase 12: Integrate Global Neural Network Status
  const { broadcastPulse } = await import('./neural')
  const { getRelayState } = await import('./relay')
  const pulse = await broadcastPulse()
  const relay = await getRelayState()

  report += `## 🌌 Global Neural Network\n`
  report += `- **Cognitive Origin:** \`${pulse.origin}\`\n`
  report += `- **Neural Health:** ${pulse.health === 'optimal' ? '✅' : '⚠️'} ${pulse.health.toUpperCase()}\n`
  report += `- **Volatility Index:** ${pulse.volatilityTags} active cognitive tags.\n\n`

  report += `## 🛰️ Omni-Presence Relay\n`
  relay.forEach(r => {
    report += `- **Environment:** \`${r.environment}\` (Intensity: ${(r.intensity * 100).toFixed(0)}%)\n`
    report += `  - *Active Views:* ${r.activeViews.join(', ')}\n`
  })
  report += `\n`

  report += `## 🤝 Merged Ecosystem Insights\n`
  report += `Synergy achieved across ${branches.length} branches. Detailed knowledge and results consolidated from specialized agents.\n\n`

  // Phase 12: Synergy & Collaboration Analysis
  if (relationshipMap.synergies && relationshipMap.synergies.length > 0) {
    report += `### ⚡ Strategic Synergy Matrix\n`
    report += `| Resource | Intensity | Collaborating Branches | Actionable Recommendation |\n`
    report += `| :--- | :---: | :--- | :--- |\n`
    relationshipMap.synergies.forEach((s: any) => {
      const recommendation = relationshipMap.collaborationRecommendations.find((r: any) => r.branches.includes(s.branches[0]))
      report += `| \`${s.resource}\` | ${s.intensity} | ${s.branches.slice(0, 3).join(', ')}${s.branches.length > 3 ? '...' : ''} | ${recommendation?.action || 'Consolidate effort'} |\n`
    })
    report += `\n`
  }

  const insights = branches.filter(b => b.knowledge || (b.results && b.results !== b.lastMessage)).slice(0, 10)
  if (insights.length > 0) {
    report += `### 🧠 Specialized Knowledge Nuggets\n`
    insights.forEach(b => {
      report += `- **${b.name}**: ${b.results}${b.knowledge ? ` (*Knowledge: ${b.knowledge}*)` : ''}\n`
    })
  } else {
    report += `- No new specialized insights to merge at this time.\n`
  }
  report += `\n`

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
  const knowledgePath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json')
  if (fs.existsSync(knowledgePath)) {
    try {
      const systemKnowledge = JSON.parse(fs.readFileSync(knowledgePath, 'utf8'))

      // Phase 12: Support both nested 'typescript_sections' and unified flat key structure
      const allKnowledge: any[] = []

      if (Array.isArray(systemKnowledge.sections)) allKnowledge.push(...systemKnowledge.sections)
      if (Array.isArray(systemKnowledge.typescript_sections)) allKnowledge.push(...systemKnowledge.typescript_sections)

      Object.entries(systemKnowledge).forEach(([key, value]) => {
        if (key !== 'metadata' && key !== 'sections' && key !== 'typescript_sections' && Array.isArray(value)) {
          allKnowledge.push(...value)
        }
      })

      allKnowledge.forEach((k: any) => {
        if (k && k.title) {
          report += `### ${k.title}\n`
          report += `- **Source:** ${k.metadata?.source || 'Internal'}\n`
          report += `- **Sections:** ${k.sections?.length || 0}\n`
          if (k.sections && k.sections.length > 0) {
            report += `  - *Key Topics:* ${k.sections.slice(0, 3).map((s: any) => s.header).join(', ')}\n`
          }
          report += `\n`
        }
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
  report += `\n`

  report += `## 🚀 Prioritized Action Items\n`
  if (health.mongodb !== 'connected') report += `- [CRITICAL] Restore MongoDB Atlas connectivity.\n`
  if (workOrders.length > 5) report += `- [HIGH] Process backlog of ${workOrders.length} pending work orders.\n`

  const highIntensitySynergies = relationshipMap.synergies.filter((s: any) => s.intensity === 'High')
  highIntensitySynergies.forEach((s: any) => {
    report += `- [MEDIUM] Resolve High-Intensity conflict/synergy on resource: \`${s.resource}\` (${s.branches.length} branches).\n`
  })

  if (branches.length > 1500) report += `- [LOW] Prune or merge stagnant ecosystem branches (Total: ${branches.length}).\n`
  report += `- [INFO] Continue autonomous knowledge ingestion for market intelligence.\n`

  fs.writeFileSync(reportPath, report)
  console.log(`✅ [Intelligence] Report saved to ${reportPath}`)

  return { reportPath, branchCount: branches.length }
}
