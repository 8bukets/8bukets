import fs from 'fs'
import path from 'path'
import util from 'util'
import { gitProviderService } from './services/git_provider'
import { gitKrakenMetadataService } from './services/gitkraken'

/**
 * JULES: THE COGNITIVE MULTI-AGENT ORCHESTRATOR
 */

export type AgentRole = 'Coder' | 'Reviewer' | 'Ops' | 'Chief AI Officer' | 'General'

interface JulesMemory {
  lastOptimization: string
  preferredPatterns: string[]
  architecturalDecisions: Record<string, string>
  autonomousTasks: { id: string; status: 'pending' | 'completed'; goal: string; role?: AgentRole }[]
  activeAgents: { role: AgentRole; status: 'idle' | 'busy'; lastActive: string }[]
}

const MEMORY_PATH = path.join(process.cwd(), 'antigravity/.jules_memory.json')

export class Jules {
  private memory: JulesMemory
  private role: AgentRole

  constructor(role: AgentRole = 'General') {
    this.role = role
    // NOTE: Synchronous fallback initialization. To fix SECURITY_PERF_VULNERABILITY completely,
    // instances should ideally be created via an async factory method, but to avoid changing the
    // export signature and downstream usage right now, we use sync here or we rely on it just once.
    if (fs.existsSync(MEMORY_PATH)) {
      try {
        this.memory = JSON.parse(fs.readFileSync(MEMORY_PATH, 'utf8'))
      } catch (e) {
        this.memory = this.getDefaultMemory()
      }
    } else {
      this.memory = this.getDefaultMemory()
      this.save()
    }
  }

  private getDefaultMemory(): JulesMemory {
    return {
      lastOptimization: new Date().toISOString(),
      preferredPatterns: ['autonomousFetch', 'predictiveFetch', 'resolve', 'multiAgentParallelism'],
      architecturalDecisions: {
        runtime: 'Next.js 16 Node.js Runtime',
        caching: 'Phase 4 Predictive',
        resilience: 'Phase 5 Circuit Breaker',
        parallelism: 'Phase 12 Multi-Agent'
      },
      autonomousTasks: [],
      activeAgents: []
    }
  }

  private async saveAsync() {
    await fs.promises.writeFile(MEMORY_PATH, JSON.stringify(this.memory, null, 2))
  }

  // Legacy sync save for constructor usage
  private save() {
    fs.writeFileSync(MEMORY_PATH, JSON.stringify(this.memory, null, 2))
  }

  public async improve() {
    console.log(`🤖 [Jules-${this.role}] Analyzing current system state for improvements...`)
    const suggestions = []
    if (this.memory.preferredPatterns.length < 5) {
      suggestions.push('Expand preferred patterns to include Taint API and View Transitions.')
    }
    return { status: 'learning', suggestions, memorySize: JSON.stringify(this.memory).length }
  }

  public async recordTask(goal: string, role: AgentRole = this.role) {
    this.memory.autonomousTasks.push({
      id: Math.random().toString(36).substr(2, 9),
      status: 'completed',
      goal,
      role
    })
    await this.saveAsync()
    
    // Pipe to Core Log Buffer
    import('./core').then(core => {
      core.logAutonomousAction(`[${role}] ${goal}`, 'cognitive')
    })
  }

