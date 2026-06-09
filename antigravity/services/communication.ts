/**
 * ANTIGRAVITY COMMUNICATION HUB
 * Optimized for Phase 12 Sentient Orchestration.
 */
import fs from 'fs'
import path from 'path'
import { z } from 'zod'
import { logAutonomousAction } from '@/antigravity/core'

/**
 * ANTIGRAVITY COMMUNICATION HUB (Phase 12)
 * Centralizes agent-to-stakeholder interactions and directive processing.
 */

export const DirectiveSchema = z.object({
  id: z.string(),
  intent: z.string(),
  priority: z.enum(['Low', 'Medium', 'High', 'Critical']),
  status: z.enum(['Active', 'Fulfilled', 'Obsolete']),
  timestamp: z.string()
})

export type Directive = z.infer<typeof DirectiveSchema>

const DIRECTIVES_PATH = path.join(process.cwd(), '.antigravity/directives.md')

export async function getStakeholderDirectives(): Promise<Directive[]> {
  'use cache'
  if (! fs.existsSync(DIRECTIVES_PATH)) {
    // Create default directives if missing
    const defaultDirectives = `# Stakeholder Directives\n\n- [High] Maintain 99.9% system uptime (Active)\n- [Medium] Consolidate all branch knowledge daily (Active)\n`
    const dir = path.dirname(DIRECTIVES_PATH)
    if (! fs.existsSync(dir)) await fs.promises.mkdir(dir, { recursive: true })
    await fs.promises.writeFile(DIRECTIVES_PATH, defaultDirectives)
    return [
      { id: 'dir_default_1', intent: 'Maintain 99.9% system uptime', priority: 'High', status: 'Active', timestamp: new Date().toISOString() },
      { id: 'dir_default_2', intent: 'Consolidate all branch knowledge daily', priority: 'Medium', status: 'Active', timestamp: new Date().toISOString() }
    ]
  }

  const content = await fs.promises.readFile(DIRECTIVES_PATH, 'utf8')
  const directives: Directive[] = []

  const lines = content.split('\n')
  lines.forEach(line => {
    const match = line.match(/^-\s*\[(Low|Medium|High|Critical)\]\s*(.*?)\s*\((Active|Fulfilled|Obsolete)\)$/i)
    if (match) {
      directives.push({
        id: `dir_${Math.random().toString(36).substr(2, 9)}`,
        priority: match[1] as any,
        intent: match[2].trim(),
        status: match[3] as any,
        timestamp: new Date().toISOString()
      })
    }
  })

  return directives
}

export async function dispatchStakeholderAlert(subject: string, body: string, priority: 'info' | 'warning' | 'critical' = 'info') {
  console.log(`🔔 [Communication] Dispatching Alert: ${subject}`)
  logAutonomousAction(`[ALERT] ${subject}`, priority === 'critical' ? 'error' : 'info')

  const logDir = path.join(process.cwd(), 'logs')
  if (! fs.existsSync(logDir)) await fs.promises.mkdir(logDir, { recursive: true })

  const alertEntry = `\n--- ALERT (${new Date().toISOString()}) ---\nSubject: ${subject}\nPriority: ${priority}\n\n${body}\n`
  await fs.promises.appendFile(path.join(logDir, 'stakeholder_alerts.log'), alertEntry)

  return { status: 'dispatched', timestamp: new Date().toISOString() }
}

