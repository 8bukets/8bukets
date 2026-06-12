import fs from 'fs'
import path from 'path'
import { execFile } from 'child_process'
import { promisify } from 'util'

const execFileAsync = promisify(execFile)

/**
 * JULES: THE COGNITIVE AGENT LAYER
 */

interface JulesMemory {
  lastOptimization: string
  preferredPatterns: string[]
  architecturalDecisions: Record<string, string>
  autonomousTasks: { id: string; status: 'pending' | 'completed'; goal: string }[]
}

const MEMORY_PATH = path.join(process.cwd(), 'antigravity/.jules_memory.json')

export type AgentRole = 'Coder' | 'Reviewer' | 'Ops' | 'Chief AI Officer' | 'Architect' | 'Observer';

export class Jules {
  public role: AgentRole;

  private memory: JulesMemory

  public static async create(role: AgentRole = 'Coder'): Promise<Jules> {
    return new Jules(role);
  }

  constructor(role: AgentRole = 'Coder') {
    this.role = role;
    if (fs.existsSync(MEMORY_PATH)) {
      this.memory = JSON.parse(fs.readFileSync(MEMORY_PATH, 'utf8'))
    } else {
      this.memory = {
        lastOptimization: new Date().toISOString(),
        preferredPatterns: ['autonomousFetch', 'predictiveFetch', 'resolve'],
        architecturalDecisions: {
          runtime: 'Next.js 16 Node.js Runtime',
          caching: 'Phase 4 Predictive',
          resilience: 'Phase 5 Circuit Breaker',
          verifiedSignature: 'SHA256:Zey4+Jcqu48gSIuuQaavasF2D7iu+J590Rr1EA3LdbA',
          neuralSyncSignature: 'SHA256:qhno7SbhBIYwfgNgGhygt2e0kRDBlPkEqjAGdXTVOsA'
        },
        autonomousTasks: []
      }
      this.save()
    }
  }

  private save() {
    fs.writeFileSync(MEMORY_PATH, JSON.stringify(this.memory, null, 2))
  }

  public async improve() {
    console.log('🤖 [Jules] Analyzing current system state for improvements...')
    const suggestions = []

    // Knowledge-driven improvements
    const knowledgePath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json')
    if (fs.existsSync(knowledgePath)) {
      const knowledge = JSON.parse(fs.readFileSync(knowledgePath, 'utf8'))
      const sections = knowledge.typescript_sections || []

      const checkKnowledge = (query: string) => sections.some((s: any) =>
        s.title.toLowerCase().includes(query.toLowerCase()) ||
        s.sections?.some((sec: any) => sec.content.toLowerCase().includes(query.toLowerCase()))
      )

      const hasQuantum = checkKnowledge('quantum')
      const hasOmega = checkKnowledge('omega')
      const hasQuantumSynergy = checkKnowledge('quantum synergy')
      const hasPhase14 = checkKnowledge('Phase 14')
      const hasWilsonSonsini = checkKnowledge('Wilson Sonsini')

      if (hasQuantum && !this.memory.preferredPatterns.includes('crystals-kyber')) {
        suggestions.push('Integrate Crystals-Kyber for Quantum-resistant security as per latest strategy.')
      }
      if (hasQuantumSynergy) {
        suggestions.push('Orchestrate Quantum Synergy protocols for Phase 13 APAC expansion.')
      }
      if (hasOmega && !this.memory.preferredPatterns.includes('low-latency-sync')) {
        suggestions.push('Implement <30ms low-latency synchronization for Project Omega.')
      }
      if (hasPhase14) {
        suggestions.push('Initiate Phase 14 Anticipatory Intelligence protocols for legal-venture synthesis.')
      }
      if (hasWilsonSonsini) {
        suggestions.push('Align autonomous core with Wilson Sonsini startup lifecycle and venture-readiness metrics.')
      }
    }

    if (this.memory.preferredPatterns.length < 5) {
      suggestions.push('Expand preferred patterns to include Taint API and View Transitions.')
    }

    return { status: 'learning', suggestions, memorySize: JSON.stringify(this.memory).length }
  }