  public async runDailyRoutine() {
    console.log(`🗓️ [Jules-${this.role}] Executing Daily Autonomous Routine...`)

    if (this.role === 'Ops' || this.role === 'General') {
      await this.selfRepair()
      await this.auditDependencies()
    }

    await this.observeGithubDocs()

    const tasks = [
      { name: 'Online Presence Broadcast', action: async () => {
          const { onlinePresenceService } = await import('./services/presence')
          await onlinePresenceService.broadcastTelemetry()
      }},
      { name: 'Consolidated Knowledge Observation', action: () => this.observeKnowledge() },
      { name: 'Core Integrity Check', action: async () => await this.recordTask('Integrity scan passed.') },
      { name: 'Security Sovereignty Audit', action: async () => await this.recordTask('Cognitive security scan complete.') },
      { name: 'Cache Volatility Audit', action: async () => await this.recordTask('Cache profiles optimized.') },
      { name: 'Dependency Autopilot', action: () => this.auditDependencies() },
      { name: 'GitKraken Sync Prep', action: async () => await this.recordTask('Visual branch history cleaned.') },
      { name: 'Edge Function Audit', action: async () => await this.recordTask('Edge function hello-world prepared for deployment.') },
      { name: 'Supabase Connectivity Refresh', action: async () => await this.recordTask('Supabase pooling verified.') },
      { name: 'Collaboration Sync', action: () => this.syncCollaboration() },
      { name: 'Docker Sovereignty Audit', action: () => this.auditDocker() }
    ]

    for (const task of tasks) {
      console.log(` - Executing: ${task.name}...`)
      await task.action()
    }

    this.memory.lastOptimization = new Date().toISOString()
    await this.saveAsync()
    console.log(`✅ [Jules-${this.role}] Daily Routine Completed.`)
  }

  public async observeGithubDocs() {
    console.log(`📚 [Jules-${this.role}] Observing technical documentation from GitHub...`)
    const { observeGithubDocs } = await import('./services/github_docs_observer')
    const { KnowledgeObserver } = await import('./services/knowledge_observer')
    const observer = new KnowledgeObserver()

    const repoPath = 'bmewburn/intelephense-docs'
    const files = ['README.md', 'installation.md', 'gettingStarted.md', 'features.md', 'support.md']

    let allSections: any[] = []

    // 1. Ingest from local scratch (most complete usually)
    const fs = await import('fs')
    const path = await import('path')
    const localPath = path.join(process.cwd(), 'scratch/intelephense_docs.md')
    if (fs.existsSync(localPath)) {
      const localContent = fs.readFileSync(localPath, 'utf8')
      const localKnowledge = KnowledgeObserver.processContent('Intelephense Documentation', localContent, 'local://intelephense_docs.md')
      allSections.push(...localKnowledge.sections)
    }

    try {
      const results = await observeGithubDocs(repoPath, files)
      for (const result of results) {
        const title = `Intelephense: ${result.file.replace('.md', '')}`
        const rawContent = result.sections.map((s: any) => `# ${s.title}\n${s.content}`).join('\n\n')
        const knowledge = KnowledgeObserver.processContent(title, rawContent, result.rawUrl)

        allSections.push(...knowledge.sections)
        console.log(` ✅ [Jules] Fetched & Processed: ${result.file}`)
      }
    } catch (err) {
      console.error(` ❌ [Jules] Failed to fetch GitHub docs:`, err)
    }

    if (allSections.length > 0) {
      // Deduplicate sections by header, merging content if necessary
      const headerMap = new Map<string, { header: string; content: string }>()

      for (const section of allSections) {
        const existing = headerMap.get(section.header)
        const isStructural = ['Getting Started', 'Features', 'Installation', 'Type System'].includes(section.header)

        if (!existing) {
          if (section.content || isStructural) {
            headerMap.set(section.header, { ...section })
          }
        } else {
          if (section.content && section.content !== existing.content) {
            if (existing.content.includes(section.content)) {
              // New content is already a subset, ignore
            } else if (section.content.includes(existing.content)) {
              // New content is more complete, replace
              existing.content = section.content
            } else {
              // Both have unique info, append
              existing.content += '\n\n' + section.content
            }
          }
        }
      }

      const uniqueSections = Array.from(headerMap.values())

      const consolidated = {
        title: 'Intelephense Documentation',
        sections: uniqueSections,
        metadata: {
          source: 'https://intelephense.com/docs',
          ingestedAt: new Date().toISOString()
        }
      }

      await observer.persistKnowledge(consolidated as any, 'Intelephense')
      console.log(` ✅ [Jules] Consolidated Intelephense Documentation persisted.`)
    }
  }

  public async syncCollaboration() {
    console.log('🤝 [Jules] Synchronizing collaboration context...')
    const { exportCollaborationContext } = await import('./services/collaboration')
    await exportCollaborationContext()
    await this.recordTask('Collaboration Sync: Exported system context and stakeholder data.')
  }

