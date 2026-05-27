import fs from 'fs'
import path from 'path'
import { z } from 'zod'
import { healthCheck } from '@/antigravity/core'

export const StakeholderSchema = z.object({
  name: z.string(),
  role: z.string(),
  email: z.string()
})

export const CollaborationContextSchema = z.object({
  stakeholders: z.array(StakeholderSchema),
  systemMetadata: z.object({
    version: z.string(),
    environment: z.string(),
    uptime: z.number()
  }),
  sigmaStatus: z.object({
    mongodb: z.string(),
    supabase: z.string(),
    timestamp: z.string()
  })
})

export type Stakeholder = z.infer<typeof StakeholderSchema>
export type CollaborationContext = z.infer<typeof CollaborationContextSchema>

const MISSION_PATH = path.join(process.cwd(), '.antigravity/mission.md')

/**
 * ANTIGRAVITY COLLABORATION SERVICE
 * Bridges the autonomous ecosystem with the Antigravity platform.
 * Parses stakeholders from mission.md and exports system context.
 */
export async function getCollaborationContext(): Promise<CollaborationContext> {
  const stakeholders = parseStakeholders()
  const health = await healthCheck()
  const pkg = JSON.parse(fs.readFileSync(path.join(process.cwd(), 'package.json'), 'utf8'))

  return {
    stakeholders,
    systemMetadata: {
      version: pkg.version,
      environment: process.env.NODE_ENV || 'development',
      uptime: process.uptime()
    },
    sigmaStatus: {
      mongodb: health.mongodb,
      supabase: health.supabase,
      timestamp: health.timestamp
    }
  }
}

function parseStakeholders(): Stakeholder[] {
  if (!fs.existsSync(MISSION_PATH)) {
    return []
  }

  const content = fs.readFileSync(MISSION_PATH, 'utf8')
  const stakeholders: Stakeholder[] = []

  // Regex to match "- Name (Role) <email>"
  const stakeholderRegex = /-\s*(.*?)\s*\((.*?)\)\s*<(.*?)>/g
  let match

  while ((match = stakeholderRegex.exec(content)) !== null) {
    stakeholders.push({
      name: match[1].trim(),
      role: match[2].trim(),
      email: match[3].trim()
    })
  }

  return stakeholders
}

export async function exportCollaborationContext() {
  const context = await getCollaborationContext()
  const exportPath = path.join(process.cwd(), 'autonomous_state.json')

  let mergedContext = { ...context }
  if (fs.existsSync(exportPath)) {
    try {
      const existing = JSON.parse(fs.readFileSync(exportPath, 'utf8'))
      mergedContext = { ...existing, ...context }
    } catch (e) {
      console.warn('⚠️ [Collaboration] Could not parse existing state, overwriting.')
    }
  }

  // In a real scenario, this might push to a shared DB or external API
  fs.writeFileSync(exportPath, JSON.stringify(mergedContext, null, 2))
  console.log(`✅ [Collaboration] Exported context to ${exportPath}`)

  // Phase 9: Multi-agent collaboration notification
  const { sendNotification } = await import('./notification')
  await sendNotification({
    type: 'evolution',
    message: `Collaboration context synchronized for ${context.stakeholders.length} stakeholders.`,
    severity: 'info'
  })

  return context
}