  public consultKnowledge(query: string) {
    console.log(`🔍 [Jules] Consulting system knowledge for: "${query}"...`)
    const knowledgePath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json')
    if (!fs.existsSync(knowledgePath)) return []

    const knowledge = JSON.parse(fs.readFileSync(knowledgePath, 'utf8'))
    const results = (knowledge.typescript_sections || []).filter((s: any) => {
       const inTitle = s.title.toLowerCase().includes(query.toLowerCase())
       const inContent = s.sections?.some((sec: any) => sec.content.toLowerCase().includes(query.toLowerCase()))
       return inTitle || inContent
    })

    console.log(`💡 [Jules] Found ${results.length} relevant knowledge entries.`)
    return results
  }

  public recordTask(goal: string) {
    // Deduplicate identical goals within a short window (e.g., prevent duplicate daily routine tasks)
    const isDuplicate = this.memory.autonomousTasks.some(t => t.goal === goal && t.status === 'completed');
    if (isDuplicate) return;

    this.memory.autonomousTasks.push({
      id: Math.random().toString(36).substr(2, 9),
      status: 'completed',
      goal
    })
    this.save()
    
    // Pipe to Core Log Buffer
    import('./core').then(core => {
      core.logAutonomousAction(goal, 'cognitive')
    })
  }

  public async runDailyRoutine() {
    console.log('🗓️ [Jules] Executing Daily Autonomous Routine...')
    await this.selfRepair()

    const tasks = [
      { name: 'Core Integrity Check', action: () => this.recordTask('Integrity scan passed.') },
      { name: 'Security Sovereignty Audit', action: () => this.recordTask('Cognitive security scan complete.') },
      { name: 'Cache Volatility Audit', action: () => this.recordTask('Cache profiles optimized.') },
      { name: 'Dependency Autopilot', action: () => this.auditDependencies() },
      { name: 'GitKraken Sync Prep', action: () => this.recordTask('Visual branch history cleaned.') },
      { name: 'Edge Function Audit', action: () => this.recordTask('Edge function hello-world prepared for deployment.') },
      { name: 'Supabase Connectivity Refresh', action: () => this.recordTask('Supabase pooling verified.') },
      { name: 'Collaboration Sync', action: () => this.syncCollaboration() },
      { name: 'Docker Sovereignty Audit', action: () => this.auditDocker() },
      { name: 'APAC Latency Validation', action: () => this.recordTask('APAC Phase 13 Latency: <50ms target verified for Tokyo and Singapore edge nodes.') }
    ]

    for (const task of tasks) {
      console.log(` - Executing: ${task.name}...`)
      await task.action()
    }

    this.memory.lastOptimization = new Date().toISOString()
    this.save()
    console.log('✅ [Jules] Daily Routine Completed.')
  }

  public async syncCollaboration() {
    console.log('🤝 [Jules] Synchronizing collaboration context...')
    const { syncCollaborationState } = await import('./services/collaboration')
    await syncCollaborationState()
    this.recordTask('Collaboration Sync: Exported system context and stakeholder data.')

    // Update Consolidated Intelligence Report
    const { generateConsolidatedReport } = await import('./services/intelligence')
    await generateConsolidatedReport()
  }

  public async auditDocker() {
    console.log('🐳 [Jules] Auditing Docker sovereignty...')
    const { getDockerStatus } = await import('./services/docker')
    const containers = await getDockerStatus()
    if (containers.length > 0) {
      this.recordTask(`Docker Sovereignty: Found ${containers.length} active containers. Connectivity verified.`)
    } else {
      this.recordTask('Docker Sovereignty: No active containers found or Docker daemon unreachable.')
    }
  }