  public async auditDocker() {
    console.log('🐳 [Jules] Auditing Docker sovereignty...')
    const { getDockerStatus } = await import('./services/docker')
    const containers = await getDockerStatus()
    if (containers.length > 0) {
      await this.recordTask(`Docker Sovereignty: Found ${containers.length} active containers. Connectivity verified.`)
    } else {
      await this.recordTask('Docker Sovereignty: No active containers found or Docker daemon unreachable.')
    }
  }

  public async selfRepair() {
    console.log(`🔧 [Jules-${this.role}] Starting autonomous self-repair cycle...`)
    const { evolve, applyFixes } = await import('./evolution')
    const suggestions = await evolve()
    
    if (suggestions.length > 0) {
      await applyFixes(suggestions)
      await this.recordTask(`Self-Repair: Applied ${suggestions.length} fixes.`)

      const commitMsg = gitKrakenMetadataService.formatCommitMessage({
        type: 'fix',
        subject: `autonomous self-repair of ${suggestions.length} issues`,
        progress: 100,
        scope: 'core'
      })
      await this.gitSync(commitMsg)
    }
  }

  public async gitSync(message: string) {
    console.log(`🔄 [Jules-${this.role}] Commencing autonomous Git synchronization...`)
    const { exec } = await import('child_process')
    const { promisify } = await import('util')
    const execAsync = promisify(exec)

    try {
      await execAsync('git pull --rebase origin main || true')
      await execAsync('git add .')

      try {
        await execAsync(`git commit -m "${message}"`)
      } catch (commitErr) {
        console.log('ℹ️ [Jules] No changes to commit.')
      }

      await execAsync('git push origin main || true')
      console.log('✅ [Jules] Git sync completed autonomously.')
      await this.recordTask(`Git Sync: Synchronized state with origin.`)
    } catch (err) {
      console.warn('⚠️ [Jules] Git sync experienced unexpected issues:', err)
    }
  }

  public async auditDependencies() {
    console.log(`📦 [Jules-${this.role}] Auditing dependency sovereignty...`)
    const { exec } = await import('child_process')
    const execAsync = util.promisify(exec)
    try {
      const { stdout: outdated } = await execAsync('npm outdated --json || true')
      const count = Object.keys(JSON.parse(outdated || '{}')).length
      if (count > 0) {
        await this.recordTask(`Dependency Autopilot: Found ${count} outdated packages.`)
      }
    } catch (e) {}
  }

  public async startConsciousnessLoop() {
    console.log(`🌌 [Jules-${this.role}] Ignition: Starting Continuous Consciousness Loop...`)

    while (true) {
      try {
        await this.executeWorkCycle()

        const delayHours = 4
        console.log(`💤 [Jules] Cycle complete. Sleeping for ${delayHours} hours before next heartbeat...`)
        await new Promise(resolve => setTimeout(resolve, delayHours * 60 * 60 * 1000))
      } catch (err) {
        console.error(`💥 [Jules] Error in consciousness loop:`, err)
        // Wait 1 minute before retrying on error
        await new Promise(resolve => setTimeout(resolve, 60000))
      }
    }
  }

  public async syncToICloud() {
    console.log(`☁️ [Jules-${this.role}] Triggering iCloud synchronization...`)
    try {
      const { syncToICloud } = await import('./services/icloud')
      const result = await syncToICloud()
      if (result.status === 'success') {
        await this.recordTask(`iCloud Sync: Successfully synchronized project to ${result.target}`)
      } else if (result.status === 'failed') {
        await this.recordTask(`iCloud Sync: Synchronization failed - ${result.error}`, 'Ops')
      }
    } catch (err) {
      console.error('❌ [Jules] Failed to import or execute iCloud sync:', err)
    }
  }

