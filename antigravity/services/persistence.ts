import { exec } from 'child_process'
import { promisify } from 'util'
import { z } from 'zod'
import { autonomousFetch, logAutonomousAction } from '@/antigravity/core'

const execAsync = promisify(exec)

export const PersistenceSchema = z.object({
  agent: z.string(),
  status: z.enum(['running', 'stopped', 'error']),
  pid: z.string().optional()
})

export type PersistenceStatus = z.infer<typeof PersistenceSchema>

/**
 * Persistence Monitoring Service
 * Autonomously tracks the state of system-level Sigma agents.
 */
export async function getPersistenceHealth(): Promise<PersistenceStatus[]> {
  const agents = ['com.sigma.orchestrator', 'com.sigma.jules', 'com.sigma.syra_api']
  const isMac = process.platform === 'darwin'

  return autonomousFetch(z.array(PersistenceSchema), async () => {
    const results: PersistenceStatus[] = []

    for (const agent of agents) {
      try {
        if (isMac) {
          try {
            const { stdout } = await execAsync(`launchctl list ${agent}`)
            const output = stdout.toString()
            const pidMatch = output.match(/"PID" = (\d+);/)
            const lastExitMatch = output.match(/"LastExitStatus" = (\d+);/)

            results.push({
              agent,
              status: pidMatch ? 'running' : (lastExitMatch && lastExitMatch[1] === '0' ? 'stopped' : 'error'),
              pid: pidMatch ? pidMatch[1] : undefined
            })
          } catch (macErr) {
            results.push({ agent, status: 'error' })
          }
        } else {
          // Cloud/Linux Fallback using pgrep or ps
          try {
            const { stdout } = await execAsync(`pgrep -f ${agent}`)
            const pid = stdout.toString().trim()
            results.push({
              agent,
              status: pid ? 'running' : 'stopped',
              pid: pid || undefined
            })
          } catch (e) {
            results.push({ agent, status: 'stopped' })
          }
        }
      } catch (e) {
        results.push({ agent, status: 'error' })
      }
    }

    return results
  }, { life: 'inventory', tags: ['persistence-health'] })
}