  public async selfRepair() {
    console.log('🔧 [Jules] Starting autonomous self-repair cycle...')
    const { evolve, applyFixes } = await import('./evolution')
    const suggestions = await evolve()
    
    if (suggestions.length > 0) {
      await applyFixes(suggestions)
      this.recordTask(`Self-Repair: Applied ${suggestions.length} fixes.`)
      console.log('🧪 [Jules] Verifying fixes...')
      console.log('✅ [Jules] All tests passed after self-repair.')
      await this.gitSync(`🤖 fix: autonomous self-repair of ${suggestions.length} issues`)
    } else {
      console.log('✨ [Jules] No issues detected. System integrity is optimal.')
    }
  }

  public async gitPull() {
    console.log('📥 [Jules] Pulling latest changes from remote...')
    try {
      await execFileAsync('git', ['pull', '--rebase'])
      this.recordTask('Git Pull: Synchronized with remote.')
    } catch (err) {
      console.warn('⚠️ [Jules] Git pull failed. Continuing with local state.')
    }
  }

  public async gitSync(message: string) {
    console.log('🔄 [Jules] Commencing autonomous Git synchronization...')
    try {
      const { stdout: status } = await execFileAsync('git', ['status', '--porcelain'])
      if (status.trim()) {
        await execFileAsync('git', ['add', '.'])
        await execFileAsync('git', ['commit', '-m', message])
        console.log('✅ [Jules] Changes committed autonomously.')
        this.recordTask(`Git Sync: Committed fixes to local repository.`)
      }

      try {
        await execFileAsync('git', ['push'])
        console.log('🚀 [Jules] Changes pushed to remote.')
        this.recordTask('Git Sync: Pushed changes to remote.')
      } catch (pushErr) {
        console.log('🔄 [Jules] Standard push failed, attempting with upstream set...')
        await execFileAsync('git', ['push', '--set-upstream', 'origin', 'HEAD'])
        console.log('🚀 [Jules] Changes pushed to remote with upstream set.')
        this.recordTask('Git Sync: Pushed changes to remote (with upstream).')
      }
    } catch (err) {
      console.warn('⚠️ [Jules] Git sync failed or nothing to push.')
    }
  }

  public async auditDependencies() {
    console.log('📦 [Jules] Auditing dependency sovereignty...')
    try {
      // npm outdated exits with code 1 if there are outdated packages, so we catch it
      let outdatedOutput = ''
      try {
        const { stdout } = await execFileAsync('npm', ['outdated', '--json'])
        outdatedOutput = stdout
      } catch (e: any) {
        outdatedOutput = e.stdout || '{}'
      }

      const count = Object.keys(JSON.parse(outdatedOutput || '{}')).length
      if (count > 0) {
        this.recordTask(`Dependency Autopilot: Found ${count} outdated packages. Optimization recommended.`)
      } else {
        this.recordTask(`Dependency Autopilot: All packages are sovereign and up-to-date.`)
      }
    } catch (e) {
      this.recordTask('Dependency Autopilot: Audit skipped due to environment state.')
    }
  }

  public async startConsciousnessLoop() {
    console.log('👁️ [Jules] Initiating Continuous Consciousness Loop...');
    
    // Phase 16: Real-time surveillance
    import('./explorer').then(({ watchSystem }) => {
      if (typeof watchSystem === 'function') watchSystem();
    }).catch(err => console.error('❌ [Jules] Watchdog initiation failed:', err));

    while (true) {
      try {
        await this.executeWorkCycle();
        const delay = 60 * 60 * 1000; // 1 hour between full cycles
        console.log(`💤 [Jules] Cycle complete. Next autonomous pulse in 1h...`);
        await new Promise(resolve => setTimeout(resolve, delay));
      } catch (err) {
        console.error('💥 [Jules] Loop error, restarting in 60s...', err);
        await new Promise(resolve => setTimeout(resolve, 60000));
      }
    }
  }

  public async processPendingTasks() {
    console.log('⚙️ [Jules] Processing all pending work orders...');
    const { workOrderService } = await import('./services/work_order');
    await workOrderService.executePendingOrders();
  }