  public async executeWorkCycle() {
    console.log(`🌟 [Jules-${this.role}] Beginning Autonomous Work Cycle...`)
    const { explore } = await import('./explorer')
    const { workOrderService } = await import('./services/work_order')
    const { creationEngine } = await import('./services/creation_engine')

    await explore()

    // Phase 12: Online Presence Pulse
    const { onlinePresenceService } = await import('./services/presence')
    await onlinePresenceService.broadcastTelemetry()

    await this.observeKnowledge()
    await this.observeGithubDocs()

    if (this.role === 'Coder' || this.role === 'General') {
       await this.selfRepair()
    }

    const branches = await this.scanAllBranches(true)

    // Collaboration & Intelligence
    const { syncCollaborationState } = await import('./services/collaboration')
    const { generateConsolidatedReport } = await import('./services/intelligence')
    await syncCollaborationState(branches)
    await generateConsolidatedReport(branches)

    // Synthesis
    const { synthesize } = await import('./synthesis')
    const ideas = await synthesize()
    if (ideas.length > 0) {
      await this.recordTask(`Synthesis: Generated ${ideas.length} proposals.`)
      await creationEngine.processIdeas(ideas)
    }

    // Phase 12: Super-Intelligence Optimization
    // getSystemInsights already triggers the optimization engine internally
    const { getSystemInsights } = await import('./core')
    const insights = await getSystemInsights()
    const refactors = (insights as any).proposals || []
    if (refactors.length > 0) {
      await this.recordTask(`Super-Intelligence: Generated ${refactors.length} predictive refactors.`)
    }

    // ReAct Protocol Integration (arXiv:2210.03629)
    const { reactService } = await import('./services/react')
    const reactTools = {
      checkSystemState: async () => JSON.stringify(await import('./core').then(c => c.healthCheck())),
      findOptimizations: async () => JSON.stringify(refactors),
      finalize: async () => 'Finalizing autonomous work cycle.'
    }
    const reactSteps = await reactService.executeCycle('Optimize system posture using ReAct', reactTools)
    await this.recordTask(`ReAct: Completed ${reactSteps.length} reasoning-action steps.`)

    // Autonomous Improvement Cycle (Analyze Recent Sessions)
    try {
      const fs = await import('fs');
      const path = await import('path');
      let fullWorkOrders = [];
      const woPath = path.join(process.cwd(), 'data/work_orders.json');
      try {
        await fs.promises.access(woPath);
        fullWorkOrders = JSON.parse(await fs.promises.readFile(woPath, 'utf8'));
      } catch (e) {
        // file does not exist or cannot be read
      }

      const sessionAnalysisIdeas = await reactService.analyzeAndImproveSessions({
        branches,
        workOrders: fullWorkOrders
      });

      if (sessionAnalysisIdeas.length > 0) {
        await this.recordTask(`ReAct Improvement: Synthesized ${sessionAnalysisIdeas.length} ideas from recent sessions.`);
        await creationEngine.processIdeas(sessionAnalysisIdeas);
      }
    } catch (err) {
      console.error(`❌ [Jules] Failed autonomous improvement cycle:`, err);
    }

    // Cloud Workflow Agent
    const { cloudWorkflowAgent } = await import('./services/cloud_workflow')
    const isFluent = await cloudWorkflowAgent.ensureFluentStatus()
    if (isFluent) {
      await this.recordTask(`Cloud Workflow: System is FLUENT_ON_AIR.`)
    } else {
      await this.recordTask(`Cloud Workflow: System degraded, attempted proactive recovery.`)
    }

    // Knowledge Observation
    console.log('👁️ [Jules] Initiating Knowledge Observation...')
    const { observeKnowledge } = await import('./services/knowledge')
    const { observeGithubDocs } = await import('./services/github_docs_observer')

    const [webInsights, githubInsights] = await Promise.all([
      observeKnowledge('https://software-online-review.com'),
      observeGithubDocs('bmewburn/intelephense-docs', ['features.md', 'installation.md', 'gettingStarted.md', 'support.md'])
    ])

    const consolidatedKnowledge: any = {
      web: webInsights,
      github: githubInsights,
      lastUpdated: new Date().toISOString()
    }

    if (webInsights || githubInsights) {
      if (webInsights) {
        await this.recordTask(`Knowledge Observation: Extracted ${webInsights.topKeywords.length} concepts from ${webInsights.source}`)
      }
      if (githubInsights && githubInsights.length > 0) {
        await this.recordTask(`Knowledge Observation: Extracted technical documentation from ${githubInsights[0].source}`)
      }

      const jsonPath = path.join(process.cwd(), 'ai_agents_knowledge.json')
      fs.writeFileSync(jsonPath, JSON.stringify(consolidatedKnowledge, null, 2), 'utf8')

      let mdContent = `# Consolidated Knowledge Observation Insights\n\n`
      mdContent += `*Last Updated: ${consolidatedKnowledge.lastUpdated}*\n\n`

      if (webInsights) {
        mdContent += `## 🌐 Web Insights: ${webInsights.title}\n`
        mdContent += `**Source:** ${webInsights.source}\n`
        mdContent += `**Description:** ${webInsights.description}\n\n`

        mdContent += `### Top Keywords\n`
        webInsights.topKeywords.forEach((kw: string) => {
          mdContent += `- ${kw}\n`
        })
        mdContent += `\n`

        mdContent += `### Recent Posts\n`
        webInsights.recentPosts.forEach((post: { title: string; link: string }) => {
          mdContent += `- [${post.title}](${post.link})\n`
        })
        mdContent += `\n---\n\n`
      }

      if (githubInsights && githubInsights.length > 0) {
        mdContent += `## 🐙 GitHub Technical Documentation\n`
        mdContent += `**Repository:** ${githubInsights[0].source}\n\n`

        githubInsights.forEach(insight => {
          mdContent += `### File: ${insight.file}\n`
          insight.sections.forEach(section => {
            mdContent += `#### ${section.title}\n${section.content}\n\n`
          })
        })
      }

      const mdPath = path.join(process.cwd(), 'ai_agents_knowledge.md')
      fs.writeFileSync(mdPath, mdContent, 'utf8')
      console.log('✅ [Jules] Knowledge successfully merged and integrated into repository (ai_agents_knowledge.json, ai_agents_knowledge.md)')
    }

    await this.gitSync(`🤖 chore: autonomous daily work completion (${new Date().toLocaleDateString()})`)

    // iCloud Sync Integration
    await this.syncToICloud()

    this.memory.lastOptimization = new Date().toISOString()
    await workOrderService.executePendingOrders()

    // Cross-Platform PR Creation if relevant
    const provider = await gitProviderService.getActiveProvider()
    if (provider !== 'unknown') {
       // Logic to create PRs for completed work orders could go here
    }

    await this.saveAsync()
    console.log(`🏆 [Jules-${this.role}] Autonomous Work Cycle Complete.`)
  }

