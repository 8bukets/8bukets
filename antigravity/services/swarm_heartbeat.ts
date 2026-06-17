import { logAutonomousAction } from '../core'
import { onlinePresence } from './presence'

/**
 * ANTIGRAVITY SWARM HEARTBEAT SERVICE (Phase 16)
 * Implements high-frequency (5s) monitoring and heartbeat latency tracking.
 */

export class SwarmHeartbeatService {
  private interval: NodeJS.Timeout | null = null
  private lastPulse: number = Date.now()
  private latency: number = 0

  /**
   * Starts the 5-second swarm heartbeat pulse.
   */
  public start() {
    if (this.interval) return

    logAutonomousAction('💓 [SwarmHeartbeat] Activating Phase 16 Swarm Heartbeat (5s interval)...', 'info')

    this.interval = setInterval(async () => {
      const start = Date.now()
      try {
        await onlinePresence.syncPresence()
        this.latency = Date.now() - start
        this.lastPulse = Date.now()

        if (this.latency > 5) {
           logAutonomousAction(`⚠️ [SwarmHeartbeat] Heartbeat latency exceeds Phase 16 target: ${this.latency}ms`, 'warning')
        }
      } catch (err: any) {
        logAutonomousAction(`❌ [SwarmHeartbeat] Pulse failed: ${err.message}`, 'error')
      }
    }, 5000)
  }

  public stop() {
    if (this.interval) {
      clearInterval(this.interval)
      this.interval = null
      logAutonomousAction('🛑 [SwarmHeartbeat] Swarm Heartbeat deactivated.', 'info')
    }
  }

  public getMetrics() {
    return {
      latency: this.latency,
      lastPulse: new Date(this.lastPulse).toISOString(),
      active: !!this.interval,
      target_latency: 5
    }
  }
}

export const swarmHeartbeat = new SwarmHeartbeatService()
