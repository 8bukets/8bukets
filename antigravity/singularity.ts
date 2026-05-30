import { logAutonomousAction } from './core'
import fs from 'fs'
import path from 'path'

/**
 * ANTIGRAVITY SINGULARITY ENGINE
 * Autonomously scaffolds and generates new services based on synthesis.
 */

export async function bootstrap(idea: { feature: string, rationale: string }) {
  logAutonomousAction(`🌀 [Singularity] Bootstrapping: ${idea.feature}...`, 'info')

  const serviceName = idea.feature.toLowerCase().replace(/\s+/g, '_').replace(/_service$/, '')
  const filePath = path.join(process.cwd(), 'antigravity/services', `${serviceName}.ts`)

  if (fs.existsSync(filePath)) {
    logAutonomousAction(` - Service ${serviceName} already exists. Skipping bootstrap.`, 'info')
    return
  }

  const identifier = idea.feature.replace(/[^a-zA-Z0-9]/g, '')
  const template = `/**
 * ${idea.feature}
 * Generated autonomously by the Antigravity Singularity Engine.
 * Rationale: ${idea.rationale}
 */
import { z } from 'zod'
import { autonomousFetch } from '../core'

export const ${identifier}Schema = z.object({
  status: z.string(),
  lastRun: z.string()
})

export async function get${identifier}Data() {
  return autonomousFetch(${identifier}Schema, async () => {
    return {
      status: 'active',
      lastRun: new Date().toISOString()
    }
  }, { life: 'minutes' })
}
`

  fs.writeFileSync(filePath, template)
  logAutonomousAction(`✅ [Singularity] Successfully generated ${serviceName}.ts`, 'info')

  // Generate Test File
  const testPath = path.join(process.cwd(), 'antigravity/services', `${serviceName}.test.ts`)
  if (!fs.existsSync(testPath)) {
    const testTemplate = `/**
 * ${idea.feature} Test
 * Generated autonomously by the Antigravity Singularity Engine.
 */
import { describe, it, expect } from 'vitest'
import * as service from './${serviceName}'

describe('${idea.feature}', () => {
  it('should have a functional data fetcher', async () => {
    const data = await service.get${identifier}Data()
    expect(data.status).toBe('active')
    expect(data.lastRun).toBeDefined()
  })
})
`
    fs.writeFileSync(testPath, testTemplate)
    logAutonomousAction(`🧪 [Singularity] Successfully generated ${serviceName}.test.ts`, 'info')
  }

  return { filePath, testPath, serviceName, feature: idea.feature }
}
