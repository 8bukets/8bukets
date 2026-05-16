import { execSync, exec } from 'child_process'
import { promisify } from 'util'
import { z } from 'zod'
import { autonomousFetch } from '@/antigravity/core'

const execAsync = promisify(exec)

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
      const output = execSync('docker ps --format "{{.ID}}|{{.Image}}|{{.Status}}|{{.Names}}"').toString()
      const lines = output.trim().split('\n')

      if (!output.trim()) return []

      return lines.map(line => {
        const [id, image, status, names] = line.split('|')
        return { id, image, status, names }
      })
    } catch (e) {
      console.warn('⚠️ [Docker] Failed to query Docker daemon. Ensure it is running.', e)
      return []
    }
  }, { tags: ['docker-fleet-status'], life: 'inventory' })
}

export async function checkDockerHealth() {
  const fleet = await getDockerFleetStatus()
  let isHealthy = fleet.length > 0
  let isRecovering = false

  if (!isHealthy) {
    try {
      // Use async exec to prevent blocking the event loop
      execAsync('docker-compose up -d').catch(e => {
        console.warn('⚠️ [Docker] Async recovery failed.', e)
      })
      isRecovering = true
    } catch (e) {
      console.warn('⚠️ [Docker] Failed to initiate recovery.', e)
    }
  }

  return {
    status: isHealthy ? 'optimal' : (isRecovering ? 'recovering' : 'disconnected'),
    containerCount: fleet.length,
    timestamp: new Date().toISOString()
  }
}
