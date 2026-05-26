import { z } from 'zod'
import { autonomousFetch, logAutonomousAction, getMongoClient, supabase } from '@/antigravity/core'
import { checkDockerHealth } from './docker'
import { gitProviderService } from './git_provider'

/**
 * ANTIGRAVITY ONLINE PRESENCE SERVICE (Phase 12)
 * Centralizes cloud-native status aggregation and telemetry broadcasting.
 */

export const PresenceSchema = z.object({
  id: z.string(),
  agent: z.string(),
  status: z.enum(['online', 'busy', 'offline', 'degraded']),
  environment: z.string(),
  telemetry: z.object({
    docker: z.any(),
    git: z.any(),
    databases: z.object({
      mongodb: z.string(),
      supabase: z.string()
    }),
    uptime: z.number()
  }),
  lastPulse: z.string()
})

export type Presence = z.infer<typeof PresenceSchema>

class OnlinePresenceService {
  private agentName: string = 'Jules-Orchestrator'
  private env: string = process.env.NODE_ENV || 'development'

  /**
   * Aggregates system-wide status for the current node.
   */
  public async getSystemPosture(): Promise<Presence> {
    const docker = await checkDockerHealth()
    const gitProvider = await gitProviderService.getActiveProvider()

    // Check DB Latency/Status
    let mongoStatus = 'unknown'
    try {
      const client = await getMongoClient()
      const start = Date.now()
      await client.db().admin().ping()
      mongoStatus = `${Date.now() - start}ms`
    } catch (e) {
      mongoStatus = 'error'
    }

    let supabaseStatus = 'unknown'
    try {
      const start = Date.now()
      const { error } = await supabase.from('_health').select('id').limit(1)
      supabaseStatus = error && error.code !== 'PGRST116' ? 'error' : `${Date.now() - start}ms`
    } catch (e) {
      supabaseStatus = 'error'
    }

    return {
      id: `presence_${Math.random().toString(36).substring(2, 11)}`,
      agent: this.agentName,
      status: (docker.status === 'optimal' || docker.status === 'simulated') ? 'online' : 'degraded',
      environment: this.env,
      telemetry: {
        docker,
        git: { provider: gitProvider },
        databases: {
          mongodb: mongoStatus,
          supabase: supabaseStatus
        },
        uptime: process.uptime()
      },
      lastPulse: new Date().toISOString()
    }
  }

  /**
   * Phase 12: Broadcasts telemetry to persistent stores (MongoDB & Supabase).
   */
  public async broadcastTelemetry() {
    const posture = await this.getSystemPosture()
    console.log(`📡 [Presence] Broadcasting telemetry for ${this.agentName}...`)

    // 1. Broadcast to MongoDB (agent_presence collection)
    try {
      const client = await getMongoClient()
      await client.db().collection('agent_presence').updateOne(
        { agent: this.agentName },
        { $set: posture },
        { upsert: true }
      )
    } catch (e) {
      console.warn('⚠️ [Presence] Failed to broadcast to MongoDB.')
    }

    // 2. Broadcast to Supabase (agent_presence table)
    try {
      const { error } = await supabase
        .from('agent_presence')
        .upsert({
          agent: this.agentName,
          status: posture.status,
          environment: posture.environment,
          telemetry: posture.telemetry,
          last_pulse: posture.lastPulse
        }, { onConflict: 'agent' })

      if (error) throw error
    } catch (e) {
      console.warn('⚠️ [Presence] Failed to broadcast to Supabase.')
    }

    logAutonomousAction(`[PRESENCE] Heartbeat broadcast complete. Environment: ${this.env}`, 'sync')
    return posture
  }
}

export const onlinePresenceService = new OnlinePresenceService()