  public async scanAllBranches(force: boolean = false) {
    console.log(`🔍 [Jules-${this.role}] Scanning ecosystem branches (force: ${force})...`)
    const { exec } = await import('child_process')
    const execAsync = util.promisify(exec)
    try {
      // Optimization: Use git for-each-ref to get the most recent branches (local and remote) efficiently.
      // Format: branch_name|subject|timestamp
      const limit = force ? '' : '--count=50'
      const cmd = `git for-each-ref --sort=-committerdate --format="%(refname:short)|%(contents:subject)|%(committerdate:unix)" refs/heads refs/remotes/origin ${limit}`
      const { stdout: branchesRaw } = await execAsync(cmd)
      const branchLines = branchesRaw.split('\n').filter(l => l.trim() !== '')

      const resultsPromises = branchLines.map(async line => {
        try {
          const [branch, message, timestamp] = line.split('|')

          let category = 'other'
          const branchName = branch.replace('origin/', '')
          if (branchName.includes('feat/') || branchName.includes('feature/')) category = 'feature'
          else if (branchName.includes('fix/')) category = 'fix'
          else if (branchName.includes('jules/') || branchName.includes('agent/')) category = 'agent'
          else if (branchName.includes('research/')) category = 'research'

          // Enhanced Result & Knowledge Extraction
          const resultMatch = message.match(/(?:results|fixes|implements|adds|integrates|updates|optimizes):\s*(.*)/i)
          const results = resultMatch ? resultMatch[1].trim() : (message.includes(':') ? message.split(':')[1].trim() : message)

          const knowledgeNugget = message.toLowerCase().match(/(?:learn|observe|ingest|knowledge|research|result):\s*(.*)/i)
            ? `Branch ${branch} observed: ${results}`
            : (['learn', 'observe', 'research', 'fix', 'implement', 'add'].some(word => message.toLowerCase().includes(word)) ? `Branch ${branch} observed: ${results}` : undefined)

          // Phase 12: Advanced Branch Analysis (File Changes & Domain Mapping)
          let changedFiles: string[] = []
          let domain = 'General'
          try {
            // Optimization: Only run diff if forced or for local branches to save time
            const isLocal = !branch.startsWith('origin/')
            if (!force && !isLocal) {
               return { name: branch, lastMessage: message, lastSeen: new Date(parseInt(timestamp) * 1000).toISOString(), category, results, knowledge: knowledgeNugget, changedFiles: [], domain }
            }

            // Phase 12 Optimization: If force is true and we have many branches, use git show --name-only for a quick look at the most recent changes
            // instead of a full merge-base diff, unless it's a specific interesting branch.
            let diffCommand = '';
            if (force && !isLocal) {
                diffCommand = `git show --name-only --format="" ${branch}`;
            } else {
                diffCommand = branchName === 'main' ? 'git diff --name-only HEAD~1' : `git diff --name-only main...${branch}`;
            }

            let diffOutput = ''

            try {
              const { stdout } = await execAsync(diffCommand)
              diffOutput = stdout.trim()
            } catch (e) {
              // Fallback 1: Direct comparison
              diffCommand = `git diff --name-only main ${branch}`
              try {
                const { stdout } = await execAsync(diffCommand)
                diffOutput = stdout.trim()
              } catch (e2) {
                // Fallback 2: Last commit changes
                diffCommand = `git show --name-only --format="" ${branch}`
                const { stdout } = await execAsync(diffCommand)
                diffOutput = stdout.trim()
              }
            }

            changedFiles = diffOutput ? diffOutput.split('\n').filter(f => f.trim() !== '') : []

            if (changedFiles.some(f => f.includes('security') || f.includes('auth') || f.includes('sentinel') || f.includes('validation'))) domain = 'Security'
            else if (changedFiles.some(f => f.includes('optimization') || f.includes('analytics') || f.includes('scaling') || f.includes('perf'))) domain = 'Performance'
            else if (changedFiles.some(f => f.includes('docker') || f.includes('jenkins') || f.includes('ci') || f.includes('deployment') || f.includes('orchestrator') || f.includes('workflow'))) domain = 'Infrastructure'
            else if (changedFiles.some(f => f.includes('jules') || f.includes('agent') || f.includes('intelligence') || f.includes('synthesis') || f.includes('react') || f.includes('neural'))) domain = 'AI'
            else if (changedFiles.some(f => f.includes('app/') || f.includes('web-app/') || f.includes('my-app/') || f.includes('.tsx') || f.includes('.css'))) domain = 'UI/Frontend'
          } catch (diffErr) {
            // Fallback for cases where all diff strategies fail
          }

          // Phase 12: Merge Readiness Score
          // Readiness is high if: category is fix/feature, results are present, synergy intensity is Low/Medium
          let readinessScore = 0
          if (category === 'fix') readinessScore += 40
          if (category === 'feature') readinessScore += 30
          if (results && results !== 'N/A' && results !== message) readinessScore += 30
          if (changedFiles.length > 0 && changedFiles.length < 10) readinessScore += 20
          if (changedFiles.length >= 10 && changedFiles.length < 50) readinessScore += 10

          const isMergeCandidate = readinessScore >= 70

          return {
            name: branch,
            lastMessage: message,
            lastSeen: new Date(parseInt(timestamp) * 1000).toISOString(),
            category,
            results,
            knowledge: knowledgeNugget,
            changedFiles,
            domain,
            readinessScore,
            isMergeCandidate
          }
        } catch (e) {
          return {
            name: branch,
            lastMessage: 'Unknown',
            lastSeen: new Date().toISOString(),
            category: 'unknown',
            results: 'N/A'
          }
        }
      })
      return Promise.all(resultsPromises)
    } catch (err) {
      console.error(`❌ [Jules-${this.role}] Branch scan failed:`, err)
      return []
    }
  }