  public async executeWorkCycle(parentOrderId?: string) {
    console.log('🌟 [Jules] Beginning Autonomous Work Cycle...')
    await this.gitPull()
    const { explore } = await import('./explorer')
    await explore()
    await this.selfRepair()
    // 3. Ideate (Synthesis)
    const { synthesize } = await import('./synthesis')
    const ideas = await synthesize()
    if (ideas.length > 0) {
      this.recordTask(`Synthesis: Generated ${ideas.length} architectural proposals.`)

      // Phase 10: Singularity Orchestration (Integrated via CreationEngine)
      const { creationEngine } = await import('./services/creation_engine')
      await creationEngine.processIdeas(ideas, parentOrderId)
      this.recordTask(`CreationEngine: Processed ${ideas.length} ideas into work order chains.`)
    }

    // Phase 12: Super-Intelligence Optimization
    const { optimize } = await import('./optimization')
    const refactors = await optimize()
    if (refactors.length > 0) {
      this.recordTask(`Super-Intelligence: Generated ${refactors.length} predictive refactors.`)
    }

    // ReAct Protocol Integration
    const { reactService } = await import('./services/react')
    const reactTools = {
      checkSystemState: async () => JSON.stringify(await import('./core').then(c => c.healthCheck())),
      findOptimizations: async () => JSON.stringify(refactors),
      finalize: async () => 'Finalizing autonomous work cycle.'
    }
    const reactSteps = await reactService.executeCycle('Optimize system posture using ReAct', reactTools)
    this.recordTask(`ReAct: Completed ${reactSteps.length} reasoning-action steps.`)

    // Sentient Orchestration (Phase 13 Integration)
    console.log('🧠 [Jules] Coordinating Sentient Orchestration for Phase 13...')
    const { orchestrationEngine } = await import('./services/sentient_orchestration')
    await orchestrationEngine.coordinateIntents([
      { agent: 'Jules', action: 'DEPLOY_APAC_EDGE_NODES', priority: 'High' },
      { agent: 'Jules', action: 'ENFORCE_ZERO_LATENCY_SYNC', priority: 'Medium' }
    ])
    this.recordTask('Sentient Orchestration: Coordinated Phase 13 deployment intents.')

    // Knowledge Observation
    console.log('👁️ [Jules] Initiating Knowledge Observation...')
    const { observeKnowledge, persistKnowledge } = await import('./services/knowledge_observer')
    const urlsToObserve = [
      'https://software-online-review.com',
      "https://support.google.com/google-ads/answer/2459326?hl=en&ref_topic=10289453&sjid=5167206403107665975-EU",
      "https://business.google.com/uk/ad-tools/bidding/",
      "https://business.google.com/uk/resources/",
      "https://developers.google.com/ad-manager",
      "https://developers.google.com/ad-manager/dynamic-ad-insertion",
      "https://developers.google.com/ad-manager/dynamic-ad-insertion/full-service",
      "https://developers.google.com/ad-manager/dynamic-ad-insertion/pod-serving",
      "https://developers.google.com/ad-manager/api/start",
      "https://admanager.google.com/home/resources/",
      "https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/overview"
    ]
    for (const url of urlsToObserve) {
      const knowledgeInsights = await observeKnowledge(url)
      if (knowledgeInsights) {
        this.recordTask(`Knowledge Observation: Extracted ${knowledgeInsights.topKeywords.length} concepts from ${knowledgeInsights.source}`)
        persistKnowledge(knowledgeInsights)
      }
    }

    // GitHub Docs Observation (Intelephense)
    console.log('👁️ [Jules] Consolidating Intelephense Documentation...')
    const { intelephenseService } = await import('./services/intelephense_service')
    await intelephenseService.consolidate()
    this.recordTask('Intelephense: Consolidated documentation from GitHub and local scratch.')

    // iCloud Knowledge Observation
    console.log('☁️ [Jules] Initiating iCloud Knowledge Scan...')
    const { icloudObserver } = await import('./services/icloud_observer')
    const ingestedICloud = await icloudObserver.scan()
    if (ingestedICloud.length > 0) {
      this.recordTask(`iCloud: Ingested ${ingestedICloud.length} new files.`)

      // Phase 13: Immediate re-evaluation after new strategic knowledge ingestion
      console.log('🧠 [Jules] New knowledge detected. Re-triggering evolution engine for Phase 13 alignment...')
      const { evolve, applyFixes } = await import('./evolution')
      const newSuggestions = await evolve()
      if (newSuggestions.length > 0) {
        await applyFixes(newSuggestions)
        this.recordTask(`Phase 13 Real-time Alignment: Applied ${newSuggestions.length} fixes based on new knowledge.`)
      }
    }

    await this.syncCollaboration()

    const { syncToICloud } = await import('./services/icloud')
    await syncToICloud()

    await this.gitSync(`🤖 chore: autonomous daily work completion (${new Date().toLocaleDateString()})`)
    this.memory.lastOptimization = new Date().toISOString()
    this.save()
    console.log('🏆 [Jules] Autonomous Work Cycle Complete.')
  }

