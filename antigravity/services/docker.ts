import { execSync } from 'child_process'
import { z } from 'zod'
import { autonomousFetch } from '@/antigravity/core'

/**
 * ANTIGRAVITY DOCKER CONNECTIVITY SERVICE (Phase 1)
 * Monitors the status of the Docker fleet.
 */

export const DockerContainerSchema = z.object({
  id: z.string(),
  image: z.string(),
  status: z.string(),
  names: z.string()
})

export type DockerContainer = z.infer<typeof DockerContainerSchema>

export async function getDockerFleetStatus(): Promise<DockerContainer[]> {
  return autonomousFetch(z.array(DockerContainerSchema), async () => {
    try {
      // Attempt to query the Docker daemon
      const output = execSync('docker ps --format "{{.ID}}|{{.Image}}|{{.Status}}|{{.Names}}"').toString().trim()

      if (!output && process.env.ANTIGRAVITY_SIMULATE_DOCKER === 'true') {
        throw new Error('Simulation requested')
      }

      if (!output) return []

      const lines = output.split('\n')

      return lines.map(line => {
        const [id, image, status, names] = line.split('|')
        return { id, image, status, names }
      })
    } catch (e) {
      // Phase 12: Adaptive Connectivity
      // If we are in a restricted environment (like a serverless sandbox or CI without Docker socket access),
      // we fall back to a simulated but descriptive state rather than just failing.
      const isRestrictedEnv = process.env.NODE_ENV === 'test' || process.env.ANTIGRAVITY_SIMULATE_DOCKER === 'true'

      if (isRestrictedEnv) {
        console.log('🧪 [Docker] Restricted environment detected. Engaging simulated fleet observability.')
        return [
          { id: 'sim-01', image: 'antigravity-core:latest', status: 'Up 24 hours', names: 'primary-node-alpha' },
          { id: 'sim-02', image: 'mongo:latest', status: 'Up 24 hours', names: 'primary-database' }
        ]
      }

      console.warn('⚠️ [Docker] Failed to query Docker daemon. Ensure it is running or set ANTIGRAVITY_SIMULATE_DOCKER=true.', e)
      return []
    }
  }, { tags: ['docker-fleet-status'], life: 'inventory' })
}

export async function checkDockerHealth() {
  const fleet = await getDockerFleetStatus()
  const isHealthy = fleet.length > 0
  const isSimulated = fleet.some(c => c.id.startsWith('sim-'))

  return {
    status: isHealthy ? (isSimulated ? 'simulated' : 'optimal') : 'disconnected',
    containerCount: fleet.length,
    simulated: isSimulated,
    timestamp: new Date().toISOString()
  }
}
