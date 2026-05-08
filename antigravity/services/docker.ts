import { execSync } from 'child_process'
import { z } from 'zod'
import { autonomousFetch } from '@/antigravity/core'

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
      const output = execSync('docker ps --format "{{.ID}}|{{.Image}}|{{.Status}}|{{.Names}}"').toString()
      if (!output) return []

      return output.trim().split('\n').map(line => {
        const [id, image, status, name] = line.split('|')
        return { id, image, status, name }
      })
    } catch (e) {
      console.warn('⚠️ [Docker] Could not connect to Docker daemon.')
      return []
    }
  }, { life: 'inventory', tags: ['docker-status'] })
}

export async function isDockerHealthy(): Promise<boolean> {
  try {
    execSync('docker ps')
    return true
  } catch (e) {
    return false
  }
}