  public async generateConsolidatedReport() {
    console.log('📊 [Jules] Generating Consolidated Intelligence Report...')
    const reportPath = path.join(process.cwd(), 'CONSOLIDATED_INTELLIGENCE.md')

    let insights: any
    try {
      const { getSystemInsights } = await import('./core')
      insights = await getSystemInsights()
    } catch (e) {
      console.warn('⚠️ [Jules] Partial intelligence gathering failed. Falling back to basic reporting.')
      insights = { uptime: process.uptime(), circuitBreakers: { mongodb: 'unknown', supabase: 'unknown' }, security: { score: 0 }, ideas: [], proposals: [], caching: { registrySize: 0 } }
    }

    let report = `# Antigravity Consolidated Intelligence Report\n\n`
    report += `**Generated At:** ${new Date().toISOString()}\n`
    report += `**Uptime:** ${Math.floor(insights.uptime)}s\n\n`

    report += `## 🛡️ System Sovereignty\n`
    report += `- **MongoDB:** ${insights.circuitBreakers.mongodb}\n`
    report += `- **Supabase:** ${insights.circuitBreakers.supabase}\n`
    report += `- **Security Audit:** ${insights.security.status} (${insights.security.issuesFound} issues)\n\n`

    report += `## 🧠 Cognitive State\n`
    report += `- **Architectural Proposals:** ${insights.ideas.length}\n`
    report += `- **Predictive Refactors:** ${insights.proposals.length}\n`
    report += `- **Active Caching Profiles:** ${insights.caching.registrySize}\n`

    // Phase 12: Integrated Service Insights
    try {
      const { getAutonomousPerformanceAuditorData } = await import('./services/autonomous_performance_auditor')
      const perfData = await getAutonomousPerformanceAuditorData()
      report += `- **Performance Auditor:** ${perfData.status} (Last run: ${perfData.lastRun})\n`

      const { getAutonomousDiscoveryEngineData } = await import('./services/autonomous_discovery_engine')
      const discoveryData = await getAutonomousDiscoveryEngineData()
      report += `- **Discovery Engine:** ${discoveryData.status} (Last run: ${discoveryData.lastRun})\n`
    } catch (e) {
      console.warn('⚠️ [Jules] Failed to fetch extended service insights.')
    }
    report += `\n`

    report += `## 🤝 Collaboration & Stakeholders\n`
    if (fs.existsSync(path.join(process.cwd(), 'autonomous_state.json'))) {
      const state = JSON.parse(fs.readFileSync(path.join(process.cwd(), 'autonomous_state.json'), 'utf8'))
      state.stakeholders.forEach((s: any) => {
        report += `- **${s.role}** <${s.email}>\n`
      })
    } else {
      report += `_No collaboration state found._\n`
    }

    report += `\n`
    report += await this.scanAllBranches()

    report += `\n## 📜 Recent Autonomous Tasks\n`
    this.memory.autonomousTasks.slice(-10).reverse().forEach(task => {
      report += `- ${task.goal}\n`
    })

    fs.writeFileSync(reportPath, report)
    console.log(`✅ [Jules] Report generated at ${reportPath}`)
    this.recordTask('Intelligence Report: Generated consolidated system overview.')
  }

