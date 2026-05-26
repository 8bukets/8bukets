import fs from 'fs'
import path from 'path'
import { z } from 'zod'
import { logAutonomousAction } from '@/antigravity/core'

/**
 * ANTIGRAVITY COMMUNICATION HUB (Phase 12)
 * Centralizes agent-to-stakeholder interactions and directive processing.
 */

export const DirectiveSchema = z.object({
  id: z.string(),
  intent: z.string(),
  priority: z.enum(['Low', 'Medium', 'High', 'Critical']),
  status: z.enum(['Active', 'Fulfilled', 'Obsolete']),
  timestamp: z.string()
})

export type Directive = z.infer<typeof DirectiveSchema>

const DIRECTIVES_PATH = path.join(process.cwd(), '.antigravity/directives.md')

export async function getStakeholderDirectives(): Promise<Directive[]> {
  if (!fs.existsSync(DIRECTIVES_PATH)) {
    // Create default directives if missing
    const defaultDirectives = `# Stakeholder Directives\n\n- [High] Maintain 99.9% system uptime (Active)\n- [Medium] Consolidate all branch knowledge daily (Active)\n`
    const dir = path.dirname(DIRECTIVES_PATH)
    if (!fs.existsSync(dir)) await fs.promises.mkdir(dir, { recursive: true })
    await fs.promises.writeFile(DIRECTIVES_PATH, defaultDirectives)
    return [
      { id: 'dir_default_1', intent: 'Maintain 99.9% system uptime', priority: 'High', status: 'Active', timestamp: new Date().toISOString() },
      { id: 'dir_default_2', intent: 'Consolidate all branch knowledge daily', priority: 'Medium', status: 'Active', timestamp: new Date().toISOString() }
    ]
  }

  const content = await fs.promises.readFile(DIRECTIVES_PATH, 'utf8')
  const directives: Directive[] = []

  const lines = content.split('\n')
  lines.forEach(line => {
    const match = line.match(/^-\s*\[(Low|Medium|High|Critical)\]\s*(.*?)\s*\((Active|Fulfilled|Obsolete)\)$/i)
    if (match) {
      directives.push({
        id: `dir_${Math.random().toString(36).substr(2, 9)}`,
        priority: match[1] as any,
        intent: match[2].trim(),
        status: match[3] as any,
        timestamp: new Date().toISOString()
      })
    }
  })

  return directives
}

export async function dispatchStakeholderAlert(subject: string, body: string, priority: 'info' | 'warning' | 'critical' = 'info') {
  console.log(`🔔 [Communication] Dispatching Alert: ${subject}`)
  logAutonomousAction(`[ALERT] ${subject}`, priority === 'critical' ? 'error' : 'info')

  const logDir = path.join(process.cwd(), 'logs')
  if (!fs.existsSync(logDir)) await fs.promises.mkdir(logDir, { recursive: true })

  const alertEntry = `\n--- ALERT (${new Date().toISOString()}) ---\nSubject: ${subject}\nPriority: ${priority}\n\n${body}\n`
  await fs.promises.appendFile(path.join(logDir, 'stakeholder_alerts.log'), alertEntry)

  return { status: 'dispatched', timestamp: new Date().toISOString() }
}

export async function generateActionableBriefing(state: any, directives: Directive[]) {
  const activeDirectives = directives.filter(d => d.status === 'Active')

  let briefing = `### 🎯 Active Stakeholder Directives\n`
  if (activeDirectives.length > 0) {
    activeDirectives.forEach(d => {
      briefing += `- **[${d.priority}]** ${d.intent}\n`
    })
  } else {
    briefing += `- No active directives currently registered.\n`
  }

  briefing += `\n### 🚀 System Actions Required\n`

  if (state.docker.status !== 'optimal' && state.docker.status !== 'simulated') {
    briefing += `- [CRITICAL] Investigate Docker node degradation.\n`
  }

  if (state.intelligence.pendingTasks > 10) {
    briefing += `- [HIGH] Background work order queue is exceeding capacity (${state.intelligence.pendingTasks} tasks).\n`
  }

  const synergies = state.intelligence.relationshipMap.synergies || []
  const highIntensity = synergies.filter((s: any) => s.intensity === 'High')

  if (highIntensity.length > 0) {
    briefing += `- [MEDIUM] Resource contention detected across ${highIntensity.length} clusters. See Synergy Matrix.\n`
  }

  return briefing
}
