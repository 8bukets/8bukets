import fs from 'fs'
import path from 'path'
import { z } from 'zod'
import { autonomousFetch } from '@/antigravity/core'
import { checkDockerHealth } from './docker'

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
  console.log('🌐 [Collaboration] Exporting ecosystem metadata for global sync...')
  return {
    ...metadata,
    systemId: 'antigravity-alpha-01',
    timestamp: new Date().toISOString()
  }
}

export async function syncCollaborationState(branchIntelligence?: any[]) {
  console.log('🔄 [Collaboration] Synchronizing autonomous state...')
  const metadata = await getMissionMetadata()
  const dockerHealth = await checkDockerHealth()
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
  const workOrders = workOrderService.getPendingOrders() // Simplified for now

  const newState = {
    ...currentState,
    mission: metadata.missionStatement,
    stakeholders: metadata.stakeholders,
    docker: dockerHealth,
    intelligence: {
      branches: branches.length,
      pendingTasks: workOrders.length
    },
    last_sync: new Date().toISOString()
  }

  fs.writeFileSync(statePath, JSON.stringify(newState, null, 4))
  console.log('✅ [Collaboration] Autonomous state synchronized successfully.')
  return newState
}

export async function mergeEcosystemInsights(branchIntelligence: any[], workOrders: any[]) {
  const metadata = await getMissionMetadata()
  console.log('🧠 [Collaboration] Merging ecosystem insights...')

  return {
    mission: metadata.missionStatement,
    goals: metadata.goals,
    branches: branchIntelligence,
    recentWork: workOrders.slice(-5),
    timestamp: new Date().toISOString()
  }
}
