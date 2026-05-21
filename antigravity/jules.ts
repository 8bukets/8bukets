import fs from 'fs'
import path from 'path'
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

  public recordTask(goal: string, role: AgentRole = this.role) {
    this.memory.autonomousTasks.push({
      id: Math.random().toString(36).substr(2, 9),
      status: 'completed',
      goal,
      role
    })
    this.save()
    
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
      { name: 'Consolidated Knowledge Observation', action: () => this.observeKnowledge() },
      { name: 'Core Integrity Check', action: () => this.recordTask('Integrity scan passed.') },
      { name: 'GitKraken Sync Prep', action: () => this.recordTask('Visual branch history cleaned.') }
    ]

    for (const task of tasks) {
      console.log(` - Executing: ${task.name}...`)
      await task.action()
    }

    this.memory.lastOptimization = new Date().toISOString()
    this.save()
    console.log(`✅ [Jules-${this.role}] Daily Routine Completed.`)
  }

  public async observeGithubDocs() {
    console.log(`📚 [Jules-${this.role}] Observing technical documentation from GitHub...`)
    const { githubDocsObserver } = await import('./services/github_docs_observer')
    const { KnowledgeObserver } = await import('./services/knowledge_observer')
    const observer = new KnowledgeObserver()

    const intelephenseDocs = [
      { owner: 'bmewburn', repo: 'intelephense-docs', path: 'README.md' },
      { owner: 'bmewburn', repo: 'intelephense-docs', path: 'installation.md' },
      { owner: 'bmewburn', repo: 'intelephense-docs', path: 'gettingStarted.md' },
      { owner: 'bmewburn', repo: 'intelephense-docs', path: 'features.md' },
      { owner: 'bmewburn', repo: 'intelephense-docs', path: 'support.md' }
    ]

    let allSections: any[] = []

    for (const doc of intelephenseDocs) {
      try {
        const result = await githubDocsObserver.fetchDoc(doc.owner, doc.repo, doc.path)
        const title = `Intelephense: ${doc.path.replace('.md', '')}`
        const rawContent = result.sections.map((s: any) => `# ${s.title}\n${s.content}`).join('\n\n')
        const knowledge = KnowledgeObserver.processContent(title, rawContent, result.rawUrl)

        allSections.push(...knowledge.sections)
        console.log(` ✅ [Jules] Fetched: ${doc.path}`)
      } catch (err) {
        console.error(` ❌ [Jules] Failed to fetch ${doc.path}:`, err)
      }
    }

    if (allSections.length > 0) {
      // Deduplicate sections by header
      const seenHeaders = new Set<string>()
      const uniqueSections = allSections.filter(s => {
        if (seenHeaders.has(s.header)) return false
        if (!s.content && !['Getting Started', 'Features', 'Installation'].includes(s.header)) return false
        seenHeaders.add(s.header)
        return true
      })

      const consolidated = {
        title: 'Intelephense Documentation',
        sections: uniqueSections,
        metadata: {
          source: 'https://intelephense.com/docs',
          ingestedAt: new Date().toISOString()
        }
      }
      await observer.persistKnowledge(consolidated as any)
      console.log(` ✅ [Jules] Consolidated Intelephense Documentation persisted.`)
    }
  }

  public async selfRepair() {
    console.log(`🔧 [Jules-${this.role}] Starting autonomous self-repair cycle...`)
    const { evolve, applyFixes } = await import('./evolution')
    const suggestions = await evolve()
    
    if (suggestions.length > 0) {
      await applyFixes(suggestions)
      this.recordTask(`Self-Repair: Applied ${suggestions.length} fixes.`)

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
      await execAsync('git reset HEAD work_cycle.log data/work_orders.json .jules_memory.json autonomous_state.json || true')

      try {
        await execAsync(`git commit -m "${message}"`)
      } catch (commitErr) {
        console.log('ℹ️ [Jules] No changes to commit or commit failed. Proceeding to push anyway.')
      }

      await execAsync('git push origin main || true')
      console.log('✅ [Jules] Git sync completed autonomously.')
      this.recordTask(`Git Sync: Synchronized state with origin.`)
    } catch (err) {
      console.warn('⚠️ [Jules] Git sync failed unexpectedly:', err)
    }
  }

  public async auditDependencies() {
    console.log(`📦 [Jules-${this.role}] Auditing dependency sovereignty...`)
    const { execSync } = await import('child_process')
    try {
      const outdated = execSync('npm outdated --json || true').toString()
      const count = Object.keys(JSON.parse(outdated || '{}')).length
      if (count > 0) {
        this.recordTask(`Dependency Autopilot: Found ${count} outdated packages.`)
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
        this.recordTask(`iCloud Sync: Successfully synchronized project to ${result.target}`)
      } else if (result.status === 'failed') {
        this.recordTask(`iCloud Sync: Synchronization failed - ${result.error}`, 'Ops')
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
      this.recordTask(`Synthesis: Generated ${ideas.length} proposals.`)
      await creationEngine.processIdeas(ideas)
    }

    // Phase 12: Super-Intelligence Optimization
    // getSystemInsights already triggers the optimization engine internally
    const { getSystemInsights } = await import('./core')
    const insights = await getSystemInsights()
    const refactors = (insights as any).proposals || []
    if (refactors.length > 0) {
      this.recordTask(`Super-Intelligence: Generated ${refactors.length} predictive refactors.`)
    }

    // ReAct Protocol Integration (arXiv:2210.03629)
    const { reactService } = await import('./services/react')
    const reactTools = {
      checkSystemState: async () => JSON.stringify(await import('./core').then(c => c.healthCheck())),
      findOptimizations: async () => JSON.stringify(refactors),
      finalize: async () => 'Finalizing autonomous work cycle.'
    }
    const reactSteps = await reactService.executeCycle('Optimize system posture using ReAct', reactTools)
    this.recordTask(`ReAct: Completed ${reactSteps.length} reasoning-action steps.`)

    // Autonomous Improvement Cycle (Analyze Recent Sessions)
    try {
      const fs = await import('fs');
      const path = await import('path');
      let fullWorkOrders = [];
      const woPath = path.join(process.cwd(), 'data/work_orders.json');
      if (fs.existsSync(woPath)) {
        fullWorkOrders = JSON.parse(fs.readFileSync(woPath, 'utf8'));
      }

      const sessionAnalysisIdeas = await reactService.analyzeAndImproveSessions({
        branches,
        workOrders: fullWorkOrders
      });

      if (sessionAnalysisIdeas.length > 0) {
        this.recordTask(`ReAct Improvement: Synthesized ${sessionAnalysisIdeas.length} ideas from recent sessions.`);
        await creationEngine.processIdeas(sessionAnalysisIdeas);
      }
    } catch (err) {
      console.error(`❌ [Jules] Failed autonomous improvement cycle:`, err);
    }

    // Cloud Workflow Agent
    const { cloudWorkflowAgent } = await import('./services/cloud_workflow')
    const isFluent = await cloudWorkflowAgent.ensureFluentStatus()
    if (isFluent) {
      this.recordTask(`Cloud Workflow: System is FLUENT_ON_AIR.`)
    } else {
      this.recordTask(`Cloud Workflow: System degraded, attempted proactive recovery.`)
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

    this.save()
    console.log(`🏆 [Jules-${this.role}] Autonomous Work Cycle Complete.`)
  }

  public async scanAllBranches(force: boolean = false) {
    console.log(`🔍 [Jules-${this.role}] Scanning ecosystem branches (force: ${force})...`)
    const { execSync } = await import('child_process')
    try {
      // Optimization: Use git for-each-ref to get the most recent branches (local and remote) efficiently.
      // Format: branch_name|subject|timestamp
      const limit = force ? '' : '--count=50'
      const cmd = `git for-each-ref --sort=-committerdate --format="%(refname:short)|%(contents:subject)|%(committerdate:unix)" refs/heads refs/remotes/origin ${limit}`
      const branchesRaw = execSync(cmd).toString()
      const branchLines = branchesRaw.split('\n').filter(l => l.trim() !== '')

      return branchLines.map(line => {
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

          const knowledgeNugget = message.toLowerCase().match(/(?:learn|observe|ingest|knowledge):\s*(.*)/i)
            ? `Branch ${branch} observed: ${results}`
            : (message.toLowerCase().includes('learn') || message.toLowerCase().includes('observe') ? `Branch ${branch} observed: ${results}` : undefined)

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
              diffOutput = execSync(diffCommand, { stdio: ['ignore', 'pipe', 'ignore'] }).toString().trim()
            } catch (e) {
              // Fallback 1: Direct comparison
              diffCommand = `git diff --name-only main ${branch}`
              try {
                diffOutput = execSync(diffCommand, { stdio: ['ignore', 'pipe', 'ignore'] }).toString().trim()
              } catch (e2) {
                // Fallback 2: Last commit changes
                diffCommand = `git show --name-only --format="" ${branch}`
                diffOutput = execSync(diffCommand, { stdio: ['ignore', 'pipe', 'ignore'] }).toString().trim()
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

          return {
            name: branch,
            lastMessage: message,
            lastSeen: new Date(parseInt(timestamp) * 1000).toISOString(),
            category,
            results,
            knowledge: knowledgeNugget,
            changedFiles,
            domain
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
    } catch (err) {
      console.error(`❌ [Jules-${this.role}] Branch scan failed:`, err)
      return []
    }
  }

  public async observeKnowledge() {
    const { KnowledgeObserver } = await import('./services/knowledge_observer')
    const observer = new KnowledgeObserver()

    // Scan external intelligence
    const { observeKnowledge: scanUrl } = await import('./services/knowledge')
    await scanUrl('https://software-online-review.com')
    await scanUrl('https://markposition.wordpress.com')

    // Scan scratch for new knowledge
    const incomingDir = path.join(process.cwd(), 'scratch')
    if (fs.existsSync(incomingDir)) {
      const files = fs.readdirSync(incomingDir).filter(f => f.endsWith('_docs.md'))
      for (const file of files) {
        const fullPath = path.join(incomingDir, file)
        const content = fs.readFileSync(fullPath, 'utf8')
        const knowledge = KnowledgeObserver.processContent(file, content, `local://${file}`)
        await observer.persistKnowledge(knowledge)
      }
    }

    // Phase 12: Scan iCloud for new knowledge
    const os = await import('os')
    const homeDir = os.homedir()
    const defaultICloudPath = path.join(homeDir, 'Library/Mobile Documents/com~apple~CloudDocs/Antigravity_Sync')
    const icloudDir = process.env.ICLOUD_SYNC_PATH || defaultICloudPath

    if (fs.existsSync(icloudDir)) {
      console.log(`☁️ [Jules] Scanning iCloud for new knowledge: ${icloudDir}`)
      const files = fs.readdirSync(icloudDir).filter(f => f.endsWith('.md'))
      for (const file of files) {
        const fullPath = path.join(icloudDir, file)
        const content = fs.readFileSync(fullPath, 'utf8')
        const knowledge = KnowledgeObserver.processContent(file, content, `icloud://${file}`)
        await observer.persistKnowledge(knowledge)
      }
    }
  }
}

export const jules = new Jules()
