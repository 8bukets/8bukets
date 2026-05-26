import fs from 'fs'
import path from 'path'
import { z } from 'zod'
import { autonomousFetch } from '@/antigravity/core'
import { checkDockerHealth } from './docker'
import { getLatestBuildStatus } from './jenkins'
import { dispatchExecutiveBriefing } from './notification'
import { getStakeholderDirectives, generateActionableBriefing, dispatchStakeholderAlert } from './communication'


/**
 * ANTIGRAVITY COLLABORATION SERVICE (Phase 12)
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
    if (! fs.existsSync(MISSION_PATH)) {
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
 * Phase 12: Multi-Agent Collaboration Protocol
 * Notifies stakeholders of the current system state and recent autonomous evolutions.
 */
export async function broadcastToStakeholders(state: any) {
  const metadata = await getMissionMetadata()
  const directives = await getStakeholderDirectives()

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
  console.log(summary)

  const actionableBriefing = await generateActionableBriefing(state, directives)

  // Dispatch executive briefing for high-level communication
  const highIntensitySynergies = state.intelligence.relationshipMap.synergies?.filter((s: any) => s.intensity === 'High') || []
  const synergyAlert = highIntensitySynergies.length > 0
    ? `⚠️ ALERT: ${highIntensitySynergies.length} High-Intensity resource conflicts detected.`
    : 'System synergy is optimal.'

  const synergySummary = state.intelligence.relationshipMap.synergies && state.intelligence.relationshipMap.synergies.length > 0
    ? state.intelligence.relationshipMap.synergies.map((s: any) => `- SYNERGY [${s.intensity}]: ${s.resource} (via ${s.branches.length} branches)`).join('\n')
    : 'No direct resource synergies detected.'

  const detailedBriefing = `--- ACTIONABLE INSIGHTS ---\n${actionableBriefing}\n\n--- SYNERGY ANALYSIS ---\n${synergySummary}`

  await dispatchExecutiveBriefing(
    `${synergyAlert} Posture: ${state.docker.status}. Sync: ${state.intelligence.branches} branches.`,
    detailedBriefing
  )

  if (highIntensitySynergies.length > 0) {
    await dispatchStakeholderAlert(
      'High Intensity Resource Synergy Detected',
      `System has detected ${highIntensitySynergies.length} clusters of high-intensity resource overlap. Immediate consolidation recommended.`,
      'warning'
    )
  }

  const logDir = path.join(process.cwd(), 'logs')
  if (! fs.existsSync(logDir)) await fs.promises.mkdir(logDir, { recursive: true })

  await fs.promises.appendFile(path.join(logDir, 'collaboration.log'), summary)

  return { notifiedCount: metadata.stakeholders.length }
}

