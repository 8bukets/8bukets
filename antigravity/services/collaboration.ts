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
  const highIntensitySynergies = state.intelligence.relationshipMap.synergies?.filter((s: any) => s.intensity === 'High') || []
  const criticalActions = state.intelligence.relationshipMap.collaborationRecommendations?.filter((r: any) => r.priority === 'Critical') || []

  const synergyAlert = highIntensitySynergies.length > 0 || criticalActions.length > 0
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

  const { getStakeholderDirectives, generateActionableBriefing } = await import('./communication')
  const directives = await getStakeholderDirectives()
  const actionableBriefing = await generateActionableBriefing(state, directives)

  const detailedBriefing = `--- STRATEGIC SYNERGY ---\n${synergySummary}\n\n--- REQUIRED COORDINATION ---\n${recommendations}\n\n--- KEY RESULTS ---\n${branchSummary}\n\n--- ACTIONABLE INSIGHTS ---\n${actionableBriefing}`

  await dispatchExecutiveBriefing(
    `${synergyAlert} Posture: ${state.docker.status}. Analyzed ${state.intelligence.branches} branches.`,
    detailedBriefing
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
    synergies: [],
    functionalClusters: {}
  }

  // Phase 12: Dynamic Resource Discovery (Expanded)
  const scanDirs = [
    { path: 'antigravity/services', type: 'Service', pattern: /\.ts$/ },
    { path: 'scripts', type: 'Automation Script', pattern: /\.ts$|\.sh$/ },
    { path: 'agents', type: 'AI Agent', pattern: /\.md$|\.py$/ },
    { path: 'docs', type: 'Documentation', pattern: /\.md$/ },
    { path: 'app', type: 'UI Component', pattern: /\.tsx$|\.ts$/ },
    { path: 'web-app', type: 'UI Component', pattern: /\.tsx$|\.ts$/ },
    { path: 'database', type: 'Database Schema', pattern: /\.sql$|\.json$/ },
    { path: 'bin', type: 'Binary/Executable', pattern: /.*/ },
    { path: 'terraform', type: 'Infrastructure', pattern: /\.tf$/ },
    { path: 'public', type: 'Asset', pattern: /.*/ }
  ]

  for (const dir of scanDirs) {
    const fullPath = path.join(process.cwd(), dir.path)
    if (fs.existsSync(fullPath)) {
      try {
        const files = await fs.promises.readdir(fullPath)
        for (const file of files) {
          if (!file.includes('.test.') && (dir.pattern.test(file))) {
            map.resourceInventory.push({
              type: dir.type,
              name: file.split('.')[0],
              status: 'Active',
              path: `${dir.path}/${file}`
            })
          }
        }
      } catch (e) {}
    }
  }

  // Integrate autonomous knowledge into resource inventory
  const knowledgePath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json')
  if (fs.existsSync(knowledgePath)) {
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

  // Phase 12: Advanced Synergy Detection (Resource Overlap & Functional Dependencies)
  const resourceUsage: Record<string, Set<string>> = {}
  const functionalClusters: Record<string, Set<string>> = {}

  branches.forEach(b => {
    if (b.changedFiles) {
      b.changedFiles.forEach((f: string) => {
        const matchedResource = map.resourceInventory.find((r: any) => r.path && f.includes(r.path))
        if (matchedResource) {
          if (!resourceUsage[matchedResource.name]) resourceUsage[matchedResource.name] = new Set()
          resourceUsage[matchedResource.name].add(b.name)

          // Group by Functional Cluster (e.g., 'auth', 'database', 'cloud')
          const clusterMatch = matchedResource.name.match(/^(auth|db|database|cloud|neural|edge|api|ui|ux|security|knowledge|intelligence|analytics|evolution|creation|sync|collaboration)/i)
          if (clusterMatch) {
            const cluster = clusterMatch[0].toLowerCase()
            if (!functionalClusters[cluster]) functionalClusters[cluster] = new Set()
            functionalClusters[cluster].add(b.name)
          }
        }
      })
    }
  })

  map.collaborationRecommendations = []
  map.resourceDependencies = []
  map.crossDomainSynergies = []

  // Phase 12: Resource Dependency Tracking (Expanded Static Analysis)
  const trackableResources = map.resourceInventory.filter((r: any) => ['Service', 'UI Component', 'Automation Script'].includes(r.type))
  for (const resource of trackableResources) {
    if (!resource.path) continue
    try {
      const content = await fs.promises.readFile(path.join(process.cwd(), resource.path), 'utf8')
      // Support ./, ../, and @/ aliases, and account for varying import styles
      const imports = content.match(/import .* from ['"](@\/antigravity\/services\/|@\/antigravity\/|\.\/|\.\.\/services\/|\.\.\/)(.*)['"]/g) || []
      imports.forEach(imp => {
        const depMatch = imp.match(/['"](@\/antigravity\/services\/|@\/antigravity\/|\.\/|\.\.\/services\/|\.\.\/)(.*)['"]/)
        if (depMatch) {
          const depPathPart = depMatch[2].replace(/\.[jt]sx?$/, '')
          const depName = depPathPart.split('/').pop() || depPathPart

          // Find the specific resource that matches this dependency
          const target = map.resourceInventory.find((s: any) =>
            s.name === depName ||
            (s.path && s.path.includes(depPathPart)) ||
            (s.path && depPathPart.includes(s.name))
          )

          if (target && target.name !== resource.name) {
            // Deduplicate dependencies
            const exists = map.resourceDependencies.some((d: any) => d.source === resource.name && d.target === target.name)
            if (!exists) {
              map.resourceDependencies.push({
                source: resource.name,
                target: target.name,
                type: 'import',
                sourceType: resource.type,
                targetType: target.type
              })

              // Phase 13: Cross-Domain Synergy Detection
              if (resource.type !== target.type) {
                map.crossDomainSynergies.push({
                  source: resource.name,
                  sourceType: resource.type,
                  target: target.name,
                  targetType: target.type,
                  intensity: 'Medium'
                })
              }
            }
          }
        }
      })
    } catch (e) {}
  }

  // Resource Overlap Synergy
  Object.entries(resourceUsage).forEach(([resource, branchSet]) => {
    if (branchSet.size > 1) {
      const synergyBranchNames = Array.from(branchSet)
      const intensity = synergyBranchNames.length > 2 ? 'High' : 'Medium'
      map.synergies.push({
        type: 'Resource Conflict/Synergy',
        resource,
        branches: synergyBranchNames,
        intensity
      })

      const primaryStakeholders = stakeholders.filter(s => {
        const rolePrefix = s.role.toLowerCase().split(' ')[0]
        const emailPrefix = s.email.split('@')[0].toLowerCase()
        return synergyBranchNames.some(bn =>
          bn.toLowerCase().includes(rolePrefix) || bn.toLowerCase().includes(emailPrefix)
        )
      }).map(s => s.role)

      map.collaborationRecommendations.push({
        priority: intensity === 'High' ? 'Critical' : 'Routine',
        action: `Consolidate effort on '${resource}'`,
        resource,
        branches: synergyBranchNames,
        rationale: `${synergyBranchNames.length} branches are concurrently modifying '${resource}'. This indicates high developmental contention. ${primaryStakeholders.length > 0 ? `Urgent coordination required between: ${primaryStakeholders.join(', ')}.` : 'Strategic alignment recommended across independent teams.'}`
      })
    }
  })

  // Store functional clusters in the map for cross-service use
  Object.entries(functionalClusters).forEach(([cluster, branchSet]) => {
    map.functionalClusters[cluster] = Array.from(branchSet)
  })

  // Functional Cluster Synergy
  Object.entries(functionalClusters).forEach(([cluster, branchSet]) => {
    if (branchSet.size > 5) { // High density functional focus
      const synergyBranchNames = Array.from(branchSet)
      map.synergies.push({
        type: 'Functional Focus Synergy',
        resource: `Cluster: ${cluster}`,
        branches: synergyBranchNames,
        intensity: 'High'
      })

      map.collaborationRecommendations.push({
        priority: 'Medium',
        action: `Review '${cluster}' functional roadmaps`,
        resource: cluster,
        branches: synergyBranchNames,
        rationale: `${synergyBranchNames.length} branches are targeting the '${cluster}' functional area. This suggests a high-priority system evolution. Recommend a architectural review to ensure consistency.`
      })
    }
  })

  // Phase 13: Strategic Impact Scoring
  map.impactfulBranches = branches.map(b => {
    let score = 0;

    // 1. Category Priority
    const categoryWeights: Record<string, number> = {
      'security': 50,
      'performance': 40,
      'fix': 30,
      'feature': 20,
      'documentation': 10,
      'maintenance': 5,
      'other': 0
    };
    score += categoryWeights[b.category] || 0;

    // 2. Alignment with Strategic Goals
    Object.entries(map.goalAlignment).forEach(([goal, relevantBranches]: [string, any]) => {
      if (relevantBranches.includes(b.name)) {
        score += 25; // Bonus for each goal it aligns with
      }
    });

    // 3. Artifact Impact
    if (b.changedFiles) {
      score += Math.min(b.changedFiles.length * 2, 40); // Cap artifact bonus at 40

      const coreFiles = b.changedFiles.filter((f: string) =>
        f.includes('core.ts') || f.includes('jules.ts') || f.includes('collaboration.ts') || f.includes('intelligence.ts')
      );
      score += coreFiles.length * 15; // Extra weight for core file modifications
    }

    return {
      name: b.name,
      category: b.category,
      score,
      results: b.results
    };
  }).sort((a, b) => b.score - a.score).slice(0, 20);

  // Integrate branch results into resources (Expanded categories)
  const resultCategories = ['feature', 'fix', 'performance', 'security', 'ux']
  branches.filter(b => resultCategories.includes(b.category) && b.results && b.results !== 'N/A').forEach(b => {
    map.resourceInventory.push({
      type: 'Branch Result',
      name: b.name,
      status: 'Ready for Merge',
      result: b.results,
      category: b.category
    })
  })

  return map
}

export async function syncCollaborationState(branchIntelligence?: any[]) {
  console.log('🔄 [Collaboration] Synchronizing autonomous state...')
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
  const workOrders = await workOrderService.getPendingOrders() // Simplified for now
  const relationshipMap = await generateRelationshipMap(branches, metadata.stakeholders, metadata.goals)

  // Phase 12: Synchronize Global Neural Pulse and Omni-Presence Relay
  const neuralPulse = await broadcastPulse()
  const relayState = await getRelayState()

  // Phase 12: Integrate Stakeholder Directives
  const { getStakeholderDirectives } = await import('./communication')
  const directives = await getStakeholderDirectives()

  await mergeBranchInsights(branches, relationshipMap)

  const newState = {
    ...currentState,
    mission: metadata.missionStatement,
    stakeholders: metadata.stakeholders,
    directives,
    docker,
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

export async function mergeBranchInsights(branches: any[], relationshipMap?: any) {
  console.log('🧠 [Collaboration] Merging branch insights into ecosystem matrix...')
  const knowledgePath = path.join(process.cwd(), 'KNOWLEDGE_MERGE.md')

  let existingContent = '';
  if (fs.existsSync(knowledgePath)) {
    existingContent = await fs.promises.readFile(knowledgePath, 'utf8');
  }

  // Phase 13: Enhanced ID-based deduplication
  const seenInsights = new Set<string>();

  const relevantBranches = branches.filter(b => {
    // Phase 12: Broadened filter to include more meaningful results
    const hasMeaningfulResult = b.results && b.results !== 'N/A' && b.results.length > 5;

    if (!(b.knowledge || hasMeaningfulResult)) {
      return false;
    }

    // Generate unique ID for this insight
    const insightId = `${b.name}|${b.category}|${b.results}|${b.knowledge || ''}`;
    if (seenInsights.has(insightId)) return false;
    seenInsights.add(insightId);

    // Improved deduplication: Check if this specific result or knowledge for this branch is already recorded
    const branchIdentifier = `- **Branch:** \`${b.name}\``;
    const resultIdentifier = `  - **Result:** ${b.results}`;
    const knowledgeIdentifier = b.knowledge ? `  - **Knowledge:** ${b.knowledge}` : '';

    if (existingContent.includes(branchIdentifier)) {
        // Isolate the section for this branch to avoid cross-branch false positives
        const parts = existingContent.split(branchIdentifier)
        for (let i = 1; i < parts.length; i++) {
          const branchSection = parts[i].split('##')[0];
          // Robust deduplication matching both results and knowledge nuggets
          const matchResult = branchSection.includes(resultIdentifier);
          const matchKnowledge = !knowledgeIdentifier || branchSection.includes(knowledgeIdentifier);
          if (matchResult && matchKnowledge) {
              return false;
          }
        }
    }

    return true;
  })

  if (relevantBranches.length === 0) return

  // Phase 13: Group by Domain for higher strategic signal
  const domains: Record<string, any[]> = {}
  relevantBranches.forEach(b => {
    const domain = b.domain || 'General'
    if (!domains[domain]) domains[domain] = []
    domains[domain].push(b)
  })

  let newEntries = `\n## Ecosystem Knowledge Consolidation (${new Date().toISOString()})\n`

  // Phase 12: Integrated Resource Dependency Summary
  if (relationshipMap?.resourceDependencies && relationshipMap.resourceDependencies.length > 0) {
    newEntries += `### 🔗 Resource Dependency Matrix\n`
    const dependencies = relationshipMap.resourceDependencies.slice(0, 10)
    dependencies.forEach((d: any) => {
      newEntries += `- \`${d.source}\` -> depends on -> \`${d.target}\` (${d.type})\n`
    })
    if (relationshipMap.resourceDependencies.length > 10) {
      newEntries += `- _...and ${relationshipMap.resourceDependencies.length - 10} more dependencies._\n`
    }
    newEntries += `\n`
  }

  // Highlight Strategic Synergies from the relationship map
  if (relationshipMap?.synergies && relationshipMap.synergies.length > 0) {
    newEntries += `### ⚡ Strategic Synergy Highlights\n`
    const synergies = relationshipMap.synergies.slice(0, 10)
    synergies.forEach((s: any) => {
      newEntries += `- **SYNERGY [${s.intensity}]:** \`${s.resource}\` involves branches: ${s.branches.slice(0, 3).join(', ')}${s.branches.length > 3 ? '...' : ''}\n`
    })
    newEntries += `\n`
  }

  // Phase 13: High-Impact Strategic Results
  if (relationshipMap?.impactfulBranches && relationshipMap.impactfulBranches.length > 0) {
    newEntries += `### 🏆 Top Impactful Strategic Results\n`
    relationshipMap.impactfulBranches.slice(0, 5).forEach((b: any) => {
      newEntries += `- **[Score: ${b.score}]** \`${b.name}\` (${b.category}): ${b.results}\n`
    })
    newEntries += `\n`
  }

  Object.entries(domains).forEach(([domain, branchList]) => {
    newEntries += `### 🌐 Strategic Domain: ${domain}\n`
    branchList.forEach(b => {
      newEntries += `- **Branch:** \`${b.name}\`\n`
      newEntries += `  - **Category:** ${b.category?.toUpperCase()}\n`
      newEntries += `  - **Result:** ${b.results || b.result || 'N/A'}\n`
      if (b.lastSeen) {
        newEntries += `  - **Activity:** Last active ${b.lastSeen}\n`
      }
      if (b.knowledge) {
        newEntries += `  - **Knowledge:** ${b.knowledge}\n`
      }
      if (b.changedFiles && b.changedFiles.length > 0) {
        newEntries += `  - **Artifacts:** ${b.changedFiles.length} files modified.\n`
        const criticalFiles = b.changedFiles.filter((f: string) => f.includes('core.ts') || f.includes('jules.ts') || f.includes('collaboration.ts'))
        if (criticalFiles.length > 0) {
          newEntries += `  - **Critical Impact:** Branch modifies core ecosystem files.\n`
        }
      }
    })
    newEntries += `\n`
  })

  if (existingContent) {
      await fs.promises.writeFile(knowledgePath, existingContent + newEntries, 'utf8')
  } else {
      await fs.promises.writeFile(knowledgePath, `# Market Intelligence Matrix\n${newEntries}`, 'utf8')
  }

  const domainCount = Object.keys(domains).length;
  console.log(`✅ [Collaboration] Merged ${relevantBranches.length} branch insights across ${domainCount} strategic domains.`)
}

export async function mergeEcosystemInsights(branchIntelligence: any[], workOrders: any[]) {
  const metadata = await getMissionMetadata()
  console.log('🧠 [Collaboration] Merging ecosystem insights...')

  const relationshipMap = await generateRelationshipMap(branchIntelligence, metadata.stakeholders, metadata.goals)
  await mergeBranchInsights(branchIntelligence, relationshipMap)
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
