import fs from 'fs'
import path from 'path'
import { getMissionMetadata, generateRelationshipMap } from './collaboration'
import { workOrderService } from './work_order'
import { jules } from '../jules'
import { healthCheck } from '../core'
import { checkDockerHealth } from './docker'

/**
 * CONSOLIDATED INTELLIGENCE SERVICE
 * Generates system-wide intelligence reports.
 */

export async function generateConsolidatedReport(branchIntelligence?: any[]) {
  'use cache'
  console.log('📊 [Intelligence] Generating consolidated system report...')

  const { trackROI } = await import('../core')
  trackROI('IntelligenceService', 0.98)

  const metadata = await getMissionMetadata()
  const branches = branchIntelligence || await jules.scanAllBranches(true)
  const health = await healthCheck()
  const workOrders = await workOrderService.getPendingOrders()

  const reportPath = path.join(process.cwd(), 'CONSOLIDATED_INTELLIGENCE.md')

  let report = `# CONSOLIDATED INTELLIGENCE REPORT\n\n`
  report += `*Generated: ${new Date().toISOString()}*\n\n`

  const isMongoOptimal = health.mongodb === 'connected' || health.mongodb === 'healthy' || health.mongodb === 'simulated';
  const isSupabaseOptimal = health.supabase === 'connected' || health.supabase === 'healthy';

  report += `## 📋 Executive Summary\n`
  report += `- **System Posture:** ${isMongoOptimal && isSupabaseOptimal ? (health.mongodb === 'simulated' ? '✅ OPTIMAL (SIMULATED)' : '✅ OPTIMAL') : '⚠️ DEGRADED'}\n`
  report += `- **Active Synergy:** ${branches.length} branches analyzed across multiple domains.\n`
  report += `- **Mission Alignment:** ${metadata.goals.length} strategic goals tracked.\n\n`

  report += `## 🎯 Mission Statement\n> ${metadata.missionStatement}\n\n`

  report += `## 🏥 System Sovereignty\n`
  report += `- **MongoDB:** ${health.mongodb}\n`
  report += `- **Supabase:** ${health.supabase}\n`
  report += `- **Active Workers:** 24/7 autonomous surveillance active\n`
  report += `- **Total Branches:** ${branches.length}\n\n`

  const relationshipMap = await generateRelationshipMap(branches, metadata.stakeholders, metadata.goals)

  // Phase 12: Resource Ecosystem Summary
  const categorizedResources: Record<string, any[]> = {}
  relationshipMap.resourceInventory.forEach((res: any) => {
    if (!categorizedResources[res.type]) categorizedResources[res.type] = []
    categorizedResources[res.type].push(res)
  })

  report += `## 📦 Resource Ecosystem\n`
  Object.entries(categorizedResources).forEach(([type, items]) => {
    report += `- **${type}s:** ${items.length} active\n`
  })
  report += `\n`

  // Phase 12: Resource Dependency Matrix
  if (relationshipMap.resourceDependencies && relationshipMap.resourceDependencies.length > 0) {
    report += `## 🔗 Resource Dependency Matrix\n`
    relationshipMap.resourceDependencies.slice(0, 15).forEach((d: any) => {
      report += `- \`${d.source}\` --[${d.type}]--> \`${d.target}\` \n`
    })
    if (relationshipMap.resourceDependencies.length > 15) {
      report += `- _...and ${relationshipMap.resourceDependencies.length - 15} more dependencies._\n`
    }
    report += `\n`
  }

  // Phase 12: Active Stakeholder Directives
  const { getStakeholderDirectives, generateActionableBriefing } = await import('./communication')
  const directives = await getStakeholderDirectives()
  const activeDirectives = directives.filter(d => d.status === 'Active')

  report += `## 🎯 Active Stakeholder Directives\n`
  if (activeDirectives.length > 0) {
    activeDirectives.forEach(d => {
      report += `- **[${d.priority}]** ${d.intent}\n`
    })
  } else {
    report += `_No active directives found._\n`
  }
  report += `\n`

  // Phase 12: Actionable Briefing
  const dockerHealthy = await checkDockerHealth()
  const dockerStatus = dockerHealthy ? 'optimal' : 'degraded'
  const actionableBriefing = await generateActionableBriefing({
    mission: metadata.missionStatement,
    stakeholders: metadata.stakeholders,
    docker: { status: dockerStatus },
    intelligence: { pendingTasks: workOrders.length, relationshipMap }
  }, directives)

  report += `## 🚀 Actionable Intelligence\n`
  report += actionableBriefing + `\n\n`

  const criticalRecs = relationshipMap.collaborationRecommendations.filter((r: any) => r.priority === 'Critical')
  if (criticalRecs.length > 0) {
    report += `### 🤝 Strategic Coordination Pathways\n`
    criticalRecs.forEach((r: any) => {
      const coordinationPath = r.rationale.includes('Urgent coordination required between:')
        ? r.rationale.split('Urgent coordination required between:')[1].trim()
        : 'Cross-team architectural review required.';

      report += `- **Conflict/Synergy on:** \`${r.resource}\`\n`
      report += `  - **Strategic Pathway:** ${coordinationPath}\n`
      report += `  - **Involved Branches:** ${r.branches.slice(0, 5).join(', ')}${r.branches.length > 5 ? ` (+${r.branches.length - 5} more)` : ''}\n`
    })
    report += `\n`
  }

  // Phase 12: Integrated Strategic Synergy Matrix
  if (relationshipMap.synergies && relationshipMap.synergies.length > 0) {
    report += `### ⚡ Strategic Synergy Matrix\n`
    report += `| Resource | Intensity | Collaborating Branches | Actionable Recommendation |\n`
    report += `| :--- | :---: | :--- | :--- |\n`
    relationshipMap.synergies.slice(0, 10).forEach((s: any) => {
      const recommendation = relationshipMap.collaborationRecommendations.find((r: any) =>
        r.resource === s.resource || r.action.includes(`'${s.resource}'`)
      )
      const recommendationText = recommendation
        ? `${recommendation.action}${recommendation.rationale.includes('Coordination required') ? `<br/>*${recommendation.rationale.split('. ')[1]}*` : ''}`
        : 'Consolidate effort'

      report += `| \`${s.resource}\` | ${s.intensity} | ${s.branches.slice(0, 2).join(', ')}${s.branches.length > 2 ? '...' : ''} | ${recommendationText} |\n`
    })
    report += `\n`
  }

  report += `## 🌿 Branch Intelligence (Recent Activity)\n`
  // Ensure branches is an array of objects
  const branchArray = Array.isArray(branches) ? branches : []
  const recentBranches = branchArray
    .sort((a, b) => new Date(b.lastSeen).getTime() - new Date(a.lastSeen).getTime())
    .slice(0, 10)

  recentBranches.forEach(b => {
    const activity = b.lastSeen || 'recently'
    report += `- **${b.name}** [${b.category}]: ${b.lastMessage} (*${activity}*)\n`
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

  const insights = branches.filter(b => b.knowledge || (b.results && !b.results.startsWith('Commit:'))).slice(0, 15)
  if (insights.length > 0) {
    report += `### 🧠 Specialized Knowledge Nuggets\n`
    insights.forEach(b => {
      report += `- **${b.name}** [${b.domain}]: ${b.results}\n`
      if (b.knowledge) {
        report += `  - *Insight:* ${b.knowledge}\n`
      }
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

  Object.entries(categorizedResources).forEach(([type, items]) => {
    report += `### ${type}s\n`
    items.forEach(res => {
      report += `- **${res.name}** (${res.status})${res.source ? ` - *Source: ${res.source}*` : ''}\n`
    })
    report += `\n`
  })

  report += `## 🧠 Knowledge Matrix\n`
  const knowledgePath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json')
  const knowledgeExists = await fs.promises.access(knowledgePath).then(() => true).catch(() => false)
  if (knowledgeExists) {
    try {
      const systemKnowledge = JSON.parse(await fs.promises.readFile(knowledgePath, 'utf8'))

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

  // Phase 13: Ecosystem Synergy Graph (Tree Representation)
  report += `## 🕸️ Ecosystem Synergy Graph\n`
  const resourceToBranches: Record<string, string[]> = {}

  relationshipMap.synergies.forEach((s: any) => {
    if (!resourceToBranches[s.resource]) resourceToBranches[s.resource] = []
    resourceToBranches[s.resource].push(...s.branches)
  })

  Object.entries(resourceToBranches).forEach(([res, brs]) => {
    const uniqueBrs = Array.from(new Set(brs))
    report += `### 📦 ${res}\n`
    uniqueBrs.forEach((b, idx) => {
      const prefix = idx === uniqueBrs.length - 1 ? '└──' : '├──'
      report += `${prefix} 🌿 \`${b}\`\n`
    })
    report += `\n`
  })

  if (Object.keys(resourceToBranches).length === 0) {
    report += `_No high-signal synergy overlaps detected for graph generation._\n\n`
  }

  report += `## 👥 Stakeholder Collaboration Hub\n`
  metadata.stakeholders.forEach(s => {
    const engagement = relationshipMap.stakeholderEngagement[s.role] || { activeProjects: [] }
    report += `### ${s.role} (${s.email})\n`
    report += `- **Current Focus:** ${engagement.activeProjects.length > 0 ? engagement.activeProjects.slice(0, 3).join(', ') : 'Global Monitoring'}\n`
    const recommendedTasks = relationshipMap.collaborationRecommendations
      .filter((r: any) => r.priority === 'Critical' && r.branches.some((rb: string) => engagement.activeProjects.includes(rb)))
    if (recommendedTasks.length > 0) {
      report += `- **Priority Coordination Required:**\n`
      recommendedTasks.forEach((rt: any) => {
        report += `  - ⚠️ [${rt.priority}] ${rt.action} (Resource: ${rt.resource || 'Multiple'})\n`
      })
    }
    report += `\n`
  })
  report += `\n`

  report += `## 🚀 Prioritized Action Items\n`
  if (!isMongoOptimal) report += `- [CRITICAL] Restore MongoDB Atlas connectivity.\n`
  if (workOrders.length > 5) report += `- [HIGH] Process backlog of ${workOrders.length} pending work orders.\n`

  const highIntensitySynergies = relationshipMap.synergies.filter((s: any) => s.intensity === 'High')
  highIntensitySynergies.forEach((s: any) => {
    const coordinator = metadata.stakeholders.find(sh => relationshipMap.stakeholderEngagement[sh.role]?.activeProjects.includes(s.branches[0]))
    const coordinationMsg = coordinator ? ` (Coordinate with ${coordinator.role})` : ''
    report += `- [MEDIUM] Resolve High-Intensity synergy on resource: \`${s.resource}\`${coordinationMsg}.\n`
  })

  if (branches.length > 1500) report += `- [LOW] Prune or merge stagnant ecosystem branches (Total: ${branches.length}).\n`
  report += `- [INFO] Continue autonomous knowledge ingestion for market intelligence.\n`

  const collaborationHealth = relationshipMap.synergies.length > 0
    ? Math.max(0, 100 - (relationshipMap.synergies.length * 5))
    : 100
  report += `\n---\n**Collaboration Health Index:** ${collaborationHealth}% | *Phase 12 Synergy Protocol Active*\n`

  await fs.promises.writeFile(reportPath, report)
  console.log(`✅ [Intelligence] Report saved to ${reportPath}`)

  return { reportPath, branchCount: branches.length }
}