export async function generateRelationshipMap(branches: any[], stakeholders: Stakeholder[], goals: string[]) {
  console.log('🗺️ [Collaboration] Generating relationship map...')

  const map: any = {
    stakeholderEngagement: {},
    goalAlignment: {},
    resourceInventory: [],
    synergies: [],
    domainOwnership: {},
    resourceHealth: {}
  }

  // Phase 12: Dynamic Resource Discovery (Expanded)
  const scanDirs = [
    { path: 'antigravity/services', type: 'Service', pattern: /\.ts$/ },
    { path: 'scripts', type: 'Automation Script', pattern: /\.ts$|\.sh$/ },
    { path: 'app', type: 'UI Component', pattern: /\.tsx$|\.ts$/ },
    { path: 'web-app', type: 'UI Component', pattern: /\.tsx$|\.ts$/ },
    { path: 'agents', type: 'AI Agent', pattern: /\.md$|\.py$/ },
    { path: 'docs', type: 'Documentation', pattern: /\.md$/ },
    { path: 'public', type: 'Asset', pattern: /.*/ }
  ]

  for (const dir of scanDirs) {
    const fullPath = path.join(process.cwd(), dir.path)
    if ( fs.existsSync(fullPath)) {
      try {
        const files = await fs.promises.readdir(fullPath)
        for (const file of files) {
          if (!file.includes('.test.') && (dir.pattern.test(file))) {
            const fileName = file.split('.')[0];
            const filePath = `${dir.path}/${file}`;
            const stats = await fs.promises.stat(fullPath + '/' + file);

            map.resourceInventory.push({
              type: dir.type,
              name: fileName,
              status: 'Active',
              path: filePath
            })

            // Resource Health Metrics
            map.resourceHealth[fileName] = {
              lastModified: stats.mtime.toISOString(),
              contributorCount: branches.filter(b => b.changedFiles?.includes(filePath)).length,
              status: (Date.now() - stats.mtime.getTime() > 1000 * 60 * 60 * 24 * 7) ? 'Stale' : 'Healthy'
            }
          }
        }
      } catch (e) {}
    }
  }

  // Integrate autonomous knowledge into resource inventory
  const knowledgePath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json')
  if ( fs.existsSync(knowledgePath)) {
    try {
      const content = await fs.promises.readFile(knowledgePath, 'utf8')
      const systemKnowledge = JSON.parse(content)

      // Phase 12: Support both nested 'typescript_sections' and unified flat key structure
      const allKnowledge: any[] = []

      // Explicitly handled legacy/standard keys
      if (Array.isArray(systemKnowledge.sections)) allKnowledge.push(...systemKnowledge.sections)
      if (Array.isArray(systemKnowledge.typescript_sections)) allKnowledge.push(...systemKnowledge.typescript_sections)

      // Dynamic discovery for flat hierarchical structure (market_data, ai_agents, etc.)
      Object.entries(systemKnowledge).forEach(([key, value]) => {
        if (key !== 'metadata' && key !== 'sections' && key !== 'typescript_sections' && Array.isArray(value)) {
          allKnowledge.push(...value)
        }
      })

      allKnowledge.forEach((k: any) => {
        if (k && k.title) {
          map.resourceInventory.push({
            type: 'Knowledge',
            name: k.title,
            status: 'Ingested',
            source: k.metadata?.source
          })
        }
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
    const rolePrefix = s.role.toLowerCase().split(' ')[0]
    const emailPrefix = s.email.split('@')[0].toLowerCase()

    const activeBranches = branches.filter(b => {
      const branchName = (b?.name || '').toLowerCase();
      return b.category === 'agent' ||
             branchName.includes(rolePrefix) ||
             branchName.includes(emailPrefix);
    });

    map.stakeholderEngagement[s.role] = {
      email: s.email,
      activeProjects: activeBranches.map(b => b.name)
    }

    // Domain Ownership Tracking
    activeBranches.forEach(b => {
      const domain = b.domain || 'General';
      if (!map.domainOwnership[domain]) map.domainOwnership[domain] = new Set();
      map.domainOwnership[domain].add(s.role);
    });
  })

  // Convert Sets to Arrays for JSON serialization
  Object.keys(map.domainOwnership).forEach(d => {
    map.domainOwnership[d] = Array.from(map.domainOwnership[d]);
  });

  // Identify Static "Resources" (Documentation)
  map.resourceInventory.push(
    { type: 'Documentation', name: 'AGENTS.md', status: 'Active' },
    { type: 'Documentation', name: 'CONSOLIDATED_INTELLIGENCE.md', status: 'Active' },
    { type: 'Documentation', name: 'KNOWLEDGE_MERGE.md', status: 'Active' }
  )

  // Phase 12: Advanced Synergy Detection (Resource Overlap & Weighted Analysis)
  const resourceUsage: Record<string, Set<string>> = {}
  const BASELINE_BRANCHES = ['main', 'origin/main', 'origin/HEAD', 'origin']
  const BOILERPLATE_RESOURCES = ['layout', 'page', 'globals', 'favicon', 'file', 'globe', 'next', 'vercel', 'window']

  const resourceWeights: Record<string, number> = {
    'Service': 10,
    'Automation Script': 8,
    'AI Agent': 15,
    'UI Component': 5,
    'Documentation': 3,
    'Knowledge': 2,
    'Asset': 1
  }

  branches.forEach(b => {
    if (BASELINE_BRANCHES.includes(b.name)) return // Skip baseline branches for synergy detection

    if (b.changedFiles) {
      b.changedFiles.forEach((f: string) => {
        const matchedResource = map.resourceInventory.find((r: any) => r.path && f.includes(r.path))
        if (matchedResource) {
          if (!resourceUsage[matchedResource.name]) resourceUsage[matchedResource.name] = new Set()
          resourceUsage[matchedResource.name].add(b.name)
        }
      })
    }
  })

  map.collaborationRecommendations = []
  const domainRecommendations: Record<string, any[]> = {}

  Object.entries(resourceUsage).forEach(([resourceName, branchSet]) => {
    if (branchSet.size > 1) {
      const resource = map.resourceInventory.find((r: any) => r.name === resourceName)
      const type = resource?.type || 'Other'
      const weight = resourceWeights[type] || 1
      const branchesNames = Array.from(branchSet)

      // Suppress high-intensity noise for common boilerplate files unless they have extreme overlap (>10 branches)
      const isBoilerplate = BOILERPLATE_RESOURCES.includes(resourceName)
      let intensity = 'Medium'
      if (branchesNames.length > 5 || (weight >= 10 && branchesNames.length > 2)) intensity = 'High'
      if (isBoilerplate && branchesNames.length < 10) intensity = 'Low'

      map.synergies.push({
        type: 'Resource Conflict/Synergy',
        resource: resourceName,
        resourceType: type,
        branches: branchesNames,
        intensity,
        weight
      })

      // Phase 12: Generate Actionable Collaboration Recommendations
      const stakeholdersToCoordinate = stakeholders.filter(s =>
        map.stakeholderEngagement[s.role]?.activeProjects.some((ap: string) => branchesNames.includes(ap))
      )

      const coordinationAdvice = stakeholdersToCoordinate.length > 1
        ? `Coordinate with ${stakeholdersToCoordinate.map(s => s.role).join(' and ')}.`
        : (stakeholdersToCoordinate.length === 1 ? `Coordinate with ${stakeholdersToCoordinate[0].role}.` : 'Review branch owners for alignment.')

      // Group by Domain
      const branchObjs = branches.filter(b => branchesNames.includes(b.name))
      const domain = branchObjs[0]?.domain || 'General'

      if (!domainRecommendations[domain]) domainRecommendations[domain] = []

      domainRecommendations[domain].push({
        priority: intensity === 'High' ? 'Critical' : (intensity === 'Medium' ? 'Routine' : 'Low'),
        action: `Consolidate effort on '${resourceName}' (${type})`,
        resource: resourceName,
        branches: branchesNames,
        rationale: `${branchesNames.length} branches are concurrently modifying this ${type.toLowerCase()}. ${coordinationAdvice}`,
        stakeholders: stakeholdersToCoordinate.map(s => s.role),
        domain
      })

      if (intensity === 'High') {
        console.warn(`🤝 [Collaboration] High-Intensity Synergy Detected: ${branchesNames.length} branches working on ${resourceName} (${type}).`)
      }
    }
  })

  // Flatten and Deduplicate recommendations by prioritizing Critical ones
  Object.values(domainRecommendations).forEach(recs => {
    map.collaborationRecommendations.push(...recs)
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
  if ( fs.existsSync(statePath)) {
    try {
      const content = await fs.promises.readFile(statePath, 'utf8')
      currentState = JSON.parse(content)
    } catch (e) {
      console.warn('⚠️ [Collaboration] Failed to parse autonomous_state.json, starting fresh.')
    }
  }

  const { jules } = await import('../jules')
  const { workOrderService } = await import('./work_order')
  const { broadcastPulse } = await import('./neural')
  const { getRelayState } = await import('./relay')

  // Phase 12: Trigger deep branch scan (force: true) to ensure all 1,800+ branches are analyzed
  const branches = branchIntelligence || await jules.scanAllBranches(true)
  const workOrders = workOrderService.getPendingOrders() // Simplified for now
  const relationshipMap = await generateRelationshipMap(branches, metadata.stakeholders, metadata.goals)

  // Phase 12: Synchronize Global Neural Pulse and Omni-Presence Relay
  const neuralPulse = await broadcastPulse()
  const relayState = await getRelayState()

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
      relationshipMap,
      neuralPulse,
      relayState
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
  if ( fs.existsSync(knowledgePath)) {
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
          const hasResult = branchSection.includes(resultIdentifier);
          const hasKnowledge = !knowledgeIdentifier || branchSection.includes(knowledgeIdentifier);

          if (hasResult && hasKnowledge) {
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
  newEntries += `*Phase 12 Multi-Agent Synergy Protocol Active*\n\n`

  Object.entries(categories).forEach(([category, domains]) => {
    newEntries += `### 📂 Category: ${category.toUpperCase()}\n`
    Object.entries(domains).forEach(([domain, branchList]) => {
      newEntries += `#### 🌐 Strategic Domain: ${domain}\n`
      branchList.forEach(b => {
        const impactEmoji = (b.changedFiles && b.changedFiles.length > 20) ? '🔥' : (b.changedFiles && b.changedFiles.length > 5 ? '⚡' : '✨');
        newEntries += `- **Branch:** \`${b.name}\` ${impactEmoji}\n`
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
  if ( fs.existsSync(knowledgePath)) {
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
