import { logAutonomousAction } from '../core'
import fs from 'fs'
import path from 'path'
import { z } from 'zod'
import { autonomousFetch, getMongoClient } from '@/antigravity/core'
import { checkDockerHealth } from './docker'
import { checkJenkinsHealth, triggerJenkinsPipeline } from './jenkins'

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
    if (!fs.existsSync(MISSION_PATH)) {
      throw new Error('Mission document missing. System collaboration impaired.')
    }

    const content = fs.readFileSync(MISSION_PATH, 'utf8')

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
  logAutonomousAction('🌐 [Collaboration] Exporting ecosystem metadata for global sync...', 'info')
  return {
    ...metadata,
    systemId: 'antigravity-alpha-01',
    timestamp: new Date().toISOString()
  }
}

/**
 * Aggregates knowledge nuggets from across all Git branches.
 */
export async function mergeBranchInsights(branchIntelligence: any[]) {
  logAutonomousAction('🌿 [Collaboration] Merging multi-branch insights...', 'info')

  const nuggets: string[] = []
  const branchMap: Record<string, string[]> = {}

  branchIntelligence.forEach(branch => {
    // Extract potential knowledge nuggets from commit messages
    const message = branch.lastMessage || ''
    const match = message.match(/\[(.*?)\] (.*)/)
    if (match) {
       const tag = match[1]
       const insight = match[2]
       nuggets.push(`${tag}: ${insight} (Source: ${branch.name})`)
       if (!branchMap[tag]) branchMap[tag] = []
       branchMap[tag].push(branch.name)
    }
  })

  // Deduplicate
  const uniqueNuggets = Array.from(new Set(nuggets))

  // Generate KNOWLEDGE_MERGE.md
  const mergePath = path.join(process.cwd(), 'KNOWLEDGE_MERGE.md')
  let content = `# ECOSYSTEM KNOWLEDGE MERGE\n\n`
  content += `*Generated: ${new Date().toISOString()}*\n\n`
  content += `## 🧠 Discovered Knowledge Nuggets\n`

  if (uniqueNuggets.length > 0) {
    uniqueNuggets.forEach(n => {
      content += `- ${n}\n`
    })
  } else {
    content += `*No structured knowledge nuggets discovered in recent branch history.*\n`
  }

  content += `\n## 🌿 Branch Map by Tag\n`
  Object.entries(branchMap).forEach(([tag, branches]) => {
     content += `- **${tag}**: ${Array.from(new Set(branches)).join(', ')}\n`
  })

  content += `\n---\nAll the best - https://markposition.wordpress.com\n`

  fs.writeFileSync(mergePath, content)
  logAutonomousAction(`✅ [Collaboration] Knowledge merge saved to ${mergePath}`, 'info')

  return { nuggets: uniqueNuggets.length, mergePath }
}

/**
 * Generates a relationship map of system resources and their synergies.
 */
export async function generateRelationshipMap() {
  logAutonomousAction('🗺️ [Collaboration] Generating resource relationship map...', 'info')

  const map: Record<string, any> = {
    agents: [],
    documentation: [],
    synergies: [],
    timestamp: new Date().toISOString()
  }

  // 1. Discover Agents
  const agentsDir = path.join(process.cwd(), 'agents')
  if (fs.existsSync(agentsDir)) {
    const files = fs.readdirSync(agentsDir).filter(f => f.endsWith('.py') || f.endsWith('.ts'))
    files.forEach(file => {
      map.agents.push({
        id: file,
        type: file.endsWith('.py') ? 'python' : 'typescript',
        status: 'active'
      })
    })
  }

  // 2. Discover Documentation
  const docsDir = path.join(process.cwd(), 'docs')
  const rootDocs = fs.readdirSync(process.cwd()).filter(f => f.endsWith('.md'))

  rootDocs.forEach(doc => {
    map.documentation.push({ id: doc, location: 'root' })
  })

  if (fs.existsSync(docsDir)) {
    const docs = fs.readdirSync(docsDir).filter(f => f.endsWith('.md'))
    docs.forEach(doc => {
      map.documentation.push({ id: doc, location: 'docs/' })
    })
  }

  // 3. Heuristic Synergy Identification
  // Identify agents that likely work together based on naming or metadata
  const evolutionAgents = map.agents.filter((a: any) => a.id.toLowerCase().includes('evolution'))
  const intelligenceAgents = map.agents.filter((a: any) => a.id.toLowerCase().includes('intelligence') || a.id.toLowerCase().includes('knowledge'))

  if (evolutionAgents.length > 0 && intelligenceAgents.length > 0) {
    map.synergies.push({
      pair: ['EvolutionAgents', 'IntelligenceAgents'],
      type: 'COGNITIVE_FEEDBACK_LOOP',
      intensity: 0.9,
      actionable_item: 'Integrate real-time intelligence into autonomous refactoring cycles.'
    })
  }

  // Docker & CI/CD Synergies
  const cloudAgents = map.agents.filter((a: any) => a.id.toLowerCase().includes('cloud') || a.id.toLowerCase().includes('docker'))
  if (cloudAgents.length > 0) {
     map.synergies.push({
       pair: ['CloudAgents', 'DevOpsPipeline'],
       type: 'INFRASTRUCTURE_SOVEREIGNTY',
       intensity: 0.85,
       actionable_item: 'Enable automated container recovery and multi-cloud failover.'
     })
  }

  return map
}

