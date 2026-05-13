import { execSync } from 'child_process'
import { z } from 'zod'
import { autonomousFetch, logAutonomousAction } from '@/antigravity/core'

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

  return autonomousFetch(z.array(PersistenceSchema), async () => {
    'use cache'
    const results: PersistenceStatus[] = []

    for (const agent of agents) {
      try {
        const output = execSync(`launchctl list ${agent}`).toString()
        const pidMatch = output.match(/"PID" = (\d+);/)
        const lastExitMatch = output.match(/"LastExitStatus" = (\d+);/)

        results.push({
          agent,
          status: pidMatch ? 'running' : (lastExitMatch && lastExitMatch[1] === '0' ? 'stopped' : 'error'),
          pid: pidMatch ? pidMatch[1] : undefined
        })
      } catch (e) {
        results.push({ agent, status: 'error' })
      }
    }

    return results
  }, { life: 'inventory', tags: ['persistence-health'] })
}