export async function generateActionableBriefing(state: any, directives: Directive[]) {
  const activeDirectives = directives.filter(d => d.status === 'Active')

  let briefing = `### 🎯 Directive Fulfillment Status\n`
  if (activeDirectives.length > 0) {
    activeDirectives.forEach(d => {
      const isFulfilled = state.intelligence.branches > 0 // Logic could be more complex
      briefing += `- **[${d.priority}]** ${d.intent} -> Status: ${isFulfilled ? '✅ ON TRACK' : '⚠️ IN PROGRESS'}\n`
    })
  } else {
    briefing += `- No active directives currently registered.\n`
  }

  briefing += `\n### ⚡ Strategic Synergy Summary\n`
  const crossDomain = state.intelligence.relationshipMap.crossDomainSynergies || []
  if (crossDomain.length > 0) {
    briefing += `- Detected **${crossDomain.length} Cross-Domain synergies**. High potential for architectural alignment across service types.\n`
  }

  const synergies = state.intelligence.relationshipMap.synergies || []
  const highIntensity = synergies.filter((s: any) => s.intensity === 'High')
  if (highIntensity.length > 0) {
    briefing += `- Detected **${highIntensity.length} High-Intensity synergies**. Immediate cross-branch coordination recommended.\n`
  } else {
    briefing += `- System synergy is within optimal parameters.\n`
  }

  const recommendations = state.intelligence.relationshipMap.collaborationRecommendations || []
  const criticalRecs = recommendations.filter((r: any) => r.priority === 'Critical')

  if (criticalRecs.length > 0) {
    briefing += `\n### 🤝 Direct Coordination Paths\n`
    criticalRecs.forEach((r: any) => {
      const coordinationRequired = r.rationale.includes('Urgent coordination required between:')
      const coordinationPath = coordinationRequired
        ? r.rationale.split('Urgent coordination required between:')[1].trim()
        : 'Cross-team architectural review required.'

      briefing += `- **Resource Conflict/Synergy:** \`${r.resource}\`\n`
      briefing += `  - **Strategic Pathway:** ${coordinationPath}\n`
      briefing += `  - **Action Item:** ${r.action}\n`
      if (r.branches && Array.isArray(r.branches)) {
        briefing += `  - **Impacted Branches:** ${r.branches.slice(0, 5).join(', ')}${r.branches.length > 5 ? ` (+${r.branches.length - 5} more)` : ''}\n`
      }
    })
  }

  // Phase 12: Specific Agent-to-Stakeholder Directives
  briefing += `\n### 🤖 Agent-to-Stakeholder Directives\n`
  if (synergies.length > 0) {
    const highIntensity = synergies.filter((s: any) => s.intensity === 'High')
    if (highIntensity.length > 0) {
      const targetResources = highIntensity.map((s: any) => `\`${s.resource}\``).join(', ')
      briefing += `- **Jules Directive (CRITICAL):** "Immediate intervention required for high-intensity resource overlaps on ${targetResources}. Consolidate these branches to prevent significant architectural fragmentation."\n`
    } else {
      briefing += `- **Jules Directive:** "I have detected ${synergies.length} developmental overlaps. Stakeholders should prioritize the 'Strategic Coordination Paths' defined above to avoid architectural drift."\n`
    }
  } else {
    briefing += `- **Jules Directive:** "System alignment is optimal. No manual intervention required for current development streams."\n`
  }

  // Phase 13: Data-Driven Cross-Domain Insight
  if (crossDomain.length > 0) {
    const topSynergy = crossDomain[0]
    briefing += `- **Intelligence Directive:** "Strategic cross-domain connection detected between \`${topSynergy.source}\` (${topSynergy.sourceType}) and \`${topSynergy.target}\` (${topSynergy.targetType}). Recommend unified architectural review."\n`
  }

  // Phase 12: Resource Synergy Insights
  if (state.intelligence.relationshipMap.resourceDependencies?.length > 0) {
    const deps = state.intelligence.relationshipMap.resourceDependencies.length
    briefing += `- **Intelligence Directive:** "Ecosystem features ${deps} cross-service dependencies. Ensure that changes to core services are preceded by automated dependency impact analysis."\n`
  }

  // Phase 13: Direct Coordination Matrix
  const clusters = state.intelligence.relationshipMap.functionalClusters || {}
  if (Object.keys(clusters).length > 0) {
    briefing += `\n### 📊 Direct Coordination Matrix\n`
    briefing += `| Functional Cluster | Involved Branches | Potential For Friction |\n`
    briefing += `| :--- | :--- | :---: |\n`

    Object.entries(clusters).forEach(([cluster, branches]: [string, any]) => {
      const friction = branches.length > 5 ? '🔴 High' : (branches.length > 2 ? '🟡 Medium' : '🟢 Low')
      briefing += `| \`${cluster}\` | ${branches.slice(0, 3).join(', ')}${branches.length > 3 ? ` (+${branches.length - 3})` : ''} | ${friction} |\n`
    })
  }

  // Phase 13: Strategic Priority Matrix
  const impactful = state.intelligence.relationshipMap.impactfulBranches || []
  if (impactful.length > 0) {
    briefing += `\n### 📊 Strategic Priority Matrix\n`
    briefing += `| Strategic Initiative | Impact Score | Estimated Effort | Priority |\n`
    briefing += `| :--- | :---: | :---: | :---: |\n`

    impactful.slice(0, 8).forEach((b: any) => {
      const effort = b.score > 80 ? 'High' : (b.score > 40 ? 'Medium' : 'Low')
      const priority = b.score > 60 ? 'Critical' : 'Routine'
      briefing += `| \`${b.name}\` | ${b.score} | ${effort} | ${priority} |\n`
    })
  }

  // Phase 14: Strategic Alignment & Cross-Agent Dependency Matrix
  const dependencies = state.intelligence.relationshipMap.resourceDependencies || []
  if (dependencies.length > 0) {
    briefing += `\n### 🔗 Strategic Dependency Matrix\n`
    briefing += `| Source Service | Target Dependency | Connection Type |\n`
    briefing += `| :--- | :--- | :---: |\n`
    dependencies.slice(0, 10).forEach((d: any) => {
      briefing += `| \`${d.source}\` | \`${d.target}\` | ${d.type} |\n`
    })
    if (dependencies.length > 10) {
      briefing += `\n*...and ${dependencies.length - 10} more cross-agent dependencies.*\n`
    }
  }

  briefing += `\n### 🚀 Required Stakeholder Decisions\n`
  let decisionsCount = 0

  if (state.docker.status !== 'optimal' && state.docker.status !== 'simulated') {
    briefing += `- **Infrastructure:** Approve failover to cloud-native secondary nodes due to Docker degradation.\n`
    decisionsCount++
  }

  if (state.intelligence.branches > 2000) {
    briefing += `- **Ecosystem:** Approve branch pruning protocol to reduce cognitive overhead (${state.intelligence.branches} branches detected).\n`
    decisionsCount++
  }

  if (state.intelligence.pendingTasks > 15) {
    briefing += `- **Operations:** Approve resource reallocation for background task processing.\n`
    decisionsCount++
  }

  if (decisionsCount === 0) {
    briefing += `- No critical stakeholder decisions required at this time.\n`
  }

  return briefing
}