export async function triggerEcosystemCollaboration() {
  logAutonomousAction('🚀 [Collaboration] Triggering ecosystem collaboration pipeline...', 'info')
  try {
    const jenkinsResult = await triggerJenkinsPipeline()
    logAutonomousAction(`✅ [Collaboration] Jenkins pipeline triggered: ${JSON.stringify(jenkinsResult)}`, 'info')
    return jenkinsResult
  } catch (error: any) {
    console.error('❌ [Collaboration] Failed to trigger Jenkins pipeline:', error.message)
    throw error
  }
}

export async function syncCollaborationState(branchIntelligence?: any[]) {
  logAutonomousAction('🔄 [Collaboration] Synchronizing autonomous state...', 'info')
  const metadata = await getMissionMetadata()
  const dockerHealth = await checkDockerHealth()
  const jenkinsHealth = await checkJenkinsHealth()
  const statePath = path.join(process.cwd(), 'autonomous_state.json')

  let currentState: any = {}
  if (fs.existsSync(statePath)) {
    try {
      currentState = JSON.parse(fs.readFileSync(statePath, 'utf8'))
    } catch (e) {
      console.warn('⚠️ [Collaboration] Failed to parse autonomous_state.json, starting fresh.')
    }
  }

  const { jules } = await import('../jules')
  const { workOrderService } = await import('./work_order')
  const branches = branchIntelligence || await jules.scanAllBranches()
  const workOrders = await workOrderService.getPendingOrders()

  const isCloud = !!(process.env.GITHUB_ACTIONS || process.env.GITLAB_CI || process.env.VERCEL || process.env.AUTONOMOUS_MODE === 'cloud')
  const cloudProvider = process.env.GITHUB_ACTIONS ? 'github-actions' : (process.env.GITLAB_CI ? 'gitlab-ci' : (process.env.VERCEL ? 'vercel' : (process.env.AUTONOMOUS_MODE === 'cloud' ? 'autonomous-cloud' : 'none')))

  const newState = {
    ...currentState,
    mission: metadata.missionStatement,
    stakeholders: metadata.stakeholders,
    docker: dockerHealth,
    jenkins: jenkinsHealth,
    intelligence: {
      branches: branches.length,
      pendingTasks: workOrders.length,
      totalOrders: (await import('./work_order').then(m => m.workOrderService.getPendingOrders())).length
    },
    execution_mode: isCloud ? 'cloud' : 'local',
    autonomous_mode: process.env.AUTONOMOUS_MODE || 'standard',
    cloud_provider: cloudProvider,
    system_presence: {
      status: 'online',
      agent: 'Jules',
      hostname: (await import('os')).hostname(),
      platform: process.platform
    },
    last_sync: new Date().toISOString()
  }

  // Persist to local fallback
  fs.writeFileSync(statePath, JSON.stringify(newState, null, 4))

  // Persist to MongoDB
  try {
    const client = await getMongoClient()
    const db = client.db()
    await db.collection('system_state').updateOne(
      { systemId: 'antigravity-alpha-01' },
      { $set: newState },
      { upsert: true }
    )
    logAutonomousAction('✅ [Collaboration] Autonomous state synchronized to MongoDB.', 'info')
  } catch (e) {
    console.error('❌ [Collaboration] Failed to sync state to MongoDB:', e)
  }

  return newState
}

export async function mergeEcosystemInsights(branchIntelligence: any[], workOrders: any[]) {
  const metadata = await getMissionMetadata()
  logAutonomousAction('🧠 [Collaboration] Merging ecosystem insights...', 'info')

  return {
    mission: metadata.missionStatement,
    goals: metadata.goals,
    branches: branchIntelligence,
    recentWork: workOrders.slice(-5),
    timestamp: new Date().toISOString()
  }
}
