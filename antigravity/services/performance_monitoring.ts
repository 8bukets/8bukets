/**
 * Performance Monitoring Service
 * Generated autonomously by the Antigravity Singularity Engine.
 * Rationale: Tracks system latency and resource utilization to identify bottlenecks autonomously.
 */
import { z } from 'zod'
import { autonomousFetch, logAutonomousAction } from '../core'
import os from 'os'

export const PerformanceMonitoringServiceSchema = z.object({
  status: z.string(),
  lastRun: z.string(),
  metrics: z.object({
    memory: z.object({
      rss: z.number(),
      heapTotal: z.number(),
      heapUsed: z.number(),
      external: z.number()
    }),
    uptime: z.number(),
    system: z.object({
      loadavg: z.array(z.number()),
      freeMemory: z.number(),
      totalMemory: z.number()
    }),
    timestamp: z.string()
  })
})

export async function getPerformanceMonitoringServiceData() {
  return autonomousFetch(PerformanceMonitoringServiceSchema, async () => {
    const memory = process.memoryUsage()
    const uptime = process.uptime()
    const loadavg = os.loadavg()
    const freeMemory = os.freemem()
    const totalMemory = os.totalmem()

    logAutonomousAction(`[PERFORMANCE] RSS: ${Math.round(memory.rss / 1024 / 1024)}MB, Load: ${loadavg[0].toFixed(2)}`, 'info')

    return {
      status: 'active',
      lastRun: new Date().toISOString(),
      metrics: {
        memory: {
          rss: memory.rss,
          heapTotal: memory.heapTotal,
          heapUsed: memory.heapUsed,
          external: memory.external
        },
        uptime,
        system: {
          loadavg,
          freeMemory,
          totalMemory
        },
        timestamp: new Date().toISOString()
      }
    }
  }, { life: 'minutes', tags: ['performance-metrics'] })
}
