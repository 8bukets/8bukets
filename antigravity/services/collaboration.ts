import { logAutonomousAction } from '../core'
import fs from 'fs'
import path from 'path'
import { z } from 'zod'
import { autonomousFetch } from '@/antigravity/core'
import { isDockerHealthy as checkDockerHealth } from './docker'
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
    if (!fs.existsSync(MISSION_PATH)) {
      throw new Error('Mission document missing. System collaboration impaired.')
    }

    const content = fs.readFileSync(MISSION_PATH, 'utf8')

    const missionStatementMatch = content.match(/#(?:# Mission Statement| Antigravity Mission)\n([\s\S]*?)(\n##|$)/)
    let missionStatement = missionStatementMatch ? missionStatementMatch[1].trim() : 'Autonomous Evolution'
    if (!missionStatement) missionStatement = 'Autonomous Evolution'

    const stakeholders: Stakeholder[] = []
    const stakeholderSection = content.match(/## Stakeholders\n([\s\S]*?)(\n##|$)/)
    if (stakeholderSection) {
      const lines = stakeholderSection[1].trim().split('\n')
      lines.forEach(line => {
        const parts = line.match(/-\s*(.*?)\s*<(.*?)>/)
        if (parts && parts.length === 3) {
          stakeholders.push({
            role: parts[1].trim(),
            email: parts[2].trim()
          })
        }
      })
    }

    const goals: string[] = []
    const goalsSection = content.match(/## (?:Strategic Goals|Goals)\n([\s\S]*?)(\n##|$)/)
    if (goalsSection) {
      const lines = goalsSection[1].trim().split('\n')
      lines.forEach(line => {
        const goal = line.replace(/^(?:\d+\.|\-)\s*/, '').trim()
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
  const highIntensitySynergies = state.intelligence.relationshipMap.synergies?.filter((s: any) => s.intensity === 'High') || []
  const criticalActions = state.intelligence.relationshipMap.collaborationRecommendations?.filter((r: any) => r.priority === 'Critical') || []

  const synergyAlert = highIntensitySynergies.length > 0
    ? `⚠️ CRITICAL: ${highIntensitySynergies.length} High-Intensity synergies requiring coordination.`
    : 'System synergy is optimal.'

  const synergySummary = state.intelligence.relationshipMap.synergies && state.intelligence.relationshipMap.synergies.length > 0
    ? state.intelligence.relationshipMap.synergies.slice(0, 5).map((s: any) => `- SYNERGY [${s.intensity}]: ${s.resource} (via ${s.branches.length} branches)`).join('\n')
    : 'No direct resource synergies detected.'

  const recommendations = state.intelligence.relationshipMap.collaborationRecommendations?.length > 0
    ? state.intelligence.relationshipMap.collaborationRecommendations.slice(0, 10).map((r: any) => `- [${r.priority}] ${r.action}: ${r.rationale}`).join('\n')
    : 'No immediate collaboration actions required.'

  const branchSummary = state.intelligence.relationshipMap.resourceInventory
    .filter((r: any) => r.type === 'Branch Result')
    .slice(0, 5)
    .map((r: any) => `- RESULT: ${r.name} -> ${r.result}`)
    .join('\n')

  const detailedBriefing = `--- STRATEGIC SYNERGY ---\n${synergySummary}\n\n--- REQUIRED COORDINATION ---\n${recommendations}\n\n--- KEY RESULTS ---\n${branchSummary}`

  await dispatchExecutiveBriefing(
    `${synergyAlert} Posture: ${state.docker.status}. Analyzed ${state.intelligence.branches} branches.`,
    detailedBriefing
  )

  const logDir = path.join(process.cwd(), 'logs')
  if (!fs.existsSync(logDir)) await fs.promises.mkdir(logDir, { recursive: true })

  // Deduplication logic: scan for existing titles
  const existingNuggets = content.match(/### .+/g) || [];
  const existingTitles = new Set(existingNuggets.map(t => t.replace('### ', '').trim()));

  let newNuggets = '\n## 🧠 Discovered Knowledge Nuggets\n';

  // Limit to most recent branches to reduce bloat
  const relevantBranches = branches
    .sort((a, b) => new Date(b.lastSeen).getTime() - new Date(a.lastSeen).getTime())
    .slice(0, 20);

  for (const branch of relevantBranches) {
    // Selection criteria: must have a colon, must be > 10 chars, must not be a chore/fix unless significant
    const msg = branch.lastMessage || '';
    if (msg.includes(':') && msg.length > 10 && !existingTitles.has(msg)) {
      const [prefix, description] = msg.split(':');
      const lowerPrefix = prefix.toLowerCase();

      // Filter for high-signal prefixes
      const highSignal = ['feat', 'docs', 'bolt', 'palette', 'sentinel', 'research'].some(s => lowerPrefix.includes(s));

      if (highSignal && description && description.trim().length > 5) {
        newNuggets += `### ${prefix.trim()}\n- **Source**: branch ${branch.name}\n- **Insight**: ${description.trim()}\n\n`;
        existingTitles.add(msg);
        nuggetsAdded++;
      }
    }
  }

  if (nuggetsAdded > 0) {
    // Insert before signature
    const escapedSignature = signature.replace(/[-/\\^$*+?.()|[\]{}]/g, '\\$&');
    const sigRegex = new RegExp(`\\n*---\\n*${escapedSignature}\\n*|\\n*${escapedSignature}\\n*`, 'g');

    if (content.includes(signature)) {
      content = content.replace(sigRegex, '\n\n' + newNuggets + '\n\n---\n' + signature + '\n');
    } else {
      content += '\n' + newNuggets + '\n\n---\n' + signature + '\n';
    }

    fs.writeFileSync(knowledgePath, content);
  }

  return { nuggets: nuggetsAdded };
}

export async function generateRelationshipMap() {
  logAutonomousAction('🗺️ [Collaboration] Generating resource relationship map...', 'info');
  const metadata = await getMissionMetadata();
  const { jules } = await import('../jules');
  const branches = await jules.scanAllBranches();

  // Cross-reference stakeholders and goals with ecosystem components
  const relationshipMap = {
    system: 'antigravity-alpha-01',
    stakeholders: metadata.stakeholders.map(s => ({
      ...s,
      associated_domains: branches
        .filter(b => b.name.includes(s.role.toLowerCase()) || b.lastMessage.toLowerCase().includes(s.role.toLowerCase()))
        .map(b => b.name)
    })),
    strategic_goals: metadata.goals.map(g => ({
      goal: g,
      tracking_branches: branches
        .filter(b => g.toLowerCase().split(' ').some(word => word.length > 3 && b.name.toLowerCase().includes(word)))
        .map(b => b.name)
    })),
    timestamp: new Date().toISOString()
  };

  return relationshipMap;
}

export async function syncCollaborationState(branchIntelligence?: any[]) {
  logAutonomousAction('🔄 [Collaboration] Synchronizing autonomous state...', 'info')
  const metadata = await getMissionMetadata()

  const dockerHealthy = await checkDockerHealth()
  const dockerContainers = await (await import('./docker')).getDockerStatus()
  const docker = {
    status: dockerHealthy ? 'optimal' : 'degraded',
    containerCount: dockerContainers.length
  }

  const jenkinsStatus = await getLatestBuildStatus()
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
    docker,
    jenkins: jenkinsStatus,
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

export async function mergeBranchInsights(branches: any[]) {
  console.log('🧠 [Collaboration] Merging branch insights into ecosystem matrix...')
  const knowledgePath = path.join(process.cwd(), 'KNOWLEDGE_MERGE.md')

  let existingContent = '';
  if (fs.existsSync(knowledgePath)) {
    existingContent = await fs.promises.readFile(knowledgePath, 'utf8');
  }

  const relevantBranches = branches.filter(b => {
    // Only include branches with meaningful knowledge or results
    if (!(b.knowledge || (b.results && b.results !== b.lastMessage && b.results !== 'N/A'))) {
      return false;
    }

    // Improved deduplication: Check if this specific result or knowledge for this branch is already recorded
    const branchIdentifier = `- **Branch:** \`${b.name}\``;
    const resultIdentifier = `  - **Result:** ${b.results}`;
    const knowledgeIdentifier = b.knowledge ? `  - **Knowledge:** ${b.knowledge}` : '';

    if (existingContent.includes(branchIdentifier)) {
        // Isolate the section for this branch to avoid cross-branch false positives
        const parts = existingContent.split(branchIdentifier)
        for (let i = 1; i < parts.length; i++) {
          const branchSection = parts[i].split('##')[0];
          if (branchSection.includes(resultIdentifier) && (!knowledgeIdentifier || branchSection.includes(knowledgeIdentifier))) {
              return false;
          }
        }
    }

    return true;
  })

  if (relevantBranches.length === 0) return

  const categories: Record<string, Record<string, any[]>> = {}
  relevantBranches.forEach(b => {
    const category = b.category || 'other'
    const domain = b.domain || 'General'
    if (!categories[category]) categories[category] = {}
    if (!categories[category][domain]) categories[category][domain] = []
    categories[category][domain].push(b)
  })

  let newEntries = `\n## Ecosystem Knowledge Consolidation (${new Date().toISOString()})\n`

  Object.entries(categories).forEach(([category, domains]) => {
    newEntries += `### 📂 Category: ${category.toUpperCase()}\n`
    Object.entries(domains).forEach(([domain, branchList]) => {
      newEntries += `#### 🌐 Strategic Domain: ${domain}\n`
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
  })

  if (existingContent) {
      await fs.promises.writeFile(knowledgePath, existingContent + newEntries, 'utf8')
  } else {
      await fs.promises.writeFile(knowledgePath, `# Market Intelligence Matrix\n${newEntries}`, 'utf8')
  }

  const domainCount = Object.values(categories).reduce((acc, d) => acc + Object.keys(d).length, 0)
  console.log(`✅ [Collaboration] Merged ${relevantBranches.length} branch insights across ${Object.keys(categories).length} categories and ${domainCount} domains.`)
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
