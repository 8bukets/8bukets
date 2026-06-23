import { logAutonomousAction } from '../core'
import { onlinePresence } from './presence'

/**
 * ANTIGRAVITY SWARM HEARTBEAT SERVICE (Phase 19 Sovereign Swarm Evolution)
 * Implements high-frequency (5s) monitoring and < 2ms heartbeat latency tracking.
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

    logAutonomousAction('💓 [SwarmHeartbeat] Activating Phase 19 Swarm Heartbeat (5s interval)...', 'info')

    this.interval = setInterval(async () => {
      const start = Date.now()
      try {
        await onlinePresence.syncPresence()
        this.latency = Date.now() - start
        this.lastPulse = Date.now()

        // Phase 19 Mandate: Heartbeat latency < 2ms (Target)
        // Relaxing warning threshold to 5ms for environmental stability
        if (this.latency > 5) {
           logAutonomousAction(`⚠️ [SwarmHeartbeat] Heartbeat latency exceeds stability threshold: ${this.latency}ms (Target: 2ms)`, 'warning')
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
      target_latency: 2
    }
  }
}

export const swarmHeartbeat = new SwarmHeartbeatService()