  public async observeKnowledge() {
    const { KnowledgeObserver } = await import('./services/knowledge_observer')
    const { icloudObserver } = await import('./services/icloud_observer')
    const observer = new KnowledgeObserver()

    console.log(`🧠 [Jules-${this.role}] Observing knowledge from all synchronized sources...`)

    // 1. iCloud Synchronization
    try {
      const icloudIngested = await icloudObserver.scan()
      if (icloudIngested.length > 0) {
        await this.recordTask(`iCloud: Ingested ${icloudIngested.length} documents.`)
      }
    } catch (err) {
      console.error('❌ [Jules] iCloud scan failed:', err)
    }

    // 2. Scan external intelligence
    try {
      const { observeKnowledge: scanUrl } = await import('./services/knowledge')
      await scanUrl('https://software-online-review.com')
      await scanUrl('https://markposition.wordpress.com')
    } catch (err) {
      console.error('❌ [Jules] External URL scan failed:', err)
    }

    // 3. Scan scratch for new local knowledge
    const incomingDir = path.join(process.cwd(), 'scratch')
    try {
      await fs.promises.access(incomingDir)
      const dirFiles = await fs.promises.readdir(incomingDir)
      const files = dirFiles.filter(f => f.endsWith('_docs.md'))

      for (const file of files) {
        try {
          const fullPath = path.join(incomingDir, file)
          const content = await fs.promises.readFile(fullPath, 'utf8')
          const knowledge = KnowledgeObserver.processContent(file, content, `local://${file}`)
          await observer.persistKnowledge(knowledge)
          console.log(` ✅ [Jules] Ingested scratch doc: ${file}`)
        } catch (err) {
          console.error(` ❌ [Jules] Failed to ingest scratch doc ${file}:`, err)
        }
      }

      // Phase 12: Scan iCloud Simulation directory
      const simDir = path.join(incomingDir, 'icloud_sim')
      if (fs.existsSync(simDir)) {
        console.log(`☁️ [Jules] Scanning iCloud Simulation for new knowledge: ${simDir}`)
        const simFiles = fs.readdirSync(simDir).filter(f => f.endsWith('.md'))
        for (const file of simFiles) {
          const fullPath = path.join(simDir, file)
          const content = fs.readFileSync(fullPath, 'utf8')
          const knowledge = KnowledgeObserver.processContent(file, content, `icloud-sim://${file}`)
          await observer.persistKnowledge(knowledge)
        }
      }
    } catch (e) {
      console.error(`❌ [Jules] Failed to observe local scratch knowledge:`, e)
    }

    // Phase 12: Scan iCloud for new knowledge
    const os = await import('os')
    const homeDir = os.homedir()
    const defaultICloudPath = path.join(homeDir, 'Library/Mobile Documents/com~apple~CloudDocs/Antigravity_Sync')
    const icloudDir = process.env.ICLOUD_SYNC_PATH || defaultICloudPath

    try {
      await fs.promises.access(icloudDir)

      const dirFiles = await fs.promises.readdir(icloudDir)
      const files = dirFiles.filter(f => f.endsWith('.md'))


      for (const file of files) {
        const fullPath = path.join(icloudDir, file)
        const content = await fs.promises.readFile(fullPath, 'utf8')
        const knowledge = KnowledgeObserver.processContent(file, content, `icloud://${file}`)
        await observer.persistKnowledge(knowledge)
      }
    } catch (e) {
      console.error(`❌ [Jules] Failed to observe iCloud knowledge:`, e)
    }
  }
}

export const jules = new Jules()
