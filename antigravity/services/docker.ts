import { exec } from 'child_process'
import { promisify } from 'util'
import { z } from 'zod'
import { autonomousFetch } from '@/antigravity/core'

const execAsync = promisify(exec)

export const DockerContainerSchema = z.object({
  id: z.string(),
  image: z.string(),
  status: z.string(),
  name: z.string()
})

export type DockerContainer = z.infer<typeof DockerContainerSchema>

/**
 * ANTIGRAVITY DOCKER SERVICE
 * Autonomously monitors Docker container connectivity and status.
 */
export async function getDockerStatus(): Promise<DockerContainer[]> {
  return autonomousFetch(z.array(DockerContainerSchema), async () => {
    'use cache'
    try {
      const { stdout } = await execAsync('docker ps --format "{{.ID}}|{{.Image}}|{{.Status}}|{{.Names}}"')
      if (!stdout) return []

      return stdout.trim().split('\n').map(line => {
        const [id, image, status, name] = line.split('|')
        return { id, image, status, name }
      })
    } catch (e) {
      console.warn('⚠️ [Docker] Could not connect to Docker daemon. Attempting autonomous recovery...')

      try {
        // Phase 5: Autonomous Recovery
        // Attempt to start services if docker-compose is available
        await execAsync('docker compose up -d')

        const { stdout } = await execAsync('docker ps --format "{{.ID}}|{{.Image}}|{{.Status}}|{{.Names}}"')
        if (!stdout) return []

        return stdout.trim().split('\n').map(line => {
          const [id, image, status, name] = line.split('|')
          return { id, image, status, name }
        })
      } catch (recoveryError) {
        console.error('❌ [Docker] Autonomous recovery failed.')
        return []
      }
    }
  }, { life: 'inventory', tags: ['docker-status'] })
}

export async function isDockerHealthy(): Promise<boolean> {
  try {
    await execAsync('docker ps')
    return true
  } catch (e) {
    return false
  }
}

// Phase 12: Standardized Aliases for high-fidelity simulation and tests
export const getDockerFleetStatus = getDockerStatus
export const checkDockerHealth = isDockerHealthy