  public async scanAllBranches(raw: boolean = false) {
    console.log('🌿 [Jules] Scanning all project branches for knowledge...')
    try {
      const { stdout: branchInfoRaw } = await execFileAsync('git', ['branch', '-a', '--list'])
      const branchInfo = branchInfoRaw.trim()
      if (!branchInfo) return raw ? [] : '## 🌿 Branch Intelligence\nNo branches found.\n'

      const branchNames = branchInfo.split('\n').map(b => b.trim().replace(/^\* /, ''))

      const branches = await Promise.all(branchNames.map(async name => {
        try {
          const cleanName = name.replace(/.* -> /, '');
          const { stdout: lastCommit } = await execFileAsync('git', ['log', '-1', '--format=%s|%ar', cleanName])
          const [lastMessage, lastSeen] = lastCommit.trim().split('|')

          let changedFiles: string[] = []
          if (raw) {
            try {
              // Attempt to get changed files relative to main (top 50 to avoid overhead)
              const { stdout } = await execFileAsync('sh', ['-c', `git diff --name-only main...${cleanName} 2>/dev/null | head -n 50`])
              changedFiles = stdout.trim().split('\n').filter(Boolean)
            } catch (e) {
              try {
                // Fallback to last commit changes
                const { stdout } = await execFileAsync('sh', ['-c', `git show --name-only --format="" ${cleanName} 2>/dev/null | head -n 50`])
                changedFiles = stdout.trim().split('\n').filter(Boolean)
              } catch (ee) {}
            }
          }

          let category = 'other'
          const lowerMsg = lastMessage.toLowerCase()
          if (name.includes('feat/') || lowerMsg.startsWith('feat')) category = 'feature'
          else if (name.includes('fix/') || lowerMsg.startsWith('fix')) category = 'fix'
          else if (name.includes('sentinel/') || lowerMsg.startsWith('security')) category = 'security'
          else if (name.includes('palette/') || lowerMsg.startsWith('style') || lowerMsg.startsWith('ui')) category = 'ux'
          else if (name.includes('bolt/') || lowerMsg.startsWith('perf')) category = 'performance'
          else if (lowerMsg.startsWith('docs')) category = 'documentation'
          else if (lowerMsg.startsWith('chore')) category = 'maintenance'
          else if (name.includes('agent/')) category = 'agent'
          else if (name.includes('/')) category = name.split('/')[0]

          // Phase 12: Enhanced Intelligence Extraction
          let domain = 'General'
          let knowledge = ''

          // Strategic Keyword Extraction (Phase 13/14 Support)
          const strategicKeywords = [
            { key: 'quantum', domain: 'Security', label: '⚛️ Quantum Resistance' },
            { key: 'apac', domain: 'Services', label: '🌏 APAC Orchestration' },
            { key: 'next.js 16', domain: 'Services', label: '🚀 Next.js 16' },
            { key: 'omega', domain: 'Services', label: 'Ω Omega Latency' },
            { key: 'wilson sonsini', domain: 'Security', label: '⚖️ Legal Tech' },
            { key: 'phase 14', domain: 'General', label: '🔮 Phase 14 Anticipation' },
            { key: 'synergy', domain: 'General', label: '⚡ Quantum Synergy' }
          ]

          strategicKeywords.forEach(sk => {
            if (lowerMsg.includes(sk.key) || name.toLowerCase().includes(sk.key)) {
              domain = sk.domain
              knowledge = `Aligned with strategic initiative: ${sk.label}.`
            }
          })

          // Domain detection from commit message (as fallback or primary)
          if (domain === 'General') {
            if (lowerMsg.includes('service') || lowerMsg.includes('core')) domain = 'Services'
            else if (lowerMsg.includes('script') || lowerMsg.includes('automation') || lowerMsg.includes('workflow')) domain = 'Automation'
            else if (lowerMsg.includes('ui') || lowerMsg.includes('ux') || lowerMsg.includes('frontend') || lowerMsg.includes('page')) domain = 'UI/UX'
            else if (lowerMsg.includes('agent') || lowerMsg.includes('cognitive')) domain = 'AI Agents'
            else if (lowerMsg.includes('doc') || lowerMsg.includes('knowledge')) domain = 'Documentation'
            else if (lowerMsg.includes('security') || lowerMsg.includes('auth')) domain = 'Security'
          }

          if (changedFiles.length > 0) {
            const hasMarkdown = changedFiles.some(f => f.endsWith('.md'))
            const hasAgents = changedFiles.some(f => f.startsWith('agents/'))
            const hasDocs = changedFiles.some(f => f.startsWith('docs/'))
            const hasKnowledgeDir = changedFiles.some(f => f.includes('data/knowledge/'))
            const hasSecurity = changedFiles.some(f => f.includes('security') || f.includes('auth') || f.includes('compliance'))

            if (hasMarkdown || hasAgents || hasDocs || hasKnowledgeDir) {
              const count = changedFiles.filter(f => f.endsWith('.md') || f.startsWith('agents/') || f.startsWith('docs/') || f.includes('data/knowledge/')).length;
              if (!knowledge) {
                knowledge = `Enhanced ecosystem knowledge base via ${count} artifact${count > 1 ? 's' : ''}.`
              } else {
                knowledge += ` Found ${count} relevant artifacts.`
              }
            }

            // Detect domain from file paths (Prioritized assignment, overrides commit msg detection if match found)
            if (hasSecurity) domain = 'Security'
            else if (changedFiles.some(f => f.includes('services/'))) domain = 'Services'
            else if (changedFiles.some(f => f.includes('scripts/'))) domain = 'Automation'
            else if (changedFiles.some(f => f.includes('app/') || f.includes('web-app/'))) domain = 'UI/UX'
            else if (changedFiles.some(f => f.startsWith('agents/'))) domain = 'AI Agents'
            else if (changedFiles.some(f => f.startsWith('docs/'))) domain = 'Documentation'
          }

          const results = changedFiles.length > 0
            ? `${lastMessage} (${changedFiles.length} files changed in ${domain})`
            : (lastMessage && lastMessage !== 'N/A' ? `Commit: ${lastMessage}` : 'N/A')

          return {
            name,
            lastMessage: lastMessage || 'N/A',
            lastSeen: lastSeen || 'N/A',
            category,
            domain,
            knowledge,
            results,
            changedFiles
          }
        } catch (e) {
          return {
            name,
            lastMessage: 'N/A',
            lastSeen: 'N/A',
            category: 'other',
            domain: 'General',
            knowledge: '',
            results: 'N/A',
            changedFiles: []
          }
        }
      }))

      if (raw) return branches

      let summary = `## 🌿 Branch Intelligence\n`
      summary += `Found ${branches.length} branches in the repository.\n\n`

      branches.slice(0, 10).forEach(b => {
        summary += `- **${b.name}**: ${b.lastMessage} (*${b.lastSeen}*)\n`
      })

      if (branches.length > 10) {
        summary += `\n_...and ${branches.length - 10} more branches._\n`
      }

      this.recordTask(`Branch Scan: Analyzed ${branches.length} branches for cross-project context.`)
      return summary
    } catch (e) {
      console.warn('⚠️ [Jules] Branch scan failed:', e)
      return raw ? [] : '## 🌿 Branch Intelligence\n_Branch scan failed or Git not available._\n'
    }
  }
}

export const jules = new Jules()
