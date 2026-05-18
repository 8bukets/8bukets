import fs from 'fs'
import path from 'path'
import { z } from 'zod'
import { autonomousFetch } from '@/antigravity/core'
import { checkDockerHealth } from './docker'
import { getLatestBuildStatus } from './jenkins'
import { dispatchExecutiveBriefing } from './notification'


/**
 * ANTIGRAVITY COLLABORATION SERVICE (Phase 9)
 * Manages multi-agent collaboration and stakeholder synchronization.
 */

export const StakeholderSchema = z.object({
  role: z.string(),
  email: z.string()
})

export const MissionMetadataSchema = z.object({
  missionStatement: z.string(),
  stakeholders: z.array(StakeholderSchema),
  goals: z.array(z.string())
})

export type Stakeholder = z.infer<typeof StakeholderSchema>
export type MissionMetadata = z.infer<typeof MissionMetadataSchema>

const MISSION_PATH = path.join(process.cwd(), '.antigravity/mission.md')

export async function getMissionMetadata(): Promise<MissionMetadata> {
  return autonomousFetch(MissionMetadataSchema, async () => {
    // Note: In Next.js server context, we don't use 'use cache' here to avoid some issues we saw earlier
    if (!fs.existsSync(MISSION_PATH)) {
      throw new Error('Mission document missing. System collaboration impaired.')
    }

    const content = await fs.promises.readFile(MISSION_PATH, 'utf8')

    const missionStatementMatch = content.match(/## Mission Statement\n([\s\S]*?)\n##/)
    const missionStatement = missionStatementMatch ? missionStatementMatch[1].trim() : 'Autonomous Evolution'

    const stakeholders: Stakeholder[] = []
    const stakeholderSection = content.match(/## Stakeholders\n([\s\S]*?)\n##/)
    if (stakeholderSection) {
      const lines = stakeholderSection[1].trim().split('\n')
      lines.forEach(line => {
        const parts = line.split(':')
        if (parts.length === 2) {
          stakeholders.push({
            role: parts[0].replace('-', '').trim(),
            email: parts[1].trim()
          })
        }
      })
    }

    const goals: string[] = []
    const goalsSection = content.match(/## Strategic Goals\n([\s\S]*)/)
    if (goalsSection) {
      const lines = goalsSection[1].trim().split('\n')
      lines.forEach(line => {
        const goal = line.replace(/^\d+\.\s*/, '').trim()
        if (goal) goals.push(goal)
      })
    }

    return {
      missionStatement,
      stakeholders,
      goals
    }
  }, { tags: ['collaboration-metadata'], life: 'catalog' })
}

export async function exportEcosystemMetadata() {
  const metadata = await getMissionMetadata()
  console.log('🌐 [Collaboration] Exporting ecosystem metadata for global sync...')
  return {
    ...metadata,
    systemId: 'antigravity-alpha-01',
    timestamp: new Date().toISOString()
  }
}

/**
 * Phase 9: Multi-Agent Collaboration Protocol
 * Notifies stakeholders of the current system state and recent autonomous evolutions.
 */
export async function broadcastToStakeholders(state: any) {
  const metadata = await getMissionMetadata()
  console.log('📢 [Collaboration] Broadcasting system posture to stakeholders...')

  const summary = `
--- ANTIGRAVITY COLLABORATION SUMMARY ---
Timestamp: ${state.last_sync}
Mission: ${metadata.missionStatement}
Docker Status: ${state.docker.status} (${state.docker.containerCount} containers)
Intelligence: ${state.intelligence.branches} branches synchronized, ${state.intelligence.pendingTasks} tasks pending.

Stakeholders notified:
${metadata.stakeholders.map(s => ` - ${s.role} (${s.email})`).join('\n')}
------------------------------------------
`
  // In Phase 9, we log this to the console and a collaboration log file.
  // In future phases, this could trigger actual email or slack notifications.
  console.log(summary)

  // Dispatch executive briefing for high-level communication
  const synergyDetails = state.intelligence.relationshipMap.resourceInventory
    .filter((r: any) => r.type === 'Branch Result')
    .slice(0, 5)
    .map((r: any) => `- ${r.name}: ${r.result}`)
    .join('\n')

  await dispatchExecutiveBriefing(
    `System synchronized: ${state.intelligence.branches} branches, ${state.intelligence.pendingTasks} tasks. Docker: ${state.docker.status}.`,
    synergyDetails || 'No new branch results consolidated in this cycle.'
  )

  const logDir = path.join(process.cwd(), 'logs')
  if (!fs.existsSync(logDir)) await fs.promises.mkdir(logDir, { recursive: true })

  await fs.promises.appendFile(path.join(logDir, 'collaboration.log'), summary)

  return { notifiedCount: metadata.stakeholders.length }
}

export async function generateRelationshipMap(branches: any[], stakeholders: Stakeholder[], goals: string[]) {
  console.log('🗺️ [Collaboration] Generating relationship map...')

  const map: any = {
    stakeholderEngagement: {},
    goalAlignment: {},
    resourceInventory: [],
    synergies: []
  }

  // Phase 12: Dynamic Resource Discovery
  const servicesDir = path.join(process.cwd(), 'antigravity/services')
  if (fs.existsSync(servicesDir)) {
    const files = await fs.promises.readdir(servicesDir)
    for (const file of files) {
      if (file.endsWith('.ts') && !file.endsWith('.test.ts')) {
        map.resourceInventory.push({
          type: 'Service',
          name: file.replace('.ts', ''),
          status: 'Active',
          path: `antigravity/services/${file}`
        })
      }
    }
  }

  // Integrate autonomous knowledge into resource inventory
  const knowledgePath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json')
  if (fs.existsSync(knowledgePath)) {
    try {
      const content = await fs.promises.readFile(knowledgePath, 'utf8')
      const systemKnowledge = JSON.parse(content)
      const knowledge = systemKnowledge.typescript_sections || []
      knowledge.forEach((k: any) => {
        map.resourceInventory.push({
          type: 'Knowledge',
          name: k.title,
          status: 'Ingested',
          source: k.metadata.source
        })
      })
    } catch (e) {
      console.warn('⚠️ [Collaboration] Failed to parse system_knowledge.json for relationship map.')
    }
  }

  // Correlate branches to goals based on keywords and domains
  goals.forEach(goal => {
    const relevantBranches = branches.filter(b => {
      const branchName = b?.name || '';
      const lastMsg = b?.lastMessage || '';
      const domain = b?.domain || '';
      return goal.toLowerCase().split(' ').some(word =>
        word.length > 3 && (branchName.toLowerCase().includes(word) || lastMsg.toLowerCase().includes(word) || domain.toLowerCase().includes(word))
      );
    })
    map.goalAlignment[goal] = relevantBranches.map(b => b.name)
  })

  // Correlate stakeholders to roles/branches
  stakeholders.forEach(s => {
    map.stakeholderEngagement[s.role] = {
      email: s.email,
      activeProjects: branches.filter(b => {
        const branchName = b?.name || '';
        return b.category === 'agent' || branchName.includes(s.role.toLowerCase().split(' ')[0]);
      }).map(b => b.name)
    }
  })

  // Identify Static "Resources" (Documentation)
  map.resourceInventory.push(
    { type: 'Documentation', name: 'AGENTS.md', status: 'Active' },
    { type: 'Documentation', name: 'CONSOLIDATED_INTELLIGENCE.md', status: 'Active' },
    { type: 'Documentation', name: 'KNOWLEDGE_MERGE.md', status: 'Active' }
  )

  // Phase 12: Advanced Synergy Detection (Resource Overlap)
  const resourceUsage: Record<string, string[]> = {}
  branches.forEach(b => {
    if (b.changedFiles) {
      b.changedFiles.forEach((f: string) => {
        const matchedResource = map.resourceInventory.find((r: any) => r.path && f.includes(r.path))
        if (matchedResource) {
          if (!resourceUsage[matchedResource.name]) resourceUsage[matchedResource.name] = []
          resourceUsage[matchedResource.name].push(b.name)
        }
      })
    }
  })

  Object.entries(resourceUsage).forEach(([resource, branchList]) => {
    if (branchList.length > 1) {
      map.synergies.push({
        type: 'Resource Conflict/Synergy',
        resource,
        branches: branchList,
        intensity: branchList.length > 2 ? 'High' : 'Medium'
      })
      console.warn(`🤝 [Collaboration] Synergy Detected: ${branchList.length} branches working on ${resource}.`)
    }
  })

  // Integrate branch results into resources if they implement a specific feature
  branches.filter(b => b.category === 'feature' && b.results).forEach(b => {
    map.resourceInventory.push({
      type: 'Branch Result',
      name: b.name,
      status: 'Ready for Merge',
      result: b.results
    })
  })

  return map
}

export async function syncCollaborationState(branchIntelligence?: any[]) {
  console.log('🔄 [Collaboration] Synchronizing autonomous state...')
  const metadata = await getMissionMetadata()
  const dockerHealth = await checkDockerHealth()
  const jenkinsStatus = await getLatestBuildStatus()
  const statePath = path.join(process.cwd(), 'autonomous_state.json')

  let currentState: any = {}
  if (fs.existsSync(statePath)) {
    try {
      const content = await fs.promises.readFile(statePath, 'utf8')
      currentState = JSON.parse(content)
    } catch (e) {
      console.warn('⚠️ [Collaboration] Failed to parse autonomous_state.json, starting fresh.')
    }
  }

  const { jules } = await import('../jules')
  const { workOrderService } = await import('./work_order')
  const branches = branchIntelligence || await jules.scanAllBranches()
  const workOrders = workOrderService.getPendingOrders() // Simplified for now
  const relationshipMap = await generateRelationshipMap(branches, metadata.stakeholders, metadata.goals)
  await mergeBranchInsights(branches)

  const newState = {
    ...currentState,
    mission: metadata.missionStatement,
    stakeholders: metadata.stakeholders,
    docker: dockerHealth,
    jenkins: jenkinsStatus,
    intelligence: {
      branches: branches.length,
      pendingTasks: workOrders.length,
      relationshipMap
    },
    last_sync: new Date().toISOString()
  }

  await fs.promises.writeFile(statePath, JSON.stringify(newState, null, 4))
  console.log('✅ [Collaboration] Autonomous state synchronized successfully.')
  return newState
}

export async function mergeBranchInsights(branches: any[]) {
  console.log('🧠 [Collaboration] Merging branch insights into ecosystem matrix...')
  const knowledgePath = path.join(process.cwd(), 'KNOWLEDGE_MERGE.md')

  let existingContent = '';
  if (fs.existsSync(knowledgePath)) {
    existingContent = await fs.promises.readFile(knowledgePath, 'utf8');
  }

  const relevantBranches = branches.filter(b => {
    if (!(b.knowledge || (b.results && b.results !== b.lastMessage))) {
      return false;
    }
    return !existingContent.includes(`- **Branch:** ${b.name}`);
  })

  if (relevantBranches.length === 0) return

  const domains: Record<string, any[]> = {}
  relevantBranches.forEach(b => {
    const domain = b.domain || 'General'
    if (!domains[domain]) domains[domain] = []
    domains[domain].push(b)
  })

  let newEntries = `\n## Ecosystem Knowledge Consolidation (${new Date().toISOString()})\n`

  Object.entries(domains).forEach(([domain, branchList]) => {
    newEntries += `### 🌐 Strategic Domain: ${domain}\n`
    branchList.forEach(b => {
      newEntries += `- **Branch:** \`${b.name}\`\n`
      newEntries += `  - **Result:** ${b.results}\n`
      if (b.knowledge) {
        newEntries += `  - **Knowledge:** ${b.knowledge}\n`
      }
      if (b.changedFiles && b.changedFiles.length > 0) {
        newEntries += `  - **Artifacts:** ${b.changedFiles.length} files modified.\n`
      }
    })
    newEntries += `\n`
  })

  if (existingContent) {
      await fs.promises.writeFile(knowledgePath, existingContent + newEntries, 'utf8')
  } else {
      await fs.promises.writeFile(knowledgePath, `# Market Intelligence Matrix\n${newEntries}`, 'utf8')
  }

  console.log(`✅ [Collaboration] Merged ${relevantBranches.length} branch insights across ${Object.keys(domains).length} domains.`)
}

export async function mergeEcosystemInsights(branchIntelligence: any[], workOrders: any[]) {
  const metadata = await getMissionMetadata()
  console.log('🧠 [Collaboration] Merging ecosystem insights...')

  await mergeBranchInsights(branchIntelligence)
  await broadcastToStakeholders({
    last_sync: new Date().toISOString(),
    docker: { status: 'synchronized', containerCount: 0 },
    intelligence: {
        branches: branchIntelligence.length,
        pendingTasks: workOrders.length,
        relationshipMap: await generateRelationshipMap(branchIntelligence, metadata.stakeholders, metadata.goals)
    }
  })
  let marketIntelligence = ''
  const knowledgePath = path.join(process.cwd(), 'KNOWLEDGE_MERGE.md')
  if (fs.existsSync(knowledgePath)) {
    marketIntelligence = await fs.promises.readFile(knowledgePath, 'utf8')
  }

  return {
    mission: metadata.missionStatement,
    goals: metadata.goals,
    branches: branchIntelligence,
    recentWork: workOrders.slice(-5),
    timestamp: new Date().toISOString(),
    marketIntelligence
  }
}
