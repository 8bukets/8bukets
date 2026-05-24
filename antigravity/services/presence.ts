import { logAutonomousAction, getMongoClient, supabase, healthCheck } from '../core'
import { z } from 'zod'
import { checkDockerHealth } from './docker'
import { gitProvider } from './git_provider'
import os from 'os'

/**
 * ANTIGRAVITY ONLINE PRESENCE SERVICE
 * Aggregates and broadcasts system health and agent telemetry.
 */

export const PresenceSchema = z.object({
  agent: z.string(),
  status: z.enum(['online', 'offline', 'maintenance', 'error']),
  lastSeen: z.string(),
  version: z.string(),
  environment: z.enum(['cloud', 'local']),
  active_providers: z.array(z.string()),
  docker: z.object({
    status: z.string(),
    container_count: z.number(),
    mode: z.string()
  }),
  connectivity: z.object({
    mongodb: z.object({ status: z.string(), latency: z.number() }),
    supabase: z.object({ status: z.string(), latency: z.number() })
  }),
  git: z.object({
    open_prs: z.number(),
    providers: z.array(z.string())
  }),
  system: z.object({
    hostname: z.string(),
    uptime: z.number(),
    memory_usage: z.record(z.number())
  }),
  telemetry: z.object({
    workflow_id: z.string().optional(),
    run_attempt: z.string().optional(),
    node_id: z.string().optional()
  }).optional()
})

export type Presence = z.infer<typeof PresenceSchema>

export class OnlinePresenceService {
  /**
   * Synchronizes the agent's online presence across the ecosystem.
   */
  public async syncPresence() {
    logAutonomousAction('📡 [OnlinePresence] Synchronizing system presence...', 'info')

    try {
      const isCloud = !!(process.env.GITHUB_ACTIONS || process.env.GITLAB_CI || process.env.VERCEL || process.env.AUTONOMOUS_MODE === 'cloud' || process.env.MACBOOK_CLOUD_SIMULATION === 'true')

      // 1. Fetch component health
      const dockerHealth = await checkDockerHealth()
      const prs = await gitProvider.listPullRequests()

      const start = Date.now()
      const coreHealth = await healthCheck()
      const latency = Date.now() - start

      const providers = []
      if (process.env.GITHUB_TOKEN) providers.push('github')
      if (process.env.GITLAB_TOKEN) providers.push('gitlab')
      if (process.env.MONGODB_URI) providers.push('mongodb')
      if (process.env.NEXT_PUBLIC_SUPABASE_URL) providers.push('supabase')

      const presence: Presence = {
        agent: 'Jules',
        status: 'online',
        lastSeen: new Date().toISOString(),
        version: '1.6.0-alpha',
        environment: isCloud ? 'cloud' : 'local',
        active_providers: providers,
        docker: {
          status: dockerHealth.status,
          container_count: dockerHealth.containerCount,
          mode: dockerHealth.mode
        },
        connectivity: {
          mongodb: { status: coreHealth.mongodb, latency },
          supabase: { status: coreHealth.supabase, latency }
        },
        git: {
          open_prs: prs.length,
          providers: Array.from(new Set(prs.map(p => p.provider)))
        },
        system: {
          hostname: os.hostname(),
          uptime: process.uptime(),
          memory_usage: process.memoryUsage() as unknown as Record<string, number>
        },
        telemetry: {
          workflow_id: process.env.GITHUB_RUN_ID,
          run_attempt: process.env.GITHUB_RUN_ATTEMPT,
          node_id: isCloud ? 'cloud-relay-01' : 'macbook-primary-01'
        }
      }

      // 2. Broadcast to MongoDB
      try {
        const client = await getMongoClient()
        const db = client.db()
        await db.collection('agent_presence').updateOne(
          { agent: 'Jules' },
          { $set: presence },
          { upsert: true }
        )
      } catch (e) {
        logAutonomousAction('⚠️ [OnlinePresence] Failed to sync to MongoDB.', 'warning')
      }

      // 3. Broadcast to Supabase
      try {
        await supabase
          .from('agent_presence')
          .upsert({ ...presence, id: 'jules-alpha-01' })
      } catch (e) {
        logAutonomousAction('⚠️ [OnlinePresence] Failed to sync to Supabase.', 'warning')
      }

      logAutonomousAction(`✅ [OnlinePresence] Presence heartbeated (Environment: ${presence.environment}).`, 'info')
      return presence
    } catch (err: any) {
      logAutonomousAction(`❌ [OnlinePresence] Sync failed: ${err.message}`, 'error')
      return null
    }
  }
}

export const onlinePresence = new OnlinePresenceService()
