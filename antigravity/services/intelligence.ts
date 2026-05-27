import { logAutonomousAction } from '../core'
import fs from 'fs'
import path from 'path'
import { getMissionMetadata } from './collaboration'
import { workOrderService } from './work_order'
import { jules } from '../jules'
import { healthCheck } from '../core'
import { checkJenkinsHealth } from './jenkins'

/**
 * CONSOLIDATED INTELLIGENCE SERVICE
 * Generates system-wide intelligence reports.
 */

export async function generateConsolidatedReport(branchIntelligence?: any[]) {
  logAutonomousAction('📊 [Intelligence] Generating consolidated system report...', 'info')

  const metadata = await getMissionMetadata()
  const branches = branchIntelligence || await jules.scanAllBranches()
  const health = await healthCheck()
  const workOrders = await workOrderService.getPendingOrders()

  const reportPath = path.join(process.cwd(), 'CONSOLIDATED_INTELLIGENCE.md')

  let report = `# CONSOLIDATED INTELLIGENCE REPORT\n\n`
  report += `*Generated: ${new Date().toISOString()}*\n\n`

  report += `## 🎯 Mission Statement\n> ${metadata.missionStatement}\n\n`

  report += `## 🏥 System Sovereignty\n`
  report += `- **Execution Environment:** ${process.env.GITHUB_ACTIONS ? 'Cloud (GitHub Actions)' : (process.env.GITLAB_CI ? 'Cloud (GitLab CI)' : (process.env.VERCEL ? 'Cloud (Vercel)' : 'Local'))}\n`
  report += `- **Mode:** ${process.env.AUTONOMOUS_MODE || 'standard'}\n`
  report += `- **MongoDB:** ${health.mongodb}\n`
  report += `- **Supabase:** ${health.supabase}\n`

  const jenkinsHealth = await checkJenkinsHealth()
  report += `- **Jenkins Pipeline:** ${jenkinsHealth.status} (${jenkinsHealth.metrics.pipeline_efficiency})\n`

  const { checkDockerHealth } = await import('./docker')
  const dockerHealth = await checkDockerHealth()
  report += `- **Docker Status:** ${dockerHealth.status} (${dockerHealth.containerCount} containers)\n`

  const { GitProviderService } = await import('./git_provider')
  const prs = await (new GitProviderService()).listPullRequests()
  report += `- **Open PRs/MRs:** ${prs.length}\n`

  report += `- **Total Branches:** ${branches.length}\n\n`

  report += `## 🌿 Branch Intelligence (Recent Activity)\n`
  const recentBranches = branches
    .sort((a, b) => new Date(b.lastSeen).getTime() - new Date(a.lastSeen).getTime())
    .slice(0, 10)

  recentBranches.forEach(b => {
    report += `- **${b.name}**: ${b.lastMessage} (*${b.lastSeen}*)\n`
  })
  report += `\n`

  report += `## 🛠️ Cognitive State\n`
  report += `- **Pending Work Orders:** ${workOrders.length}\n`
  if (workOrders.length > 0) {
    workOrders.forEach(wo => {
      report += `  - [${wo.type}] ${wo.goal || wo.description}\n`
    })
  } else {
    report += `  - No pending orders. System is optimal.\n`
  }

  try {
    const { getPerformanceMonitoringServiceData } = await import('./performance_monitoring')
    const perf = await getPerformanceMonitoringServiceData()
    report += `- **System Load:** ${perf.metrics.system.loadavg[0].toFixed(2)}\n`
    report += `- **Memory RSS:** ${Math.round(perf.metrics.memory.rss / 1024 / 1024)}MB\n`
  } catch (e) {}

  try {
    const { getFeedbackAnalysisServiceData } = await import('./feedback_analysis')
    const feedback = await getFeedbackAnalysisServiceData()
    report += `- **Autonomous Feedback:** ${feedback.insights.errorCount} errors, ${feedback.insights.warningsCount} warnings detected.\n`
    if (feedback.insights.suggestions.length > 0) {
      report += `  - *Latest Suggestion:* ${feedback.insights.suggestions[feedback.insights.suggestions.length - 1]}\n`
    }
  } catch (e) {}

  report += `\n`

  report += `## 🤖 Unified Knowledge & Market Intelligence\n`
  try {
    const knowledgePath = path.join(process.cwd(), 'data/knowledge/system_knowledge.json')
    if (fs.existsSync(knowledgePath)) {
      const knowledge = JSON.parse(fs.readFileSync(knowledgePath, 'utf8'))

      // 1. Market Data (Markposition)
      if (knowledge.market_data) {
        report += `- **Market Intelligence:** ${knowledge.market_data.total_entries} specialized entries analyzed from Markposition.\n`
        if (knowledge.market_data.recent_entries && knowledge.market_data.recent_entries.length > 0) {
           const topDomains = Array.from(new Set(knowledge.market_data.recent_entries.map((e: any) => e.domain).filter(Boolean))).slice(0, 5)
           report += `  - *Recent Signals:* Tracking ${topDomains.join(', ')} and others.\n`
        }
      }

      // 2. Technical Documentation
      const techSections = ['gemma_model', 'intelephense', 'litert', 'stitch', 'vscode_intelephense', 'google_innovation_ai']
      let techCount = 0
      techSections.forEach(s => { if (knowledge[s]) techCount++ })
      report += `- **Technical Foundation:** ${techCount} deep documentation domains ingested.\n`

      // 3. AI Agents
      if (knowledge.ai_agents_structured) {
        report += `- **Agentic Framework:** ${knowledge.ai_agents_structured.length} AI agent definitions and architectural patterns merged.\n`
      }
    } else {
      report += `- **Knowledge Base:** Unified store pending initialization.\n`
    }

    const linksPath = path.join(process.cwd(), 'links.json')
    if (fs.existsSync(linksPath)) {
      const links = JSON.parse(fs.readFileSync(linksPath, 'utf8'))
      report += `- **Legacy Market Data:** ${links.length} entries in raw buffer.\n`
    }

    const resultsDir = path.join(process.cwd(), 'results')
    if (fs.existsSync(resultsDir)) {
      const files = fs.readdirSync(resultsDir)
      report += `- **Autonomous Reports:** ${files.length} history files available.\n`

      const latestReport = files.filter(f => f.startsWith('DAILY_REPORT')).sort().reverse()[0]
      if (latestReport) {
        report += `- **Latest Daily Summary:** ${latestReport}\n`
      }
    }
  } catch (e) {
    report += `- **Ecosystem Status:** Limited observability into knowledge layer.\n`
  }
  report += `\n`

  report += `## 👥 Stakeholders\n`
  metadata.stakeholders.forEach(s => {
    report += `- **${s.role}**: ${s.email}\n`
  })

  fs.writeFileSync(reportPath, report)
  logAutonomousAction(`✅ [Intelligence] Report saved to ${reportPath}`, 'info')

  return { reportPath, branchCount: branches.length }
}
